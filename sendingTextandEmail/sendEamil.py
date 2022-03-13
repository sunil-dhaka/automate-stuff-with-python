import smtplib,sys
import login

def sendEmail(sender_email,password,dest_email,subject='Hello!',body='It is an automated mail. Do not reply.\n\nThank You'):
    newServer=smtplib.SMTP('smtp.gmail.com',587)
    newServer.ehlo()
    newServer.starttls()
    newServer.login(sender_email,password)
    message='Subject:'+subject+'\n\n'+body
    newServer.sendmail(sender_email,dest_email,message)

    print('Email send to ',dest_email,' from ',sender_email)

    newServer.quit()

if __name__=="__main__":
    if len(sys.argv)>2:
        sender_email=sys.argv[1]
        dest_email=sys.argv[2]
    else:
        print('<sender-email> <receiver-email>')
        sys.exit()
    # password=getpass(prompt='password> ')
    password=login.password_m
    sendEmail(sender_email,password,dest_email)
