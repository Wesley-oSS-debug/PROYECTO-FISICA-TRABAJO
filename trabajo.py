from tkinter import *
from tkinter import messagebox
import math
import webbrowser
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import trapezoid
#ARREGLOS
#arreglos de trabajo de fuerza variable
ecuacion=[]
limiteInf=[]
limiteSup=[]
trabajoV=[]
datosTFV=[ecuacion,limiteInf,limiteSup,trabajoV]
#arreglos de trabajo fuerza constante
fuerza=[]
angulo=[]
distancia=[]
trabajo=[]
datosTFC=[fuerza,angulo,distancia,trabajo]
#arreglos de potencia
trabajoPotencia=[]
tiempo=[]
potencia=[]
datosPot=[trabajoPotencia, tiempo, potencia]

#arreglos de trabajo del resorte
constante=[]
xInicial=[]
xFinal=[]
trabajoR=[]
datosResorte = [constante, xInicial, xFinal, trabajoR]

#CONFIGURACIONES VENTANA PRINCIPAL
raiz=Tk()
raiz.iconbitmap("work.ico")
raiz.title("TRABAJO")
raiz.geometry("400x600+750+200")
raiz.resizable("False","False")
raiz.config(bg="#350b4b")
mainImage=PhotoImage(file="work.png")

titulo= Label(raiz, text ="CALCULO DEL TRABAJO", bg = "#F4D03F", fg = "#ffffff", font=("Impact", 20, "bold"))
titulo.grid(row=1,column=0,pady=10)
#frame de la imagen
frameImg=Frame(raiz,bg="#350b4b")
frameImg.grid(row=0,column=0,pady=12)
imgLbl=Label(frameImg,image=mainImage)
imgLbl.grid(row=0,column=0,padx=73)

def salir():
    valor=messagebox.askokcancel("Salir","Estas seguro que deseas salir?")
    if valor==True:
        raiz.destroy()

#VENTANA DE TEORIA DE TRABAJO
def teoriaTrabajo():
    teoria = Toplevel(raiz)
    teoria.title("Teoria")
    teoria.iconbitmap("work.ico")
    teoria.geometry("280x300+670+200")
    teoria.resizable(0,0)
    teoria.config(bg = "#350b4b")
    frameBtn=Frame(teoria, bg="#350b4b")
    frameBtn.grid()
    
    def verEnLinea():
        url = "https://csmer.uprrp.edu/wp-content/uploads/Trabajo-Potencia-y-Maquinas-Simples.pdf"
        url1 = "https://fisica.uprb.edu/cursos/FISI3173VK1/Teoria6.pdf"
        try:
            webbrowser.open(url, new=2) 
            webbrowser.open(url1, new=3) 
        except ValueError:
            messagebox.showerror("Error", "No se pudo abrir en linea, revise su conexion a internet")

    def descargarLibro():
        urlLum = "https://drive.google.com/uc?export=download&id=1Yjke8ePblaCpMXQvqJP8tQt64fDqwjgb"    
        try:
            webbrowser.open(urlLum, new=2)
        except ValueError:
            messagebox.showerror("ERROR" , "No se pudo realizar la descarga")

    def verClase():
        urlTeoClase = "https://drive.google.com/file/d/1Te-puR3r3tkcSgz4PGKi-wGc2pjfsGcZ/view?usp=sharing"
        try:
            webbrowser.open(urlTeoClase, new=2)
        except ValueError:
            messagebox.showerror("ERROR", "No se puedo abrir el archivo, revise la conexion a internet")

    def downloadTeo():
        urlTeoClase = "https://drive.google.com/uc?export=download&id=1Te-puR3r3tkcSgz4PGKi-wGc2pjfsGcZ"
        try:
            webbrowser.open(urlTeoClase, new=2)
        except ValueError:
            messagebox.showerror("ERROR", "No se puedo abrir el archivo, revise la conexion a internet")

    #MENU
    tituloTeoria = Label(frameBtn, text ="BIENVENIDO A TEORIA", bg = "#F4D03F", fg = "#ffffff", font=("Impact", 20, "bold"))
    tituloTeoria.grid(row=0,column=0,pady=25,padx=15)
    btn1=Button(frameBtn, text="Ver teoria en linea" ,bg = "#48C9B0", fg = "#ffffff", font=("Arial", 10, "bold"), command = verEnLinea)
    btn1.grid(row=1,column=0,pady=10)
    btn1=Button(frameBtn, text="Ver teoria en clase",bg = "#48C9B0", fg = "#ffffff", font=("Arial", 10, "bold"), command = verClase)
    btn1.grid(row=2,column=0,pady=10)
    btn1=Button(frameBtn, text="Descargar teoria en clase",bg = "#48C9B0", fg = "#ffffff", font=("Arial", 10, "bold"),command = downloadTeo)
    btn1.grid(row=3,column=0,pady=10)
    btn1=Button(frameBtn, text="Descargar libro de fisica",bg = "#48C9B0", fg = "#ffffff", font=("Arial", 10, "bold"), command= descargarLibro)
    btn1.grid(row=4,column=0,pady=10)
