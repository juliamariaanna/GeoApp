from tkinter import Tk, Label, Button
import requests

ip = requests.get('https://api.ipify.org/?format=json').json()['ip']
info=requests.get(f'https://ipinfo.io/{ip}/geo').json()
coords=info.get('loc').split(',')
sun_info=requests\
    .get(f'https://api.sunrise-sunset.org/json?lat={coords[0]}&lng={coords[1]}&formatted=0')\
    .json()

# fetch results from sun info
results=sun_info.get('results')
btn_dict = {}
label_dict = {}
window=None

def hide():
    for btn in btn_dict:
        btn_dict[btn].grid_forget()
    add_button('Come back', 2, come_back, '3')

def come_back():
    btn_dict['3'].grid_forget()
    if label_dict.get('0'):
        label_dict['0'].grid_forget()
    for i in range(0, 3):
        btn_dict[str(i)].grid(row=0,column=i, padx=15, pady=15)

def insert_text(lb: Label, dict: dict):
    text = ''
    for key in dict:
        text += '\n' + key + ': ' + str(dict[key])
    lb.config(text='Geolocation:' + text)

def display_ip():
    hide()
    add_label({'text':f'IP address: {ip}', 'font': ('Georgia', 14)})

def display_geo():
    hide()
    add_label({'text': f'Geolocation:',\
                'font': ('Georgia', 14), 'anchor': 'e', 'justify': 'left'}, info)
    

def display_sun_info():
    hide()
    add_label({'text': 'Day condition', 'font':('Georgia', 14),\
                'anchor': 'e', 'justify': 'left'}, results)

def add_button(txt, clm, cmd, key):
    btn = Button(text=txt, command=cmd)
    btn.grid(row=0,column=clm, padx=15, pady=15)
    btn_dict[key] = btn

def add_label(config=None, dict_txt=None):
    label = Label()
    label.config(config)
    if dict_txt:
        insert_text(label, dict_txt)
    label.grid(row=0, column=0, padx=15, pady=15)
    label_dict['0'] = label

window = Tk()
window.title("Location")
window.minsize(500, 380)
window.columnconfigure(index=1, weight=1)
add_button('Get IP', 0, display_ip, '0')
add_button('Get sun info', 1, display_sun_info, '1')
add_button('Get geolocation', 2, display_geo, '2')
window.mainloop()
