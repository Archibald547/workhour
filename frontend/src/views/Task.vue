<template>
  <div class="posts" v-if="tasks">
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
    }
  },
  mounted: function () {
    axios.get('http://localhost:8000/task/').then(response => (this.tasks = response.data))
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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
</style>
