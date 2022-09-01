# LIQUIFY TRADES

this is repo hosts code for backend development for Liquify Trades, a trading journal which aims at improving trading perfomance

## TECH STACK.



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




 

## SECURITY

## CONTRIBUTORS
