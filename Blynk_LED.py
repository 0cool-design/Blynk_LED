
import requests
import json
import tkinter as tk
import tkinter.ttk as ttk

Status = ""


class LED_class:

    def __init__(self, master=None):
        global Status
        # build ui
        self.frame1 = ttk.Frame(master)
        self.label1 = ttk.Label(self.frame1)
        self.label1.configure(anchor='e', font='{TkHeadingFont 13} 12 {bold}', justify='center', relief='flat')
        self.label1.configure(text='LED test')
        self.label1.pack(padx='10', pady='10', side='top')

        self.message1 = tk.Message(self.frame1)
        self.message1.configure(justify='center', text=Status)
        self.message1.pack(ipadx='40', padx='10', pady='10', side='top')

        self.On_button = tk.Button(self.frame1, bg='green', fg='white')
        self.On_button.configure(text='ON')
        self.On_button.pack(ipadx='10', ipady='7', padx='12', pady='12', side='left')
        self.On_button.configure(command= lambda: LED_class.SendReq(self, "1"))

        self.Off_button = tk.Button(self.frame1, bg='red', fg='white')
        self.Off_button.configure(text='OFF', )
        self.Off_button.pack(ipadx='10', ipady='7', padx='12', pady='12', side='left')
        self.Off_button.configure(command= lambda: LED_class.SendReq(self, "0"))

        self.frame1.configure(borderwidth='12', height='300', width='500')
        self.frame1.pack(side='top')

        # Main widget
        self.mainwindow = self.frame1

    def SendReq(self, value):
        global Status
        if value == 0:
            Status = "OFF"
        elif value == 1:
            Status = "ON"
        self.message1.configure(justify='center', text=Status)
        PinNM = "V2"
        BLYNK_AUTH = 'api auth'
        BLYNK_URL = 'http://188.166.206.43/'
        put_header={"Content-Type": "application/json"}
        put_body = json.dumps([value])
        r = requests.put(BLYNK_URL+BLYNK_AUTH+'/update/'+PinNM, data=put_body, headers=put_header)


    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    root.title("LED")
    app = LED_class(root)
    app.run()
