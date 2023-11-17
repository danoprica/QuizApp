import { createRouter, createWebHistory } from 'vue-router'

import Home from "./components/Home.vue"
import Login from "./components/Login.vue"
import CreateQuiz from "./components/CreateQuiz.vue"

const routes = [
  { path: '/', component: Home, name: 'home' },
  { path: '/login', component: Login, name: 'login' },
  { path: '/create-quiz', component: CreateQuiz, name: 'create-quiz' }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})


export default router;



