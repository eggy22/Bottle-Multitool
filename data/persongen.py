import requests
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter.messagebox as msg
from tkinter import filedialog



def features():
    r3=Toplevel(root)
    r3.title("What's New")
    r3.resizable(False,False)
    r3.iconbitmap("icon.ico")
    mf6=ttk.Frame(r3,padding='3 3 12 12')
    mf6.pack(fill="both",expand="yes")
    mf6.rowconfigure(0,weight=1)
    mf6.columnconfigure(0,weight=1)
    l=ttk.Label(mf6,background="#19284B")
    l.pack(fill="both",expand="yes")
    ttk.Label(l,text="v1.0.0",foreground="white",background="#19284B",font=("Arial black",16)).grid(row=2,column=0)
    ttk.Separator(l,orient="horizontal").grid(row=3,column=0,columnspan=5,sticky="ew")
    ttk.Label(l,text="1. Generate Random Person Data.",foreground="white",background="#19284B",font=("Calibri",16)).grid(row=5,column=0)
    ttk.Label(l,text="2. Export all Data to Text File.",foreground="white",background="#19284B",font=("Calibri",16)).grid(row=6,column=0)
    ttk.Label(l,text="3. Does Not Require External Libraries.",foreground="white",background="#19284B",font=("Calibri",16)).grid(row=7,column=0)
    ttk.Label(l,text="4. Gathers Personal Details,Registration Details \n\t and Accurate Address.",foreground="white",background="#19284B",font=("Calibri",16)).grid(row=8,column=0)

def export():
    filename.set(filedialog.asksaveasfilename(title="Select Location of File",filetypes=(("Text files","*.txt"),)))
    file=open(filename.get()+".txt","w")
    export_str="Name: "+name.get()+"\n"\
               "Age: "+age.get()+"\n"\
               "D.O.B: "+dob.get()+"\n"\
               "Gender: "+gender.get()+"\n"\
               "cell: "+cell.get()+"\n"\
               "Email: "+email.get()+"\n"\
               "Register Age: "+register_age.get()+"\n"\
               "Register Date: "+register_date.get()+"\n"\
               "Id Name: "+id_name.get()+"\n"\
               "Id Value: "+id_value.get()+"\n"\
               "Username: "+username.get()+"\n"\
               "Password: "+password.get()+"\n"\
               "Salt: "+salt.get()+"\n"\
               "Md5: "+md5.get()+"\n"\
               "SHA1: "+sha1.get()+"\n"\
               "SHA256: "+sha256.get()+"\n"\
               "UUID: "+uuid.get()+"\n"\
               "City: "+city.get()+"\n"\
               "Street Name: "+street_name.get()+"\n"\
               "Street Number: "+street_number.get()+"\n"\
               "State: "+state.get()+"\n"\
               "Country: "+country.get()+"\n"\
               "Post Code: "+postcode.get()+"\n"\
               "Latitude: "+lat.get()+"\n"\
               "Longitude: "+lon.get()+"\n"\
               "Timezone Offset: "+timezone_offset.get()+"\n"\
               "Timezone Description: "+timezone_desc.get()+"\n"\
               "Picture URL: "+pic_large.get()+"\n"             
    file.write(export_str)
    file.close()

def generate():
    url="https://randomuser.me/api/"
    try:
        response=requests.get(url)
        data=response.json()
    except:
        msg.showerror("Error","Check your Connection!!")
    else:
        name.set(data['results'][0]['name']['title']+" "+data['results'][0]['name']['first']+" "+data['results'][0]['name']['last'])
        age.set(data['results'][0]['dob']['age'])
        dob.set(data['results'][0]['dob']['date'])
        gender.set(data['results'][0]['gender'])
        cell.set(data['results'][0]['cell'])
        email.set(data['results'][0]['email'])
        register_age.set(data['results'][0]['registered']['age'])
        register_date.set(data['results'][0]['registered']['date'])
        id_name.set(data['results'][0]['id']['name'])
        id_value.set(data['results'][0]['id']['value'])
        username.set(data['results'][0]['login']['username'])
        password.set(data['results'][0]['login']['password'])
        salt.set(data['results'][0]['login']['salt'])
        md5.set(data['results'][0]['login']['md5'])
        sha1.set(data['results'][0]['login']['sha1'])
        sha256.set(data['results'][0]['login']['sha256'])
        uuid.set(data['results'][0]['login']['uuid'])
        street_name.set(data['results'][0]['location']['street']['name'])
        street_number.set(data['results'][0]['location']['street']['number'])
        city.set(data['results'][0]['location']['city'])
        state.set(data['results'][0]['location']['state'])
        country.set(data['results'][0]['location']['country'])
        postcode.set(data['results'][0]['location']['postcode'])
        lat.set(data['results'][0]['location']['coordinates']['latitude'])
        lon.set(data['results'][0]['location']['coordinates']['longitude'])
        timezone_offset.set(data['results'][0]['location']['timezone']['offset'])
        timezone_desc.set(data['results'][0]['location']['timezone']['description'])
        pic_large.set(data['results'][0]['picture']['large'])
        try:
            response2=requests.get(pic_large.get())
        except:
            pic_large.set("Image Rendering Failed")
        else:
            file=open("pic.jpg","wb")
            file.write(response2.content)
            file.close()

            img=ImageTk.PhotoImage(Image.open("pic.jpg"))
            imglbl.configure(image=img)
            imglbl.photo=img
            
