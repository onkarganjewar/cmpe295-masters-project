'use strict';

const express = require('express');
const app = express();
const formidable = require('formidable');
const path = require('path');
const fs = require('fs');
const exec = require('child_process').execSync;
var filename = "";
var filetype = "";
var base64data = "";

app.set('port', process.env.PORT || 80);

app.use(express.static('public'));

app.get('/', (req, res, next) => {
	console.log("Request for index page recieved");
	res.sendFile(__dirname + '/views/index.html');
});

app.post('/upload', function(req, res, next){

  // create an incoming form object
  var form = new formidable.IncomingForm();

  // specify that we dont want to allow the user to upload multiple files in a single request
  form.multiples = false;

  // store all uploads in the mentioned directory
  form.uploadDir = '/home/student/cmpe295-masters-project/faster-rcnn-resnet/data/input/';

  // every time a file has been uploaded successfully,
  // rename it to it's orignal name
  form.on('file', function(field, file) {
    fs.rename(file.path, path.join(form.uploadDir, file.name));
    filename = file.name;
    console.log(filename);
    filetype = file.type;
    filetype = filetype.substring(0,5);
  });

  // log any errors that occur
  form.on('error', function(err) {
    console.log('An error has occured: \n' + err);
  });

  // once all the files have been uploaded, send a response to the client
  form.on('end', function() {
    
    console.log("File uploaded");

   if(filetype == "image"){   

    exec('sh /home/student/cmpe295-masters-project/execute', (error, stdout, stderr) => {
    	  if (error) {
    	    console.error(`exec error: ${error}`);
    	    return;
    	  }
    	  console.log(`stdout: ${stdout}`);
    	  console.log(`stderr: ${stderr}`);
	});
   }else{
	
     exec('sh /home/student/cmpe295-masters-project/videxe', (error, stdout, stderr) => {
          if (error) {
            console.error(`exec error: ${error}`);
            return;
          }
          console.log(`stdout: ${stdout}`);
          console.log(`stderr: ${stderr}`);
        });
	console.log("This line is written after exec");

   }
    
     fs.createReadStream('/home/student/cmpe295-masters-project/faster-rcnn-resnet/data/output/' + filename, {encoding: 'base64'}).pipe(res);

    /* fs.readFile('/home/student/cmpe295-masters-project/faster-rcnn-resnet/data/output/' + filename, function(err, data){
	base64data = new Buffer(data).toString('base64');
	res.send(base64data);
     });*/
     //res.sendFile(__dirname + '/uploads/000456.jpg');
     //res.sendFile('/home/student/objectDetection/py-faster-rcnn/data/output-images/' + filename);
  });


  // parse the incoming request containing the form data
  form.parse(req);

});

app.listen(app.get('port'), () => console.log("Object detection server running on port 80"));
