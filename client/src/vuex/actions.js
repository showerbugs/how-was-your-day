
async function fetchFromServer(url) {
  try {
    let response = await fetch(url, opt);
    let result = await response.res.json();
    if(result.success) {
      return result.data;
    }
  } catch (e) {
    return e.message;
  }
}

export const getStories = ({ commit, state }) => {
  let result = fetchFromServer('./mock/getStories.json').then(function(result) {
    commit('GET_STORIES', result);
  });
}

export const getTeam = ({ commit, state }) => {
  let result = fetchFromServer('./mock/getTeam.json').then(function(result) {
    commit('GET_STORIES', result);
  });
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
