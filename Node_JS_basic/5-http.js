const { createServer } = require('node:http');
const countStudents = require('./3-read_file_async');

const database = process.argv[2] || 'database.csv';

const hostname = '127.0.0.1';
const port = 1245;
const app = createServer((req, res) => {
  if (req.url === '/' && req.method === 'GET') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  }
  if (req.url === '/students' && req.method === 'GET') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    countStudents(database)
      .then((result) => {
        res.write('This is the list of our students\n');
        res.write(`${result}`);
        res.end();
      })
      .catch((error) => {
        res.end(`${error.message}`);
      });
  }
});

app.listen(port, hostname, () => {});

module.exports = app;
