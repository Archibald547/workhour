import Vue from 'vue'
import App from './App.vue'
import router from './router';
import store from './store';
// import axios from 'axios';

import { BootstrapVue, IconsPlugin, TablePlugin, FormPlugin,FormCheckboxPlugin   } from 'bootstrap-vue'

// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import './plugins/element.js'

Vue.use(ElementUI);
// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)
Vue.use(TablePlugin)
Vue.use(FormPlugin)
Vue.use(FormCheckboxPlugin)


// axios.defaults.withCredentials = true
// axios.defaults.baseURL = 'http://localhost:8000/';
// axios.defaults.headers.common = {'Authorization': `bearer ${token}`}

// axios.interceptors.response.use(undefined, function (error) {
//   if (error) {
//     const originalRequest = error.config;
//     if (error.response.status === 401 && !originalRequest._retry) {

//         originalRequest._retry = true;
//         store.dispatch('LogOut')
//         return router.push('/login')
//     }
//   }
// })

// Vue.prototype.$http = axios;
// const token = this.$store.getters.getToken
// console.log("token ", token)
// if (this.$store.getters.isAuthenticated && token) {
//   Vue.prototype.$http.defaults.headers.common['Authorization'] = "Bearer" + token
// }

Vue.config.productionTip = false
export default new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')

