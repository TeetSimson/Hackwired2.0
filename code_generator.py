import json
import openai
import numpy as np
import pandas as pd

from gpt import set_openai_key
from gpt import GPT
from gpt import Example

set_openai_key()

gpt_sql = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)
gpt_js = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)
gpt_python = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)
gpt_php = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)

#df = pd.read_csv("states_all.csv")
#df = pd.DataFrame({"Gender": ["boy", "boy", "boy", "boy", "boy", "girl", "girl", "girl", "girl"],
#                   "Division": ["one", "one", "one", "two", "two",
#                                "one", "one", "two", "two"],
#                   "Marks": [50, 55, 67, 85, 44, 84, 65, 56, 87]})
#print(df)

def train_sql_model():
    gpt_sql.add_example(Example('Fetch unique values of DEPARTMENT from Worker table.',
                            'Select distinct DEPARTMENT from Worker;'))
    gpt_sql.add_example(Example('Print the first three characters of FIRST_NAME from Worker table.',
                            'Select substring(FIRST_NAME,1,3) from Worker;'))
    gpt_sql.add_example(
        Example("Find the position of the alphabet ('a') in the first name column 'Amitabh' from Worker table.",
                "Select INSTR(FIRST_NAME, BINARY'a') from Worker where FIRST_NAME = 'Amitabh';"))

    gpt_sql.add_example(Example("Print the FIRST_NAME from Worker table after replacing 'a' with 'A'.",
                            "Select CONCAT(FIRST_NAME, ' ', LAST_NAME) AS 'COMPLETE_NAME' from Worker;"))
    gpt_sql.add_example(Example("Display the second highest salary from the Worker table.",
                            "Select max(Salary) from Worker where Salary not in (Select max(Salary) from Worker);"))
    gpt_sql.add_example(Example("Display the highest salary from the Worker table.",
                            "Select max(Salary) from Worker;"))
    gpt_sql.add_example(Example("Fetch the count of employees working in the department Admin.",
                            "SELECT COUNT(*) FROM worker WHERE DEPARTMENT = 'Admin';"))
    gpt_sql.add_example(Example("Get all details of the Workers whose SALARY lies between 100000 and 500000.",
                            "Select * from Worker where SALARY between 100000 and 500000;"))
    gpt_sql.add_example(Example("Get Salary details of the Workers",
                            "Select Salary from Worker"))

def train_python_model():

    gpt_python.add_example(Example('How many unique values in Division Column?',
                    'df["Division"].nunique()'))
    gpt_python.add_example(Example('Find the Division of boy who scored 55 marks',
                    'df,loc[(df,loc[:, "Gender"] == "boy") & (df,loc[:, "Marks"] == 55)]'))
    gpt_python.add_example(Example('Find the average Marks scored by Girls',
                    'np.mean(df.loc[(df.loc[:, "Gender"] == "girl"), "Marks"])'))

def train_js_model():

    gpt_js.add_example(Example('Connect to a MONGODB',
                    '''//Import the mongoose module
var mongoose = require('mongoose');

//Set up default mongoose connection
var mongoDB = 'mongodb://127.0.0.1/my_database';
mongoose.connect(mongoDB, {useNewUrlParser: true, useUnifiedTopology: true});

//Get the default connection
var db = mongoose.connection;

//Bind connection to error event (to get notification of connection errors)
db.on('error', console.error.bind(console, 'MongoDB connection error:'));'''))
    gpt_js.add_example(Example('Define a schema for MongoBD',
                    '''
                    //Require Mongoose
var mongoose = require('mongoose');

//Define a schema
var Schema = mongoose.Schema;

var SomeModelSchema = new Schema({
  a_string: String,
  a_date: Date
});
                    '''))
    gpt_js.add_example(Example('Create a model',
                    '''
                    // Define schema
var Schema = mongoose.Schema;

var SomeModelSchema = new Schema({
  a_string: String,
  a_date: Date
});

// Compile model from schema
var SomeModel = mongoose.model('SomeModel', SomeModelSchema );
                    '''))

def train_php_model():

    gpt_php.add_example(Example('Start a bucket for a cluster',
                    '''
                    'couchbase' => [
'driver'        => 'couchbase',
'host'          => 'couchbase://' . env('COUCHBASE_SERVER', '127.0.0.1'),
'user'          => env('COUCHBASE_USER', 'Administrator'),
'password'      => env('COUCHBASE_PASS', 'password'),
],
                    '''))
    gpt_php.add_example(Example('User management',
                    '''
                    public function create(Request $request)
{
  $credentials = [
    'name' => $request->user,
    'password' => $request->password,
  ];
  $user = new User($credentials);
  try {
    $this->db->insert("user::".$request->user, $user);
    return response()->json(["data" => ["token" => $this->buildToken($user)]]);
  } catch (\Couchbase\Exception $ex) {
      return response()->json(["failure" => 'Failed to create user'], 409);
  }
}
                    '''))
    gpt_php.add_example(Example('Generic query',
                    '''
                    $queryBody = SearchQuery::conjuncts(SearchQuery::term("hotel")->field("type"));
if (!empty($location) && $location != "*") {
  $queryBody->every(SearchQuery::disjuncts(
    SearchQuery::match($location)->field("country"),
    SearchQuery::match($location)->field("city"),
    SearchQuery::match($location)->field("state"),
    SearchQuery::match($location)->field("address")
  ));
}
                    '''))


#prompt = "Display Division of girl who scored maximum marks"
#print(gpt.get_top_reply(prompt))
#print(df.loc[(df.loc[:, "Gender"] == "girl") & (df.loc[:, "Marks"] == max(df.loc[:, "Marks"]))])