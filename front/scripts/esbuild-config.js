const cssModulesPlugin = require('esbuild-css-modules-plugin');

const shadowContainerId = 'vocab-k09asnd';

const isProd = process.env.NODE_ENV === 'production';

module.exports = {
  entryPoints: [
    './src/initializer.ts',
    './src/index.tsx'
  ],
  minify: isProd,
  sourcemap: !isProd,
  bundle: true,
  outdir: './dist',
  plugins: [
    cssModulesPlugin({
      inject: () => {
        return `var el = document.getElementById('${shadowContainerId}');
        if (el && el.shadowRoot && !el.shadowRoot.getElementById(digest)) {
            const styleEl = document.createElement('style');
            styleEl.id = digest;
            styleEl.textContent = css;
            el.shadowRoot.prepend(styleEl);
        }
        `
      },
      localsConvention: 'camelCaseOnly', // optional. value could be one of 'camelCaseOnly', 'camelCase', 'dashes', 'dashesOnly', default is 'camelCaseOnly'
    })
  ]
}
