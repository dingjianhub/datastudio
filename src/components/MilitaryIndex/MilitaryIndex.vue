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
            <button class="common-btn-item" @click="ChangePercentile">涨跌幅</button>
            <button class="common-btn-item" @click="TotalVolumes">成交量</button>
        </div>
        
        <hr>
        <div class="military-index"></div>
    </div>
</template>

<script>
// import axios from 'axios';
// import echarts from 'echarts';
// import CommonBtn from '../../CommonBtn';
import Header from '../../Header';
import {   drawPEChart, 
                drawPBChart,
                drawPriceChart,
                drawROEChart,
                drawPEPercentileChart,
                drawPBPercentileChart,
                drawChangePercentileChart,
                drawTotalVolumesChart,
                } from '../../drawCharts';
// import drawPBChart from '../../drawCharts';

export default {
    data() {
        return {indexCode: "399967", selectorName: ".military-index"}
    },
    components:{
        Header,
        // CommonBtn
    },
    methods: {
        PE(){
            const url = "http://127.0.0.1:5000/index/"+this.indexCode+"/pe";
            drawPEChart(url, this.selectorName)
        },
        PB(){
            const url = "http://127.0.0.1:5000/index/"+this.indexCode+"/pb";
            drawPBChart(url, this.selectorName)
        },
        Price(){
            const url = "http://127.0.0.1:5000/index/"+this.indexCode+"/price";
            drawPriceChart(url, this.selectorName);
        },
        ROE(){
            const url = "http://127.0.0.1:5000/index/"+this.indexCode+"/roe";
            drawROEChart(url, this.selectorName);
        },

        PEPercentile(){
            const url = "http://127.0.0.1:5000/index/"+this.indexCode+"/pe-percent";
            drawPEPercentileChart(url, this.selectorName);
        },
        PBPercentile(){
            const url = "http://127.0.0.1:5000/index/"+this.indexCode+"/pb-percent";
            drawPBPercentileChart(url, this.selectorName);
        },
        ChangePercentile(){
            const url = "http://127.0.0.1:5000/index/"+this.indexCode+"/change-percent";
            drawChangePercentileChart(url, this.selectorName);
        },
        TotalVolumes(){
            const url = "http://127.0.0.1:5000/index/"+this.indexCode+"/volumes";
            drawTotalVolumesChart(url, this.selectorName);
        }
    },  
}
</script>

<style scoped>
*{
    margin: 0;
    padding: 0;
}

#main{
    overflow: hidden;
}

.detial-aside-left{
    width: 20%;

    background-color: #c0c2c9;
    float: left;
}

.common-btn-item {
    display: block;
    width:100%;
    height: 100px;
    font-size: 20px;
    padding: 20px 0;
    /* margin: 5px 0; */
    border: 1px dotted #c0b7b7;
    color: #0b2649
}
.common-btn-item:hover{
    font-size: 22px;
    cursor: pointer;
    background-color: #6d8bb1;
    font-weight: bold;
}

.military-index {
    background: gainsboro;
    width: 80%;
    height: 800px;
    text-align: center;
    margin: 0 auto;
    float: left;
    /* margin-top: 20px; */
    
}
</style>