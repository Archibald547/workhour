import Vue from 'vue'
import VueRouter from 'vue-router'
// import store from '../store';
import Home from '../views/Home.vue'
import Register from '../views/Register'
import Login from '../views/Login'
import Posts from '../views/Posts'
import Test from '../views/Test'
import User from '../views/User'
import Task from '../views/Task'
import Workhour from '../views/Workhour'

Vue.use(VueRouter)
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/register',
    name: "Register",
    component: Register,
    meta: { guest: true },
  },
  {
    path: '/login',
    name: "Login",
    component: Login,
    meta: { guest: true },
  },
  {
    path: '/posts',
    name: "Posts",
    component: Posts,
    meta: {requiresAuth: true},
  },
  {
    path: '/test',
    name: "Test",
    component: Test,
    meta: { guest: true },
  },
  {
    path: '/users',
    name: "User",
    component: User,
    meta: { guest: true },
  },
  {
    path: '/tasks',
    name: "Task",
    component: Task,
    meta: { guest: true },
  },
  {
    path: '/workhours',
    name: "Workhour",
    component: Workhour,
    meta: { guest: true },
  }
]
const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
