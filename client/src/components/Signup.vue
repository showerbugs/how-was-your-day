<template>
  <div class="login-form-wrap">
    <form class="login-form" @submit.prevent>
      <div class="split-form">
        <h4>How was your day에 오신것을 환영합니다.</h4>
        <img src="/src/assets/signin_image.png"/>
      </div>
      <div class="split-form">
        <div><label>name</label></div>
        <div><input name="name" type="text" v-model="form.name" placeholder="Hou"/></div>
        <div><label>Email</label></div>
        <div><input name="email" type="text" v-model="form.email" placeholder="Enter your email"/></div>
        <div><label>Password</label></div>
        <div><input name="password" type="password" v-model="form.password"/></div>
        <div><label>Password repeat</label></div>
        <div><input name="password" type="password" v-model="form.passwordRepeat"/></div>
        <div class="button-wrap">
            <button @click="signup" class="button" type="submit">회원가입</button>
        </div>
      </div>
    </form>
  </div>
</template>
<script>
  import { mapGetters } from 'vuex'

  export default {
    data () {
      return {
        form: {}
      }
    },
    methods: {
      signup(){
        this.$store.dispatch('signup', this.form).then(() => {
          this.$router.push('/signin')
        });
      }
    }
  }

</script>
<style lang="sass" scoped>

  .login-form-wrap {
    padding: 80px;
    background: #ddded4;
  }

  .login-form {
    left: 0;
    right: 0;
    width: 800px;
    height: 600px;
    margin: 20px auto;
    box-shadow: 0 0 10em rgba(0, 0, 0, 0.4);
    border-radius: 8px;
  }

  .split-form {
    width: 50%;
    height: 100%;
    float: left;
    color: #fff;

    &:first-child {
      background-color: #e94347;
      border-radius: 8px 0 0 8px;
      padding: 50px 0;
      text-align: center;

      img {
        margin-top: 50px;
        width: 80%;
      }
    }

    &:last-child {
      background-color: #081d3c;
      border-radius: 0 8px 8px 0;
      padding: 100px 50px;
      font-size: 15px;

      label {
        display: block;
        margin-top: 30px;
        margin-bottom: 15px;
      }

      input[type="text"],
      input[type="password"] {
        background: none;
        border: 0;
        padding-bottom: 10px;
        color: #fff;
        outline: 0;
        border-bottom: 1px solid #666;
        width: 100%;
        font-size: 15px;
      }

      .button-wrap {
          display: flex;

          .button {
            background-color: #e94347;
            border: 0;
            font-size: 15px;
            color: #fff;
            border-radius: 20px;
            padding: 0 40px;
            height: 40px;
            line-height: 40px;
            text-align: center;
            min-width: 150px;
            margin-top: 50px;
            text-decoration: none;
            outline: 0;

            &:not(:first-child) {
              margin-left: 10px;
              background-color: #3879d9;
            }
          }
      }
    }
  }

</style>
