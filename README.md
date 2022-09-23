![hero](https://user-images.githubusercontent.com/111843624/187912322-acbc1b5b-6748-4c53-a43e-fc03e7f85c13.png)





# LIQUIFY TRADES

this is repo hosts code for backend development for Liquify Trades, a trading journal which aims at improving trading perfomance

## TECH STACK.
https://img.shields.io/static/v1?label=&message=HEROKU&color=<COLOR>


## DEPLOYMENT


## ROUTES DOCUMENTATION
The swaggger documentation can be found at https://liquifytrades.herokuapp.com/docs   <br/>

### Login route

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


### Register Route

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
    "date": 2012-23-02
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
A sample request
``` javascript
  sample code here
```

to view all users journal send a GET request to <br/> https://liquifytrades.herokuapp.com/journal.  <br/>
if the access_token header is validated , all users journals are returned with the following schema. 200 status code
```json
{
  "sample schema here"
}
```

to view a single journal details send a GET request to <br/>
https://liquifytrades.herokuapp.com/journal/journal_id_here <br/>
sample response
```json
{
  "sample response"
}
```
to delete a Journal send a DELETE request to <br/>
https://liquifytrades.herokuapp.com/journal/id_here <br/>
a 200 status code is returned.
sample response
```json
{
    "sample schema"
} 
```
 sample javascript code
```javascript 
    sample code
```




## SECURITY

## CONTRIBUTORS
