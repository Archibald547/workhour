@@ -1,52 +0,0 @@
<template>
  <div class="hello">
      <h1>users</h1>
      {{ users }}
      <h1>tasks</h1>
      {{ tasks }}
      <h1>workhours</h1>
      {{ workhours }}
      
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data () {
    return {
      users: null,
      task: null,
      workhours: null
    }
  },
  mounted () {
    axios.get('http://localhost:8000/user').then(response => (this.users = response.data))
    axios.get('http://localhost:8000/task').then(response => (this.tasks = response.data))
    axios.get('http://localhost:8000/workhour').then(response => (this.workhours = response.data))
  }
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