import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import { fileURLToPath, URL } from "node:url";

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)), // Alias para o diretório 'src'
      vue: "vue/dist/vue.esm-bundler.js", // Necessário para garantir compatibilidade com Vite e Vue 3
    },
  },
  server: {
    host: "127.0.0.1",
    port: 3000,
    open: true,
  },
  build: {
    outDir: "dist",
    emptyOutDir: true,
    rollupOptions: {
      output: {
        manualChunks: {
          // Divida as dependências maiores em chunks separados
          vue: ["vue", "@vitejs/plugin-vue"],
        },
      },
    },
  },
  optimizeDeps: {
    include: [
      "vue",
      "@vitejs/plugin-vue",
      "@fortawesome/fontawesome-svg-core",
      "@fortawesome/vue-fontawesome",
    ],
  },
});
