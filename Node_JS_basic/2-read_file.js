const fs = require('fs');

function countStudents(path) {
  try {
    const file = fs.readFileSync(path, 'utf-8');

    const newFile = file.split('\n');
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

    Object.keys(fields).forEach((field) => {
      console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
    });
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
