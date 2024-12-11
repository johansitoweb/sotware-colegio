import tkinter as tk
from tkinter.font import Font

def Admin():
  root = tk.Tk()
  root.title("Admin")
  root.geometry("300x100")
  Label_PassAdmin = tk.Label(root,text="Ingresa la contraseña de administrador")
  Label_PassAdmin.pack()
  Textboc_PassAdmin = tk.Entry(root,width=30)
  Textboc_PassAdmin.pack()
  button_PssAdmin = tk.Button(root,text="Confirnar",fg="white",bg="green")
  button_PssAdmin.pack()
  






def New_user():
 root.destroy()
 class NuevoUsario():
    
    root = tk.Tk()
    root.geometry("700x500")
    root.title("Nuevo Usuario")
    Label_Nusuario = tk.Label(root,text="Nuevo Usuario")
    Label_Nusuario.pack()
    Label_Nusuario.place(x=40,y=10)
    Textboc_Nuser = tk.Entry(root,width=30)
    Textboc_Nuser.pack()
    Textboc_Nuser.place(x=40,y=30)
    Label_Contraseña1 = tk.Label(root,text="Contraseña")
    Label_Contraseña1.pack()
    Label_Contraseña1.place(x=40,y=60)
    Textboc_Pass1 = tk.Entry(root,width=30)
    Textboc_Pass1.pack()
    Textboc_Pass1.place(x=40,y=80)
    Label_Contraseña2 = tk.Label(root, text="Confirmar Contraseña")
    Label_Contraseña2.pack()
    Label_Contraseña2.place(x=40,y=110)
    Textboc_Pass2 = tk.Entry(root,width=30)
    Textboc_Pass2.pack()
    Textboc_Pass2.place(x=40,y=130)
    
    button_Agregar_usuario = tk.Button(root,text="Agregar Usuario",command=Admin, bg="green",fg="white" )
    button_Agregar_usuario.pack()
    button_Agregar_usuario.place(x=40,y=160)
    button_volver = tk.Button(root,text="Volver", bg="#c1121f",fg="white",)
    button_volver.pack()
    button_volver.place(x=140,y=160)


    root.mainloop()





def volver():
 
 class main():
   
  root = tk.Tk()
  root.geometry("700x500")
  root.title("Login-escolar")
  Label_Usuario = tk.Label(root,text="Nombre de Usuario")
  Label_Usuario.pack()
  Label_Usuario.place(x=40,y=10)
  Textboc_User = tk.Entry(root,width=30)
  Textboc_User.pack()
  Textboc_User.place(x=40,y=30)
  Label_Contraseña=tk.Label(root,text="Contraseña")
  Label_Contraseña.pack()
  Label_Contraseña.place(x=40,y=60)
  Textboc_Pass = tk.Entry(root,width=30)
  Textboc_Pass.pack()
  Textboc_Pass.place(x=40,y=80)
  button_login = tk.Button(root,text="Iniciar Sesion")
  button_login.pack()
  button_login.place(x=40,y=110)
  button_New_User = tk.Button(root,text="Agregar N Usuario",bg="green",fg="white",command=New_user)
  button_New_User.pack()
  button_New_User.place(x=130,y=110)
  root.mainloop()



root = tk.Tk()
root.geometry("700x500")
root.title("")
button_I = tk.Button(root, text="Iniciar", command=volver, font="bold",width=20,bg="#219ebc")
button_I.pack()
button_I.place(x=240,y=100)
root.mainloop()

