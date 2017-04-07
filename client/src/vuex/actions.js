
async function fetchFromServer(url, opt = {}) {
  opt.headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json'
  };
  opt.credentials = 'include'

  if(opt.method === 'POST') {
    opt.body = JSON.stringify(opt.body);
  }
  try {
    let response = await fetch(url.includes('/mock') ? url : '/api' + url, opt);
    let result = await response.json();
    if(result.success) {
      return result.data;
    } else {
      alert(resut.msg)
    }
  } catch (e) {
    return e.message;
  }
}

export const getTeam = async ({ commit, state }, teamId) => {
  let result = await fetchFromServer('/teams/' + teamId);
  commit('GET_TEAM', result);
  return result;
}

export const createTeam = async ({ commit, state }, body) => {
  let result = await fetchFromServer('/teams', {method: 'POST', body});
  return result;
}

export const getMyInfo = async ({ commit, state }) => {
  let result = await fetchFromServer('/users/me');
  commit('GET_MYINFO', result);
  return result;
}

export const signin = async ({ commit }, body) => {
  commit('SIGNIN', result);
  let result = await fetchFromServer('/users/signin', {method: 'POST', body});
  commit('SIGNIN_SUCCESS', result);
  return result;
}

export const signout = async ({ commit }, body) => {
  commit('SIGNOUT', await fetchFromServer('/users/signout', {method: 'DELETE'}));
}

export const signup = async ({ commit }, body) => {
  await fetchFromServer('/users', {method: 'POST', body});
}

export const createStory = ({ commit }, content) => {
    // fetchFromServer('/stories', {method: 'POST', content}).then(function(result) {
    //     commit('GET_STORIES', result);
    // });
    commit('UPDATE_STORY', content);
}

export const getStories = async ({ commit, state }) => {
  let result = await fetchFromServer('/mock/getStories.json');
  commit('GET_STORIES', result);
  return result;
}


export const increment = ({ commit }) => commit('INCREMENT')
export const decrement = ({ commit }) => commit('DECREMENT')
