import axios from 'axios';
import echarts from 'echarts';

const optionsSettings = {
    axis: {
        lineStyle: {
            color: "#022042",
            width: 2
        },
        xAxisTick: {
            inside:true,
            lineStyle:{
                width:2,
                type:"solid"
            }
        },
        yAxisTick: {
            inside:false,
            lineStyle:{
                width:2,
                type:"solid"
            }
        },
        yAxisSplitLine: {
            show: true,
            lineStyle: {
                color: "#0d76b3",
                width:2,
                type: "solid"
            }
        }
    },
    tooltip : {
        trigger: 'axis',
        axisPointer: {
            type: 'cross',
            label: {
                backgroundColor: '#6a7985'
            }
        }
    },
    toolbox: {
        show: true,
        showTitle: true,
        // left: "center",
        top: "top",
        right:10,
        feature: {
            // magicType: {show: true, type: ['line', 'bar']},
            // dataView: {},
            dataZoom: {
                yAxisIndex: "none"
            },
            saveAsImage: {},
            restore:{},
        }
    },
    dataZoom: [{startValue: "2019-07-01"}, {type: "inside"}],
    visualMap: {
        top: "middle",
        right: 20,
        pieces: [{
            gt: 0,
            lte: 10,
            color: '#33CC66 '
        }, {
            gt: 10,
            lte: 20,
            color: '#339966 '
        }, {
            gt: 20,
            lte: 30,
            color: '#336666 '
        }, {
            gt: 30,
            lte: 80,
            color: '#CC9966'
        },{
            gt: 80,
            lte: 100,
            color: '#CC0033 '
        }, ],
        outOfRange: {
            color: '#CC0033 '
        }
    },
}

export function PEChart(url, selectorName) {
    // 指数的PE
    const peChart = echarts.init(document.querySelector(selectorName));
    
    axios.get(url).then((res) => {
        // alert("res:" + res);
        let options = {
            title: {
                text: res.data.name + "-PE",
                left:"center",
                top: 20,
                // textAlign:"left"
            },
            xAxis: {
                type: "category",
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick: optionsSettings.axis.xAxisTick,
                axisLabel: {fontSize: 18},
                data: res.data.date
            },
            yAxis: {
                type: "value",
                axisLabel:{
                    fontSize:18, 
                    // formatter: "{value}"
                },
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick:optionsSettings.axis.yAxisTick,
                splitLine: optionsSettings.axis.yAxisSplitLine,
            },
            dataZoom: optionsSettings.dataZoom,
            tooltip: optionsSettings.tooltip,
            toolbox: optionsSettings.toolbox,
            // visualMap: optionsSettings.visualMap,
            series: [
                {
                    data: res.data.pe,
                    type:"line",
                    symbol:"none",
                    itemStyle: {
                        normal:{
                            color: "#0b2649",
                            lineStyle: {
                                width: 3
                            }
                        }
                    }
                }
            ]
        }
        // alert(options.title.text);
        peChart.setOption(options, true)
        
    });
}

export  function PBChart(url, selectorName) {
    // 指数的PB
    const pbChart = echarts.init(document.querySelector(selectorName));
    
    axios.get(url).then((res) => {
        // alert("res:" + res);
        let options = {
            title: {
                text: res.data.name + "-PB",
                left:"center",
                top: 20,
                // textAlign:"left"
            },
            xAxis: {
                type: "category",
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick: optionsSettings.axis.xAxisTick,
                axisLabel: {fontSize: 18},
                data: res.data.date
            },
            yAxis: {
                type: "value",
                axisLabel:{
                    fontSize:18, 
                    // formatter: "{value}"
                },
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick:optionsSettings.axis.yAxisTick,
                splitLine: optionsSettings.axis.yAxisSplitLine,
            },
            dataZoom: optionsSettings.dataZoom,
            tooltip: optionsSettings.tooltip,
            toolbox: optionsSettings.toolbox,
            // visualMap: optionsSettings.visualMap,
            series: [
                {
                    data: res.data.pb,
                    type:"line",
                    symbol:"none",
                    itemStyle: {
                        normal:{
                            color: "#0b2649",
                            lineStyle: {
                                width: 3
                            }
                        }
                    }
                }
            ]
        }
        // alert(options.title.text);
        pbChart.setOption(options, true)
    });
}

