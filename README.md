# backend-auth


You need to build a small authentication server using python (we recommend you use Flask, Starlette or another low footprint framework supporting it).
The server will serve the following endpoints:

* User registration: given an email address and a password as parameters, it creates a user record
* User login: given an email and password, it returns a session token if successfu, 40* error is not (distinguish between the different types of error)
* Password change: give an email, current password and new password.

The authentication server should be built using a mySQL database.
Passwords should not be stored in open form in the database, the administrator should not be able to see the current passwords of users.
The session token returned by the auth server should encode the user ID, the creation date and any other information you deem interesting.

Please provide:
* a working server using Docker and Dockerfile to run it
* Unit tests for the server
* Well commented code that can serve as documentation of the  system
 
Once finished, please invite the following people to your repo:
* @xavier.anguera
* @dev1x


Bonus points: Add a script that tests the API end-to-end that can be used as an automated regression test.


