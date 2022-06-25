
import tkinter as tk
from PIL import Image, ImageTk
import json




    
#creating the Window

window=tk.Tk()
window.title(" DEVELOPMENT OF MY INVESTMENTS  ")
window.geometry("1200x1200")

### Basic Layout ###


# Titel

titel = tk.Label(text = 'DEVELOPMENT OF MY INVESTMENTS        ' , font=('Avenir',22))
titel.grid(column=2,row=0)

#Space
space = tk.Label(text = '')
space.grid(column=1,row=1)


#### Descriptions ###


#Start Investment
start_inv = tk.Label(text = "Start Investment DFI/BTC: ")
start_inv.grid(column=0,row=2)

#Date of Investment
start_date_btc_dfi = tk.Label(text = 'Start BTC/DFI Pool: 17/03/2021 - 6500€ *', font=('Avenir',15))
start_date_btc_dfi.grid(column=2,row=3)

#Space
space = tk.Label(text = '')
space.grid(column=0,row=3)

#BTC Start/Current
start_btc = tk.Label(text = 'Start Price/Amount BTC: ')
start_btc.grid(column=0,row=4)

current_btc = tk.Label(text = "Current Price/Amount BTC: ")
current_btc.grid(column=0,row=5)

#Space
space = tk.Label(text = '')
space.grid(column=0,row=6)

#DFI
start_dfi = tk.Label(text = "Start Price/Amount DFI: ")
start_dfi.grid(column=0,row=7)

current_dfi = tk.Label(text = "Current Price/Amount DFI: ")
current_dfi.grid(column=0,row=8)

#Space
space = tk.Label(text = '')
space.grid(column=0,row=9)

#ETH
start_date_eth_dfi = tk.Label(text = "Start ETH/DFI Pool: 30/05/2021 - 2000€", font=('Avenir',15))
start_date_eth_dfi.grid(column=2,row=9)

start_eth = tk.Label(text = "Start Price/Amount ETH: ")
start_eth.grid(column=0,row=10)

current_eth = tk.Label(text = "Current Price/Amount ETH: ")
current_eth.grid(column=0,row=11)

#space
space = tk.Label(text = 'Result Without Investment:',font=('Avenir',15))
space.grid(column=1,row=12)

space = tk.Label(text = 'Result With Investment:',font=('Avenir',15))
space.grid(column=2,row=12)

#btc/dfi increase/decrease
btc_label = tk.Label(text = 'increase/decrease BTC: ')
btc_label.grid(column=0,row=13)

dfi_label = tk.Label(text = 'increase/decrease DFI: ')
dfi_label.grid(column=0,row=14)

eth_label = tk.Label(text = 'increase/decrease ETH: ')
eth_label.grid(column=0,row=15)

current_investment = tk.Label(text = 'Value of Investment Now: ')
current_investment.grid(column=0,row=16)

#### ENTRY FIELDS ###

#fixed values

start_inv_fix = tk.IntVar(value='10900')

start_btc_fix = tk.IntVar(value='55000')
amount_btc_fix = tk.IntVar(value='0.072')

start_dfi_fix = tk.IntVar(value='3.5')
amount_dfi_fix = tk.IntVar(value='1767')

start_eth_fix = tk.IntVar(value='2450')
amount_eth_fix = tk.IntVar(value='0.589')



start_btc_fix_1 = tk.IntVar(value='55000')
amount_btc_fix_1 = tk.IntVar(value='0.072')

start_dfi_fix_1 = tk.IntVar(value='3.5')
amount_dfi_fix_1 = tk.IntVar(value='1767')

start_eth_fix_1 = tk.IntVar(value='2450')
amount_eth_fix_1 = tk.IntVar(value='0.589')

#LOAD

with open("/Users/jonasmeteling/Documents/Programming/Learning_Python/App_Project/json-dump5.json", "r") as read_file:
    data = json.load(read_file)

cbtc_3 = tk.IntVar(value=data['cbtc_3'])
cdfi_3 = tk.IntVar(value=data['cdfi_3'])
ceth_3 = tk.IntVar(value=data['ceth_3'])

cambtc_3 = tk.IntVar(value=data['cambtc_3'])
camdfi_3 = tk.IntVar(value=data['camdfi_3'])
cameth_3 = tk.IntVar(value=data['cameth_3'])
date_3 = tk.IntVar(value=data['date_2'])

#

#date = tk.IntVar(value=data['date_1'])
      
#Start Investments
start_inv = tk.Entry(textvariable=start_inv_fix)
start_inv.grid(column=1,row=2)

#Date
date_1 = tk.Entry(textvariable=date_3)
date_1.grid(column=2,row=2)

#BTC Start/Amount/Current
start_btc = tk.Entry(textvariable=start_btc_fix)
start_btc.grid(column=1,row=4)

start_amount_btc = tk.Entry(textvariable=amount_btc_fix)
start_amount_btc.grid(column=2,row=4)

current_btc = tk.Entry(textvariable=cbtc_3)
current_btc.grid(column=1,row=5)

current_amount_btc = tk.Entry(textvariable=cambtc_3)
current_amount_btc.grid(column=2,row=5)

#DFI
start_dfi = tk.Entry(textvariable=start_dfi_fix)
start_dfi.grid(column=1,row=7)

start_amount_dfi = tk.Entry(textvariable=amount_dfi_fix)
start_amount_dfi.grid(column=2,row=7)

current_dfi = tk.Entry(textvariable=cdfi_3)
current_dfi.grid(column=1,row=8)

current_amount_dfi = tk.Entry(textvariable=camdfi_3)
current_amount_dfi.grid(column=2,row=8)


