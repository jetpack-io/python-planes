import vue from '@vitejs/plugin-vue';

export default {
  plugins: [vue()],
  build: {
    outDir: '../api/public'
  },
  server: {
    port: 8000,
    proxy: {
      '/api/': 'http://127.0.0.1:8080/'
    }
  }
};
