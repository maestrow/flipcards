copy-for/front:
	cp public/index.html dist

copy-for/ext:
	cp -r public/ext/* dist

clean:
	rm -rf ./dist/*

front/build/prod: copy-for/front
	NODE_ENV=production node scripts/build.js

front/build: copy-for/front
	NODE_ENV=development node scripts/build.js

front/run: 
	NODE_ENV=development node scripts/dev.js

ext/build: copy-for/ext
	NODE_ENV=development node scripts/build.js

ext/pub: copy-for/ext
	NODE_ENV=development node scripts/build.js
	web-ext build --source-dir=dist --artifacts-dir=dist/ext --overwrite-dest

# https://extensionworkshop.com/documentation/develop/getting-started-with-web-ext/
ext/run: build/ext
	web-ext run --source-dir=dist


fake-gen:
	node scripts/fake-gen.js
