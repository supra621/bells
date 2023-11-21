import {defineConfig} from "vite";
import solidPlugin from 'vite-plugin-solid';


export default defineConfig({
    appType: 'custom',
    // base: base public path when served?
    base: '/static/',
    plugins: [
        solidPlugin(),
    ],
    publicDir: "static",
    build: {
        manifest: true,
        rollupOptions: {
            // input: '/src/index.ts'
            input: [
                '/src/index.ts',
                '/chat/static/chat/*',
                '/core/static/core/main.ts',
            ]
        }
    },
    server: {
        proxy: {
            '^/static/chat/(?!.*/)': {
                target: 'http://localhost:1234/static/chat/',
                changeOrigin: true,
            },
            '^/static/core/(?!.*/)': {
                target: 'http://localhost:1234/static/core/',
                changeOrigin: true,
            },
        },
        strictPort: true
    },
});
