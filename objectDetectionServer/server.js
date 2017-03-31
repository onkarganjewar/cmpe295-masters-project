'use strict';

const express = require('express');
const app = express();
app.set('port', process.env.PORT || 3000);

app.get('/', (req, res, next) => {
	res.send("<h1>Object Detection Server</h1>");
});

app.listen(app.get('port'), () => console.log("Object detection server running on port 3000"));