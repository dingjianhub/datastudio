<template>
    <div id="dashboard">
        <Header></Header>
        <hr>
        <div id="main">
            <IndexItems></IndexItems>
            <MainContent></MainContent>
            
        </div>
    </div>
</template>


<script>
import axios from 'axios';
import IndexItems from './IndexItems';
import MainContent from './content';
import Header from '../../Header';

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
    },
    components: {
        Header,
        IndexItems,
        MainContent,

    }
}
</script>


<style scoped>
/* 
.header {
    width: 100%;
    height: 100px;
    background-color: #f3f5f7;
    float: hidden;
} 
*/
/* 
.header-logo {
    display: block;
    width: 100%;
    line-height: 100px;
    float: left;
    margin-left: 60px;
    text-decoration: none;
    font-size: 20px;
    font-weight: bold;
}
 */

#aside-left {
    width: 20%;
    background: #cbd3cc;
    float: left;
}

#mian-content{
    width: 80%;
    background: #034c94;
    float: right;
}
</style>
