<template>
  <div id="app">
    <NavBar></NavBar>
    <router-view />
    <Footer></Footer>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue';
import Footer from './components/Footer.vue';

export default {
  name: 'app',
  components: {
    NavBar,
    Footer,
  },
};
</script>

<style>

#app {
  font-family: 'Raleway', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: #d9d9d9;;
}
</style>
