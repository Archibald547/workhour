<template>
<div>
  <div class="posts" v-if="users">
        <table class="table table-striped table-bordered">
            <thead>
                <tr>
                    <th>id</th>
                    <th>username</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="u in users" :key="u.id">
                    <td>{{u.id}}</td>
                    <td>{{u.username}}</td>
                </tr>
            </tbody>
        </table>
      </div>
      <div v-else>
        Oh no!!! We have no tasks
      </div>
      <div v-if="isLoggedIn">
Hi User Logged In
      </div>
      <div  v-else>
        <form @submit.prevent="post_user">
        <b-container fluid>
          <b-row class="my-1">
            <b-col sm="2">
              <label for="input-default">User Name:</label>
            </b-col>
            <b-col sm="10">
              <b-form-input id="input-default" placeholder="Enter User Name" v-model="form.username" ></b-form-input>
            </b-col>
          </b-row>
          <b-row class="my-1">
            <b-col sm="2">
              <label for="input-default">Full Name:</label>
            </b-col>
            <b-col sm="10">
              <b-form-input id="input-default" placeholder="Enter Full Name" v-model="form.fullname"></b-form-input>
            </b-col>
          </b-row>
          <b-row class="my-1">
            <b-col sm="2">
              <label for="input-default">Password:</label>
            </b-col>
            <b-col sm="10">
              <b-form-input id="input-default" placeholder="Enter password" v-model="form.password"></b-form-input>
            </b-col>
          </b-row>
          <b-button pill variant="primary" type="submit">Submit</b-button>
</b-container>
 </form>
</div>
</div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    msg: String
  },
  computed : {
    isLoggedIn : function(){ return this.$store.getters.isAuthenticated}
  },
  data() {
    return {
      user: null,
      users: null,
      form: {
        username: '',
        fullname: '',
      }
    }
  },
  mounted: function () {
    this.get_user()
    if(this.isLoggedIn){
      console.log("i am logged in")
      this.get_user_my()
    }
    else{
      console.log("i am not logged in")
    }
  },
  methods: {
    async get_user_my(){
      await axios.get('http://localhost:8000/user/my').then(response => (this.user = response.data))
    },
    async get_user(){
      await axios.get('http://localhost:8000/user/').then(response => (this.users = response.data))
    },
    async post_user() {
      try {
        console.log("posting a task")
        var api = '/user/'
        var body = {
          "taskname": this.form.username,
          "fullname": this.form.fullname,
          "password": this.form.password,
        }
        await axios.post(api, body).then(function (response) {
            console.log("post", api, response.status)
            if(response.status == 200){
              console.log("posted task")
            }
        })
      } catch (error) {
         console.log('Exception: ', error)
        throw "Sorry you can't create a new task now!"
      }
      await axios.get('http://localhost:8000/user/').then(response => (this.users = response.data))
    },  
  }
}
</script>