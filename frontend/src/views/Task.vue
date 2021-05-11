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
      </div>
      <div>
        <form @submit.prevent="post_task">
        <b-container fluid>
          <b-row class="my-1">
            <b-col sm="2">
              <label for="input-default">Task Name:</label>
            </b-col>
            <b-col sm="10">
              <b-form-input id="input-default" placeholder="Enter task name" v-model="form.taskname" ></b-form-input>
            </b-col>
          </b-row>

          <b-row class="my-1">
            <b-col sm="2">
              <label for="input-default">Full Name:</label>
            </b-col>
            <b-col sm="10">
              <b-form-input id="input-default" placeholder="Enter task full name" v-model="form.fullname"></b-form-input>
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
        taskname: '',
        fullname: '',
        organization: '',
      }
    }
  },
  mounted: function () {
    this.get_task()
  },
  methods: {
    async get_task(){
      await axios.get('http://localhost:8000/task/').then(response => (this.tasks = response.data))
    },
    async post_task() {
      try {
        console.log("posting a task")
        var api = '/task/'
        var body = {
          "taskname": this.form.taskname,
          "fullname": this.form.fullname,
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