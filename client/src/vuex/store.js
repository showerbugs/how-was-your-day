import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const defaultState = {
  topics: [],
  count: 0
}

const inBrowser = typeof window !== 'undefined'

// if in browser, use pre-fetched state injected by SSR
const state = (inBrowser && window.__INITIAL_STATE__) || defaultState

const mutations = {
  TOPICS_LIST: (state, topics) => {
    state.topics = topics
  },

  INCREMENT: (state) => {
    state.count++
  },

  DECREMENT: (state) => {
    state.count--
  }
}

export default new Vuex.Store({
  state,
  mutations
})
