#sending emails using python

import smtplib
from email.message import EmailMessage
email=EmailMessage()  ## creating a object for emailmessage
email['from']='xyz name'   ##Person who is sending
email['to']='xyz id'            ##Whom we are sending
email['subject']='xyz subject'  ##subject of email
email.set_content("Xyz content of email")  ## content of email
with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:   ##sending request to server
    smtp.ehlo()        ##server object
smtp.starttls()     ##used to send data between server and client
smtop.login("email_id","Password") ##login id and password gmail
smtp.send_message(email)    ## sending email
print("email sent!!")    ## printing success message
