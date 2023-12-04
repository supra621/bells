import {defineConfig} from "vite";
import solidPlugin from 'vite-plugin-solid';


export default defineConfig({
    appType: 'custom',
    base: "/assets/",
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
        host: true,
        strictPort: true
    },
});
