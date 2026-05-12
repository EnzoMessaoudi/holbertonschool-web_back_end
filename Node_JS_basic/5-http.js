const { createServer } = require('node:http');
const fs = require('fs');

const hostname = '127.0.0.1';
const port = 1245;

const app = createServer((req, res) => {
  if (req.url === '/' && req.method === 'GET') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  }
  if (req.url === '/students' && req.method === 'GET') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    new Promise((resolve, reject) => {
      fs.readFile('database.csv', 'utf-8', (err, data) => {
        if (err) {
          return reject(new Error('Cannot load the database'));
        }
        const filterFile = data.split('\n').filter((line) => line !== '');
        const students = filterFile.slice(1);
        const fields = {};

        students.forEach((element) => {
          const field = element.split(',')[3];
          const firstname = element.split(',')[0];
          if (!fields[field]) fields[field] = [];
          fields[field].push(firstname);
        });

        const lines = [];
        lines.push(`Number of students: ${filterFile.length - 1}`);
        Object.keys(fields).forEach((field) => {
          lines.push(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
        });

        return resolve(lines.join('\n'));
      });
    })
      .then((result) => {
        res.end(result);
      })
      .catch((error) => {
        res.end(error.message);
      });
  }
});

app.listen(port, hostname, () => {});

module.exports = app;