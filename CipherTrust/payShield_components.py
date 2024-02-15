#
# GUI CipherTrust Tool to import payshield components.
# Importing tkinter module for GUI application
# Written by Matias Bendel.
# version 0.5
#

from tkinter import *
from tkinter import messagebox
from urllib3.exceptions import InsecureRequestWarning
from datetime import datetime
import requests
import time


def NextWindow(algo,n_comp,cm_ip,key_id,currentTime):
    global label_10,entry_10,label_11,entry_11,label_12,entry_12
    
    cm_user_var=StringVar()
    cm_pwd_var=StringVar()
    cm_domain_var=StringVar()
    key_var=StringVar()
    
    #messagebox.showerror('CipherTrust tool', f'CHECK:\nCM IP:{cm_ip}\nN comp:{n_comp}\nAlgo:{algo}')
        
    # Logica de la interfaz
    if (key_id==1):
        # Clear de la ventana original
        label_01.destroy()
        droplist.destroy()
        label_02.destroy()
        R1.destroy()
        R2.destroy()
        R3.destroy()
        label_03.destroy()
        entry_03.destroy()
    elif (key_id==n_comp+1):
        messagebox.showinfo('CipherTrust tool', 'Carga completa')
        exit(0)
    elif (key_id!=1):
        label_10.destroy()
        entry_10.destroy()
        label_11.destroy()
        entry_11.destroy()
        label_12.destroy()
        entry_12.destroy()
        
    label_10=Label(root,text=f"Component {key_id}",width=20,font=("bold",10))
    label_10.place(x=4,y=130)
    entry_10=Entry(root,textvariable=key_var)
    entry_10.place(x=205,y=130,width=220)
    
    label_11=Label(root,text="CipherTrust User",width=20,font=("bold",10))
    label_11.place(x=15,y=180)
    entry_11=Entry(root,textvariable =cm_user_var)
    entry_11.place(x=205,y=180,width=150)
        
    label_12=Label(root,text="CipherTrust Password",width=20,font=("bold",10))
    label_12.place(x=30,y=230)
    entry_12=Entry(root,textvariable=cm_pwd_var) #show='*'
    entry_12.place(x=205,y=230,width=150)
    
    label_12=Label(root,text="CipherTrust Domain",width=20,font=("bold",10))
    label_12.place(x=23,y=280)
    entry_12=Entry(root,textvariable = cm_domain_var)
    entry_12.place(x=205,y=280,width=150)

    #messagebox.showerror('CipherTrust tool', f'CHECK:\nCM IP:{cm_ip}\nN comp:{n_comp}\nAlgo:{algo}')
        
    B2=Button(root, text='Next', width=20, bg="black", fg='white', command=lambda:sendciphertrust(currentTime,algo,n_comp,cm_ip,key_id,key_var.get(),cm_user_var.get(),cm_pwd_var.get(),cm_domain_var.get()))
    B2.place(x=190,y=380)
    
    #messagebox.showinfo('CipherTrust tool', f'CHECK 9:\nCM IP:{cm_ip}\nN comp:{n_comp}\nAlgo:{algo}')
    

        
def sendciphertrust(currentTime,algo,n_comp,cm_ip,key_id,key,cm_user,cm_pwd,cm_domain):
    
    if (len(key) != 32):
        messagebox.showerror('CipherTrust tool', f'Error: The key length is not correct:\nKey:{key}\nKey Id:{key_id}\nUser:{cm_user}\nPass:{cm_pwd}')
        exit(0)
    
    # Suppress the warnings from urllib3
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    # Call CipherTrust API and retrieve API Key 
    data = {"name": cm_user, "password": cm_pwd, "domain": cm_domain}
    response = requests.post(f'https://{cm_ip}/api/v1/auth/tokens', json=data, verify=False)
    data = str(response.content).split('"')[1::2]
    api_key = data[1]
    if (not api_key):
        messagebox.showerror('CipherTrust tool', 'Error 401: CipherTrust Connection')    
    # Create in CipherTrust a new secret with key cryptographic material 
    headers = {'Authorization': f'Bearer {api_key}'}
    data = {"name": f"payshield_key_comp_{key_id}_{currentTime}", "dataType": "seed", "material": key}
    response = requests.post(f'https://{cm_ip}/api/v1/vault/secrets', headers=headers, json=data, verify=False)
    
    if (response):
        messagebox.showinfo('CipherTrust tool', f'payshield_key_comp_{key_id}_{currentTime} uploaded success')
        NextWindow(algo,n_comp,cm_ip,key_id+1,currentTime)
    else:
        messagebox.showerror('CipherTrust tool', 'Error 402: CipherTrust Connection') 

# Creating object 'root' of Tk()
root = Tk()

# Defining variables
algo_var=StringVar()
n_comp_var=IntVar()
cm_ip_var=StringVar()

# Providing Geometry to the form
root.geometry("500x450")

# Providing title to the form
root.title('Thales Group')

# Title widget using place() method
label_00=Label(root,text="payShield components\nCipherTrust import tool ", width=30,font=("bold",16))
label_00.place(x=55,y=25)

# Algorithm widget
label_01=Label(root,text="Algorithm",width=20,font=("bold",10))
label_01.place(x=12,y=130)
list_of_algo=[ 'DES [56 bits]' , '2DES [112 bits]' , '3DES [168 bits]' , 'AES [256 bits]']
droplist=OptionMenu(root,algo_var,*list_of_algo)
droplist.config(width=15)
algo_var.set('Select')
droplist.place(x=205,y=125)

# Number of components widget
label_02=Label(root,text="Components", width=20,font=("bold",10))
label_02.place(x=21,y=180)
R1=Radiobutton(root,text="1",padx=5, variable=n_comp_var, value=1)
R1.place(x=200,y=180)
R2=Radiobutton(root,text="2",padx=15, variable=n_comp_var, value=2)
R2.place(x=245,y=180)
R3=Radiobutton(root,text="3",padx=25, variable=n_comp_var, value=3)
R3.place(x=290,y=180)

# CipherTrust information
label_03=Label(root,text="CipherTrust IP", width=20,font=("bold",10))
label_03.place(x=25,y=230)
entry_03=Entry(root, textvariable = cm_ip_var)
entry_03.place(x=205, y=230, width=135)

currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%H%M%S")
key_id=1

#this creates button for next window
B1=Button(root, text='Next', width=20, bg="black", fg='white', command=lambda:NextWindow(algo_var.get(),n_comp_var.get(),cm_ip_var.get(),key_id,currentTime))
B1.place(x=190,y=380)

#this will run the mainloop.
root.mainloop()