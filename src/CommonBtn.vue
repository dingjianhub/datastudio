<template>
    <div class="common-btn">
        <button class="common-btn-item" @click="PE">PE</button>
        <button class="common-btn-item" @click="Price">价格</button>
        <button class="common-btn-item" @click="PEPercentile">PE百分位</button>
        <button class="common-btn-item" @click="TotalVolumes">成交量</button>
    </div>
</template>

<script>
export default {
    methods: {
        Price(){
            // alert("Price");
        },
        PE(){
            // alert("PE");
        },
        PEPercentile(){
            // alert("PEPercentile");
        },
        TotalVolumes(){
            // alert("TotalVolumes");
        }
    },
}
</script>

<style scoped>
.common-btn {
    /* margin-top: 100px; */
    /* padding: 0 10px; */

}
.common-btn-item {
    display: block;
    width:100%;
    
    font-size: 20px;
    padding: 10px 0;
    /* margin: 5px 0; */
    border: 1px dotted #c0b7b7;

}
.common-btn-item:hover{
    font-size: 22px;
    cursor: pointer;
    background-color: #9de4a6;
    font-weight: bold;
}

</style>