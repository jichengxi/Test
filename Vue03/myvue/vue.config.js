const path = require('path')

const resolve = dir => path.join(__dirname, dir)

const BASE_URL = process.env.NODE_ENV === 'production' ? '/iview-admin' : '/'

module.exports = {
  // presets: [
  //   '@vue/cli-plugin-babel/preset'
  // ],
  publicPath: BASE_URL,
  chainWebpack: config => {
    config.resolve.alias
      .set('@', resolve('src'))
      .set('_c', resolve('src/components'))
  },
  // 打包时不生成.map文件，减少打包体积
  productionSourceMap: false,
  devServer: {
    proxy: 'http://localhost:4000'
  }
}
