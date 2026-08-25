import smtplib
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
From="kolalavanyapriya9@gmail.com"
password="tfuo wtrr wneo kcue"
server.login(From,password)
To="21np1a4216@gmail.com"
subject="Sending mail using SMTP"
body="Hello lav how are you"
info=f"{subject}\n{body}"
server.sendmail(From,To,info)
print(f"Mail sent Successfully to {To}")
server.quit()