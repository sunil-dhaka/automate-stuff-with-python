import login,imaplib,pyzmail,csv

password=login.password_2t
email=login.email_2t
HOST='imap.gmail.com'
CSV_DATA=[]
headers=['nameR','emailR','nameS','emailS','subject','body_html','body_text']
CSV_DATA.append(headers)

def getEmailInfo():
    server=imaplib.IMAP4_SSL(HOST)
    server.login('dhaka.sonu.monu@gmail.com','edvojnoqplywvtwd')
    print('Logged In.')
    server.select(readonly=True)
    '''
    flags:
        UNSEEN, ALL, SEEN, DELETED, ANSWERED, FLAGGED, DRAFT, RECENT 
    '''
    messages=server.search(None,'ALL') 
    bytes_ids=[id.encode() for id in (messages[1][0].decode()).split(' ')]
    # print(bytes_ids)
    for id in bytes_ids:
        print(id)
        tmp_data=[]
        try:
            email_data=server.fetch(id,'RFC822') # 'BODY[]'
            print('Got data')
            pyzmail_data=pyzmail.PyzMessage.factory(email_data[1][0][1]) # see email_data to understand
            sender_info=list(pyzmail_data.get_address('from'))
            recv_info=list(pyzmail_data.get_address('to'))
            sub=pyzmail_data.get_subject()
            # sometimes html or text part are empty or don;t exist, in that case needs to be careful
            html_body=''
            if pyzmail_data.html_part!=None:
                html_body=pyzmail_data.html_part.get_payload().decode(pyzmail_data.html_part.charset)
            text_body=''
            if pyzmail_data.text_part!=None:
                text_body=pyzmail_data.text_part.get_payload().decode(pyzmail_data.text_part.charset)

            # add data to the list
            tmp_data.extend(recv_info)
            tmp_data.extend(sender_info)
            tmp_data.append(sub)
            tmp_data.append(html_body)
            tmp_data.append(text_body)

            CSV_DATA.append(tmp_data)

            with open('email_data.csv','w') as file:
                csvWriter=csv.writer(file)
                csvWriter.writerows(CSV_DATA)
        except Exception as error:
            print('Error: ',error)
        
    server.logout()

if __name__=="__main__":
    getEmailInfo()