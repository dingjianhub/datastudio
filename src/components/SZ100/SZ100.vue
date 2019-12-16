<template>

    <div id="main">
        <Header></Header>
        <div class="detial-aside-left">
            <!-- <CommonBtn></CommonBtn> -->
            <button class="common-btn-item" @click="PE">PE</button>
            <button class="common-btn-item" @click="PB">PB</button>
            <button class="common-btn-item" @click="Price">价格</button>
            <button class="common-btn-item" @click="ROE">ROE</button>
            <button class="common-btn-item" @click="PEPercentile">PE百分位</button>
            <button class="common-btn-item" @click="PBPercentile">PB百分位</button>
            <button class="common-btn-item" @click="dailyChangePercentile">日涨跌幅</button>
            <button class="common-btn-item" @click="yearChangePercentile">年涨跌幅</button>
            <button class="common-btn-item" @click="TotalVolumes">成交量</button>
            <button class="common-btn-item" @click="PERate">预期收益率</button>
        </div>
        
        <hr>
        <div class="sz-100-index"></div>
    </div>
</template>

<script>

import Header from '../../Header';
import {   
    PEChart, 
    PBChart,
    PriceChart,
    ROEChart,
    PEPercentileChart,
    PBPercentileChart,
    DailyChangePercentileChart,
    YearChangePercentileChart,
    TotalVolumesChart,
    ExpectedYeildChart
} from '../../Charts';


export default {
    data() {
        return {
            indexCode: "399330",
            baseurl:"http://101.37.30.183:5000/index/",
            // baseurl:"http://127.0.0.1:5000/index/",
            selectorName: ".sz-100-index"
        }
    },
    components:{
        Header,
        // CommonBtn
    },
    methods: {
        PE(){
            const url = this.baseurl+this.indexCode+"/pe";
            PEChart(url, this.selectorName)
        },
        PB(){
            const url = this.baseurl+this.indexCode+"/pb";
            PBChart(url, this.selectorName)
        },
        Price(){
            const url = this.baseurl+this.indexCode+"/price";
            PriceChart(url, this.selectorName);
        },
        ROE(){
            const url = this.baseurl+this.indexCode+"/roe";
            ROEChart(url, this.selectorName);
        },

        PEPercentile(){
            const url = this.baseurl+this.indexCode+"/pe-percent";
            PEPercentileChart(url, this.selectorName);
        },
        PBPercentile(){
            const url = this.baseurl+this.indexCode+"/pb-percent";
            PBPercentileChart(url, this.selectorName);
        },
        dailyChangePercentile(){
            const url = this.baseurl+this.indexCode+"/daily-change-percent";
            DailyChangePercentileChart(url, this.selectorName);
        },
        yearChangePercentile(){
            const url = this.baseurl+this.indexCode+"/year-change-percent";
            YearChangePercentileChart(url, this.selectorName);
        },
        TotalVolumes(){
            const url = this.baseurl+this.indexCode+"/volumes";
            TotalVolumesChart(url, this.selectorName);
        },
        PERate(){
            const url = this.baseurl+this.indexCode+"/expected-yeild";
            ExpectedYeildChart(url, this.selectorName); 
        }
    },  
}
</script>

<style scoped>

.sz-100-index {
    background: gainsboro;
    width: 80%;
    height: 548px;
    text-align: center;
    margin: 0 auto;
    float: left;
    /* margin-top: 20px; */
    
}
</style>