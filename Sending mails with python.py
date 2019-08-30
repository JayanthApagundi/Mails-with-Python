""" YOU CAN SEND MAILS IN A EASIER WAY AND CAN SEND TO AS MANY PEOPLE AS U WANT WITH THIS SNIPPET OF CODE
  This is code written in Python and a Glimpse of HTML tags 
  to render the format of email. There are steps of execution to be followed:
1. Open terminal and type "python" [enter] this wil take you to the python interpreter shell
2. Copy and paste the 1st four lines of code i.e; from import smtplib to port =587 [enter]
3. Copy and paste the user name and password lines in python interpreter shell  [enter]
4. Hence, evrything is estalished alter the email contents acccording to your need and copy and paste the whole thing i.e; from_email to end of the code email_connquit()
   and the job is done"""

import smtplib                   
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText             #to get the proper libraries and packages imported
host = "smtp.gmail.com"                          #is a universal host for mails
port = 587                                       #universal Port
username = "sample@gmail.com"     #Your email
password = "sample"               #Your password 
from_email = username
to_list = ["sample0gmail.com","sample1@gmail.com"]     #There could be N no. of emails mentioned
email_conn = smtplib.SMTP(host,port)             #to provide the connection of host and port
email_conn.ehlo()                                #to see the status of email
email_conn.starttls()                            #start the connection with internet
email_conn.login(username, password)             #take the login and passwords
the_msg=MIMEMultipart("alternative")             #the_msg treated as objects to render the contents of email with MIME____ package or module
the_msg['subject']="hello world"                 #subject of the email
the_msg["from"]=from_email
plain_txt="testing the message"
#in this section you can write your emails and mention links and so on
html_txt="""\
<html>
 <head></head>
 <body>
  <p>Hey..!<br>
    Message to be sent<b>message(bold)<b> made by <a href= (can mention links) </a>.
  </p>
 </body>
</html>
"""
#The above part basically can implement the message in any formats and manipulate it using HTML tags
part1=MIMEText(plain_txt,'plain')
part2=MIMEText(html_txt,"html")
the_msg.attach(part1)
the_msg.attach(part2) 
email_conn.sendmail(from_email, to_list, the_msg.as_string())        #sending the email
email_conn.quit()                                                    #quit the connection