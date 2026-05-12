const readDatabase = require('../utils');

class StudentsController {
  static getAllStudents(req, res) {
    readDatabase(process.argv[2])
      .then((students) => {
        const lines = ['This is the list of our students'];

        const fields = Object.keys(students);
        fields.sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

        fields.forEach((field) => {
          const list = students[field];
          lines.push(
            `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`,
          );
        });

        res.status(200).send(lines.join('\n'));
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(process.argv[2])
      .then((students) => {
        const list = students[major] || [];
        res.status(200).send(`List: ${list.join(', ')}`);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }
}

module.exports = StudentsController;
