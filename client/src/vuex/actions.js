function fetchFromServer (url, method = 'GET') {
  return fetch(url, {method: method}).then(function(res){
    if (res.ok) {
      return res.json().then(function(res) {
        return res.result;
      });
    } else {
      console.log("Looks like the response wasn't perfect, got status", res.status);
    }
  }, function(e) {
    console.log("Fetch failed!", e);
  });
}


export const getStories = ({ commit, state }) => {
  return fetchFromServer('./mock/getStroies.json').then(function(result) {
      console.log(result);
      commit('GET_STORIES', result);
  }).catch(function(err) {
  	// Error :(
  });
}

export const getTeam = ({ commit, state }) => {
  return fetchFromServer('./mock/getTeam.json').then(function(result) {
      console.log(result, result.entries);
      commit('GET_TEAM', result);
  });
}

export const writeStory = ({ commit, state }) => {

}




export const increment = ({ commit }) => commit('INCREMENT')
export const decrement = ({ commit }) => commit('DECREMENT')
