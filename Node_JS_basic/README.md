## run javascript using NodeJS  


## use NodeJS modules  


## use specific Node JS module to read files  


## use process to access command line arguments and the environment  


## create a small HTTP server using Node JS  
    const { createServer } = require('node:http');
    const hostname = '127.0.0.1';
    const port = 3000;
    const server = createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello World');
    });
    server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
    });

## create a small HTTP server using Express JS  


## create advanced routes with Express JS  


## use ES6 with Node JS with Babel-node  


## use Nodemon to develop faster  

