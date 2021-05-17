<template>
  <div class="login">
    <div>
      <!-- <form @submit.prevent="submit">
        <div>
          <label for="username">Username:</label>
          <input id="input-default" type="text" name="username" v-model="form.username" />
        </div>
        <div>
          <label for="password">Password:</label>
          <input id="input-default" type="password" name="password" v-model="form.password" />
        </div>
        <button type="submit">Submit</button>
      </form> -->
      <form @submit.prevent="submit">
        <b-container fluid>
          <b-row class="my-1">
            <b-col sm="2">
              <label for="input-default">Username:</label>
            </b-col>
            <b-col sm="10">
              <b-form-input id="input-default" placeholder="Enter User Name" v-model="form.username" ></b-form-input>
            </b-col>
          </b-row>

          <b-row class="my-2">
            <b-col sm="2">
              <label for="input-default">Password:</label>
            </b-col>
            <b-col sm="10">
              <b-form-input id="input-default" type="password" placeholder="Enter password" v-model="form.password"></b-form-input>
            </b-col>
          </b-row>
          <b-button pill variant="primary" type="submit">Submit</b-button>
        </b-container>
        </form>
      <p v-if="showError" id="error">Username or Password is incorrect</p>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "Login",
  components: {},
  data() {
    return {
      form: {
        username: "",
        password: "",
      },
      showError: false
    };
  },
  methods: {
    ...mapActions(["LogIn"]),
    async submit() {
      const User = new FormData();
      User.append("username", this.form.username);
      User.append("password", this.form.password);
      try {
          await this.LogIn(User);
          this.$router.push("/user");
          this.showError = false
      } catch (error) {
        this.showError = true
      }
    },
  },
};
</script>

<!--
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
-->