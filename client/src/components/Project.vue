<template>
  <div>
    <projectHeader project="project"></projectHeader>
    <projectPostInfo></projectPostInfo>
    <timeLine></timeLine>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

import ProjectHeader from './ProjectHeader.vue'
import ProjectPostInfo from './ProjectPostInfo.vue'
import TimeLine from './TimeLine.vue'

const fetchInitialData = store => {
  return store.dispatch(`getPosts`)
}
export default {
  prefetch: fetchInitialData,
  computed: {
    ...mapGetters({
      project: 'getProject',
      posts: 'getPosts'
    })
  },
  mounted () {
    fetchInitialData(this.$store)
  },
  components: {
    ProjectHeader,
    ProjectPostInfo,
    TimeLine
  }
}
</script>
<style lang="sass?outputStyle=expanded" scoped>


</style>
