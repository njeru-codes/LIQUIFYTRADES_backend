# LIQUIFY TRADES

this is repo hosts code for backend development for Liquify Trades, a trading journal which aims at improving trading perfomance

## TECH STACK.



## DEPLOYMENT


## ROUTES DOCUMENTATION
The swaggger documentation can be found at https://liquifytrades.herokuapp.com/docs   <br/>

### Login route
<details><summary>details</summary>
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
</details>

### Register Route
<details><summary>Details</summary>
https://liquifytrades.herokuapp.com/register
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
</details>


 

## SECURITY

## CONTRIBUTORS
