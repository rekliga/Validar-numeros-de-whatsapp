import requests
import tkinter as tk

def validacion(numero):
    INSTANCE_ID = "instance24184"
    #TOKEN = "c"
    url = "https://api.ultramsg.com/instance24184/contacts/check"

    querystring = {"token":"b7rwblm3zozzsfgo","chatId":f'52{numero}@c.us'}

    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("GET", url, headers=headers, params=querystring)

    resupuesta =response.text
    resjson = response.json()
    print(resjson)
    #print(resjson["status"])
def mensaje(numero,mensaje):
    INSTANCE_ID = "instance24184"
    TOKEN = "b7rwblm3zozzsfgo"
    url = "https://api.ultramsg.com/instance24184/messages/chat"

    payload = f'token={TOKEN}&to=34{numero}&body={mensaje}&priority=10&referenceId='
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, data=payload, headers=headers)
    resjson = response.json()
    print(resjson)
    #print(resjson['sent'],resjson['id'])



mensaje(692686798, "Prueba de mensaje desde la aplicacion")
#validacion(4811069951)


window = tk.Tk()
window.geometry("300x200")
window.title("Encargo")

numers_validos = []
cont_numeros = 0
def get_value1():
   minimo=in1.get()
   #print(minimo)
   maximo=in2.get()
   #print(maximo)
   for i in range(int(minimo),int(maximo)):
    print(i)
    validacion(i)
    # if validacion(i)['status']=='valid':
    #     numers_validos.append(validacion(i)['i'])
    #     cont_numeros +=1
    #tk.Label(window,text=f'se encontraron {cont_numeros} numeros validos')
    print()
lb1 = tk.Label(window,text="min").pack()
in1 = tk.Entry(window)
in1.pack()

lb2 = tk.Label(window,text="max").pack()
in2 = tk.Entry(window)
in2.pack()
lada = tk.Label(window,text="lada +52",padx=10,pady=10).pack()

button1= tk.Button(window, text="Enter", command= get_value1)
button1.pack()














window.mainloop()