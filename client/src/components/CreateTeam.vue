
<template>
  <div class="create-team">
    <form class="login-form" @submit.prevent>
      <div class="split-form">
        <div><label>팀이름</label></div>
        <div><input name="name" type="text" v-model="form.name" placeholder="showerbugs"/></div>
        <div><label>설명</label></div>
        <div><input name="description" type="text" v-model="form.description" placeholder="Enter your description"/></div>
        <div><label>이메일</label></div>
        <div><input name="email" type="text" v-model="email" @keyup.enter="addUser"/></div><button type="button" @click="addUser">추가</button>
        <div v-for="userEmail in form.userEmails">
          <div>{{userEmail}}</div>
        </div>
        <div class="button-wrap">
            <button @click="createTeam" class="button" type="submit">팀만들기</button>
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
        form: {
          userEmails: []
        }
      }
    },
    methods: {
      createTeam() {
        this.$store.dispatch('createTeam', this.form).then((result) => {
          //this.$router.push('/team/new')
        });
      },
      addUser() {
        if(!this.email) {
          return;
        }
        this.form.userEmails.push(this.email)
        this.email = ""
      }
    }
  }

</script>
<style lang="sass" scoped>


</style>