#VENTANA DE LA OPCION TRABAJO VARIABLE
def trabajoV():
    def calculo():
        def procesar_funcion(equacion):
            funciones = ["sin", "cos", "tan", "exp", "log", "sqrt"]
            for func in funciones:
                equacion = equacion.replace(func, f"np.{func}")
            return equacion
        
        ecua=ecuacionIn.get()
        datosTFV[0].append(ecua)
        ecua=procesar_funcion(ecua)
        
        limIn=float(limiteInfIn.get())
        limSup=float(limiteSupIn.get())
        
        datosTFV[1].append(limIn)
        datosTFV[2].append(limSup)
        
        plt.gcf().canvas.manager.set_window_title("Fuerza vs Posicion")
        plt.get_current_fig_manager().window.geometry("+50+200") 

        x=np.linspace(limIn,limSup,500)
        y=eval(ecua)
        
        minX=min(x)
        maxX=max(x)
        minY=min(y)
        maxY=max(y)
        
        t=round(trapezoid(y,x),3)
        datosTFV[3].append(t)
            
        resultadoIn.config(state="normal")
        resultadoIn.delete(0,"end")
        resultadoIn.insert(0,t)
        resultadoIn.config(state="readonly")
        
        plt.plot(x,y, color="red", label="f(x)")
        plt.fill_between(x,y,color="purple",alpha=0.5, label="Trabajo")
        plt.legend()
        plt.xlabel("Posicion (m)")
        plt.ylabel("Fuerza (N)")
        plt.xlim(minX,maxX)
        plt.ylim(minY-0.05,maxY+0.05)
        plt.grid()
        plt.show()
        
    def mostrarDatos():
        if len(datosTFV[0])==0:
            messagebox.showerror("ERROR","No hay datos para visualizar")
            vTV.destroy()
            return;
        vDat=Toplevel(vTV)
        vDat.title("Datos")
        vDat.geometry("590x400+100+300")
        vDat.resizable(0,0)
        vDat.config( bg= "#F4D03F")
        frameLista=Frame(vDat, bg= "#F4D03F")
        frameLista.grid(padx=2)
        #Labels
        tituloHistorial=Label(frameLista, text="HISTORIAL DE TRABAJO", bg="#F4D03F", fg="#ffffff", font=("Impact", 20, "bold"))
        tituloHistorial.grid(row=0, column=0, columnspan=4, pady=10, sticky="nsew")


        fLbl=Label(frameLista, text="Ecuacion", bg="#7D3C98",fg= "#ffffff", width=17, height=1)
        fLbl.grid(row=1,column=0, padx=10, pady=5)
        
        aLbl=Label(frameLista, text="Lim. Inferior",bg="#7D3C98",fg= "#ffffff", width=17, height=1)
        aLbl.grid(row=1,column=1, padx=10, pady=5)
        
        dLbl=Label(frameLista, text="Lim. Superior",bg="#7D3C98",fg= "#ffffff", width=17, height=1)
        dLbl.grid(row=1,column=2, padx=10,pady=5)
        
        tLbl=Label(frameLista,text="Trabajo",bg="#7D3C98",fg= "#ffffff", width=17, height=1)
        tLbl.grid(row=1,column=3, padx=10, pady=5)
        
        #Entrys
        
        for i in range(len(datosTFV[0])): #solo es necesario la longitud de un subarreglo
            
            fIn=Entry(frameLista, justify="center")
            fIn.grid(row=i+2,column=0,padx=10)
            fIn.insert(0,datosTFV[0][i])
            fIn.config(state="readonly")

            aIn=Entry(frameLista,justify="center")
            aIn.grid(row=i+2,column=1)
            aIn.insert(0,datosTFV[1][i])
            aIn.config(state="readonly")
            
            dIn=Entry(frameLista,justify="center")
            dIn.grid(row=i+2,column=2, padx=10)
            dIn.insert(0,datosTFV[2][i])
            dIn.config(state="readonly")
            
            tIn=Entry(frameLista,justify="center")
            tIn.grid(row=i+2,column=3)
            tIn.insert(0,datosTFV[3][i])
            tIn.config(state="readonly")
    vTV=Toplevel(raiz)
    vTV.title("Fuerza variable")
    vTV.geometry("330x300+750+400")
    vTV.resizable(0,0)
    vTV.config(bg="#F4D03F")
    #Label, entry y botones
    frameT1=Frame(vTV,bg="#F4D03F")
    frameT1.grid()
    tituloLbl=Label(frameT1, text="TRABAJO DE UNA \nFUERTA VARIABLE", bg="#F4D03F", fg="#ffffff", font=("Impact", 20, "bold"))
    tituloLbl.grid(row=0, column=0, columnspan=4, pady=5, sticky="nsew")
    
    ecuacionLbl=Label(frameT1, text="Ecuacion:",bg= "#F4D03F" ,fg = "#ffffff", font=("Arial",11,"bold"))
    ecuacionLbl.grid(row=1,column=0, sticky="nsew", padx=10, pady=5)
    
    ecuacionIn=Entry(frameT1, justify="center")
    ecuacionIn.grid(row=1,column=1)
    
    limiteInfLbl=Label(frameT1, text="Limite inferior:",bg= "#F4D03F",fg = "#ffffff", font=("Arial",11,"bold"))
    limiteInfLbl.grid(row=2,column=0, sticky="nsew", padx=10, pady=5)
    
    limiteInfIn=Entry(frameT1,justify="center")
    limiteInfIn.grid(row=2,column=1)
    
    limiteSupLbl=Label(frameT1, text="Limite superior:",bg= "#F4D03F",fg = "#ffffff", font=("Arial",11,"bold"))
    limiteSupLbl.grid(row=3,column=0, sticky="nsew", padx=10,pady=5)
    
    limiteSupIn=Entry(frameT1,justify="center")
    limiteSupIn.grid(row=3,column=1)
    
    btn=Button(frameT1, text="Calcular", command=calculo)
    btn.grid(row=2,column=2, padx=10)
    
    resultadoLbl=Label(frameT1,text="Trabajo:",bg= "#F4D03F",fg = "#ffffff", font=("Arial",11,"bold"))
    resultadoLbl.grid(row=4,column=0,sticky="nsew", padx=10, pady=5)
    
    resultadoIn=Entry(frameT1, readonlybackground="#ffffff",state="readonly",justify="center")
    resultadoIn.grid(row=4,column=1)
    
    mostrarBtn=Button(frameT1, text="Mostrar Datos", command=mostrarDatos)
    mostrarBtn.grid(row=5,column=1, pady=20)
    
    
    
