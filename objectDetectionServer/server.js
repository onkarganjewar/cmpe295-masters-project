'use strict';

const express = require('express');
const app = express();

app.get('/', (req, res, next) => {
	res.send("<h1>Object Detection Server</h1>");
});

app.listen(3000, () => console.log("Object detection server running on port 3000"));