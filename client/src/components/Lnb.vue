<template>
  <header class="lnb">
    <button class="icon-btn dropdown"><i class="material-icons">menu</i></button>
    <span class="logo">how-was-your-day</span>
    <ul v-if="isSignin">
      <li><router-link :to="{ name: 'team', params: { teamId: teamId }}">Team</router-link></li>
      <li><router-link to="/organization">Organization</router-link></li>
      <li><a @click="signout">singout</a></li>
    </ul>
    <ul v-if="!isSignin">
      <li>로그인이 필요합니다.</li>
    </ul>
  </header>
</template>
<style lang="sass" scoped>
  header {
    height: 50px;
    padding: 10px;
    background: #fff;
    border-bottom: 1px solid #ccc;
  }

  li {
    float: left;
    margin-left: 10px;

    a {
      cursor: pointer;
    }
  }

  .logo {
    float: right;
  }

  .dropdown {
    float: right;
  }

</style>
<script>
import { mapGetters } from 'vuex'
import {router} from '../main.js'

export default {
  data () {
    return {
      teamId: '123'
    }
  },
  methods: {
    signout(){
      console.log('123123123', this.$route.router, this.$route);
      this.$store.dispatch('signout');
      this.$router.push('/signin');
    }
  },
  computed: {
    ...mapGetters({
      isSignin: 'isSignin'
    })
  }
}
</script>
