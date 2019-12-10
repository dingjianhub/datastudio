<template>
  <div id="app">

    <!-- <dashboard></dashboard> -->
    <router-view></router-view>
  </div>
</template>

<script>

// import dashboard from './components/dashboard/dashboard.vue';
export default {
  name: 'app',
  // components: {
  //   dashboard
  // },

}
</script>

<style>

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
  margin: 0;
}
</style>
