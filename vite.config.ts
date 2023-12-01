import {defineConfig} from "vite";
import solidPlugin from 'vite-plugin-solid';


export default defineConfig({
    appType: 'custom',
    plugins: [
        solidPlugin(),
    ],
    build: {
        manifest: true,
        rollupOptions: {
            // input: '/src/index.ts'
            input: [
                '/src/index.ts',
                '/chat/assets/chat/*',
                '/core/assets/core/main.ts',
            ]
        }
    },
    server: {
        proxy: {
            '^/assets/chat/(?!.*/)': {
                target: 'http://localhost:1234/static/chat/',
                changeOrigin: true,
            },
            '^/assets/core/(?!.*/)': {
                target: 'http://localhost:1234/static/core/',
                changeOrigin: true,
            },
        },
        strictPort: true
    },
});
