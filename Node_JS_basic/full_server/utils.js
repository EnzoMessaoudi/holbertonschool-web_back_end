const fs = require('fs').promises;

async function readDatabase(filePath) {
  const content = await fs.readFile(filePath, 'utf8');
  const lines = content.split('\n').filter((line) => line.trim());

  const headers = lines[0].split(',');
  const fieldIndex = headers.indexOf('field');
  const firstnameIndex = headers.indexOf('firstname');

  const result = {};

  lines.slice(1).forEach((line) => {
    const values = line.split(',');
    const field = values[fieldIndex];
    const firstname = values[firstnameIndex];

    if (field && firstname) {
      if (!result[field]) {
        result[field] = [];
      }
      result[field].push(firstname);
    }
  });

  return result;
}

module.exports = readDatabase;