export  function PriceChart(url, selectorName) {
    // 指数当前的价位
    const priceChart = echarts.init(document.querySelector(selectorName));
    axios.get(url).then((res) => {
        // alert(res.data.price)
        if (!res.data.price){
            alert("未获取到[" + res.data.name + "]指数的价格");
            return
        }
        // alert("res:" + res);
        let options = {
            title: {
                text: res.data.name + "-价格",
                left:"center",
                top: 20,
                // textAlign:"left"
            },
            xAxis: {
                type: "category",
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick: optionsSettings.axis.xAxisTick,
                axisLabel: {fontSize: 18},
                data: res.data.date
            },
            yAxis: {
                type: "value",
                axisLabel:{
                    fontSize:18, 
                    // formatter: "{value}"
                },
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick:optionsSettings.axis.yAxisTick,
                splitLine: optionsSettings.axis.yAxisSplitLine,
            },
            dataZoom: optionsSettings.dataZoom,
            tooltip: optionsSettings.tooltip,
            toolbox: optionsSettings.toolbox,
            // visualMap: optionsSettings.visualMap,
            series: [
                {
                    data: res.data.price,
                    type:"line",
                    symbol:"none",
                    itemStyle: {
                        normal:{
                            color: "#0b2649",
                            lineStyle: {
                                width: 3
                            }
                        }
                    }
                }
            ]
        }
        // alert(options.title.text);
        priceChart.setOption(options, true)
    });
}

export  function ROEChart(url, selectorName) {
    // 指数的ROE
    const ROEChart = echarts.init(document.querySelector(selectorName));
    
    axios.get(url).then((res) => {
        // alert("res:" + res.data.roe);
        let options = {
            title: {
                text: res.data.name + "-ROE(%)",
                left:"center",
                top: 20,
                // textAlign:"left"
            },
            xAxis: {
                type: "category",
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick: optionsSettings.axis.xAxisTick,
                axisLabel: {fontSize: 18},
                data: res.data.date
            },
            yAxis: {
                type: "value",
                axisLabel:{
                    fontSize:18, 
                    formatter: "{value} %"
                },
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick:optionsSettings.axis.yAxisTick,
                splitLine: optionsSettings.axis.yAxisSplitLine,
            },
            dataZoom: optionsSettings.dataZoom,
            tooltip: optionsSettings.tooltip,
            toolbox: optionsSettings.toolbox,
            // visualMap: optionsSettings.visualMap,
            series: [
                {
                    data: res.data.roe,
                    type:"line",
                    symbol:"none",
                    itemStyle: {
                        normal:{
                            color: "#0b2649",
                            lineStyle: {
                                width: 3
                            }
                        }
                    }
                }
            ]
        }
        // alert(options.title.text);
        ROEChart.setOption(options, true)
    });
}

export  function PEPercentileChart(url, selectorName) {
    // PE百分位
    const chart = echarts.init(document.querySelector(selectorName));
    
    axios.get(url).then((res) => {
        // alert("res:" + res.data.roe);
        if (! res.data.pePercent){
            alert(`${res.data.name}还没有PE百分位`);
            return 
        }
        let options = {
            title: {
                text: res.data.name + "-PE百分位(%)",
                left:"center",
                top: 20,
                // textAlign:"left"
            },
            xAxis: {
                type: "category",
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick: optionsSettings.axis.xAxisTick,
                axisLabel: {fontSize: 18},
                data: res.data.date
            },
            yAxis: {
                type: "value",
                interval:10,
                axisLabel:{
                    fontSize:18, 
                    formatter: "{value} %"
                },
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick:optionsSettings.axis.yAxisTick,
                splitLine: optionsSettings.axis.yAxisSplitLine,
            },
            dataZoom: optionsSettings.dataZoom,
            tooltip: optionsSettings.tooltip,
            toolbox: optionsSettings.toolbox,
            visualMap: optionsSettings.visualMap,
            series: [
                {
                    data: res.data.pePercent,
                    type:"line",
                    symbol:"none",
                    itemStyle: {
                        normal:{
                            color: "#01071d",
                            lineStyle: {
                                width: 3
                            }
                        }
                    },
                }
            ]
        }
        // alert(options.title.text);
        chart.setOption(options, true)
    });
}

