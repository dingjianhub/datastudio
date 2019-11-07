var myChart = echarts.init(document.getElementById('main'));
myChart.showLoading(); // 显示加载动画

var index_code = "000905";
console.log(index_code);
 $.get("http://127.0.0.1:5000/index/" + index_code).done(function (data) {
     myChart.hideLoading(); // 隐藏加载动画
     var data_json = JSON.parse(data);

     myChart.setOption(
         option = {
             title : {
                 text: "中证500PE"
             },
             xAxis: {
                 type: "category",
                 data: data_json.date
             },
             yAxis: {
                 type: "value"
             },
             series: {
                 name: "中证500PE",
                 type: "line",
                 data: data_json.pe
             }
         }
     )
 });

