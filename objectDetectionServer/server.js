'use strict';

const express = require('express');
const app = express();
const formidable = require('formidable');
const path = require('path');
const fs = require('fs');

app.set('port', process.env.PORT || 3000);

app.use(express.static('public'));

app.get('/', (req, res, next) => {
	res.sendFile(__dirname + '/views/index.html');
});

app.post('/upload', function(req, res, next){

  // create an incoming form object
  var form = new formidable.IncomingForm();

  // specify that we want to allow the user to upload multiple files in a single request
  form.multiples = true;

  // store all uploads in the /uploads directory
  form.uploadDir = __dirname + '/uploads';

  // every time a file has been uploaded successfully,
  // rename it to it's orignal name
  form.on('file', function(field, file) {
    fs.rename(file.path, path.join(form.uploadDir, file.name));
  });

  // log any errors that occur
  form.on('error', function(err) {
    console.log('An error has occured: \n' + err);
  });

  // once all the files have been uploaded, send a response to the client
  form.on('end', function() {
    res.end('success');
  });

  // parse the incoming request containing the form data
  form.parse(req);

});

app.listen(app.get('port'), () => console.log("Object detection server running on port 3000"));