#VENTANA DE LA OPCION TRABAJO CONSTANTE
def trabajoC():
    vTF=Toplevel(raiz)
    vTF.iconbitmap("work.ico")
    vTF.title("Fuerza constante")
    vTF.geometry("330x300+750+400")     
    vTF.config( bg= "#F4D03F")
    vTF.resizable(0,0)
    #FUNCION QUE CALCULA EL TRABAJO DE UNA FUERZA CONSTANTE
    def calculo():
        try:

            f=float(fuerzaIn.get())
            a=float(anguloIn.get())
            d=float(distanciaIn.get())
            
            #VALIDACION DE DISTANCIA
            if d < 0:
                messagebox.showerror("Error", "La distancia no puede ser negativa")
                return
            
            aRad=math.radians(float(a))
            r=round(float(f)*float(d)*math.cos(aRad),4) #round(numero,decimales)
            
            datosTFC[0].append(f)
            datosTFC[1].append(a)
            datosTFC[2].append(d)
            datosTFC[3].append(r)
            
            resultadoIn.config(state="normal")
            resultadoIn.delete(0,"end")
            resultadoIn.insert(0,r)
            resultadoIn.config(state="readonly")

        except ValueError:
            #SI INGRESA DATOS INVALIDOS
            messagebox.showerror("Error", "Vuelve a ingresar los datos")
        
    def mostrarDatos():
        if len(datosTFC[0])==0:
            messagebox.showerror("ERROR","No hay datos para visualizar")
            vTF.destroy()
            return;
        vDat=Toplevel(vTF)
        vDat.title("Datos")
        vDat.geometry("590x400+100+300")
        vDat.resizable(0,0)
        vDat.config( bg= "#F4D03F")
        frameLista=Frame(vDat, bg= "#F4D03F")
        frameLista.grid(padx=2)
        #Labels
        tituloHistorial = Label(frameLista, text="HISTORIAL DE TRABAJO", bg="#F4D03F", fg="#ffffff", font=("Impact", 20, "bold"))
        tituloHistorial.grid(row=0, column=0, columnspan=4, pady=10, sticky="nsew")


        fLbl=Label(frameLista, text="Fuerza", bg="#7D3C98",fg= "#ffffff", width=17, height=1)
        fLbl.grid(row=1,column=0, padx=10, pady=5)
        
        aLbl=Label(frameLista, text="Angulo",bg="#7D3C98",fg= "#ffffff", width=17, height=1)
        aLbl.grid(row=1,column=1, padx=10, pady=5)
        
        dLbl=Label(frameLista, text="Distancia",bg="#7D3C98",fg= "#ffffff", width=17, height=1)
        dLbl.grid(row=1,column=2, padx=10,pady=5)
        
        tLbl=Label(frameLista,text="Trabajo",bg="#7D3C98",fg= "#ffffff", width=17, height=1)
        tLbl.grid(row=1,column=3, padx=10, pady=5)
        
        #Entrys
        
        for i in range(len(datosTFC[0])): #solo es necesario la longitud de un subarreglo
            
            fIn=Entry(frameLista, justify="center")
            fIn.grid(row=i+2,column=0,padx=10)
            fIn.insert(0,datosTFC[0][i])
            fIn.config(state="readonly")

            aIn=Entry(frameLista,justify="center")
            aIn.grid(row=i+2,column=1)
            aIn.insert(0,datosTFC[1][i])
            aIn.config(state="readonly")
            
            dIn=Entry(frameLista,justify="center")
            dIn.grid(row=i+2,column=2, padx=10)
            dIn.insert(0,datosTFC[2][i])
            dIn.config(state="readonly")
            
            tIn=Entry(frameLista,justify="center")
            tIn.grid(row=i+2,column=3)
            tIn.insert(0,datosTFC[3][i])
            tIn.config(state="readonly")



    
    #LABEL,ENTRY Y BOTONES
    frameEnt=Frame(vTF, bg= "#F4D03F")
    frameEnt.grid(padx=10,pady=5)
    
    tituloHistorial = Label(frameEnt, text="TRABAJO DE UNA \nFUERTA CONSTANTE", bg="#F4D03F", fg="#ffffff", font=("Impact", 20, "bold"))
    tituloHistorial.grid(row=0, column=0, columnspan=4, pady=5, sticky="nsew")

    fuerzaLbl=Label(frameEnt, text="Fuerza:",bg= "#F4D03F" ,fg = "#ffffff", font=("Arial",11,"bold"))
    fuerzaLbl.grid(row=1,column=0, sticky="nsew", padx=10, pady=5)
    
    fuerzaIn=Entry(frameEnt, justify="center")
    fuerzaIn.grid(row=1,column=1)
    
    anguloLbl=Label(frameEnt, text="Angulo:",bg= "#F4D03F",fg = "#ffffff", font=("Arial",11,"bold"))
    anguloLbl.grid(row=2,column=0, sticky="nsew", padx=10, pady=5)
    
    anguloIn=Entry(frameEnt,justify="center")
    anguloIn.grid(row=2,column=1)
    
    distanciaLbl=Label(frameEnt, text="Distancia:",bg= "#F4D03F",fg = "#ffffff", font=("Arial",11,"bold"))
    distanciaLbl.grid(row=3,column=0, sticky="nsew", padx=10,pady=5)
    
    distanciaIn=Entry(frameEnt,justify="center")
    distanciaIn.grid(row=3,column=1)
    
    btn=Button(frameEnt, text="Calcular", command=calculo)
    btn.grid(row=2,column=2, padx=10)
    
    resultadoLbl=Label(frameEnt,text="Resultado:",bg= "#F4D03F",fg = "#ffffff", font=("Arial",11,"bold"))
    resultadoLbl.grid(row=4,column=0,sticky="nsew", padx=10, pady=5)
    
    resultadoIn=Entry(frameEnt, readonlybackground="#ffffff",state="readonly",justify="center")
    resultadoIn.grid(row=4,column=1)
    
    mostrarBtn=Button(frameEnt, text="Mostrar Datos", command=mostrarDatos)
    mostrarBtn.grid(row=5,column=1, pady=20)

