import Vue from 'vue';
import App from './app.vue';

console.log("进入main.js...");



new Vue({
    el: "#app",
    render: h => h(App)
})