
async function fetchFromServer(url, opt = {}) {
  opt.headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json'
  };
  if(opt.method === 'POST') {
    opt.body = JSON.stringify(opt.body);
  }
  try {
    let response = await fetch(url, opt);
    console.log(response)
    let result = await response.json();
    if(result.success) {
      return result.data;
    }
  } catch (e) {
    return e.message;
  }
}

export const getStories = async ({ commit, state }) => {
  let result = await fetchFromServer('/mock/getStories.json');
  commit('GET_STORIES', result);
  return result;
}

export const getTeam = async ({ commit, state }) => {
  let result = await fetchFromServer('/mock/getTeam.json');
  commit('GET_TEAM', result);
  return result;
}

export const getMyInfo = async ({ commit, state }) => {
  let result = await fetchFromServer('/mock/getMe.json');
  commit('GET_MYINFO', result);
  return result;
}

export const signin = ({ commit }, body) => {
  commit('SIGNIN', result);
  let result = fetchFromServer('/api/users/signin', {method: 'POST', body}).then(function(result) {
    commit('SIGNIN_SUCCESS', result);
  });
}

export const signout = async ({ commit }, body) => {
  commit('SIGNOUT', await fetchFromServer('/api/users/signout', {method: 'DELETE'}));
}

export const signup = async ({ commit }, body) => {
  await fetchFromServer('/api/users', {method: 'POST', body});
}

export const writeStory = ({ commit }, content) => {
    // fetchFromServer('/stories', {method: 'POST', content}).then(function(result) {
    //     commit('GET_STORIES', result);
    // });
    console.log(content)
    commit('UPDATE_STORY', content);
}


export const increment = ({ commit }) => commit('INCREMENT')
export const decrement = ({ commit }) => commit('DECREMENT')
