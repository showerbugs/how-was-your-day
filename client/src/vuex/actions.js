export const getPosts = ({ commit, state }) => {
  return fetch('http://jsonplaceholder.typicode.com/', {
  	method: 'get'
  }).then(function(response) {

  }).catch(function(err) {
  	// Error :(
  });
}

export const getProject = ({ commit, state }) => {
  return fetch('http://jsonplaceholder.typicode.com/', {
  	method: 'get'
  }).then(function(response) {
    //commit()
  }).catch(function(err) {
  	// Error :(
  });
}

export const getProjectInfo = ({ commit, state }) => {
  commit('GET_PROJECT_INFO', [
    {name: "My Diary", count: "15"},
    {name: "Team Diary", count: "64"},
    {name: "Day", count: "20"}
  ])
  return;
}


export const increment = ({ commit }) => commit('INCREMENT')
export const decrement = ({ commit }) => commit('DECREMENT')