root=Tk()
root.iconbitmap("icon.ico")
root.resizable(False,False)
rl=ttk.Label(root,background="#19284B")
rl.pack(fill="both",expand="yes")
mf = ttk.Frame(rl, padding="3 3 12 12")
mf.grid(row=0,column=0, sticky=('N, W, E, S'),rowspan=3)
mf.columnconfigure(0, weight=1)
mf.rowconfigure(0, weight=1)
mf2 = ttk.Frame(rl, padding="3 3 12 12")
mf2.grid(row=0,column=2, sticky=('N, W, E, S'))
mf2.columnconfigure(0, weight=1)
mf2.rowconfigure(0, weight=1)
mf3 = ttk.Frame(rl, padding="3 3 12 12")
mf3.grid(row=0,column=4, sticky=('N, W, E, S'))
mf3.columnconfigure(0, weight=1)
mf3.rowconfigure(0, weight=1)
mf4 = ttk.Frame(rl, padding="3 3 12 12")
mf4.grid(row=0,column=6, sticky=('N, W, E, S'))
mf4.columnconfigure(0, weight=1)
mf4.rowconfigure(0, weight=1)

filename=StringVar()
cell=StringVar()
age=StringVar()
dob=StringVar()
email=StringVar()
gender=StringVar()
id_name=StringVar()
id_value=StringVar()
city=StringVar()
lat=StringVar()
lon=StringVar()
country=StringVar()
postcode=StringVar()
state=StringVar()
street_name=StringVar()
street_number=StringVar()
timezone_desc=StringVar()
timezone_offset=StringVar()
password=StringVar()
md5=StringVar()
salt=StringVar()
sha1=StringVar()
sha256=StringVar()
username=StringVar()
uuid=StringVar()
name=StringVar()
phone=StringVar()
pic_large=StringVar()
register_age=StringVar()
register_date=StringVar()

pic_large.set("No Image Available!!")

mfl=ttk.Label(mf,background="#19284B")
mfl.pack(fill="both",expand="yes")
global imglbl
img=ImageTk.PhotoImage(Image.open("icon.ico"))
imglbl=ttk.Label(mfl,image=img)
imglbl.grid(row=2,column=2,sticky="nwes")
imglbl.photo=img

mf2l=ttk.Label(mf2,background="#19284B")
mf2l.pack(fill="both",expand="yes")
ttk.Label(mf2l,text="Name: ",background="#19284B",foreground="white").grid(row=1,column=1)
ttk.Label(mf2l,textvariable=name,background="#19284B",foreground="white").grid(row=1,column=2)
ttk.Label(mf2l,text="Age: ",background="#19284B",foreground="white").grid(row=2,column=1)
ttk.Label(mf2l,textvariable=age,background="#19284B",foreground="white").grid(row=2,column=2)
ttk.Label(mf2l,text="D.O.B: ",background="#19284B",foreground="white").grid(row=3,column=1)
ttk.Label(mf2l,textvariable=dob,background="#19284B",foreground="white").grid(row=3,column=2)
ttk.Label(mf2l,text="Gender: ",background="#19284B",foreground="white").grid(row=4,column=1)
ttk.Label(mf2l,textvariable=gender,background="#19284B",foreground="white").grid(row=4,column=2)
ttk.Label(mf2l,text="Cell: ",background="#19284B",foreground="white").grid(row=5,column=1)
ttk.Label(mf2l,textvariable=cell,background="#19284B",foreground="white").grid(row=5,column=2)
ttk.Label(mf2l,text="email: ",background="#19284B",foreground="white").grid(row=6,column=1)
ttk.Label(mf2l,textvariable=email,background="#19284B",foreground="white").grid(row=6,column=2)
ttk.Label(mf2l,text="Register Age: ",background="#19284B",foreground="white").grid(row=7,column=1)
ttk.Label(mf2l,textvariable=register_age,background="#19284B",foreground="white").grid(row=7,column=2)
ttk.Label(mf2l,text="Register Date: ",background="#19284B",foreground="white").grid(row=8,column=1)
ttk.Label(mf2l,textvariable=register_date,background="#19284B",foreground="white").grid(row=8,column=2)

