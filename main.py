from tkinter import Tk, Label, Button
import requests

ip = requests.get('https://api.ipify.org/?format=json').json()['ip']
info=requests.get(f'https://ipinfo.io/{ip}/geo').json()

btn_dict = {}
label_dict = {}
window=None

def come_back():
    btn_dict['2'].grid_forget()
    label_dict['0'].grid_forget()
    for i in range(0, 2):
        if i == 0:
            btn_dict[str(i)].grid(row=0,column=i, padx=15, pady=15)
        else:
            btn_dict[str(i)].grid(row=0,column=i+1, padx=15, pady=15)

def insert_text(lb: Label, dict: dict):
    text = ''
    for key in dict:
        text += '\n' + key + ': ' + dict[key]
    lb.config(text='Geolocation:' + text)

def display_ip():
    for btn in btn_dict:
        btn_dict[btn].grid_forget()
    label = Label(text=f'IP address: {ip}', font=('Georgia', 14))
    label.grid(row=0, column=0, padx=15, pady=15)
    label_dict['0'] = label
    add_button('Come back', 2, come_back, '2')

def display_geo():
    for btn in btn_dict:
        btn_dict[btn].grid_forget()
    label = Label(text=f'Geolocation:', font=('Georgia', 14), anchor='e', justify='left')
    insert_text(label, info)
    label.grid(row=0, column=0, padx=15, pady=15)
    label_dict['0'] = label
    add_button('Come back', 2, come_back, '2')

def add_button(txt, clm, cmd, key):
    btn = Button(text=txt, command=cmd)
    btn.grid(row=0,column=clm, padx=15, pady=15)
    btn_dict[key] = btn

window = Tk()
window.title("Location")
window.minsize(500, 380)
window.columnconfigure(index=1, weight=1)
add_button('Get IP', 0, display_ip, '0')
add_button('Get geolocation', 2, display_geo, '1')
window.mainloop()
