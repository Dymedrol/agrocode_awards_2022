const path = require('path');
const webpack = require('webpack')
// const HtmlWebpackPlugin = require('html-webpack-plugin');
// const WebpackMd5Hash = require('webpack-md5-hash');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');
const TerserJSPlugin = require('terser-webpack-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');

module.exports =  env => {
  return {
    entry: { main: ["@babel/polyfill", './src/js/index.js'] },
    output: {
      path: path.resolve(__dirname, './public/static/build'),
      filename: 'bundle.js'
    },
    watchOptions: {
      ignored: /node_modules/
    },
    module: {
      rules: [
        {
          test: /\.(js|jsx)$/,
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env'],
          },
          exclude: /node_modules/,
          resolve: {
            extensions: [".js", ".jsx"]
          },
        },
        {
          test: /\.(less|css)$/,
          use:  [
            'style-loader',
            {
              loader: MiniCssExtractPlugin.loader,
              options: {
                // publicPath: (resourcePath, context) => {
                //   // publicPath is the relative path of the resource to the context
                //   // e.g. for ./css/admin/main.css the publicPath will be ../../
                //   // while for ./css/main.css the publicPath will be ../
                //   return path.relative(path.dirname(resourcePath), context) + '/';
                // }
              }
            },
            { loader: 'css-loader', options: { url: false, sourceMap: true } },
            'less-loader'
          ]
        }
      ]
    },


    optimization: {
      minimizer:  [new TerserJSPlugin({}), new OptimizeCSSAssetsPlugin({})],
    },
    plugins: [
      // new CleanWebpackPlugin(),
      new MiniCssExtractPlugin({
        filename: 'css/style.css',
      }),
      new CopyWebpackPlugin([
          {from:'src/img',to: path.resolve(__dirname, './public/static/build/img')},
          {from:'src/fonts',to: path.resolve(__dirname, './public/static/build/fonts')},
          {from:'src/js/plugins',to: path.resolve(__dirname, './public/static/build/js/plugins/')},
          {from:'src/css/',to: path.resolve(__dirname, './public/static/build/css/')},
      ]),
      new webpack.DefinePlugin({
        PRODUCTION: Boolean(env && env.production)
      })
    ]
  }

};
