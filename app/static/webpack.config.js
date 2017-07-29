var path = require('path');
var webpack = require('webpack');
var ExtractTextPlugin = require("extract-text-webpack-plugin");

module.exports = {
  entry: {
    index: './js/index.js',
    index2: './js/index2.js',
    style: [
        'bootstrap/dist/css/bootstrap.css',
        'font-awesome/css/font-awesome.css',
        './css/modern-business.css',
        './css/cupid.css',
    ]
  },
  output: {
    path: path.join(__dirname, 'dist/'),
    filename: '[name].js'
  },
  module: {
    loaders: [
      {
        test: /\.sass$/,
        loader: 'style!css!sass'
      }, 
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: /(node_modules|bower_components)/,
        query: {
          presets: ['es2015']
        }
      },
      {
         test: /\.css$/,
         loader: ExtractTextPlugin.extract({
           fallback: "style-loader",
           use: "css-loader"
         }),
      },
      {
        test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/,
        loader: "url-loader",
      },
      {
        test: /\.(ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
        loader: "url-loader",
      },
      {
          test: /\.(ico|map|png)$/,
          loader:'file-loader?name=[name].[ext]',
      }]
  },
  plugins: [
        new ExtractTextPlugin("[name].css"),
        new webpack.ProvidePlugin({
          $: "jquery",
          jQuery: "jquery",
          jquery: "jquery",
        })
  ],

};

