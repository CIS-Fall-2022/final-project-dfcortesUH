"use strict";

// load the things we need 
//REFERENCE: CLASS 8 FILES
var express = require('express');

var app = express();

var bodyParser = require('body-parser'); // required module to make calls to a REST API
//REFERENCE: CLASS 8 FILES


var axios = require('axios');

app.use(bodyParser.urlencoded({
  extended: false
})); // set the view engine to ejs
//REFERENCE: CLASS 8 FILES

app.set('view engine', 'ejs'); // index page goes automatically to signin.ejs

app.get('/', function (req, res) {
  res.render("pages/signin.ejs", {});
}); // what happens after you submit your log-in information (assuming that it is correct)

app.get('/login', function (req, res) {
  var username = req.body.username;
  var pw = req.body.password; //call to my login API 

  axios.post('http://127.0.0.1:5000/login', {
    username: username,
    password: pw
  }).then(function (response) {
    res.render("pages/allflights.ejs", {}); // user can add or delete flights (no update) as part of the overview page 

    app.get('/add_flight', function (req, res) {
      var planeid = req.body.planeid;
      var airportfromid = req.body.airportfromid;
      var airporttoid = req.body.airporttoid;
      var date = req.body.date;
      axios.post('http://127.0.0.1:5000/api/flights/post', {
        planeid: planeid,
        airportfromid: airportfromid,
        airporttoid: airporttoid,
        date: date
      });
    });
    axios.post('http://127.0.0.1:5000/api/flights/delete');
  });
});
app.listen(8080);
console.log('8080 is the magic port');