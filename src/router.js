import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);


import Dashboard from './components/dashboard/dashboard.vue';
import SHIndex50 from './components/SHIndex50/SHIndex50.vue';
import Index100 from './components/Index100/Index100.vue';
import SZ100 from './components/SZ100/SZ100.vue';
import Index300 from './components/Index300/Index300.vue';
import Index500 from './components/Index500/Index500.vue';
import Index1000 from './components/Index1000/Index1000.vue';
import MediumSmallIndex from './components/MeduimSmallIndex/MeduimSmallIndex.vue';
import GEMIndex from './components/GEMIndex/GEMIndex.vue';
import BonusIndex from './components/BonusIndex/BonusIndex.vue';
import BankIndex from './components/BankIndex/BankIndex.vue';
import IndexComsume from './components/IndexComsume/IndexComsume.vue';
import FullMedicineIndex from './components/FullMedicineIndex/FullMedicineIndex.vue';
import PensionIndustryIndex from './components/PensionIndustryIndex/PensionIndustryIndex.vue';
import FullInfoIndex from './components/FullInfoIndex/FullInfoIndex.vue';
import IndexMedia from './components/IndexMedia/IndexMedia.vue';
import FullComsueIndex from './components/FullComsumeIndex/FullComsumeIndex.vue';
import EnvironmentIndex from './components/EnvironmentIndex/EnvironmentIndex.vue';
import MalitaryIndex from './components/MilitaryIndex/MilitaryIndex.vue';
import SecurityCompany from './components/ SecuritiesCompany/SecuritiesCompany.vue';

const routes = [
    {
        path: "/dashboard",
        component: Dashboard
    },
    {
        path: "/000016", // 上证50
        component: SHIndex50,
    },
    {
        path: "/000903", // 中证100
        component: Index100
    },
    {
        path: "/399330", // 深证100
        component: SZ100
    },
    {
        path: "/000300", // 沪深300
        component: Index300
    },
    {
        path: "/000905", // 中证500
        component: Index500,
    },
    {
        path: "/000852", // 中证1000
        component:Index1000,
    },
    {
        path: "/399005", // 中小板指
        component: MediumSmallIndex
    },
    {
        path: "/000932", // 中证消费
        component: IndexComsume
    },
    {
        path: "/399006", // 创业板
        component:GEMIndex
    },
    {
        path: "/000922", // 中证红利
        component: BonusIndex
    },
    {
        path: "/000991", // 全指医药
        component: FullMedicineIndex
    },
    {
        path: "/399812", // 养老产业
        component: PensionIndustryIndex
    },
    {
        path: "/399986", // 中证银行
        component: BankIndex
    },
    {
        path: "/000993", // 全指信息
        component: FullInfoIndex
    },
    {
        path: "/399971",
        component: IndexMedia
    },
    {
        path: "/000989", // 全指消费
        component: FullComsueIndex
    },
    {
        path: "/399975", // 证券公司
        component: SecurityCompany
    },
    {
        path: "/000827", // 中证环保
        component: EnvironmentIndex
    },
    {
        path: "/399967", // 中证军工
        component: MalitaryIndex
    },
    {
        path: "/",
        component: Dashboard
    }
];

var routers = new VueRouter({
    routes,
});


export default routers;