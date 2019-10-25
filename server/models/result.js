const mongoose = require('mongoose');
let Schema = mongoose.Schema;

let ResultSchema = new Schema({
  username: String,
  score: INT
});

let Result = mongoose.model("Result", ResultSchema);
module.exports = Result;