// load the things we need 
//REFERENCE: CLASS 8 FILES
var express = require('express');
var app = express();
const bodyParser  = require('body-parser');


// required module to make calls to a REST API
//REFERENCE: CLASS 8 FILES
const axios = require('axios');

app.use(bodyParser.urlencoded());

// set the view engine to ejs
//REFERENCE: CLASS 8 FILES
app.set('view engine', 'ejs');

// index page goes automatically to signin.ejs
app.get('/', function(req, res) {
    res.render("pages/signin.ejs", {});
});

app.get('/allflights', function(req,res){
    res.render("pages/allflights.ejs", {
    });
})

// app.post('/process_login', function(req, res){
//     var user = req.body.username;
//     var password = req.body.password;
//     //call to my login API 
//     axios.get('http://127.0.0.1:5000/')
//         .then((response)=>{
//             if(user === 'davidfcortes007atUH' && password ===        'finalProjectatUHpu')
//             {
//                 res.render("pages/allflights.ejs", {});
//             }
//         }); 
//   })



app.listen(8080);
console.log('8080 is the magic port');