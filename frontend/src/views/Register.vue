<template>
  <div class="register">
      <div>
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
              <b-form-input type="password" id="input-default" placeholder="Enter password" v-model="form.password"></b-form-input>
            </b-col>
          </b-row>
          <b-button pill variant="primary" type="submit">Register</b-button>
</b-container>
 </form>
      </div>
      <p v-if="showError" id="error">Username already exists</p>
  </div>
</template>

<script>
import { postUserAPI} from "../service/apis.js";
import router from '../router/index.js'
export default {
  name: "Register",
  components: {},
  data() {
    return {
      form: {
        username: "",
        full_name: "",
        password: "",
      },
      showError: false
    };
  },
  methods: {
    async post_user() {
      try {
        var data = {
          "username": this.form.username,
          "fullname": this.form.fullname,
          "password": this.form.password,
        }
        await postUserAPI(data).then(function (response) {
            if(response.status == 200){
              router.push("/users");
            }
        })
      } catch (error) {
         console.log('Exception: ', error)
        throw "Sorry you can't create a new task now!"
      }
    },
  },
};
</script>

<style scoped>
* {
  box-sizing: border-box;
}
label {
  padding: 12px 12px 12px 0;
  display: inline-block;
}
button[type=submit] {
  background-color: #4CAF50;
  color: white;
  padding: 12px 20px;
  cursor: pointer;
  border-radius:30px;
}
button[type=submit]:hover {
  background-color: #45a049;
}
input {
  margin: 5px;
  box-shadow:0 0 15px 4px rgba(0,0,0,0.06);
  padding:10px;
  border-radius:30px;
}
#error {
  color: red;
}
</style>
