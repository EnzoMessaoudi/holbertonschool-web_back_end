const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    if (!path) {
        return reject(new Error('Cannot load the database'));
    }
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        return reject(new Error('Cannot load the database'));
      }
      const newFile = data.split('\n');
      const filterFile = newFile.filter((line) => line !== '');

      console.log(`Number of students: ${filterFile.length - 1}`);
      const students = filterFile.slice(1);

      const fields = {};
      students.forEach((element) => {
        const field = element.split(',')[3];
        const firstname = element.split(',')[0];
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      });
      const lines = [];

      lines.push(`Number of students: ${filterFile.length - 1}`);

      Object.keys(fields).forEach((field) => {
          console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
          lines.push(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
      });

      return resolve(lines.join('\n'));
          });
  });
}

module.exports = countStudents;
