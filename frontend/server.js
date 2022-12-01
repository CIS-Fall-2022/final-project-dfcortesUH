// load the things we need 
//REFERENCE: CLASS 8 FILES
var express = require('express');
var app = express();
const bodyParser  = require('body-parser');


// required module to make calls to a REST API
//REFERENCE: CLASS 8 FILES
const axios = require('axios');

app.use(bodyParser.urlencoded());
app.use(express.urlencoded({extended: true}))

// set the view engine to ejs
//REFERENCE: CLASS 8 FILES
app.set('view engine', 'ejs');


// index page goes automatically to signin.ejs
app.get('/', function(req, res) {
    res.render("pages/signin.ejs", {});
});

// what happens after you submit your log-in information (assuming that it is correct)
app.post('/login', function(req, res){
    var username = req.body.username;
    var pw = req.body.password;
    //call to my login API 
    axios.post('http://127.0.0.1:5000/login')
    .then((response)=>{
        res.render("pages/signin.ejs", {
            username: username,
            password: pw
        });
    }); 
  })



app.listen(8080);
console.log('8080 is the magic port');