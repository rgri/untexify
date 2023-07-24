        import json from '@rollup/plugin-json';

        export default {
            input: './frontend/untexifyweb/staticfiles/testapp/pixijs.js',
            output: {
                file: 'bundle.js',
                format: 'cjs'
            },
            plugins: [json()]
        };
