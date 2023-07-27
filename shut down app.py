from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
    
def restart_time():
    os.system("shutdown /r /t 15")
    
def logout():
    os.system("shutdown -l")
    
def shutsown():
    os.system("shutdown /s /t 1")

st = Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="light blue")

r_button = Button(st, text="Restart", font=(20), relief=RAISED, command=restart)
r_button.place(x=150, y=60, height=50, width=200)

rt_button = Button(st, text="Restart Time", font=(20), relief=RAISED, command=restart_time)
rt_button.place(x=150, y=170, height=50, width=200)

lg_button = Button(st, text="Log-Out", font=(20), relief=RAISED, command=logout)
lg_button.place(x=150, y=270, height=50, width=200)

sd_button = Button(st, text="Shut Down", font=(20), relief=RAISED, command=shutsown)
sd_button.place(x=150, y=370, height=50, width=200)


st.mainloop()