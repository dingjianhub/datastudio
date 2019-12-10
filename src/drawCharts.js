import axios from 'axios';
import echarts from 'echarts';

export function drawPEChart(url, selectorName) {
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
            tooltip : {
                trigger: 'axis',
                axisPointer: {
                    type: 'cross',
                    label: {
                        backgroundColor: '#6a7985'
                    }
                }
            },
            xAxis: {
                // name: "全指信息",
                // nameLocation: "center",
                // nameGap: "40",
                // nameTextStyle: {fontWeight: "bolder", fontSize: "16"},
                type: "category",
                axisTick:{inside:true},
                axisLabel: {fontSize: 16},
                data: res.data.date
            },
            yAxis: {
                type: "value",
                axisLabel:{fontSize:16},
            },
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

export  function drawPBChart(url, selectorName) {
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
            tooltip : {
                trigger: 'axis',
                axisPointer: {
                    type: 'cross',
                    label: {
                        backgroundColor: '#6a7985'
                    }
                }
            },
            xAxis: {
                // name: "全指信息",
                // nameLocation: "center",
                // nameGap: "40",
                // nameTextStyle: {fontWeight: "bolder", fontSize: "16"},
                type: "category",
                axisTick:{inside:true},
                axisLabel: {fontSize: 16},
                data: res.data.date
            },
            yAxis: {
                type: "value",
                axisLabel:{fontSize:16},
            },
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

export  function drawPriceChart(url, selectorName) {
    // 指数当前的价位
    const priceChart = echarts.init(document.querySelector(selectorName));
    
    axios.get(url).then((res) => {
        // alert("res:" + res);
        let options = {
            title: {
                text: res.data.name + "-价格",
                left:"center",
                top: 20,
                // textAlign:"left"
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
            xAxis: {
                // name: "全指信息",
                // nameLocation: "center",
                // nameGap: "40",
                // nameTextStyle: {fontWeight: "bolder", fontSize: "16"},
                type: "category",
                axisTick:{inside:true},
                axisLabel: {fontSize: 16},
                data: res.data.date
            },
            yAxis: {
                type: "value",
                axisLabel:{fontSize:16},
            },
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

export  function drawROEChart(url, selectorName) {
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
            tooltip : {
                trigger: 'axis',
                axisPointer: {
                    type: 'cross',
                    label: {
                        backgroundColor: '#6a7985'
                    }
                }
            },
            xAxis: {
                // name: "全指信息",
                // nameLocation: "center",
                // nameGap: "40",
                // nameTextStyle: {fontWeight: "bolder", fontSize: "16"},
                type: "category",
                axisTick:{inside:true},
                axisLabel: {fontSize: 16},
                data: res.data.date
            },
            yAxis: {
                type: "value",
                axisLabel:{fontSize:16, formatter: "{value} %"},
            },
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

export  function drawPEPercentileChart(url, selectorName) {
    // PE百分位
    const chart = echarts.init(document.querySelector(selectorName));
    
    axios.get(url).then((res) => {
        // alert("res:" + res.data.roe);
        let options = {
            title: {
                text: res.data.name + "-PE百分位(%)",
                left:"center",
                top: 20,
                // textAlign:"left"
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
            xAxis: {
                // name: "全指信息",
                // nameLocation: "center",
                // nameGap: "40",
                // nameTextStyle: {fontWeight: "bolder", fontSize: "16"},
                type: "category",
                axisTick:{inside:true},
                axisLabel: {fontSize: 16},
                data: res.data.date
            },
            yAxis: {
                type: "value",
                axisLabel:{fontSize:16, formatter: "{value} %"},
            },
            series: [
                {
                    data: res.data.pePercent,
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
        chart.setOption(options, true)
    });
}

export  function drawPBPercentileChart(url, selectorName) {
    // 指数PB百分位
    const chart = echarts.init(document.querySelector(selectorName));
    
    axios.get(url).then((res) => {
        // alert("res:" + res.data.roe);
        let options = {
            title: {
                text: res.data.name + "-PB百分位(%)",
                left:"center",
                top: 20,
                // textAlign:"left"
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
            xAxis: {
                // name: "全指信息",
                // nameLocation: "center",
                // nameGap: "40",
                // nameTextStyle: {fontWeight: "bolder", fontSize: "16"},
                type: "category",
                axisTick:{inside:true},
                axisLabel: {fontSize: 16},
                data: res.data.date
            },
            yAxis: {
                type: "value",
                axisLabel:{fontSize:16, formatter: "{value} %"},
            },
            series: [
                {
                    data: res.data.pbPercent,
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
        chart.setOption(options, true)
    });
}

export  function drawChangePercentileChart(url, selectorName) {
    const chart = echarts.init(document.querySelector(selectorName));
    
    axios.get(url).then((res) => {
        // alert("res:" + res.data.roe);
        let options = {
            title: {
                text: res.data.name + "-涨跌幅(%)",
                left:"center",
                top: 20,
                // textAlign:"left"
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
            xAxis: {
                // name: "全指信息",
                // nameLocation: "center",
                // nameGap: "40",
                // nameTextStyle: {fontWeight: "bolder", fontSize: "16"},
                type: "category",
                axisTick:{inside:true},
                axisLabel: {fontSize: 16},
                data: res.data.date
            },
            yAxis: {
                type: "value",
                axisLabel:{
                    fontSize:16, 
                    formatter: "{value} %"
                },
            },
            series: [
                {
                    data: res.data.chPercent,
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
        chart.setOption(options, true)
    });
}

export  function drawTotalVolumesChart(url, selectorName) {
    // 指数的成交量
    const chart = echarts.init(document.querySelector(selectorName));
    
    axios.get(url).then((res) => {
        // alert("res:" + res.data.roe);
        let options = {
            title: {
                text: res.data.name + "-成交量(亿元)",
                left:"center",
                top: 20,
                // textAlign:"left"
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
            xAxis: {
                // name: "全指信息",
                // nameLocation: "center",
                // nameGap: "40",
                // nameTextStyle: {fontWeight: "bolder", fontSize: "16"},
                type: "category",
                axisTick:{inside:true},
                axisLabel: {fontSize: 16},
                data: res.data.date
            },
            yAxis: {
                type: "value",
                axisLabel:{
                    fontSize:16,
                    formatter: "{value} 亿元"
                },
            },
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