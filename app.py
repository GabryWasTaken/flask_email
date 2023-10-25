from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com' #Smtp server
app.config['MAIL_PORT'] = 587 #Smtp port
app.config['MAIL_USE_TLS'] = True #Transport layer security
app.config['MAIL_USERNAME'] = 'YOUR_EMAIL'
app.config['MAIL_PASSWORD'] = 'GOOGLE APP PASSWORD -->' #https://myaccount.google.com/apppasswords

mail = Mail(app)

@app.route('/')
def index():
    msg = Message(
        'Email tutorial', #Subject
        sender=('YOUR NAME','YOUR EMAIL'), #Sender
        recipients=['jack@fakemail.com'], #recipient list
        #Message body with html
        html='''<!DOCTYPE html> 
<html>
  <head>
    <meta charset="UTF-8">
    <title>HTML Email with Inline CSS</title>
    <style>
      /* Inline CSS styles */
      body {
        font-family: Arial, sans-serif;
        font-size: 16px;
        line-height: 1.5;
        color: #333;
        background-color: #f5f5f5;
      }
      h1 {
        font-size: 24px;
        font-weight: bold;
        color: #007bff;
        margin-top: 0;
      }
      p {
        margin-bottom: 1em;
      }
      a {
        color: #007bff;
        text-decoration: none;
      }
      a:hover {
        text-decoration: underline;
      }
      .container {
        max-width: 600px;
        margin: 0 auto;
        padding: 20px;
        background-color: #fff;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        border-radius: 5px;
      }
      .header {
        background-color: #007bff;
        color: #fff;
        padding: 10px;
        border-radius: 5px 5px 0 0;
      }
      .header h1 {
        margin: 0;
      }
      .content {
        padding: 20px;
      }
      .footer {
        background-color: #f5f5f5;
        color: #333;
        padding: 10px;
        border-radius: 0 0 5px 5px;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="header">
        <h1>HTML Email with Inline CSS</h1>
      </div>
      <div class="content">
        <p>This is an example of an HTML email with inline CSS styles.</p>
        <p>You can use inline CSS to style your HTML email, but keep in mind that not all email clients support all CSS properties. It's best to keep your styles simple and test your email in different email clients to ensure that it looks good for everyone.</p>
        <p>Here's an example of a <a href="#">link</a> in the email.</p>
      </div>
      <div class="footer">
        <p>Copyright © 2021</p>
      </div>
    </div>
  </body>
</html>'''
    )
    with app.open_resource('test.txt') as txt:
        msg.attach('text.txt','text/plain',txt.read())
    mail.send(msg)
    return 'Message sent!'

@app.route('/bulk')
def bulk():
    users = [{'name': 'Jack', 'email': 'jack@fakemail.com'},{'name': 'Nick', 'email': 'nick@fakemail.com'}]
    with mail.connect() as conn:
        for user in users:
            msg = Message(
                'Bulk test', #Subject
                recipients=[user['email']], #recipient list
                sender=('YOUR NAME','YOUR EMAIL'),
                html='''<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>HTML Email with Inline CSS</title>
    <style>
      /* Inline CSS styles */
      body {
        font-family: Arial, sans-serif;
        font-size: 16px;
        line-height: 1.5;
        color: #333;
        background-color: #f5f5f5;
      }
      h1 {
        font-size: 24px;
        font-weight: bold;
        color: #007bff;
        margin-top: 0;
      }
      p {
        margin-bottom: 1em;
      }
      a {
        color: #007bff;
        text-decoration: none;
      }
      a:hover {
        text-decoration: underline;
      }
      .container {
        max-width: 600px;
        margin: 0 auto;
        padding: 20px;
        background-color: #fff;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        border-radius: 5px;
      }
      .header {
        background-color: #007bff;
        color: #fff;
        padding: 10px;
        border-radius: 5px 5px 0 0;
      }
      .header h1 {
        margin: 0;
      }
      .content {
        padding: 20px;
      }
      .footer {
        background-color: #f5f5f5;
        color: #333;
        padding: 10px;
        border-radius: 0 0 5px 5px;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="header">
        <h1>HTML Email with Inline CSS</h1>
      </div>
      <div class="content">
        <p>This is an example of an HTML email with inline CSS styles.</p>
        <p>You can use inline CSS to style your HTML email, but keep in mind that not all email clients support all CSS properties. It's best to keep your styles simple and test your email in different email clients to ensure that it looks good for everyone.</p>
        <p>Here's an example of a <a href="#">link</a> in the email.</p>
      </div>
      <div class="footer">
        <p>Copyright © 2021</p>
      </div>
    </div>
  </body>
</html>'''
            )
            conn.send(msg)
    


if __name__ == '__main__':
    app.run(debug=True)