export  function PBPercentileChart(url, selectorName) {
    // 指数PB百分位
    const chart = echarts.init(document.querySelector(selectorName));
    
    axios.get(url).then((res) => {
        // alert("res:" + res.data.roe);
        // alert(res.data.pbPercent)
        if (! res.data.pbPercent){
            alert(`${res.data.name}还没有PB百分位`);
            return 
        }
        let options = {
            title: {
                text: res.data.name + "-PB百分位(%)",
                left:"center",
                top: 20,
                // textAlign:"left"
            },
            xAxis: {
                type: "category",
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick: optionsSettings.axis.xAxisTick,
                axisLabel: {fontSize: 18},
                data: res.data.date
            },
            yAxis: {
                type: "value",
                interval:10,
                axisLabel:{
                    fontSize:18, 
                    formatter: "{value} %"
                },
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick:optionsSettings.axis.yAxisTick,
                splitLine: optionsSettings.axis.yAxisSplitLine,
            },
            dataZoom: optionsSettings.dataZoom,
            tooltip: optionsSettings.tooltip,
            toolbox: optionsSettings.toolbox,
            visualMap: optionsSettings.visualMap,
            series: [
                {
                    data: res.data.pbPercent,
                    type:"line",
                    symbol:"none",
                    itemStyle: {
                        normal:{
                            color: "#01071d",
                            lineStyle: {
                                width: 3
                            }
                        }
                    }
                }
            ]
        }
        // alert(options.title.text);
        chart.setOption(options, true)
    });
}

export  function DailyChangePercentileChart(url, selectorName) {
    const chart = echarts.init(document.querySelector(selectorName));
    
    axios.get(url).then((res) => {
        if (!res.data.dailyChPercent) {
            alert("未获取到[" + res.data.name + "]指数的日涨跌幅");
            return
        }
        // alert("res:" + res.data.roe);
        let options = {
            title: {
                text: res.data.name + "-涨跌幅(%)",
                left:"center",
                top: 20,
                // textAlign:"left"
            },
            xAxis: {
                type: "category",
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick: optionsSettings.axis.xAxisTick,
                axisLabel: {fontSize: 18},
                data: res.data.date
            },
            yAxis: {
                type: "value",
                // interval:2,
                axisLabel:{
                    fontSize:18, 
                    formatter: "{value} %"
                },
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick:optionsSettings.axis.yAxisTick,
                splitLine: optionsSettings.axis.yAxisSplitLine,
            },
            dataZoom: optionsSettings.dataZoom,
            tooltip: optionsSettings.tooltip,
            toolbox: optionsSettings.toolbox,
            visualMap: {top: "middle",
            right: 20,
            pieces: [{
                gt: 0,
                color: '#CC0033 '
            }, {
                lt: 0,
                color: '#339966 '
            }, ],
            // outOfRange: {
            //     color: '#CC0033 '
            // }
            },
            series: [
                {
                    data: res.data.dailyChPercent,
                    type:"bar",
                    symbol:"none",
                    // label: {
                    //     normal: {
                    //         show: true,
                    //         position: 'left'
                    //     }
                    // },
                    itemStyle: {
                        normal:{
                            color: "#0b2649",
                            lineStyle: {
                                width: 3
                            }
                        }
                    }
                }
            ]
        }
        // alert(options.title.text);
        chart.setOption(options, true)
    });
}

