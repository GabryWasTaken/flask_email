![Email](https://cdn.discordapp.com/attachments/733391066136313879/1166767520733208587/FLASK_EMAIL.png?ex=654bafee&is=65393aee&hm=afdb74f9198edd37a94b4281176c545d3e5e31a4a8c58bb6d3a685bde9b5d53f&)

![Logo](https://img.shields.io/badge/Created%20by-GabryWasTaken-darkblue)
## DESCRIPTION
This API send a preimpostated mail with an html body to an email that you decide in the app.py code, the app send an email when you enter in the '/' route. You can apply this code easily to a register/login page easily. This API uses the google smtp so to use it you need to create an password app from the google site (more information directly in the code). \
In the bulk route you can send the same email to more users at the same time.
## PREREQUISITES

![Python3](https://img.shields.io/badge/Install-Python%203%20or%20greater-blue?link=https%3A%2F%2Fwww.python.org%2Fdownloads%2F)

Install the external dependencies, they are located in
```bash
requirements.txt
```
## HOW TO RUN PROGRAM

* Install all of the prerequisites in your virtual environment or your machine with the following command:
```bash
pip install -r requirements.txt
```
* Write this command to run the webapp:
```bash
python3 ./app.py
``` 
* Or : 
```bash
flask run
``` 
if you wanna start the program with flask run you need to set the environment variable with the command:
```bash
set FLASK_APP=app.py
``` 