#ETH
start_eth = tk.Entry(textvariable=start_eth_fix)
start_eth.grid(column=1,row=10)

start_amount_eth = tk.Entry(textvariable=amount_eth_fix)
start_amount_eth.grid(column=2,row=10)

current_eth = tk.Entry(textvariable=ceth_3)
current_eth.grid(column=1,row=11)

current_amount_eth = tk.Entry(textvariable=cameth_3)
current_amount_eth.grid(column=2,row=11)


# Calculations

def entry(event):

    #variables

    sinv = float(start_inv.get())

    sbtc = float(start_btc.get())
    cbtc = float(current_btc.get())
        
    sdfi = float(start_dfi.get())
    cdfi = float(current_dfi.get())

    seth = float(start_eth.get())
    ceth = float(current_eth.get())

    sambtc = float(start_amount_btc.get())
    cambtc = float(current_amount_btc.get())

    sameth = float(start_amount_eth.get())
    cameth = float(current_amount_eth.get())

    samdfi = float(start_amount_dfi.get())
    camdfi = float(current_amount_dfi.get())
    
    #calculation
    btc_result = (sbtc - cbtc) / sbtc * -100
    dfi_result = (sdfi - cdfi) / sdfi * -100
    eth_result = (seth - ceth) / seth * -100
    
    amount_result_btc = (sambtc - cambtc) / sambtc * -100
    amount_result_eth = (sameth - cameth) / sameth * -100
    amount_result_dfi = (samdfi - camdfi) / samdfi * -100

    inv_result = (btc_result + dfi_result +eth_result) /3 * 0.01 * sinv + sinv
    
    total_percentage_gain = (amount_result_btc + amount_result_eth + amount_result_dfi) / 3
    
    inv_total_percentage = (sinv - inv_result) / sinv * -100

    total_value_gain = (cbtc*cambtc) + (cdfi*camdfi) + (ceth*cameth)

    btc_result = format(btc_result, '.2f')
    dfi_result = format(dfi_result, '.2f')
    eth_result = format(eth_result, '.2f')
    
    inv_result = format(inv_result, '.2f')
    
    amount_result_btc = format(amount_result_btc, '.2f')
    amount_result_eth = format(amount_result_eth, '.2f')
    amount_result_dfi = format(amount_result_dfi, '.2f')

    inv_total_percentage = format(inv_total_percentage, '.2f')
    total_percentage_gain = format(total_percentage_gain, '.2f')
    total_value_gain = format(total_value_gain, '.2f')
    
    
    
#label
    btc_label1 = tk.Label(text = f'{btc_result}%')
    btc_label1.grid(column=1,row=13)
    btc_label2 = tk.Label(text = f'{amount_result_btc}% more BTC')
    btc_label2.grid(column=2,row=13)

    dfi_label1 = tk.Label(text = f'{dfi_result}%')
    dfi_label1.grid(column=1,row=14)
    dfi_label2 = tk.Label(text = f'{amount_result_dfi}% more DFI')
    dfi_label2.grid(column=2,row=14)

    eth_label1 = tk.Label(text = f'{eth_result}%')
    eth_label1.grid(column=1,row=15)
    eth_label2 = tk.Label(text = f'{amount_result_eth}% more ETH')
    eth_label2.grid(column=2,row=15)

#result
    inv_label = tk.Label(text = f'{inv_total_percentage}% = ${inv_result}')
    inv_label.grid(column=1,row=16)
    inv_labe2 = tk.Label(text = f'{total_percentage_gain}% = ${total_value_gain}')
    inv_labe2.grid(column=2,row=16)
    
    return sinv


#safe function



def safe(event):

    date_2 = str(date_1.get())

    cbtc_1 = float(current_btc.get())
    cdfi_1 = float(current_dfi.get())
    ceth_1 = float(current_eth.get())
    
    cambtc_1 = float(current_amount_btc.get())
    cameth_1 = float(current_amount_eth.get())
    camdfi_1 = float(current_amount_dfi.get())

    # date_1 = date.today()
    
    data = { 'cbtc_3' : cbtc_1,
             'cdfi_3' : cdfi_1,
             'ceth_3' : ceth_1,
             
             'cambtc_3' : cambtc_1,
             'camdfi_3' : camdfi_1,
             'cameth_3' : cameth_1,
             'date_2' : date_2 }

    with open("/Users/jonasmeteling/Documents/Programming/Learning_Python/App_Project/json-dump5.json", "w") as write_file:
        json.dump(data, write_file)
        

#Button Calculate

space = tk.Label(text = '',font=('Times new roman',20))
space.grid(column=3,row=17)

button = tk.Button(window,text='Calculate',width=20,height=3)
button.grid(column=1,row=18)
button.bind('<Button-1>',entry)

#Button Save

button_safe = tk.Button(window,text='Safe',width=20,height=3)
button_safe.grid(column=1,row=19)
button_safe.bind('<Button-1>',safe)

#Notes

note_1 = tk.Label(text = "*+700€ at the time I invested")
note_1.grid(column=2,row=19)

# Image

image = Image.open('/Users/jonasmeteling/Documents/Programming/Learning_Python/App_Project/Lotus.jpeg')     #specify the path of the image
image.thumbnail((100,100),Image.ANTIALIAS)    #100,100 is the resolution
#ANTIALIAS helps to deal some problems while using images
photo= ImageTk.PhotoImage(image)   #converts the image to a tkinter image
label_image= tk.Label(image=photo)  #stores the image in a label
label_image.grid(column=1,row=0)
label_image2= tk.Label(image=photo)  #stores the image in a label
label_image2.grid(column=3,row=0)



window.mainloop()