export  function YearChangePercentileChart(url, selectorName) {
    const chart = echarts.init(document.querySelector(selectorName));
    
    axios.get(url).then((res) => {
        // alert(res.data.yearChPercent);
        if (res.data.errno) {
            alert("未获取到[" + res.data.name + "]指数的年涨跌幅");
            return
        }
        // alert("res:" + res.data.roe);
        let options = {
            title: {
                text: res.data.name + "-年涨跌幅(%)",
                left:"center",
                top: 20,
                // textAlign:"left"
            },
            xAxis: {
                type: "category",
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick: optionsSettings.axis.xAxisTick,
                axisLabel: {fontSize: 18},
                data: res.data.date
            },
            yAxis: {
                type: "value",
                // interval:2,
                axisLabel:{
                    fontSize:18, 
                    formatter: "{value} %"
                },
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick:optionsSettings.axis.yAxisTick,
                splitLine: optionsSettings.axis.yAxisSplitLine,
            },
            dataZoom: optionsSettings.dataZoom,
            tooltip: optionsSettings.tooltip,
            toolbox: optionsSettings.toolbox,
            visualMap: {top: "middle",
            right: 20,
            pieces: [{
                gt: 0,
                color: '#CC0033 '
            }, {
                lt: 0,
                color: '#339966 '
            }, ],
            // outOfRange: {
            //     color: '#CC0033 '
            // }
            },
            series: [
                {
                    data: res.data.yearChPercent,
                    type:"bar",
                    symbol:"none",
                    label: {
                        normal: {
                            show: true,
                            position: 'inside',
                            fontWeight:"bold"
                        }
                    },
                    itemStyle: {
                        normal:{
                            color: "#0b2649",
                            lineStyle: {
                                width: 3
                            }
                        }
                    }
                }
            ]
        }
        // alert(options.title.text);
        chart.setOption(options, true)
    });
}

export  function TotalVolumesChart(url, selectorName) {
    // 指数的成交量
    
    const chart = echarts.init(document.querySelector(selectorName));
    
    axios.get(url).then((res) => {
        if (! res.data.totalVolumes) {
            alert("未获取到[" + res.data.name + "]指数的成交量");
            return
        }
        // alert("res:" + res.data.roe);
        let options = {
            title: {
                text: res.data.name + "-成交量(亿元)",
                left:"center",
                top: 20,
                // textAlign:"left"
            },
            xAxis: {
                type: "category",
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick: optionsSettings.axis.xAxisTick,
                axisLabel: {fontSize: 18},
                data: res.data.date
            },
            yAxis: {
                type: "value",
                axisLabel:{
                    fontSize:18, 
                    formatter: "{value} 亿元"
                },
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick:optionsSettings.axis.yAxisTick,
                splitLine: optionsSettings.axis.yAxisSplitLine,
            },
            dataZoom: optionsSettings.dataZoom,
            tooltip: optionsSettings.tooltip,
            toolbox: optionsSettings.toolbox,
            series: [
                {
                    data: res.data.totalVolumes,
                    type:"bar",
                    symbol:"none",
                    itemStyle: {
                        normal:{
                            color: "#0b2649",
                            lineStyle: {
                                width: 3
                            }
                        }
                    }
                }
            ]
        }
        // alert(options.title.text);
        chart.setOption(options, true)
    });
}


export  function TotalNorthMoney(url, queryString, selectorName) {
    // 指数的成交量
    
    const chart = echarts.init(document.querySelector(selectorName));
    
    axios.get(url + queryString).then((res) => {

        if (! res.data.data_list) {
            alert("获取失败");
            return
        }
        let text = "";
        if (queryString === "?market=sh"){
            text = "沪股通";
        }else if (queryString === "?market=sz"){
            text = "深股通";
        } else{
            text = "北向资金合计";
        }
        // alert("res:" + res.data.roe);
        let options = {
            title: {
                text: text,
                left:"center",
                top: 20,
                // textAlign:"left"
            },
            xAxis: {
                type: "category",
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick: optionsSettings.axis.xAxisTick,
                axisLabel: {fontSize: 18},
                data: res.data.date
            },
            yAxis: {
                type: "value",
                // interval: 50,
                axisLabel:{
                    fontSize:18, 
                    formatter: "{value} 亿元"
                },
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick:optionsSettings.axis.yAxisTick,
                splitLine: optionsSettings.axis.yAxisSplitLine,
            },
            dataZoom: optionsSettings.dataZoom,
            tooltip: optionsSettings.tooltip,
            toolbox: optionsSettings.toolbox,
            visualMap: {top: "middle",
            right: 20,
            pieces: [{
                gt: 0,
                color: '#CC0033 '
            }, {
                lt: 0,
                color: '#339966 '
            }, ],
            // outOfRange: {
            //     color: '#CC0033 '
            // }
            },
            series: [
                {
                    data: res.data.data_list,
                    type:"bar",
                    symbol:"none",
                    // label: {
                    //     normal: {
                    //         show: true,
                    //         position: 'top'
                    //     }
                    // },
                    itemStyle: {
                        normal:{
                            color: "#0b2649",
                            lineStyle: {
                                width: 3
                            }
                        }
                    }
                }
            ]
        }
        // alert(options.title.text);
        chart.setOption(options, true)
    });
}

