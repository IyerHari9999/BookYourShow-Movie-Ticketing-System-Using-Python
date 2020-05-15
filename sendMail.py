#email with image attachment

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

if __name__!='__main__':
    def sendMsg(title,seatList,emailID,seatListText):
        msg = MIMEMultipart()
        print(type(seatList))

        print("ELE: ")
        body="Hello there, Your tickets for  have been successfully booked for "+title+" Your seats number are: \n"
        print("ELE: ")
        for ele in seatListText:
            body=body+str(ele)+"\n"


        text = MIMEText(body)
        print(body)

        fromaddr="kishaturyuga12112@gmail.com"     #enter email id to recieve email to
        toaddr=emailID
        msg['From']=fromaddr
        msg['To']=toaddr
        msg['Subject']="Booking Confirmation!"
        msg.attach(text)

        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(fromaddr,"qpvpdpmrhxirmafu")   #enter app password in place of pass
        while True:
            try:
                server.send_message(msg)
                print("Message sent...")
                server.quit()
                break
            except Exception as e:
                print("Exception {},message not sent".format(e))
