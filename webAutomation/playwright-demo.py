# from typing_extensions import ParamSpecArgs
from playwright.sync_api import sync_playwright

url='https://www.adobe.com/in/acrobat/online/ppt-to-pdf.html'

with sync_playwright() as session:
    browser=session.webkit.launch()
    page=browser.new_page()
    page.goto(url)
    print(page.title())
    page.set_input_files('text=Select a file','test.pptx')
    browser.close()