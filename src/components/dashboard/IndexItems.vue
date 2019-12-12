<template>
    <div class="aside-letf-content">
        <label class="index-group-content">低估指数</label>
        <ul class="low-index-group" v-for="item in lowIndex" :key="item.code">
            <li class="low-index-group-item">
                <a :href="'#/' + item.code" class="group-item-link">
                    {{item.name}}
                    <span class="price-item">
                        ({{item.price}})
                    </span>
                </a>
            </li>
        </ul>
        <label class="index-group-content">估值适中</label>
        <ul class="mid-index-group" v-for="item in midIndex" :key="item.code">
            <li class="mid-index-group-item">
                <a :href="'#/' + item.code" class="group-item-link">
                    {{item.name}}
                    <span class="price-item">
                        ({{item.price}})
                    </span>
                </a>
            </li>
        </ul>
        <label class="index-group-content">高估指数</label>
        <ul class="high-index-group" v-for="item in highIndex" :key="item.code">
            <li class="high-index-group-item">
                <a :href="'#/' + item.code" class="group-item-link">
                    {{item.name}}
                    <span class="price-item">
                        ({{item.price}})
                    </span>
                </a>
            </li>
        </ul>
        <label class="index-group-content">温度指标</label>
        <ul class="temperatures-index" >
            <li class="temperatures-index-item"><a href="#/market-temperature" class="group-item-link">北向资金</a></li>
            <li class="temperatures-index-item"><a href="#/market-temperature" class="group-item-link">市场成交量</a></li>
            <li class="temperatures-index-item"><a href="#/market-temperature" class="group-item-link">新增投资者</a></li>
        </ul>
    </div>
</template> 

<script>
import axios from "axios";
export default {
    data(){
        return {
            lowIndex:[],
            midIndex:[],
            highIndex:[]
            }
    },
    created(){
        axios.get("http://127.0.0.1:5000/index/group").then((res) => {
            this.lowIndex = res.data.lowIndex;
            this.midIndex = res.data.midIndex;
            this.highIndex = res.data.highIndex;
        
        })
    }

}
</script>

<style scoped>
.aside-letf-content {
    float: left;
    width: 20%;
    background-color: #cfd2d5
}
.index-group-content{
    /* background-color: #1e9407 */
    font-size: 22px;
    font-weight: bold;
}
.low-index-group{
    background-color: #1e9407
}
.low-index-group-item {
    border-bottom: 1px dotted #cfd2d5;
    cursor: pointer;
    padding: 3px 0;
}
.low-index-group-item:hover{
    background-color: #e4ecf6;
}
.mid-index-group{
    background-color: #9c9e25
}
.mid-index-group-item {
    border-bottom: 1px dotted #cfd2d5;
    cursor: pointer;
    padding: 3px 0;
}
.mid-index-group-item:hover{
    background-color: #e4ecf6;
}
.high-index-group{
    background-color: #f30101
}
.high-index-group-item {
    border-bottom: 1px dotted #cfd2d5;
    cursor: pointer;
    padding: 3px 0;
}
.high-index-group-item:hover{
    background-color: #e4ecf6;
}
.temperatures-index {
    background-color: #3a98afe7;
}
.temperatures-index-item {
    border-bottom: 1px dotted #cfd2d5;
    cursor: pointer;
    padding: 3px 0;
}
.temperatures-index-item:hover{
    background-color: #e4ecf6;
}
.group-item-link{
    font-size: 18px;
    text-decoration: none;
    color: #000;
    /* font-weight: bold; */
}

.group-item-link:hover{
    /* font-size: 20px; */
    font-weight: bold;
}

.price-item {
    font-size: 16px;
}


</style>