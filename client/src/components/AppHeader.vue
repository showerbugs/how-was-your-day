<template>
  <header class="lnb">
    <span class="logo">How was your day</span>
    <!-- <router-link class="" v-if="isSignin" :to="{ name: 'team', params: { teamId: myInfo.teams[0].teamId }}">{{myInfo.teams[0].name}}</router-link> -->
    <ul v-if="isSignin">
      <li>{{myInfo.email}}</li>
      <li><a @click="signout">singout</a></li>
      <router-link class="button" to="/team/new">팀 만들기</router-link>
      <button class="icon-btn dropdown"><i class="material-icons">menu</i></button>
    </ul>
    <ul v-if="!isSignin">
      <li>로그인이 필요합니다.</li>
    </ul>
  </header>
</template>
<style lang="sass" scoped>
  header {
    height: 50px;
    padding: 10px 0;
    background: #fff;
    display: flex;
    align-items: center;
    width: 80%;
    margin: 0 auto;
  }

  .logo {
    font-weight: bold;
  }

  ul {
      margin-left: auto;
      display: flex;
      align-items: center;

      li {
        float: left;
        margin-left: 10px;
      }
  }

  .dropdown {
    margin-top: 4px;
  }

</style>
<script>
import { mapGetters } from 'vuex'
import {router} from '../main.js'

export default {
  created() {
    var c = this.myInfo
  },
  data () {
    return {
    }
  },
  methods: {
    signout(){
      this.$store.dispatch('signout');
      this.$router.push('/signin');
    }
  },
  computed: {
    // myInfo() {
    //   return this.$store.getters.getMyInfo;
    // },
    ...mapGetters({
      isSignin: 'isSignin',
      myInfo: 'getMyInfo'
    })
  }
}
</script>
