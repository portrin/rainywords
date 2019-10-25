const express = require("express");
const app = express();
const cors = require('cors');
const bodyParser = require('body-parser')
const net = require('net');

const port = 3000;
app.use(cors())
app.use(bodyParser.urlencoded({ extended: true }))
app.use(bodyParser.json())
app.use((req, res, next) => {
    console.log(`${req.method} ${req.originalUrl}`);
    next();
  });
  
app.use(express.urlencoded());
app.use(express.static("../client/dist"));

app.get("/logout", (req, res) => {
    res.send('Success')
});

app.post("/admin-callback", async (req, res) => {
    console.log("////////////EMAILLOGIN/////////");
    console.log(req.body);
    const { email, password } = req.body;
    if (email === "gogobebe@gmail.com" && password === "gogobebe") {
      res.send('Success')
    } else {
        res.send('Invalid Password')
      console.log("email or password is invalid.");
    }
  });

var client = new net.Socket();
client.connect(5000, '172.20.10.3', function() {
    console.log('Connected');
});

app.post("/confirm-reset", async (req,res) => {
  console.log("////////////CONFIRMRESET/////////");
  console.log(req.body);
  const { confirmReset } = req.body;
  const exit = JSON.stringify({status:'exit'});
  console.log(exit);
  if (confirmReset === true) {
    client.write(exit);
    res.send('Confirm')
  } else {
    res.send('Cancel')
    console.log("cancel reset.");
  }
})

app.listen(port, () => console.log(`Example app listening on port ${port}!`));