import Vue from 'vue'
import Vuex from 'vuex'
import * as actions from './actions'
import * as getters from './getters'

Vue.use(Vuex)

const defaultState = {
  myInfo: {},
  stories: [],
  team: {},
  statisticCount: [],
  isSignin: localStorage.getItem('session'),
  pending: false
}

const inBrowser = typeof window !== 'undefined'

// if in browser, use pre-fetched state injected by SSR
const state = (inBrowser && window.__INITIAL_STATE__) || defaultState

const mutations = {
  GET_MYINFO (state, result) {
    state.myInfo = result.user
  },
  GET_STORIES (state, result) {
    state.statisticCount = result.statisticCount
    state.statisticCount.totalCount = result.count
    state.stories = result.stories
  },

  GET_TEAM (state, result){
    state.team = result.team
  },
  //mock용
  UPDATE_STORY (state, result) {
    console.log(result)
    state.stories.push({
      content: result,
      "user": {
          "id": "1",
          "thumnailImageUrl": "https://gravatar.com/awefawef",
          "name": "호우"
      }
    })
  },
  SIGNIN (state) {
    state.pending = true;
  },
  SIGNIN_SUCCESS (state) {
    state.isSignin = true;
    state.pending = false;
  },
  SIGNOUT(state) {
    state.isSignin = false;
  }

}

export default new Vuex.Store({
  state,
  actions,
  mutations,
  getters
})
