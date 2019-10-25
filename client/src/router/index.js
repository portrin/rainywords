import Vue from "vue";
import VueRouter from "vue-router";
import Dashboard from "../views/Dashboard";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  },
  {
    path: "/dashboard",
    name: "dashboard",
    component: Dashboard
  }
];

const router = new VueRouter({
  routes
});

export default router;