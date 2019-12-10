<template>
    <div class="header">
        <div class="contanier">
            <a href="/" class="header-logo ">DataStudio</a>
            <!-- <div class="search ">
                <form action=" http://127.0.0.1:5000/" @submit="checkForm" method="get">
                    <input type="text" v-model.trim="queryString" vname="q" autocomplete="off" placeholder="请输入指数...." class="search-inputbox " />
                    <input type="submit" value="搜索" class="search-btn">
                </form>
                <ul class="search-layer" v-for="index in queryResults" :key="index">
                    <li class="search-layer-item">{{ index }}</li>
                </ul>
            </div> -->
        </div>
    </div>
</template>

<script>
export default {
    
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
    width: 100%;
    /* height: 100px; */
    line-height: 100px;
    float: left;
    margin-left: 60px;
    text-decoration: none;
    font-size: 20px;
    font-weight: bold;
}
</style>