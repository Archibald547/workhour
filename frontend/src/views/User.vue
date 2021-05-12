<template>
<div class="posts" v-if="users">
<table class="table table-striped table-bordered">
<thead>
<tr>
<th>id</th>
<th>username</th>
<th>fullname</th>
</tr>
</thead>
<tbody>
<tr v-for="u in users" :key="u.id">
<td>{{u.id}}</td>
<td>{{u.username}}</td>
<td>{{u.fullname}}</td>
</tr>
</tbody>
</table>
</div>
<div v-else>
Oh no!!! We have no tasks
</div>
</template>

<script>
import { getUserAPI} from "../service/apis.js";
export default {
  components:{
  },
  props: {
    msg: String
  },
  computed : {
    isLoggedIn : function(){ return this.$store.getters.isAuthenticated},
    isUser: function(){return this.user!=null}
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
    }
    else{
      console.log("i am not logged in")
    }
  },
  methods: {
    async get_user(){
      // await axios.get('/user/').then(response => (this.users = response.data))
      await getUserAPI().then( (response) => this.users = response.data)
    }
  }
}
</script>