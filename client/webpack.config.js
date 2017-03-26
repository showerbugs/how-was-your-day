var path = require('path')
var webpack = require('webpack')
require("babel-polyfill");

module.exports = {
  context: __dirname,
  entry: ['babel-polyfill', './src/main.js'],
  output: {
    path: path.resolve(__dirname, './dist'),
    publicPath: '/dist/',
    filename: 'build.js'
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: {
          // vue-loader options go here
        }
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: /node_modules/,
        query: {
             cacheDirectory: true,
             babelrc: false,
             presets: [
                 'es2015',
                 'stage-0',
             ],
             plugins: [
                 'transform-regenerator',
             ]
         }
      },
      {
        test: /\.(png|jpg|gif|svg|ttf|eot|woff|woff2)$/,
        loader: 'file-loader',
        options: {
          name: '[name].[ext]?[hash]'
        }
      },
      {
        test: /\.(scss|css)$/,
        loaders: ["style-loader", "css-loader", "sass-loader"]
      }
    ]
  },
  resolve: {
    alias: {
      'vue$': 'vue/dist/vue'
    }
  },
  devServer: {
    historyApiFallback: true,
    noInfo: true,
    proxy: {
     '/api': {
       target:  {
          "host": "localhost",
          "protocol": 'http',
          "port": 5000
       },
       changeOrigin: true,
       pathRewrite: {
           "^/api": ""
       },
       logLevel: 'debug',
       secure: false
     }
   }
  },
  devtool: '#eval-source-map'
}

if (process.env.NODE_ENV === 'production') {
  module.exports.devtool = '#source-map'
  // http://vue-loader.vuejs.org/en/workflow/production.html
  module.exports.plugins = (module.exports.plugins || []).concat([
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: '"production"'
      }
    }),
    new webpack.optimize.UglifyJsPlugin({
      compress: {
        warnings: false
      }
    }),
    new webpack.LoaderOptionsPlugin({
      minimize: true
    })
  ])
}
//  target:  {
//     "host": "ec2-52-79-196-148.ap-northeast-2.compute.amazonaws.com",
//     "protocol": 'http',
//     "port": 8000
//  },
