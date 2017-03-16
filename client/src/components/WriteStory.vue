<template>
  <div class="write-form">
    <textarea placeholder="how was your day? write stroy" @keyup.enter="writeStroy"></textarea>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
//model을 쓸경우 상위 컴퍼넌트에 data 값이 있고 props로 받아야 한다.
export default {
  props: ['team'],
  methods: {
    writeStroy(e) {
      e.preventDefault()
      const content = e.target.value
      if(content.trim()) {
        this.$store.dispatch('writeStory', content)
      }
      e.target.value = ''
    }
  },
  mounted() {
      console.log(this.$refs)
  }
}

</script>
<style lang="sass?outputStyle=expanded" scoped>
.write-form {
  text-align: center;
  height: 100px;
}

textarea {
  display: inline-block;
  width: 80%;
  box-sizing: border-box;
  font-size: 14px;
  padding: 5px;
  border: 1px solid #999;
  margin: 20px 0;
}

</style>
