const express = require('express');
const app = express();

app.use(require('./routes/index'));

module.exports = app;