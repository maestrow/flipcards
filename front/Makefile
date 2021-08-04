copy-for/front:
	cp public/index.html dist

copy-for/ext:
	cp -r public/ext/* dist

clean:
	rm -rf ./dist/*

build/dev:
	NODE_ENV=development node scripts/build.js

build/prod:
	NODE_ENV=production node scripts/build.js

front/build: copy-for/front build/dev

front/build/prod: copy-for/front build/prod

front/run: 
	NODE_ENV=development node scripts/dev.js

ext/build: copy-for/ext build/dev

ext/pub: copy-for/ext build/prod
	web-ext build --source-dir=dist --artifacts-dir=dist/ext --overwrite-dest

# https://extensionworkshop.com/documentation/develop/getting-started-with-web-ext/
ext/run: build/ext
	web-ext run --source-dir=dist

fake-gen:
	node scripts/fake-gen.js
