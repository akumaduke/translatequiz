from tkinter import *
import pandas
import random

koule_background = "#B1DDC6"
kat={}
aprann={}
try:
    done= pandas.read_csv("data/mots_a_apprendre.csv")
except FileNotFoundError:
    done_original=pandas.read_csv("data/mo_franse.csv")
    aprann=done_original.to_dict(orient="records")
else:

    aprann= done.to_dict(orient="records")




def prochain():
    global kat, tounen
    fenet.after_cancel(tounen)
    kat= random.choice(aprann)
    penti.itemconfig(tit_kat, text= "Francais", fill= "black")
    penti.itemconfig(mo_aprann, text= kat["French"], fill= "black")
    penti.itemconfig(kat_deye,image= imaj_devan)
    tounen= fenet.after(3000,func=vire)
def vire():
    penti.itemconfig(tit_kat,text="Anglais",fill ="white")
    penti.itemconfig(mo_aprann,text=kat["English"],fill = "white")
    penti.itemconfig(kat_deye,image= imaj_deye)

def konnen():
    aprann.remove(kat)
    done= pandas.DataFrame(aprann)
    done.to_csv("data/mots_a_apprendre.csv", index=False)
    prochain()






fenet= Tk()
fenet.title("traducteur by AKUMA")
fenet.config(padx=50, pady=50, bg=koule_background)
tounen=fenet.after(3000, func= vire)

penti=Canvas(width= 800, height= 526)
imaj_devan= PhotoImage(file="images/kat_devan.png")
imaj_deye= PhotoImage(file= "images/kat_deye.png")
kat_deye=penti.create_image(400,263,image=imaj_devan,)
tit_kat=penti.create_text(400,150,text="", font=("Ariel",40, "italic"))
mo_aprann=penti.create_text(400,263, text="", font=("Ariel", 60, "bold"))
penti.config(bg=koule_background, highlightthickness=0)
penti.grid(row=0, column=0, columnspan=2)


pa_bon_image= PhotoImage(file= "images/pa_bon.png")
bouton_pa_konnen=Button(image=pa_bon_image, highlightthickness=0,command=prochain )
bouton_pa_konnen.grid(row=1, column=0)


bon_image= PhotoImage(file="images/bon.png")
bouton_konnen=Button(image=bon_image, highlightthickness=0,command= konnen)
bouton_konnen.grid(row=1, column=1)


prochain()







fenet.mainloop()