# React + esbuild + typescript starter template

## [Why esbuild? Getting Started using a TypeScript / React example](https://www.youtube.com/watch?v=4rUbQJM0BgA)

```sh
npm init -y
npm i -D esbuild typescript
npm i -S react react-dom @types/react @types/react-dom
npx tsc --init --rootDir src --jsx react --target ES2015
```

Add `"build": "esbuild src/App.tsx --bundle --minify --sourcemap --outfile=public/bundle.js"` to `package.json`.
Add: 
- src/App.tsx
- public/index.html:

```html
<body>
  <div id="root"></div>
  <script src="bundle.js"></script>
</body>
```

`npm run build`

### Add some goodies

#### esbuild options and build script

Add `scripts/build.js` that use esbuild with javascript API.
Add `npm i -D cross-env` to run build.js with NODE_ENV environment variable.

### Dev server with watch mode

`npm i -D browser-sync`

Note, that [body tag is mandatory](https://stackoverflow.com/questions/24937136/browsersync-suddenly-not-connecting-to-browser) for autoreload.

### css modules

`npm i -D esbuild-css-modules-plugin`

Add [typing declarations](https://stackoverflow.com/questions/40382842/cant-import-css-scss-modules-typescript-says-cannot-find-module) for css modules.

## Other ways to create typescript + react app

- https://www.metachris.com/2021/04/starting-a-typescript-project-in-2021/