<template>
<section class="projectInfo">
    <ul class="content">
        <li v-for="info in infos" >
            <label>{{info.name}}</label>
            <span class="count">{{info.count}}</span>
        </li>
    </ul>
</section>
</template>
<script>
import { mapGetters } from 'vuex'

export default {
  computed: {
    ...mapGetters({
      infos: 'getStatisticCount'
    })
  },
  created () {
  }
}
</script>
<style lang="sass" scoped>

    .projectInfo {
        background: #fdf4df;
        padding: 20px 0;

        li {
            font-weight: bold;
            label {
              display: block;
              font-size: 15px;
            }
            .count {
              font-size: 30px;
            }
        }
    }


</style>
