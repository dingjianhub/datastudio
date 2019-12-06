<template>
    <div id="dashboard">
        <div id="header">
            <h1>Header</h1>
        </div>
        <div id="container">
            <div id="aside">
                <h1>Aside</h1>
            </div>
            <div id="main">
                <h1>Main</h1>
            </div>
        </div>
    </div>
</template>


<script>
export default {
    
}
</script>


<style scoped>

#header{
    height: 200px;
    background: red;
    margin: 0;
}

#container{
    height: 800px;
    /* background: pink; */
    position: relative;
    overflow: hidden;
}

#container #aside {
    width: 20%;
    height: 100%;
    float: left;
    /* position: absolute; */
    display: block;
    background: blue;
}

#container #main {
    width: 80%;
    height: 100%;
    float: right;
    /* position: absolute; */
    display: block;
    background: pink;
}
</style>