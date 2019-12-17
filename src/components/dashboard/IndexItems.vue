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
        <a href="#/market-temperature" class="temperatures-link">温度指标</a>
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
        let url = "http://127.0.0.1:5000/index/group";
        axios.get(url).then((res) => {
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
    font-size: 18px;
    font-weight: bold;
}
.low-index-group{
    background-color: #1e9407
}
.low-index-group-item {
    border-bottom: 1px dotted #cfd2d5;
    cursor: pointer;
    /* padding: 1px 0; */
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
    /* padding: 1px 0; */
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
    /* padding: 1px 0; */
}
.high-index-group-item:hover{
    background-color: #e4ecf6;
}
.temperatures-link {
    display: block;
    height: 30px;
    line-height: 35px;
    font-size:16px;
    color: #000;
    background-color: #3a98afe7;
    text-decoration: none;
}

.temperatures-link:hover {
    font-weight: bold;
    background-color: #e4ecf6;
}


.group-item-link{
    font-size: 14px;
    text-decoration: none;
    color: #000;
    /* font-weight: bold; */
}

.group-item-link:hover{
    /* font-size: 18px; */
    font-weight: bold;
}

.price-item {
    font-size: 12px;
}


</style>
