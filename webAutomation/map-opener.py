#----------------------Project: mapIt.py with the webbrowser Module-----------------#
import webbrowser, sys, pyperclip

if len(sys.argv)>1:
    where_to=' '.join(sys.argv[1:])
    print('This is where you have asked to go to: ',where_to)
else:
    where_to=pyperclip.paste()
    print('This is the destination stored into your clipboard: ',where_to)

print('I will map you to: ',where_to,'. Thank you.')
webbrowser.open('https://www.google.com/maps/place/'+where_to)