#VENTANA DE LA OPCION POTENCIA
def potencia():
    vP=Toplevel(raiz)
    vP.iconbitmap("work.ico")
    vP.title("Potencia")
    vP.geometry("310x200+750+400")
    vP.resizable(0,0)
    vP.config(bg="#F4D03F")

    #FUNCION PARA CALCULAR POTENCIA
    def calculoPotencia():
        try:

            w=float(trabajoPotenciaIn.get())
            t=float(tiempoIn.get())
            if t < 0:
                messagebox.showerror("Error", "El tiempo no puede ser negativo")
                return
            p=round(float(w)/float(t),2)
            datosPot[0].append(w)
            datosPot[1].append(t)
            datosPot[2].append(p)

            resultadoPotenciaIn.config(state="normal")
            resultadoPotenciaIn.delete(0,"end")
            resultadoPotenciaIn.insert(0,p)
            resultadoPotenciaIn.config(state="readonly")
        
        except ValueError:
            #SI INGRESA DATOS INVALIDOS
            messagebox.showerror("Error", "Vuelve a ingresar los datos")
    
    def mostrarDatosPotencia():
        vDat=Toplevel(vP)
        vDat.title("Datos")
        vDat.geometry("440x400+100+300")
        vDat.config(bg= "#F4D03F")
        vDat.resizable(0,0)
        #Labels
        tituloHistorialPotencia = Label(vDat, text="HISTORIAL DE POTENCIA", bg="#F4D03F", fg="#ffffff", font=("Impact", 20, "bold"))
        tituloHistorialPotencia.grid(row=0, column=0, columnspan=4, pady=5, sticky="nsew")

        fLbl=Label(vDat, text="Trabajo", bg="#7D3C98",fg= "#ffffff", width=17, height=1)
        fLbl.grid(row=1,column=0, padx=10, pady=5)
        
        aLbl=Label(vDat, text="Tiempo",bg="#7D3C98",fg= "#ffffff", width=17, height=1)
        aLbl.grid(row=1,column=1, padx=10, pady=5)
        
        dLbl=Label(vDat, text="Potencia",bg="#7D3C98",fg= "#ffffff", width=17, height=1)
        dLbl.grid(row=1,column=2, padx=10,pady=5)
        
        #Entrys
        
        for i in range(len(datosPot[0])): #solo es necesario la longitud de un subarreglo
            
            fIn=Entry(vDat, justify="center")
            fIn.grid(row=i+2,column=0,padx=10)
            fIn.insert(0,datosPot[0][i])
            fIn.config(state="readonly")

            aIn=Entry(vDat,justify="center")
            aIn.grid(row=i+2,column=1)
            aIn.insert(0,datosPot[1][i])
            aIn.config(state="readonly")
            
            dIn=Entry(vDat,justify="center")
            dIn.grid(row=i+2,column=2, padx=10)
            dIn.insert(0,datosPot[2][i])
            dIn.config(state="readonly")

    #LABEL,ENTRY Y BOTONES

    tituloPotencia = Label(vP, text="  POTENCIA", bg="#F4D03F", fg="#ffffff", font=("Impact", 20, "bold"))
    tituloPotencia.grid(row=0, column=0, columnspan=4, pady=5, sticky="nsew")

    trabajoPotenciaLbl=Label(vP, text="Trabajo:",bg="#F4D03F", fg="#ffffff", font=("Arial", 11, "bold"))
    trabajoPotenciaLbl.grid(row=1,column=0, sticky="nsew", padx=10, pady=5)
    
    trabajoPotenciaIn=Entry(vP, justify="center")
    trabajoPotenciaIn.grid(row=1,column=1)
    
    tiempoLbl=Label(vP, text="Tiempo:", bg="#F4D03F", fg="#ffffff", font=("Arial", 11, "bold"))
    tiempoLbl.grid(row=2,column=0, sticky="nsew", padx=10, pady=5)
    
    tiempoIn=Entry(vP,justify="center")
    tiempoIn.grid(row=2,column=1)
    
    btn=Button(vP, text="Calcular", command=calculoPotencia)
    btn.grid(row=2,column=2, padx=10)
    
    resultadoPotenciaLbl=Label(vP,text="Resultado:", bg="#F4D03F", fg="#ffffff", font=("Arial", 11, "bold"))
    resultadoPotenciaLbl.grid(row=3,column=0, padx=10, pady=5,sticky="nsew")
    
    resultadoPotenciaIn=Entry(vP, readonlybackground="#ffffff",state="readonly",justify="center")
    resultadoPotenciaIn.grid(row=3,column=1)
    
    mostrarBtn=Button(vP, text="Mostrar Datos", command=mostrarDatosPotencia)
    mostrarBtn.grid(row=4,column=1, pady=10)
    
