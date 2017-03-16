<template>
<section class="projectInfo">
    <ul class="content">
        <li>
            <label>Daliy count</label>
            <span class="count">{{infos.dailyCount}}</span>
        </li>
        <li>
            <label>My story count</label>
            <span class="count">{{infos.myStoryCount}}</span>
        </li>
        <li>
            <label>total count</label>
            <span class="count">{{infos.totalCount}}</span>
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
        text-align: center;

        li {
            flex: 1;
            font-weight: bold;
            text-align: center;

            label {
              display: block;
              margin-bottom: 10px;
              font-size: 20px;
            }
            .count {
              font-size: 30px;
            }

            &:not(:first-child) {
              margin-left: 40px;
            }
        }
    }

    .projectInfo {

    }

    .content {
      width: 80%;
      display: flex;
      padding: 0 200px;
    }


</style>
