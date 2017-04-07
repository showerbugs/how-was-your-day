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

export default {
  computed: {
    ...mapGetters({
      team: 'getTeam'
    })
  },
  mounted () {
    this.$store.dispatch('getTeam', this.$route.params.teamId)
    this.$store.dispatch('getStories')
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
