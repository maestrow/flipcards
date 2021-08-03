const options = require('./esbuild-config.js');
const { build } = require('esbuild');

build(options).catch(err => {
  process.stderr.write(err.stderr)
  process.exit(1)
})