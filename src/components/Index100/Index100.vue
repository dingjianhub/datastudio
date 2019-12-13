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
        </div>
        
        <hr>
        <div class="index-100-detail"></div>
    </div>
</template>

<script>
// import axios from 'axios';
// import echarts from 'echarts';
// import CommonBtn from '../../CommonBtn';
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
    } from '../../Charts';
// import PBChart from '../../Charts';

export default {
    data() {
        return {
            indexCode: "000903",
            selectorName: ".index-100-detail",
            }
    },
    components:{
        Header,
        // CommonBtn
    },
    methods: {
        PE(){
            const url = "http://127.0.0.1:5000/index/"+this.indexCode+"/pe";
            PEChart(url, this.selectorName)
        },
        PB(){
            const url = "http://127.0.0.1:5000/index/"+this.indexCode+"/pb";
            PBChart(url, this.selectorName)
        },
        Price(){
            const url = "http://127.0.0.1:5000/index/"+this.indexCode+"/price";
            PriceChart(url, this.selectorName);
        },
        ROE(){
            const url = "http://127.0.0.1:5000/index/"+this.indexCode+"/roe";
            ROEChart(url, this.selectorName);
        },

        PEPercentile(){
            const url = "http://127.0.0.1:5000/index/"+this.indexCode+"/pe-percent";
            PEPercentileChart(url, this.selectorName);
        },
        PBPercentile(){
            const url = "http://127.0.0.1:5000/index/"+this.indexCode+"/pb-percent";
            PBPercentileChart(url, this.selectorName);
        },
        dailyChangePercentile(){
            const url = "http://127.0.0.1:5000/index/"+this.indexCode+"/daily-change-percent";
            DailyChangePercentileChart(url, this.selectorName);
        },
        yearChangePercentile(){
            const url = "http://127.0.0.1:5000/index/"+this.indexCode+"/year-change-percent";
            YearChangePercentileChart(url, this.selectorName);
        },
        TotalVolumes(){
            const url = "http://127.0.0.1:5000/index/"+this.indexCode+"/volumes";
            TotalVolumesChart(url, this.selectorName);
        }
    },  
}
</script>

<style scoped>

.index-100-detail {
    background: gainsboro;
    width: 80%;
    height: 900px;
    text-align: center;
    margin: 0 auto;
    float: left;
    /* margin-top: 20px; */
    
}
</style>