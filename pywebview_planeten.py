import webview
import time
#import planeten

'''
def load_html(window):
    time.sleep(5)
    window.load_html('<h1>This is dynamically loaded HTML</h1>')
'''

if __name__ == '__main__':
    window = webview.create_window('Load HTML Example','html.html')
    webview.start()

#ds= planeten.getres()
    
