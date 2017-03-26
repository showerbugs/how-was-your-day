<template>
  <div class="login-form-wrap">
    <form class="login-form" @submit.prevent>
      <div class="split-form">
        <h4>How was your day에 오신것을 환영합니다.</h4>
        <img src="/src/assets/signin_image.png"/>
      </div>
      <div class="split-form">
        <div><label>Email</label></div>
        <div><input name="email" type="text" v-model="email" placeholder="Enter your email"/></div>
        <div><label>Password</label></div>
        <div><input name="password" type="password" v-model="password"/></div>
        <div class="button-wrap">
            <button @click="signin" class="button" type="submit">로그인</button>
            <router-link class="button" to="/signup">회원가입</router-link>
        </div>
      </div>
    </form>
  </div>
</template>
<script>
  import { mapGetters } from 'vuex'

  export default {
    methods: {
      signin(){
        this.$store.dispatch('signin', {
          email: this.email,
          password: this.password
        }).then(() => {
          this.$router.push('/')
          this.$store.dispatch('getMyInfo').then((result)=>{
            this.$router.push({ name: 'team', params: { teamId: result.user.teams[0].id }})
          });
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
