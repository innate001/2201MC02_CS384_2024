const express = require('express');
const multer = require('multer');
const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');
const cors = require('cors');
const app = express();
const upload = multer({ dest: 'uploads/' }); // Directory for uploaded files

app.use(cors());

app.post('/upload', upload.single('file'), (req, res) => {
  if (!req.file) {
    return res.status(400).send('No file uploaded.');
  }

  // Use 'python3' instead of 'python' here
  const pythonProcess = spawn('python3', [
    path.join(__dirname, 'process_file.py'), // Path to your Python script
    req.file.path, // Path to the uploaded file
  ]);

  pythonProcess.on('close', (code) => {
    if (code !== 0) {
      return res.status(500).send(`Python script exited with code ${code}`);
    }

    const outputFilePath = path.join(__dirname, '/output/output-file.xlsx');

    // Check if the output file exists
    fs.access(outputFilePath, fs.constants.F_OK, (err) => {
      if (err) {
        return res.status(500).send('Output file not found.');
      }
      res.download(outputFilePath, 'output-file.xlsx', (downloadErr) => {
        if (downloadErr) {
          console.error('Error sending file:', downloadErr);
          res.status(500).send('Error sending file.');
        }
      });
    });
  });

  // Log Python script errors to console
  pythonProcess.stderr.on('data', (data) => {
    console.error(`Python script error: ${data}`);
  });

  // Handle any errors with the spawn process itself
  pythonProcess.on('error', (err) => {
    console.error('Failed to start Python subprocess:', err);
    res.status(500).send('Error starting Python process.');
  });
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
