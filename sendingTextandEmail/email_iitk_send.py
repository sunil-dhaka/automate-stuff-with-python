'''
usages: send automated text email from institute account
note: have to modify or give specific subject and body input
'''
import smtplib,sys
import login

def sendEmail(sender_email,password,dest_email,subject='Hello!',body='It is an automated mail. Do not reply.\n\nThank You'):
    newServer=smtplib.SMTP('smtp.cc.iitk.ac.in',465)
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
    password=login.password_k
    sendEmail(sender_email,password,dest_email)
