<template>
  <header class="lnb">
    <button class="icon-btn dropdown"><i class="material-icons">menu</i></button>
    <span class="logo">how-was-your-day</span>
    <ul>
      <li><router-link to="/project">Project</router-link></li>
      <li><router-link to="/organization">Organization</router-link></li>
    </ul>
  </header>
</template>
<style lang="sass" scoped>
  header {
    height: 30px;
    padding: 10px;
    background: #fff;
    border-bottom: 1px solid #ccc;
  }

  .logo {
    float: right;
  }

  .dropdown {
    float: right;
  }

</style>
<script>

export default {

}
</script>
