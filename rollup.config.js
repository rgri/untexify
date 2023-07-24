import { nodeResolve } from '@rollup/plugin-node-resolve';

export default {
    input: './frontend/untexifyweb/staticfiles/testapp/pixijs.js',
    external: [''],
    output: {
        file: './frontend/untexifyweb/staticfiles/testapp/bundle.js',
        format: 'iife',
        globals: {
        }
    },
    plugins: [nodeResolve({
        namedExports: {
            // Gotcha: You need to
            // explicitly name the exports
            // because commonjs plugin is
            // not smart enough to work
            // with pixi.js Browserify v4 builds
            'pixi.js': [
                'VERSION',
                'Application',
                'Graphics'
            ]
        }
    })]
};
