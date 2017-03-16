<template>
  <div class="project-title">
    <div class="content">
      <div class="team-logo"></div>
      <h1 class="team-name">{{team.name}}</h1>
      <h5 class="team-description">{{team.description}}</h5>
      <button class="team-setting-btn" v-on:click="setProject">설정</button>
    </div>
  </div>
</template>

<script>
export default {
  props: ['team'],
  computed: {
    detail (){
      return 'more detail showerbugs'
    }
  },
  methods: {
    setProject (){
      alert();
    }
  }

}
</script>
<style lang="sass?outputStyle=expanded" scoped>
.team-logo {
  width: 120px;
  height: 120px;
  border-radius: 60px;
  background: #015aff;
  position: absolute;
  top: -20px;
  left: -40px;
}
.project-title {
  background-color: #c9e3e8;
  height: 150px;
}

.content {
  position: relative;
  width: 80%;
  margin: 0 auto;
}

.team-name {
  font-size: 50px;
  margin: 30px 0 0 100px;
  display: inline-block;
}

.team-description {
  margin-left: 100px;
  margin-top: 10px;
}

.team-setting-btn {
  position: absolute;
  right: 0;
  top: 50px;
  background-color: #ccc;
  border: 0;
  margin: 0;
  color: #fff;
  font-size: 15px;
  padding: 5px 20px;
}
</style>
