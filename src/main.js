import Vue from 'vue';
import App from './App.vue';



import  "../static/css/reset.css";
import "../static/css/aside_btns.css";



import router from './router';

Vue.config.productionTip = false;


new Vue({
  router,

  render: h => h(App),
}).$mount('#app');
