const express = require('express');
const http = require('http');

const app = express();

app.set('port', 1245);
const server = http.createServer(app);

server.listen(1245);

app.get('/', (req, res) => {
  res.end('Hello Holberton School!');
});

module.exports = app;
