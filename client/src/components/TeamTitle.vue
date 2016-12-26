<template>
  <div class="project-title">
    <div class="content">
      <h1>{{team.name}}</h1>
      {{team.description}}
      <button v-on:click="setProject">Settings</button>
    </div>

  <div>
</template>

<script>
export default {
  props: ['team'],
  computed: {
    detail: function(){
      return 'more detail showerbugs'
    }
  },
  methods: {
    setProject: function(){
      alert();
    }
  }

}
</script>
<style lang="sass?outputStyle=expanded" scoped>
  .project-title {
    background-color: #c9e3e8;
  }
</style>
