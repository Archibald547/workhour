<template>
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
</template>

<script>
import axios from 'axios';

export default {
  props: {
    msg: String
  },
  data() {
    return {
      users: null,
    }
  },
  mounted: function () {
    axios.get('http://localhost:8000/user/').then(response => (this.users = response.data))
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
