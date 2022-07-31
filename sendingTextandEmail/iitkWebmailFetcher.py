'''
usages: scrapes emails data from IIT server for personal account
note: there is an issue and that is login authentication
'''
import login,pyzmail,csv,imapclient

password=login.password_k
email=login.email_k
HOST='qasid.iitk.ac.in'

CSV_DATA=[]
headers=['from','to','time','subject','body_html']
CSV_DATA.append(headers)

def getEmailInfo():
    server=imapclient.IMAPClient(HOST)
    server.login(email,password)
    print('Logged In.')
    server.select_folder('INBOX.Sent',readonly=True)
    '''
    flags:
        UNSEEN, ALL, SEEN, DELETED, ANSWERED, FLAGGED, DRAFT, RECENT 
    '''
    UIDs=server.search(['ALL']) 
    for id in UIDs:
        print(id)
        tmp_data=[]
        try:
            email_data=server.fetch([id], ['BODY[]', 'FLAGS'])
            print('Got data')
            pyzmail_data=pyzmail.PyzMessage.factory(email_data[id][b'BODY[]']) # see email_data to understand
            sender_info=pyzmail_data.get_decoded_header('from')
            recv_info=pyzmail_data.get_decoded_header('to')
            time_info=pyzmail_data.get_decoded_header('date')
            sub=pyzmail_data.get_decoded_header('subject')
            # sometimes html or text part are empty or don;t exist, in that case needs to be careful
            html_body=''
            if pyzmail_data.html_part!=None:
                html_body=pyzmail_data.html_part.get_payload().decode(pyzmail_data.html_part.charset)
            
            # add data to the list
            tmp_data.append(recv_info)
            tmp_data.append(sender_info)
            tmp_data.append(time_info)
            tmp_data.append(sub)
            tmp_data.append(html_body)

            CSV_DATA.append(tmp_data)

            with open('email_data.csv','w') as file:
                csvWriter=csv.writer(file)
                csvWriter.writerows(CSV_DATA)
        except Exception as error:
            print('Error: ',error)
        
    server.logout()

if __name__=="__main__":
    getEmailInfo()