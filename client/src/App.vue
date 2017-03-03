<template>
  <div id="app">
   <lnb></lnb>
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
import { mapGetters } from 'vuex'

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
  },
  created() {
    this.$store.dispatch('getMyInfo')
    console.log(this.isSignin)
    this.checkAuth();
    console.log(this.myInfo)
  },
  updated() {
    this.checkAuth();
  },
  computed: {
    ...mapGetters({
      isSignin: 'isSignin',
      myInfo: 'getMyInfo'
    })
  },
  methods: {
    checkAuth() {
      console.log('checkAuth!!!!!!!!!!', this.isSignin, this.$state, this.$store, this)
      if(!this.isSignin) {
          //this.$router.push('/signin')
      } else {
        this.$store.dispatch('getMyInfo').then((result)=>{
          console.log(result)
          //this.$router.push({ name: 'team', params: { teamId: result.users.teams[0].teamId }})
        });
      }
    }
  }
}
</script>

<style>
/*@import "../node_modules/material-design-icons/iconfont/material-icons.css";*/
body {
  margin: 0;
}

html,
body {
  width: 100%;
  height: 100%;
  font-family: 'Nanum Gothic'
}

#app {
  width: 100%;
  height: 100%;
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

.view {
  height: calc(100% - 50px);
  position: relative;
}

/* TODO:reset.css 분리하기*/
html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed,
figure, figcaption, footer, header, hgroup,
main, menu, nav, output, ruby, section, summary,
time, mark, audio, video {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;
  box-sizing: border-box;
}
/* HTML5 display-role reset for older browsers */
article, aside, details, figcaption, figure,
footer, header, hgroup, main, menu, nav, section {
	display: block;
}
body {
	line-height: 1;
}
ol, ul {
	list-style: none;
}
blockquote, q {
	quotes: none;
}
blockquote:before, blockquote:after,
q:before, q:after {
	content: '';
	content: none;
}
table {
	border-collapse: collapse;
	border-spacing: 0;
}

</style>
