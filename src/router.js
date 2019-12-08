import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);



import dashboard from './components/dashboard/dashboard.vue';
import fullInfoIndex from './components/FullInfoIndex/FullInfoIndex.vue';

const routes = [
    {
        path: "/dashboard",
        component: dashboard
    },
    {
        path: "/fullInfoIndex",
        component: fullInfoIndex
    },
    {
        path: "/",
        component: dashboard
    }
];

var routers = new VueRouter({
    routes,
});


export default routers;