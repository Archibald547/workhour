<template>
<div>
  <div v-if="tasks">
        <table class="table table-striped table-bordered">
            <thead>
                <tr>
                    <th>id</th>
                    <th>taskname</th>
                    <th>fullname</th>
                    <th>organization</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="t in tasks" :key="t.id">
                    <td>{{t.id}}</td>
                    <td>{{t.taskname}}</td>
                    <td>{{t.fullname}}</td>
                    <td>{{t.organization}}</td>
                </tr>
            </tbody>
        </table>
    </div>
    <div v-else>
      Oh no!!! We have no tasks
    </div>
    <div>
          <!-- <form @submit.prevent="submit">
            <div class="form-group">
              <label for="task_name">task_name:</label>
              <input type="text" name="task_name" v-model="form.task_name" class="form-control">
            </div>
            <div class="form-group">
              <label for="full_name">full_name:</label>
              <input type="text" name="full_name" v-model="form.full_name" class="form-control">
            </div>
            <div class="form-group">
              <label for="organization">task_organizationame:</label>
              <input type="text" name="organization" v-model="form.organization" class="form-control">
            </div>
            <button type="submit" class="btn btn-primary"> Submit</button>
          </form> -->
          
      </div>
      <div>
        <form @submit.prevent="post_task">
        <b-container fluid>
          <b-row class="my-1">
            <b-col sm="2">
              <label for="input-default">Task Name:</label>
            </b-col>
            <b-col sm="10">
              <b-form-input id="input-default" placeholder="Enter task name" v-model="form.task_name" ></b-form-input>
            </b-col>
          </b-row>

          <b-row class="my-1">
            <b-col sm="2">
              <label for="input-default">Full Name:</label>
            </b-col>
            <b-col sm="10">
              <b-form-input id="input-default" placeholder="Enter task full name" v-model="form.full_name"></b-form-input>
            </b-col>
          </b-row>

          <b-row class="my-1">
            <b-col sm="2">
              <label for="input-default">Organization Name:</label>
            </b-col>
            <b-col sm="10">
              <b-form-input id="input-default" placeholder="Enter task organization name" v-model="form.organization"></b-form-input>
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
  data() {
    return {
      tasks: null,
      form: {
        task_name: '',
        full_name: '',
        organization: '',
      }
    }
  },
  mounted: function () {
    this.get_task()
  },
  methods: {
    async get_task(){
      axios.get('http://localhost:8000/task/').then(response => (this.tasks = response.data))
    },
    async post_task() {
      try {
        console.log("posting a task")
        var api = '/task/'
        var body = {
          "taskname": this.form.task_name,
          "fullname": this.form.full_name,
          "organization": this.form.organization,
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
      await axios.get('http://localhost:8000/task/').then(response => (this.tasks = response.data))
    },  
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only 
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
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
  margin: 10px;
}
button[type=submit]:hover {
  background-color: #45a049;
}
input {
  width:60%;
  margin: 15px;
  border: 0;
  box-shadow:0 0 15px 4px rgba(0,0,0,0.06);
  padding:10px;
  border-radius:30px;
}
</style>
-->