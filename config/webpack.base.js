var path = require("path");
var ExtractTextPlugin = require("extract-text-webpack-plugin");
const VueLoaderPlugin = require("vue-loader/lib/plugin");

var config = {
    entry: {
        main: path.resolve(__dirname, "../src/main.js")
    },
    output: {
        path: path.join(__dirname, "./dist"),
        publicPath: "/dist/",
        filename: "[name].js",
        chunkFilename: '[name].chunk.js'
    },
    module: {
        rules: [
            {
                test: /\.css$/,
                use:  ExtractTextPlugin.extract({
                    use: "css-loader",
                    fallback: "style-loader"
                    
                })
            },
            {
                test: /\.js$/,
                loader: "babel-loader",
                exclude: /node_modules/,
            },
            {
                test: /\.vue$/,
                use: [
                    {
                        loader: "vue-loader",
                        options: {
                            loaders: {
                                css: ExtractTextPlugin.extract({
                                    use: "css-loader",
                                    fallback: "vue-style-loader"
                                })
                            }
                        }
                    },
                    {
                        loader: "iview-loader",
                        options: {
                            prefix: false
                        }
                    }
            ]
            },
            {
                test: /\.(gif|jpg|png|woff|svg|eot|ttf)\??.*$/,
                loader: "url-loader?limit=1024"
            }
        ]
    },
    plugins: [
        new VueLoaderPlugin(),
        // 把每个.vue文件中的样式，打包到mian.css中
        new ExtractTextPlugin({
            filename: "main.css",
            allChunks: true
        })
    ]
};

module.exports = config;