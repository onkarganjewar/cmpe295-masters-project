'use strict';

const express = require('express');
const app = express();
const formidable = require('formidable');
const path = require('path');
const fs = require('fs');
const exec = require('child_process').execSync;
var filename = "";

app.set('port', process.env.PORT || 80);

app.use(express.static('public'));

app.get('/', (req, res, next) => {
	console.log("Request for index page recieved");
	res.sendFile(__dirname + '/views/index.html');
});

app.post('/upload', function(req, res, next){

  // create an incoming form object
  var form = new formidable.IncomingForm();

  // specify that we want to allow the user to upload multiple files in a single request
  form.multiples = true;

  // store all uploads in the /uploads directory
  form.uploadDir = '/home/student/objectDetection/py-faster-rcnn/data/demo/';

  // every time a file has been uploaded successfully,
  // rename it to it's orignal name
  form.on('file', function(field, file) {
    fs.rename(file.path, path.join(form.uploadDir, file.name));
    filename = file.name;
  });

  // log any errors that occur
  form.on('error', function(err) {
    console.log('An error has occured: \n' + err);
  });

  // once all the files have been uploaded, send a response to the client
  form.on('end', function() {
    res.send("File Uploaded");
    console.log("File uploaded");
    exec('python2 /home/student/objectDetection/cmpe295-masters-project/faster-rcnn-resnet/tools/demo.py', (error, stdout, stderr) => {
	  if (error) {
	    console.error(`exec error: ${error}`);
	    return;
	  }
	  console.log(`stdout: ${stdout}`);
	  console.log(`stderr: ${stderr}`);
          // res.sendFile('/home/student/objectDetection/py-faster-rcnn/data/output-images/' + filename);
	});

  });

  // parse the incoming request containing the form data
  form.parse(req);

});

app.listen(app.get('port'), () => console.log("Object detection server running on port 80"));