mf3l=ttk.Label(mf3,background="#19284B")
mf3l.pack(fill="both",expand="yes")
ttk.Label(mf3l,text="ID Name: ",background="#19284B",foreground="white").grid(row=1,column=1)
ttk.Label(mf3l,textvariable=id_name,background="#19284B",foreground="white").grid(row=1,column=2)
ttk.Label(mf3l,text="ID Value: ",background="#19284B",foreground="white").grid(row=2,column=1)
ttk.Label(mf3l,textvariable=id_value,background="#19284B",foreground="white").grid(row=2,column=2)
ttk.Label(mf3l,text="Username: ",background="#19284B",foreground="white").grid(row=3,column=1)
ttk.Label(mf3l,textvariable=username,background="#19284B",foreground="white").grid(row=3,column=2)
ttk.Label(mf3l,text="Password: ",background="#19284B",foreground="white").grid(row=4,column=1)
ttk.Label(mf3l,textvariable=password,background="#19284B",foreground="white").grid(row=4,column=2)
ttk.Label(mf3l,text="Salt: ",background="#19284B",foreground="white").grid(row=5,column=1)
ttk.Label(mf3l,textvariable=salt,background="#19284B",foreground="white").grid(row=5,column=2)
ttk.Label(mf3l,text="md5: ",background="#19284B",foreground="white").grid(row=6,column=1)
ttk.Label(mf3l,textvariable=md5,background="#19284B",foreground="white").grid(row=6,column=2)
ttk.Label(mf3l,text="SHA1: ",background="#19284B",foreground="white").grid(row=7,column=1)
ttk.Label(mf3l,textvariable=sha1,background="#19284B",foreground="white").grid(row=7,column=2)
ttk.Label(mf3l,text="SHA256: ",background="#19284B",foreground="white").grid(row=8,column=1)
ttk.Label(mf3l,textvariable=sha256,background="#19284B",foreground="white").grid(row=8,column=2)
ttk.Label(mf3l,text="uuid: ",background="#19284B",foreground="white").grid(row=9,column=1)
ttk.Label(mf3l,textvariable=uuid,background="#19284B",foreground="white").grid(row=9,column=2)

mf4l=ttk.Label(mf4,background="#19284B")
mf4l.pack(fill="both",expand="yes")
ttk.Label(mf4l,text="Street Name: ",background="#19284B",foreground="white").grid(row=1,column=1)
ttk.Label(mf4l,textvariable=street_name,background="#19284B",foreground="white").grid(row=1,column=2)
ttk.Label(mf4l,text="Street Number: ",background="#19284B",foreground="white").grid(row=2,column=1)
ttk.Label(mf4l,textvariable=street_number,background="#19284B",foreground="white").grid(row=2,column=2)
ttk.Label(mf4l,text="City: ",background="#19284B",foreground="white").grid(row=3,column=1)
ttk.Label(mf4l,textvariable=city,background="#19284B",foreground="white").grid(row=3,column=2)
ttk.Label(mf4l,text="State: ",background="#19284B",foreground="white").grid(row=4,column=1)
ttk.Label(mf4l,textvariable=state,background="#19284B",foreground="white").grid(row=4,column=2)
ttk.Label(mf4l,text="Country: ",background="#19284B",foreground="white").grid(row=5,column=1)
ttk.Label(mf4l,textvariable=country,background="#19284B",foreground="white").grid(row=5,column=2)
ttk.Label(mf4l,text="Post Code: ",background="#19284B",foreground="white").grid(row=6,column=1)
ttk.Label(mf4l,textvariable=postcode,background="#19284B",foreground="white").grid(row=6,column=2)
ttk.Label(mf4l,text="Latitude: ",background="#19284B",foreground="white").grid(row=7,column=1)
ttk.Label(mf4l,textvariable=lat,background="#19284B",foreground="white").grid(row=7,column=2)
ttk.Label(mf4l,text="Longitude: ",background="#19284B",foreground="white").grid(row=8,column=1)
ttk.Label(mf4l,textvariable=lon,background="#19284B",foreground="white").grid(row=8,column=2)
ttk.Label(mf4l,text="Timezone Offset: ",background="#19284B",foreground="white").grid(row=9,column=1)
ttk.Label(mf4l,textvariable=timezone_offset,background="#19284B",foreground="white").grid(row=9,column=2)
ttk.Label(mf4l,text="TimeZone Description: ",background="#19284B",foreground="white").grid(row=10,column=1)
ttk.Label(mf4l,textvariable=timezone_desc,background="#19284B",foreground="white").grid(row=10,column=2)

ttk.Button(mfl,text="Generate",command=generate).grid(row=3,column=2)
ttk.Button(mfl,text="Export",command=export).grid(row=3,column=3)
ttk.Button(mfl,text="Features",command=features).grid(row=4,column=3)

root.bind('<Return>',lambda e:generate())
for child in mfl.winfo_children():
    child.grid_configure(padx=5,pady=10)

root.mainloop()
