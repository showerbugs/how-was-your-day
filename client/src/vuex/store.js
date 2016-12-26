import Vue from 'vue'
import Vuex from 'vuex'
import * as actions from './actions'
import * as getters from './getters'

Vue.use(Vuex)

const defaultState = {
  stories: [],
  team: {},
  teamCountInfo: []
}

const inBrowser = typeof window !== 'undefined'

// if in browser, use pre-fetched state injected by SSR
const state = (inBrowser && window.__INITIAL_STATE__) || defaultState

const mutations = {
  GET_STORIES: (state, result) => {
    state.teamCountInfo = result.countInfo
    state.stories = result.data
  },

  GET_TEAM: (state, team) => {
    state.team = team
  },
  //mock용 
  UPDATE_STORY: (state, result) => {
    console.log(result)
    state.stories.push({
      content: result,
      creator: '호우'
    })
  }
}

export default new Vuex.Store({
  state,
  actions,
  mutations,
  getters
})