export  function TotalMarketVolumes(url, selectorName) {
    // 指数的成交量
    const chart = echarts.init(document.querySelector(selectorName));
    
    axios.get(url).then((res) => {
        // alert(res.data.sh_data_list)
        if (res.data.errno) {
            alert("获取失败");
            return
        }
        
        // alert("res:" + res.data.roe);
        let options = {
            title: {
                text: "市场成交量",
                left:"center",
                top: 20,
                // textAlign:"left"
            },
            xAxis: {
                type: "category",
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick: optionsSettings.axis.xAxisTick,
                axisLabel: {fontSize: 18},
                data: res.data.date
            },
            yAxis: {
                type: "value",
                interval: 3000,
                axisLabel:{
                    fontSize:18, 
                    formatter: "{value} 亿元"
                },
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick:optionsSettings.axis.yAxisTick,
                splitLine: optionsSettings.axis.yAxisSplitLine,
            },
            legend: {
                data: ["沪市", "深市", "两市合计"]
            },
            dataZoom: optionsSettings.dataZoom,
            tooltip: optionsSettings.tooltip,
            toolbox: optionsSettings.toolbox,           
            series: [
                {
                    data: res.data.sh_data_list,
                    name: "沪市",
                    type:"line",
                    symbol:"none",
                    itemStyle: {
                        normal:{
                            // color: "#0b2649",
                            lineStyle: {
                                width: 3
                            }
                        }
                    }
                },
                {
                    data: res.data.sz_data_list,
                    type:"line",
                    name: "深市",
                    symbol:"none",
                    itemStyle: {
                        normal:{
                            // color: "#0b2649",
                            lineStyle: {
                                width: 3
                            }
                        }
                    }
                },
                {
                    data: res.data.total_volumes,
                    type:"line",
                    name: "两市合计",
                    symbol:"none",
                    itemStyle: {
                        normal:{
                            // color: "#0b2649",
                            lineStyle: {
                                width: 3
                            }
                        }
                    }
                }
            ]
        }
        // alert(options.title.text);
        chart.setOption(options, true)
    });
}

export function InvestorsCharts(url, selectorName) {
    // 指数的PE
    const peChart = echarts.init(document.querySelector(selectorName));
    
    axios.get(url).then((res) => {
        // alert("res:" + res);
        let options = {
            title: {
                text: "投资者数量变化",
                left:"center",
                top: 20,
                // textAlign:"left"
            },
            xAxis: {
                type: "category",
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick: optionsSettings.axis.xAxisTick,
                axisLabel: {fontSize: 18},
                data: res.data.date
            },
            yAxis: {
                type: "value",
                axisLabel:{
                    fontSize:18, 
                    formatter: "{value} 万"
                },
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick:optionsSettings.axis.yAxisTick,
                splitLine: optionsSettings.axis.yAxisSplitLine,
            },
            dataZoom: optionsSettings.dataZoom,
            tooltip: optionsSettings.tooltip,
            toolbox: optionsSettings.toolbox,
            // visualMap: optionsSettings.visualMap,
            series: [
                {
                    data: res.data.data_list,
                    type:"bar",
                    symbol:"none",
                    itemStyle: {
                        normal:{
                            color: "#0b2649",
                            lineStyle: {
                                width: 3
                            }
                        }
                    }
                }
            ]
        }
        // alert(options.title.text);
        peChart.setOption(options, true)
        
    });
}

