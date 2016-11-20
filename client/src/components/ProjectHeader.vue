<template>
  <div class="project-title">
    <div class="content">
      <h1>ShowerBugs</h1>
      {{detail}}
      <button v-on:click="setProject">Settings</button>
    </div>

  <div>
</template>

<script>
export default {
  props: ['project'],
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