#VENTANA DE LA OPCION TRABAJO DE RESORTE
def trabajoR():
    vR = Toplevel(raiz)
    vR.iconbitmap("work.ico")
    vR.title("Trabajo Resorte")
    vR.geometry("330x300+750+400")
    vR.resizable(0, 0)
    vR.config(bg="#F4D03F")


    #FUNCION PARA CALCULAR TRABAJO DEL RESORTE
    def calculoResorte():
        try:

            k = float(constanteIn.get())
            xi = float(xInicialIn.get())
            xf = float(xFinalIn.get())
            if k <= 0:
                messagebox.showerror("Error", "La constante no puede ser negativa")
                return
            w=round(0.5 * k *( xf**2 - xi**2), 4)
            datosResorte[0].append(k)
            datosResorte[1].append(xi)
            datosResorte[2].append(xf)
            datosResorte[3].append(w)

            resultadoTrabajoIn.config(state="normal")
            resultadoTrabajoIn.delete(0,"end")
            resultadoTrabajoIn.insert(0,w)
            resultadoTrabajoIn.config(state="readonly")
        
        except ValueError:
            #SI INGRESA DATOS INVALIDOS
            messagebox.showerror("Error", "Vuelve a ingresar los datos")
    
    def mostrarDatosResorte():
        if len(datosResorte[0])==0:
            messagebox.showerror("ERROR","No hay datos para visualizar")
            vR.destroy()
            return;
        vDat=Toplevel(vR)
        vDat.title("Datos")
        vDat.geometry("590x400+100+300")
        vDat.config(bg= "#F4D03F")
        vDat.resizable(0,0)
        frameLista=Frame(vDat, bg= "#F4D03F")
        frameLista.grid(padx=2)
        #Labels
        tituloHistorialResorte = Label(frameLista, text=" HISTORIAL DE TRABAJO", bg="#F4D03F", fg="#ffffff", font=("Impact", 20, "bold"))
        tituloHistorialResorte.grid(row=0, column=0, columnspan=4, pady=5, sticky="nsew")

        fLbl=Label(frameLista, text="Constante", bg="#7D3C98",fg= "#ffffff", width=17, height=1)
        fLbl.grid(row=1,column=0, padx=10, pady=5)
        
        aLbl=Label(frameLista, text="x inicial",bg="#7D3C98",fg= "#ffffff", width=17, height=1)
        aLbl.grid(row=1,column=1, padx=10, pady=5)
        
        dLbl=Label(frameLista, text="x final",bg="#7D3C98",fg= "#ffffff", width=17, height=1)
        dLbl.grid(row=1,column=2, padx=10,pady=5)

        tLbl=Label(frameLista, text="Trabajo",bg="#7D3C98",fg= "#ffffff", width=17, height=1)
        tLbl.grid(row=1,column=3, padx=10,pady=5)

        
        #Entrys
        
        for i in range(len(datosResorte[0])): #solo es necesario la longitud de un subarreglo
            
            fIn=Entry(frameLista, justify="center")
            fIn.grid(row=i+2,column=0,padx=10)
            fIn.insert(0,datosResorte[0][i])
            fIn.config(state="readonly")

            aIn=Entry(frameLista,justify="center")
            aIn.grid(row=i+2,column=1)
            aIn.insert(0,datosResorte[1][i])
            aIn.config(state="readonly")
            
            dIn=Entry(frameLista,justify="center")
            dIn.grid(row=i+2,column=2, padx=10)
            dIn.insert(0,datosResorte[2][i])
            dIn.config(state="readonly")

            tIn=Entry(frameLista,justify="center")
            tIn.grid(row=i+2,column=3, padx=10)
            tIn.insert(0,datosResorte[3][i])
            tIn.config(state="readonly")

    #LABEL,ENTRY Y BOTONES
    frameEnt=Frame(vR, bg= "#F4D03F")
    frameEnt.grid(padx=10,pady=5)

    tituloHistorialResorte = Label(frameEnt, text="TRABAJO DE UN RESORTE", bg="#F4D03F", fg="#ffffff", font=("Impact", 20, "bold"))
    tituloHistorialResorte.grid(row=0, column=0, columnspan=4, pady=5, sticky="nsew")

    constanteLbl=Label(frameEnt, text="Constante:",bg="#F4D03F", fg="#ffffff", font=("Arial", 11, "bold"))
    constanteLbl.grid(row=1,column=0, sticky="nsew", padx=10, pady=5)
    
    constanteIn=Entry(frameEnt, justify="center")
    constanteIn.grid(row=1,column=1)
    
    xInicialLbl=Label(frameEnt, text="x Inicial:", bg="#F4D03F", fg="#ffffff", font=("Arial", 11, "bold"))
    xInicialLbl.grid(row=2,column=0, sticky="nsew", padx=10, pady=5)
    
    xInicialIn=Entry(frameEnt,justify="center")
    xInicialIn.grid(row=2,column=1)

    xFinalLbl=Label(frameEnt, text="x final:", bg="#F4D03F", fg="#ffffff", font=("Arial", 11, "bold"))
    xFinalLbl.grid(row=3,column=0, sticky="nsew", padx=10, pady=5)
    
    xFinalIn=Entry(frameEnt,justify="center")
    xFinalIn.grid(row=3,column=1)
    
    btn=Button(frameEnt, text="Calcular", command=calculoResorte)
    btn.grid(row=3,column=2, padx=10)
    
    resultadoTrabajoLbl=Label(frameEnt,text="Resultado:", bg="#F4D03F", fg="#ffffff", font=("Arial", 11, "bold"))
    resultadoTrabajoLbl.grid(row=5,column=0, padx=10, pady=5,sticky="nsew")
    
    resultadoTrabajoIn=Entry(frameEnt, readonlybackground="#ffffff",state="readonly",justify="center")
    resultadoTrabajoIn.grid(row=5,column=1)
    
    mostrarBtn=Button(frameEnt, text="Mostrar Datos", command=mostrarDatosResorte)
    mostrarBtn.grid(row=6,column=1, pady=10)    

#BOTONES MENU PRINCIPAL
#frame de botones
frameBtn=Frame(raiz, bg="#350b4b")
frameBtn.grid()
btn1=Button(frameBtn, text="Teoria de TRABAJO", command = teoriaTrabajo)
btn1.grid(row=1,column=0,pady=10)

btn2=Button(frameBtn, text="Calcular Trabajo de una fuerza constante", command=trabajoC)
btn2.grid(row=2,column=0,pady=10)

btn3=Button(frameBtn, text="Calcular Trabajo de una fuerza variable", command=trabajoV)
btn3.grid(row=3,column=0,pady=10)

btn4=Button(frameBtn, text="Calcular Potencia", command=potencia)
btn4.grid(row=4,column=0,pady=10)

btn5=Button(frameBtn, text="Calcular Trabajo de Resorte", command=trabajoR)
btn5.grid(row=5,column=0,pady=10)

btn0=Button(frameBtn, text="Salir del programa", fg="red", command=salir)
btn0.grid(row=6,column=0,pady=10)


raiz.mainloop()