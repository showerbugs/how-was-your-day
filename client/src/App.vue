<template>
  <div id="app">
   <!-- <img src="./assets/logo.png"> -->
   {{msg}}
   <ul>
     <li><router-link to="/daily">Daily</router-link></li>
     <li><router-link to="/organization">Organization</router-link></li>
   </ul>
   <router-view class="view"></router-view>
   </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      msg: 'How was your day? Tell me anything.'
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
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
