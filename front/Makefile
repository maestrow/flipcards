copy-for/front:
	cp public/index.html dist

copy-for/ext:
	cp -r public/ext/* dist

clean:
	rm -rf ./dist/*

build/front/prod: copy-for/front
	NODE_ENV=production node scripts/build.js

build/front: copy-for/front
	NODE_ENV=development node scripts/build.js

build/ext: copy-for/ext
	NODE_ENV=development node scripts/build.js
	web-ext build --source-dir=dist --artifacts-dir=dist/ext --overwrite-dest

# https://extensionworkshop.com/documentation/develop/getting-started-with-web-ext/
run/ext: build/ext
	web-ext run --source-dir=dist

start: 
	NODE_ENV=development node scripts/dev.js

fake-gen:
	node scripts/fake-gen.js
