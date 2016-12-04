<template>
  <div>
    <teamTitle :team="team"></teamTitle>
    <teamStoryInfo></teamStoryInfo>
    <writeStory></writeStory>
    <timeLine></timeLine>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

import TeamStoryInfo from './TeamStoryInfo.vue'
import TeamTitle from './TeamTitle.vue'
import WriteStory from './WriteStory.vue'
import TimeLine from './TimeLine.vue'

const fetchInitialData = store => {
  console.log(store.dispatch(`getTeam`))
  return store.dispatch(`getTeam`)
}
export default {
  prefetch: fetchInitialData,
  computed: {
    ...mapGetters({
      team: 'getTeam'
    })
  },
  mounted () {
    fetchInitialData(this.$store)
  },
  components: {
    TeamStoryInfo,
    TeamTitle,
    WriteStory,
    TimeLine
  }
}
</script>
<style lang="sass?outputStyle=expanded" scoped>


</style>
