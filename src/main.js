import Vue from 'vue';
import VueRouter from 'vue-router';
import ViewUI from 'view-design';
import App from './app.vue';

import "view-design/dist/styles/iview.css";

Vue.use(VueRouter);
Vue.use(ViewUI);

const Routers = [
    {
        path: "/home",
        meta: {
            title: "首页"
        },
        component: (resolve) => resolve(["./routers/home.vue"], resolve)
    },
    {
        path: "*",
        redirect: "/index"
    }
];

const RouterConfig = {
    mode: "history",
    routers: Routers
}

const router = new VueRouter(RouterConfig);
router.beforeEach((to, from, next) =>{
    window.document.title = to.meta.title;
    next();
})
Vue.config.debug = true;

const app = new Vue({
    router: router,
    render: h => h(App)
}).$mount("#app");