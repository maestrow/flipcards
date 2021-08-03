const cssModulesPlugin = require('esbuild-css-modules-plugin');

const isProd = process.env.NODE_ENV === 'production';

module.exports = {
  entryPoints: ['./src/index.tsx'],
  minify: isProd,
  sourcemap: !isProd,
  bundle: true,
  outfile: './public/bundle.js',
  plugins: [
    cssModulesPlugin({
      inject: true, // optional. set to false to not inject generated CSS into <head>, default is true
      localsConvention: 'camelCaseOnly', // optional. value could be one of 'camelCaseOnly', 'camelCase', 'dashes', 'dashesOnly', default is 'camelCaseOnly'
    })
  ]
}
