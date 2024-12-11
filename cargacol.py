import os

KEYS = ["/","-","\\"];

def loading_effect(time):
  cont = 0
  time_2 = 1

  while(time_2 < time):
    for key in KEYS:
        os.system('cls')
        print(key)

        if cont <= 1:
          cont+=1
        else:
          cont=0
    time_2+=1

  os.system('cls')

  print("El Proceso se ha completado exitosamente!")

loading_effect(100)