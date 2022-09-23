![hero](https://user-images.githubusercontent.com/111843624/187912322-acbc1b5b-6748-4c53-a43e-fc03e7f85c13.png)





# LIQUIFY TRADES

this is repo hosts code for backend development for Liquify Trades, a trading journal which aims at improving trading perfomance

## TECH STACK.
![](https://img.shields.io/static/v1?label=&message=HEROKU&color=<COLOR>)
![](https://img.shields.io/static/v1?label=&message=Postgres&color=red)
![](https://img.shields.io/static/v1?label=&message=JWT_TOKENS&color=red)
![](https://img.shields.io/static/v1?label=python&message=v3.1&color=red)
![](https://img.shields.io/static/v1?label=fastapi&message=v0.81.0&color=)


## DEPLOYMENT


## ROUTES DOCUMENTATION
The swaggger documentation can be found at https://liquifytrades.herokuapp.com/docs   <br/>

### LOGIN ROUTE

https://liquifytrades.herokuapp.com/login <br/>
Login takes email and password , then fetches user_id from the database. It then embeds  user_id in the JWT token which is return.
To make a request to login route append formdata username which holds email address and also password
``` javascript
var formdata = new FormData();
formdata.append("username", "max@gmail.com");
formdata.append("password", "passkey");

var requestOptions = {
  method: 'POST',
  body: formdata,
  redirect: 'follow'
};

fetch("https://liquifytrades.herokuapp.com/login", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
Here is a sample output for successfull login. 200 Status code 
```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo0LCJleHAiOjcwNjIwMTAwNjh9.9ACMCnbTC8FWASr542oZ5UFdtg27B-6NSSm89ptdwBc",
    "token_type": "bearer"
}
```
Incorrect email address or password returns a 403 forbidden status error.


### REGISTER ROUTE

https://liquifytrades.herokuapp.com/register <br/>
Register route takes POST request with a body containing user email and password then inserts this info in the database . <br/>
Sample Javascript code
```javascript 
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
  "email": "appmax@gmail.com",
  "password": "passkey"
});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("https://liquifytrades.herokuapp.com/register", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
Here is the schema of the Body
``` json
{
    "email": "app@gmail.com",
    "password": "passkey"
}
```
Here is schema output for successful registration
``` json
{
    "email": "appmax@gmail.com",
    "user_id": 5
}
```

### JOURNAL ROUTE
https://liquifytrades.herokuapp.com/journal

to create a new journal send a POST request with the following schema. Remember to attach the bearer token header in the request
``` json
{
    "date": "2012-23-02"
}
```
A 201 status code is returned for a successsfull journal created.
here is a sample reponse body.
```json
{
    "id":  23,
    "date": "2012-12-34",
    "user_id": 34
}
```
A sample request made in javascript
``` javascript
  var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjcwNjM5M3ODd9.uBXXYNGyKVqR1qAnu4fuEI9Embu2SdZHOIAcUMpKJg8");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
  "date": "2012-12-3"
});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("https://liquifytrades.herokuapp.com/journal", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

to view all users journal send a GET request to <br/> https://liquifytrades.herokuapp.com/journal.  <br/>
if the access_token header is validated , all users journals are returned with the following schema. 200 status code
```json
[
    {
        "date": "sample date",
        "user_id": 1,
        "id": 1
    },
]
```

to view a single journal details send a GET request to <br/>
https://liquifytrades.herokuapp.com/journal/journal_id_here <br/>
sample response
```json
[
    {
        "date": "2022-09-21",
        "user_id": 1,
        "id": 1
    },
    {
        "date": "2022-09-21",
        "user_id": 1,
        "id": 3
    },
    {
        "date": "2012-12-03",
        "user_id": 1,
        "id": 6
    }
]
```
here is a sample request to get all journals written in javascript fetch module
```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjcwNjM5MzA3ODd9.uBXXYNGyKVqR1qAnu4fuEI9Embu2SdZHOIAcUMpKJg8");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://liquifytrades.herokuapp.com/journal", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
to delete a Journal send a DELETE request to  
https://liquifytrades.herokuapp.com/journal/id_here  
a 202 status code is returned with a null  response <br/>
 sample javascript code to delete a journal using javascript fetch module
```javascript 
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjcwNjM5MzA3ODd9.uBXXYNGyKVqR1qAnu4fuEI9Embu2SdZHOIAcUMpKJg8");

var requestOptions = {
  method: 'DELETE',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://liquifytrades.herokuapp.com/journal/6", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

to get details of a single journal make a GET request to the endpoint https://liquifytrades.herokuapp.com/journal/id_here.
Here is a sample response of a successful request
```json
{
    "date": "2022-09-21",
    "id": 3,
    "trades": [
        {
            "journal_id": 3,
            "user_id": 1,
            "open_time": "12:34:00",
            "entry_price": 1.91155,
            "stop_loss": 1.9115,
            "notes": "EURUSD was bullish today, so took a counter trade",
            "id": 2,
            "symbol": "EURUSD",
            "close_time": "13:32:00",
            "close_price": 1.91134,
            "take_profit": 2.6758
        }
    ]
}
```
A sample javascript code for getting details of a single journal
```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjcwNjM5MzA3ODd9.uBXXYNGyKVqR1qAnu4fuEI9Embu2SdZHOIAcUMpKJg8");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://liquifytrades.herokuapp.com/journal/3", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

  ### TRADE ROUTE
to get all trades of a logged in user, send a GET request to the endpoint 
https://liquifytrades.herokuapp.com/trade  
 Here is a sample response of successfull request with 200 status code
```json
[
    {
        "open_time": "12:34:00",
        "user_id": 1,
        "journal_id": 2,
        "entry_price": 1.91155,
        "stop_loss": 1.9115,
        "notes": "EURUSD was bullish today, so took a counter trade",
        "id": 1,
        "symbol": "EURUSD",
        "close_time": "13:32:00",
        "close_price": 1.91134,
        "take_profit": 2.6758
    },
    {
        "open_time": "12:34:00",
        "user_id": 1,
        "journal_id": 3,
        "entry_price": 1.91155,
        "stop_loss": 1.9115,
        "notes": "EURUSD was bullish today, so took a counter trade",
        "id": 2,
        "symbol": "EURUSD",
        "close_time": "13:32:00",
        "close_price": 1.91134,
        "take_profit": 2.6758
    }
]
```
Here is sample request made with javascript fetch module
```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjcwNjM5MzA3ODd9.uBXXYNGyKVqR1qAnu4fuEI9Embu2SdZHOIAcUMpKJg8");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://liquifytrades.herokuapp.com/trade", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

to create a trade make  a POST request to the endpoint 
https://liquifytrades.herokuapp.com/trade with  the following body schema  <br/>
Here is sample schema of the body to attach to the request
```json
{
  "user_id": 0,
  "symbol": "string",
  "open_time": "string",
  "close_time": "string",
  "entry_price": 0,
  "close_price": 0,
  "stop_loss": 0,
  "take_profit": 0,
  "notes": "string",
  "journal_id": 0
}
```

A successful request returns a 



## SECURITY

## CONTRIBUTORS
