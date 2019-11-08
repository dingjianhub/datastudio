var myChart = echarts.init(document.getElementById('main'));
myChart.showLoading(); // 显示加载动画

var indexCode = "000905";

var peUrl = "http://127.0.0.1:5000/index/" + indexCode + "/pe";
var priceUrl = "http://127.0.0.1:5000/index/" + indexCode + "/price";

// 获取指数的PE数据
$.get(peUrl).done(function (data) {
    // console.log(data.pe);
    myChart.hideLoading();
    myChart.setOption({
        title: {
            text: "中证500PE"
        },
        tooltip: {},
        legend: {
            data: ["当前PE"]
        },
        xAxis: {
            data: data.date
        },
        yAxis: {
            // data: [10,20,30,40,50]
        },
        series: [{
            name: "当前PE",
            type: "line",
            data: data.pe
        }]
    });
});

//  获取指数价格
$.get(priceUrl).done(function (data) {
    // console.log(data.pe);
    myChart.hideLoading();
    myChart.setOption({
        title: {
            text: "中证500价格"
        },
        tooltip: {},
        legend: {
            data: ["价格"]
        },
        xAxis: {
            data: data.date
        },
        yAxis: {
            // data: [10,20,30,40,50]
        },
        series: [{
            name: "价格",
            type: "line",
            data: data.price
        }]
    });
});
