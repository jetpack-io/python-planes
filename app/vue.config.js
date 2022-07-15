module.exports = {
  outputDir: '../api/public',
  devServer: {
    port: 8000,
    proxy: {
      '/api/*': {
        target: 'http://127.0.0.1:8080'
      }
    }
  }
};
