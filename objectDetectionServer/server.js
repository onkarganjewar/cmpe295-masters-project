'use strict';

const express = require('express');
const app = express();
app.set('port', process.env.PORT || 3000);

app.use(express.static('public'));

app.get('/', (req, res, next) => {
	res.sendFile(__dirname + '/views/index.html');
});

app.listen(app.get('port'), () => console.log("Object detection server running on port 3000"));