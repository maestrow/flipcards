const options = require('./esbuild-config.js');
const { build } = require('esbuild');
const fs = require('fs');
const path = require('path');
const { exit } = require('process');

const copy = () => {
  const src = path.resolve(__dirname, '../public/index.html')
  const dest = path.resolve(__dirname, '../dist/index.html')
  fs.copyFileSync(src, dest);
}

copy();

build(options).catch(err => {
  process.stderr.write(err.stderr)
  process.exit(1)
})