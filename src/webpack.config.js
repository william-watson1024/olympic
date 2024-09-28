// webpack.config.js
module.exports = {
  // Other configurations...
  resolve: {
    fallback: {
      url: require.resolve("url/"),
    },
  },
};
