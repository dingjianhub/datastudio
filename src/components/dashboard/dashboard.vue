<template>
    <div id="dashboard">
        <div class="header">
            <div class="contanier">
                <a href="/" class="header-logo ">DataStudio</a>
                <div class="search ">
                    <form action=" http://127.0.0.1:5000/" @submit="checkForm" method="get">
                        <input type="text" v-model.trim="queryString" vname="q" autocomplete="off" placeholder="请输入指数...." class="search-inputbox " />
                        <input type="submit" value="搜索" class="search-btn">
                    </form>
                    <ul class="search-layer" v-for="index in queryResults" :key="index">
                        <li class="search-layer-item">{{ index }}</li>
                        <!-- <li class="search-layer-item">test2</li>
                        <li class="search-layer-item">test3</li> -->
                    </ul>
                </div>
            </div>
            
            
        </div>
        <!-- <hr> -->
        <!-- <div id="container">
            <div id="aside">
                <h1>Aside</h1>
            </div>
            <div id="main">
                <h1>Main</h1>
            </div>
        </div> -->
    </div>
</template>


<script>
import axios from 'axios';

// 延迟访问，减少对服务器压力
const delayRequest = (function () {
    let timer = 0;
    return function (callback,ms) {
        clearTimeout(timer);
        timer = setTimeout(callback, ms);
    };
})()
export default {
    data(){
        return{
            queryString: "",
            queryResults: []
        }
    },
    methods: {
        checkForm(e){
            if (this.queryString){
                return true;
            }
            e.preventDefault();
        },
        fetchData(){
            axios.get("http://127.0.0.1:5000/search").then((res) => {
                // console.log(res);
                this.queryResults = res.data.results;
                // alert(res.data.results);
                // alert(this.queryResults);
            })
        }
    },
    watch: {
        // 监听input标签的数据变化
        queryString(){
            delayRequest(()=>{
                this.fetchData()
            }, 300);
        }
    }
}
</script>


<style scoped>
.header {
    width: 100%;
    height: 100px;
    background-color: #f3f5f7;
    float: hidden;
}


.header-logo {
    display: block;
    width: 100px;
    /* height: 100px; */
    line-height: 100px;
    float: left;
    margin-left: 60px;
    text-decoration: none;
}
.search {
    position: relative;
    /* border-top: 1px solid #cfd2d5; */
    float: right;
    margin: 30px 60px 0 0;
}

.search-inputbox {
    width: 680px;
    height: 40px;
    line-height: 40px;
    border: 1px solid #6eb5f8;
    padding: 0 10px;
    color: #333;
    font-size: 16px;
    /* font-weight: bolder; */
    background-color: #fff;
}

.search-btn{
    width: 80px;
    height: 42px;
    line-height: 40px;
    background-color: #07111b;
    font-size: 16px;
    text-align: center;
    cursor: pointer;
    color: #fff;
    border:none;
    
}

.search-layer {
    width:99.78%;
    
    position: absolute;
    top:100%;
    /* left: 0; */
    background-color: #fff;
    border: 1px solid #cfd2d5;
    display: block;
}

.search-layer-item {
    height: 24px;
    line-height: 24px;
    padding: 0 10px;
    cursor: pointer;
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
    /* left: 0; */
    

}
.search-layer-item:hover{
    background-color: #f3f5f7;
}
</style>