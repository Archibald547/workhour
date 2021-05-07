<template>
  <div class="workhours" v-if="workhours">
        <table class="table table-striped table-bordered">
            <thead>
                <tr>
                    <th>id</th>
                    <th>user-name</th>
                    <th>task-name</th>
                    <th>date</th>
                    <th>hour</th>
                    <th>description</th>
                    <th>is_overtime</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="w in workhours" :key="w.id">
                    <td>{{w.id}}</td>
                    <td>{{w.user.username}}</td>
                    <td>{{w.task.taskname}}</td>
                    <td>{{w.date}}</td>
                    <td>{{w.hour}}</td>
                    <td>{{w.date}}</td>
                    <td>{{w.description}}</td>
                    <td>{{w.is_overtime}}</td>
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
      workhours: null,
    }
  },
  mounted: function () {
    axios.get('http://localhost:8000/workhour/').then(response => (this.workhours = response.data))
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
