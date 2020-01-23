import  smtplib

server = smtplib.SMTP("")
server.sendmail("","","")
server.quit()
