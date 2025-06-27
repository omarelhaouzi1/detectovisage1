from tkinter import *
from tkinter import filedialog
from cadrevis import *
import threading
from hogcam import*
from PIL import Image,ImageTk
def interface1(antecedent,choix1):
    antecedent.withdraw()
    fr1=Toplevel()
    fr1.geometry("530x450")
    fr1.title("Reconnaissance faciale")
    logo_icon = PhotoImage(file="C:/Users/ASUS/Downloads/logo1.png")
    fr1.iconphoto(False, logo_icon)
    image1=Image.open("C:/Users/ASUS/Downloads/bg1.jpg")
    image1=image1.resize((530,450))
    bgimg1=ImageTk.PhotoImage(image1)
    canvas1 = Canvas(fr1, width=530, height=450)
    canvas1.pack(fill="both", expand=True)
    canvas1.create_image(0, 0, image=bgimg1, anchor="nw")
    overlay1 = Image.new("RGBA", (430, 330), (255, 255, 255, 220))  
    overlay_img1 = ImageTk.PhotoImage(overlay1)
    canvas1.create_image(50, 49, image=overlay_img1, anchor="nw")
    choix2=StringVar(value=" ")
    label=Label(fr1,text="Choisir la technique d'extraction de caractéristiques : ",font=("Arial", 11,"bold"))
    canvas1.create_window(260, 85, window=label)
    radb1=Radiobutton(fr1,text="Local Binary Patterns (LBP)",font=("Segoe UI", 10,"italic"),variable=choix2,value="lbp")
    canvas1.create_window(160, 140, window=radb1)
    radb2=Radiobutton(fr1,text="Histogram of Oriented Gradients (HOG)",font=("Segoe UI", 10,"italic"),variable=choix2,value="vecthog")
    canvas1.create_window(200, 190, window=radb2)
    radb3=Radiobutton(fr1,text="HSV (Hue – Saturation – Value)",font=("Segoe UI", 10,"italic"),variable=choix2,value="hsv")
    canvas1.create_window(175, 245, window=radb3)
    radb4=Radiobutton(fr1,text="Vecteur global (LBP+HOG+HSV)",font=("Segoe UI", 10,"italic"),variable=choix2,value="glob")
    canvas1.create_window(180, 300, window=radb4)
    def traitement():
        var1=choix1.get()
        var2=choix2.get()
        if var1 == "haar":
            if var2 == "glob":
                    visagecam()
            elif var2=="lbp":
                   visagecamlbp()
            elif var2=="vecthog": 
                    visagecamhog()
            elif var2=="hsv":
                    visagecamhsv()
        elif var1=="hog":
            if var2 == "glob":
                    glob_hog_cam()
            elif var2=="lbp":
                   lbp_hog_cam()
            elif var2=="vecthog": 
                    hog_hog_cam()
            elif var2=="hsv":
                    hsv_hog_cam()
    def retour():
        fr1.destroy()    
        antecedent.deiconify() 
   
    btn2=Button(fr1, text="Retour", command=retour)
    canvas1.create_window(400, 370, window=btn2, anchor="se")       
    btn1=Button(fr1,text="Continue",  command=traitement)
    canvas1.create_window(470, 370, window=btn1, anchor="se")
    fr1.bgimg1 = bgimg1
    fr1.overlay_img1 = overlay_img1
def interface0(antecedent):
    antecedent.withdraw()
    fr=Toplevel()
    fr.geometry("530x450")
    fr.title("Reconnaissance faciale")
    logo_icon = PhotoImage(file="C:/Users/ASUS/Downloads/logo1.png")
    fr.iconphoto(False, logo_icon)
    image=Image.open("C:/Users/ASUS/Downloads/bg1.jpg")
    image=image.resize((530,450))
    bgimg=ImageTk.PhotoImage(image)
    canvas = Canvas(fr, width=530, height=450)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bgimg, anchor="nw")
    overlay = Image.new("RGBA", (430, 310), (255, 255, 255, 220))  
    overlay_img = ImageTk.PhotoImage(overlay)
    canvas.create_image(50, 74, image=overlay_img, anchor="nw")
    choix1=StringVar(value=" ")
    label=Label(fr,text="choisir La methode de détection : ",font=("Arial", 12,"bold"),bg="#ffffff")
    canvas.create_window(280, 110, window=label)
    ck1=Radiobutton(fr,text="Haarcascade",variable=choix1,value="haar",font=("Segoe UI", 10,"italic"))
    canvas.create_window(80, 190, window=ck1, anchor="w")
    ck2=Radiobutton(fr,text="Histogramme de gradient orientés (HOG)",font=("Segoe UI", 10,"italic"),variable=choix1,value="hog")
    canvas.create_window(80, 265, window=ck2, anchor="w")
    
   
    def retour():
        fr.destroy()    
        antecedent.deiconify() 
    btn1=Button(fr,text="Continue", command=lambda:interface1(fr,choix1))
    canvas.create_window(470, 370, window=btn1, anchor="se")
    btn2=Button(fr, text="Retour", command=retour)
    canvas.create_window(400, 370, window=btn2, anchor="se")
    
    fr.mainloop()
fr0=Tk()
fr0.geometry("530x450")
fr0.title("Reconnaissance faciale")
logo_icon = PhotoImage(file="C:/Users/ASUS/Downloads/logo1.png")
fr0.iconphoto(False, logo_icon)
image0=Image.open("C:/Users/ASUS/Downloads/bg.jpg")
image0=image0.resize((530,450))
bgimg0=ImageTk.PhotoImage(image0)
canvas0 = Canvas(fr0, width=530, height=450)
canvas0.pack(fill="both", expand=True)
canvas0.create_image(0, 0, image=bgimg0, anchor="nw")
overlay0 = Image.new("RGBA", (430, 300), (255, 255, 255, 220))  
overlay_img = ImageTk.PhotoImage(overlay0)
canvas0.create_image(50, 94, image=overlay_img, anchor="nw")
label=Label(fr0,text="Detectovisage",font=("Arial", 11,"bold"),bg="#ffffff")
canvas0.create_window(260, 135, window=label)
label1=Label(fr0,text= "Detectovisage est un système de reconnaissance faciale modulaire et personnalisable. "
    "Il s’adapte aux besoins de l’utilisateur et aux conditions d’utilisation, "
    "tout en garantissant précision et efficacité."
             ,   font=("Segoe UI", 10, "italic"),    
    fg="#000000",                        
    bg="#ffffff",                         
    wraplength=380,
    justify="left",
    padx=10,
    pady=10)
canvas0.create_window(260, 220, window=label1)
btn0=Button(fr0,text="Acceder au systeme",padx=23,
    pady=3, command=lambda:interface0(fr0),font=("Segoe UI", 9,"bold"))
canvas0.create_window(350, 320, window=btn0, anchor="se")
label2=Label(fr0,text=" PFE Realisé par EL HAOUZI OMAR/Yassmine Boutallaka "
             ,font=("Segoe UI", 8,"italic"),wraplength=380, justify="left")
canvas0.create_window(250, 370, window=label2)
fr0.mainloop()

