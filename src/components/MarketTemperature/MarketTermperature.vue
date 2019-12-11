<template>

    <div id="main">
        <Header></Header>
        <div class="detial-aside-left">
            <!-- <CommonBtn></CommonBtn> -->
            <button class="common-btn-item" @click="changeInvestors">新增投资者</button>
            <button class="common-btn-item" @click="marketVolumes">市场成交量</button>
            <button class="common-btn-item" @click="totals">北向资金</button>
            <button class="common-btn-item" @click="shStockExchange">沪股通</button>
            <button class="common-btn-item" @click="szStockExchange">深股通</button>
            <button class="common-btn-item" @click="ASharesValues">A股市值</button>
            <button class="common-btn-item" @click="SHIndex">上证指数</button>
            <button class="common-btn-item" @click="SZIndex">深证指数</button>
        </div>
        
        <hr>
        <div class="market-temperature"></div>
    </div>
</template>

<script>

import Header from '../../Header';
import {
    TotalNorthMoney,
    TotalMarketVolumes,
    InvestorsCharts,
    ASharesValuesCharts,
    SHIndexCharts,
    SZIndexCharts,
} from '../../Charts'


export default {
    data() {
        return {
            baseurl: "http://127.0.0.1:5000/temperature/",
            selectorName: ".market-temperature"}
    },
    components:{
        Header,
        // CommonBtn
    },
    methods: {
        changeInvestors(){
            const url = this.baseurl + "investors";
            InvestorsCharts(url, this.selectorName);
        },
        marketVolumes(){
            const url = this.baseurl + "market-volumes";
            TotalMarketVolumes(url, this.selectorName);
        },
        totals(){
            // const url = `${this.host}:${this.port}/norty-money`
            const url = this.baseurl + "north-money"
            const queryString = "?market=all"
            TotalNorthMoney(url, queryString, this.selectorName);
        },
        shStockExchange(){
            const url = this.baseurl + "north-money"
            const queryString = "?market=sh"
            TotalNorthMoney(url, queryString, this.selectorName);
        },
        szStockExchange(){
            const url = this.baseurl + "north-money"
            const queryString = "?market=sz"
            TotalNorthMoney(url, queryString, this.selectorName);
        },
        ASharesValues(){
            const url = this.baseurl + "a-shares-values";
            ASharesValuesCharts(url, this.selectorName);
        },
        SHIndex(){
            const url = this.baseurl + "sh-index";
            SHIndexCharts(url, this.selectorName)
        },
        SZIndex(){
            const url = this.baseurl + "sz-index";
            SZIndexCharts(url, this.selectorName)
        },

    }
}
</script>

<style scoped>
.market-temperature {
    background: gainsboro;
    width: 80%;
    height: 800px;
    text-align: center;
    margin: 0 auto;
    float: left;
    /* margin-top: 20px; */
    
}
</style>