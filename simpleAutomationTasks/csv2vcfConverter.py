import csv

# takes contacts csv file and generates a vcf file 
with open('contacts-3.csv','r') as csvFile,open('contacts.vcf','a') as vcfFile:
    contacts=csv.reader(csvFile) #<-- list of lists
    foo=next(contacts) #<-- to avoid headers used next and it points to next row
    for contact in contacts:
        vcfFile.write('BEGIN:VCARD\n')
        vcfFile.write('VERSION:3.0\n')
        vcfFile.write('N:'+contact[2]+';'+contact[1]+'\n') 
        vcfFile.write('FN:'+contact[0]+'\n')
        vcfFile.write('TEL;TYPE=mobile:'+contact[32]+'\n')
        vcfFile.write('END:VCARD\n')
        vcfFile.write('\n')
    print('contants saved to vcf')

    '''
    as we have opened csv and vsf in context manager no need to close manually it does for us
    also note these specific indecies are for my own csv file you might need to change them for you to work it
    '''

    '''
    this is the formate I have used for my V-card you can add other info as well if that is important to you
    BEGIN:VCARD
    VERSION:3.0
    N:lastname;firstname;;;
    FN:full name
    TEL;TYPE=mobile:0123456789
    END:VCARD
    '''

    '''
    How to use
    just take a look at your csv file get which col info you want to save
    construct your vcf accordingly
    then just open file in read mode and write into another csv file
    '''