<template>
  <div class="login-form-wrap">
    <form class="login-form" action="POST" url="/signin">
      <h4>How was your day에 오신것을 환영합니다.</h4>
      <div><label>Email</label><input type="text"/></div>
      <div><label>Password</label><input type="text"/></div>
      <div><button type="submit">로그인하기</button></div>
    </form>
  </div>
</template>
<script>

</script>
<style lang="sass" scoped>
  .login-form {
    position: absolute;
    left: 0;
    right: 0;
    width: 400px;
    height: 200px;
    margin: 0 auto;
    border: 1px solid #ccc;
  }

</style>
