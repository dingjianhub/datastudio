<template>

    <div class="main">
        <p>{{ msg }}</p>
    </div>
</template>

<script>
import axios from 'axios';
import echarts from 'echarts';

export default {
    data() {
        return {msg: "home page"}
    }
    created() {
        this.getDatas()
    },
    methods: {
        o_init(options){
            this.myChart = echarts.init(document.getElementById(".main"));
            this.myChart.setOption(options);
        },
        getDatas(){
            axios.get("http://127.0.0.1:5000/index/000993/pe").then((res) => {
                let options = {
                    title: {
                        text: res.data.name + "PE"
                    },
                    xAxis: {
                        type: "category",
                        data: res.data.date
                    },
                    yAxis: {
                        type: "value"
                    },
                    series: [
                        {
                            data: res.data.pe,
                            type:"line"
                        }
                    ]
                }
                // console.log(res.data.date);
                // console.log(res.data.pe);
                this.o_init(options);
            });
        }
    },  
}
</script>

<style scoped>
*{
    margin: 0;
    padding: 0;
}
    #main {
        background: gainsboro;
        width: 600px;
        height: 400px;
    }
</style>