export function ASharesValuesCharts(url, selectorName) {
    // A股流通市值
    const peChart = echarts.init(document.querySelector(selectorName));
    axios.get(url).then((res) => {
        // alert("res:" + res);
        let options = {
            title: {
                text: "A股流通市值",
                left:"center",
                top: 20,
                // textAlign:"left"
            },
            xAxis: {
                type: "category",
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick: optionsSettings.axis.xAxisTick,
                axisLabel: {fontSize: 18},
                data: res.data.date
            },
            yAxis: {
                type: "value",
                axisLabel:{
                    fontSize:18, 
                    formatter: "{value} 亿"
                },
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick:optionsSettings.axis.yAxisTick,
                splitLine: optionsSettings.axis.yAxisSplitLine,
            },
            dataZoom: optionsSettings.dataZoom,
            tooltip: optionsSettings.tooltip,
            toolbox: optionsSettings.toolbox,
            // visualMap: optionsSettings.visualMap,
            series: [
                {
                    data: res.data.data_list,
                    type:"line",
                    symbol:"none",
                    itemStyle: {
                        normal:{
                            color: "#0b2649",
                            lineStyle: {
                                width: 3
                            }
                        }
                    }
                }
            ]
        }
        // alert(options.title.text);
        peChart.setOption(options, true)
        
    });
}

export function SHIndexCharts(url, selectorName) {
    // A股流通市值
    
    const peChart = echarts.init(document.querySelector(selectorName));
    axios.get(url).then((res) => {
        // alert("res:" + res.data.data_list);
        let options = {
            title: {
                text: "上证指数",
                left:"center",
                top: 20,
                // textAlign:"left"
            },
            xAxis: {
                type: "category",
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick: optionsSettings.axis.xAxisTick,
                axisLabel: {fontSize: 18},
                data: res.data.date
            },
            yAxis: {
                type: "value",
                axisLabel:{
                    fontSize:18, 
                    formatter: "{value}"
                },
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick:optionsSettings.axis.yAxisTick,
                splitLine: optionsSettings.axis.yAxisSplitLine,
            },
            dataZoom: optionsSettings.dataZoom,
            tooltip: optionsSettings.tooltip,
            toolbox: optionsSettings.toolbox,
            // visualMap: optionsSettings.visualMap,
            series: [
                {
                    data: res.data.data_list,
                    type:"line",
                    symbol:"none",
                    itemStyle: {
                        normal:{
                            color: "#0b2649",
                            lineStyle: {
                                width: 3
                            }
                        }
                    }
                }
            ]
        }
        // alert(options.title.text);
        peChart.setOption(options, true)
        
    });
}

export function SZIndexCharts(url, selectorName) {
    // A股流通市值
    
    const peChart = echarts.init(document.querySelector(selectorName));
    axios.get(url).then((res) => {
        // alert("res:" + res.data.data_list);
        let options = {
            title: {
                text: "深证成指",
                left:"center",
                top: 20,
                // textAlign:"left"
            },
            xAxis: {
                type: "category",
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick: optionsSettings.axis.xAxisTick,
                axisLabel: {fontSize: 18},
                data: res.data.date
            },
            yAxis: {
                type: "value",
                axisLabel:{
                    fontSize:18, 
                    formatter: "{value}"
                },
                axisLine:{lineStyle: optionsSettings.axis.lineStyle},
                axisTick:optionsSettings.axis.yAxisTick,
                splitLine: optionsSettings.axis.yAxisSplitLine,
            },
            dataZoom: optionsSettings.dataZoom,
            tooltip: optionsSettings.tooltip,
            toolbox: optionsSettings.toolbox,
            // visualMap: optionsSettings.visualMap,
            series: [
                {
                    data: res.data.data_list,
                    type:"line",
                    symbol:"none",
                    itemStyle: {
                        normal:{
                            color: "#0b2649",
                            lineStyle: {
                                width: 3
                            }
                        }
                    }
                }
            ]
        }
        // alert(options.title.text);
        peChart.setOption(options, true)
        
    });
}