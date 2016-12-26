<template>
  <div id="app">
    <lnb></lnb>
   <!-- <img src="./assets/logo.png"> -->
   <router-view class="view"></router-view>
   <Footer></Footer>
   </div>
</template>

<script>
import Lnb from './components/Lnb.vue'
import Footer from './components/Footer.vue'
import lodash from 'lodash'
import jquery from 'jquery'
//import bootstrap from 'bootstrap'

var _ = window._ = lodash;
var $ = window.$ = window.jQuery = jquery;

export default {
  name: 'app',
  data () {
    return {
      msg: 'How was your day? Tell me anything.'
    }
  },
  components: {
    Lnb
  }
}
</script>

<style>
/*@import "../node_modules/material-design-icons/iconfont/material-icons.css";*/
body {
  margin: 0;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

.content {
  max-width: 1080px;
  margin: 0 auto;
}

.icon-btn {
  border: 0;
  background: none;
  padding: 0;
  margin: 0;

}

img {
  width: 100%;
}
h1, h2 {
  font-weight: normal;
  margin: 0;
}
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
