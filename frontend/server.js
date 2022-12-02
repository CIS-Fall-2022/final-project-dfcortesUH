// load the things we need 
//REFERENCE: CLASS 8 FILES
var express = require('express');
var app = express();
const bodyParser = require('body-parser');

// required module to make calls to a REST API
//REFERENCE: CLASS 8 FILES
const axios = require('axios');
const { render } = require('ejs');

app.use(bodyParser.urlencoded({
    extended: false
}));

// set the view engine to ejs
//REFERENCE: CLASS 8 FILES
app.set('view engine', 'ejs');

// index page goes automatically to signin.ejs
app.get('/', function (req, res) {
    res.render("pages/signin.ejs", {});
});

// what happens after you submit your log-in information (assuming that it is correct)
app.get('/login', function (req, res) {
    var username = req.body.username;
    var pw = req.body.password;
    //call to my login API 
    axios.post('http://127.0.0.1:5000/login', {
        username: username,
        password: pw
    })
        .then((response) => {
            res.render("pages/allflights.ejs", {});
            // user can add or delete flights (no update) as part of the overview page 
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
                })
            })
            app.get('/delete_flight', function (req, res) {
                var planeid = req.body.planeid;
                var airportfromid = req.body.airportfromid;
                var airporttoid = req.body.airporttoid;
                var date = req.body.date;
                axios.delete('http://127.0.0.1:5000/api/flights/delete', {
                    planeid: planeid,
                    airportfromid: airportfromid,
                    airporttoid: airporttoid,
                    date: date
                })
            })
        });
})

//CRUD for airports 
app.get('/airports', function (req, res) {
    var airportcode = req.body.airportcode;
    var airportname = req.body.airportname;
    var country = req.body.country;
    res.render("pages/airports.ejs", {
    });
    axios.post('http://127.0.0.1:5000/api/airports/post', {
        airportcode: airportcode,
        airportname: airportname,
        country: country
    });
    axios.get('http://127.0.0.1:5000/api/airports/get', {
        airportcode: airportcode,
        airportname: airportname,
        country: country
    });
    axios.put('http://127.0.0.1:5000/api/airports/put', {
        airportcode: airportcode,
        airportname: airportname,
        country: country
    });
    axios.delete('http://127.0.0.1:5000/api/airports/delete', {
        airportcode: airportcode,
        airportname: airportname,
        country: country
    });

});

// //CRUD for planes
app.get('/planes', function (req, res) {
    var make = req.body.make;
    var model = req.body.model;
    var year = req.body.year;
    var capacity = req.body.capacity;
    res.render("pages/planes.ejs",{
    });
    axios.post('http://127.0.0.1:5000/api/planes/post',{
        make: make,
        model: model,
        year: year,
        capacity: capacity
    });
    axios.get('http://127.0.0.1:5000/api/planes/get',{
        make: make,
        model: model,
        year: year,
        capacity: capacity
    });
    axios.put('http://127.0.0.1:5000/api/planes/put',{
        make: make,
        model: model,
        year: year,
        capacity: capacity
    });
    axios.delete('http://127.0.0.1:5000/api/planes/delete',{
        make: make,
        model: model,
        year: year,
        capacity: capacity
    });

});


app.listen(8080);
console.log('8080 is the magic port');