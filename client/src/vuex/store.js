import Vue from 'vue'
import Vuex from 'vuex'
import * as actions from './actions'
import * as getters from './getters'

Vue.use(Vuex)

const defaultState = {
  posts: [],
  project: {},
  projectInfo: []
}

const inBrowser = typeof window !== 'undefined'

// if in browser, use pre-fetched state injected by SSR
const state = (inBrowser && window.__INITIAL_STATE__) || defaultState

const mutations = {
  GET_POST_LIST: (state, posts) => {
    state.posts = posts
  },

  GET_PROJECT: (state, project) => {
    state.project = project
  },

  GET_PROJECT_INFO: (state, projectInfo) => {
    state.projectInfo = projectInfo
  },
}

export default new Vuex.Store({
  state,
  actions,
  mutations,
  getters
})
