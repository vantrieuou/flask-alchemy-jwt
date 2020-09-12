# backend-auth


You need to build a small authentication server using python (we recommend you use Flask, Starlette or another low footprint framework supporting it) or Golang.
The server will serve the following endpoints:

* User registration: given an email address and a password as parameters, it creates a user record
* User login: given an email and password, it returns a session token if successful, or 40* error is not (distinguish between the different types of error)
* Password change: given an email, current password and new password.

The authentication server should be built using a mySQL database.
Passwords should not be stored in open form in the database, the administrator should not be able to see the current passwords of users.
The session token returned by the auth server should encode the user ID, the creation date and any other information you deem interesting. You can use a jwt token or define your own.

Please provide:
* A working server using Docker and Dockerfile to run it, with information in the readme on how to run it.
* Unit tests for the server.
* Well commented code that can serve as documentation of the  system.
 
In order to work on the project please clone the repo into your own account. 
Once finished, please invite the following people to your repo:
* @xavier.anguera
* @alan.shang


Bonus points: Add a script that tests the API end-to-end that can be used as an automated regression test.


