<template>
<div>
    <hr>
  <div v-if="isLoggedIn">
        <p>
          Good Day {{fullname}}! You are logged in as {{username}}. :)
        </p>
  </div>
  <div v-else>
        <p>
          Please log in to add workhour. 
        </p>
  </div>
  <hr>
</div>
</template>
<script>
export default {
  name: 'GoodDay',
  mounted: function () {
    if(this.isLoggedIn){
      this.get_user_my()
    }
  },
  computed : {
      isLoggedIn : function(){ return this.$store.getters.isAuthenticated},
      isUser: function(){return this.user!=null}
  },
  methods: {
    async get_user_my(){
        this.username = this.$store.getters.getUsername,
        this.fullname = this.$store.getters.getFullname
    }
  },
  data() {
    return {
      username: null,
      fullname: null
    }
  },
}
</script>
<style>
#nav {
  padding: 30px;
}
#nav a {
  font-weight: bold;
  color: #2c3e50;
}
a:hover {
  cursor: pointer;
}
#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
