#!/usr/bin/env python3
import nxt.locator
import nxt.brick
from nxt.motor import Port, Mode



class NXTS():
    
    Ladrillos=[]
    Servos=[]
    Puerto=[nxt.motor.Port.A,nxt.motor.Port.B,nxt.motor.Port.C]
    angulos=[0,0,0,0,0,0]
    
    def __init__(self):
        self.Conectar()
        
    def Conectar(self):
        M=[]
        try:
            for b in nxt.locator.find(find_all=True):
                self.Ladrillos.append(b)

            for i in range(0, len(self.Ladrillos), 1):
                for j in range(0, len(self.Puerto), 1):
                    M.append(self.Ladrillos[i].get_motor(self.Puerto[j]))
                self.Servos.append(M)
                M=[]

        except:
            print("No funciona")
            None
        
    def Informacion(self,i):
        return self.Ladrillos[i].get_device_info()

    def Bateria(self,i):
        return self.Ladrillos[i].get_battery_level()
    
    def Servo(self, Ladrillo, Puerto, Potencia):# Value between -127 and 128
        return self.Servos[Ladrillo][Puerto].run(Potencia)
    
    def Encoder(self, Ladrillo, Puerto):
        return vars(self.Servos[Ladrillo][Puerto].get_tacho())['tacho_count']
    
    def ResetEncoder(self):
        print("Resetear")
        for i in range(0, len(self.Servos), 1):
            for j in range(0, 3, 1):
                self.Servos[i][j].reset_position(False)
        return None

    def Desconectar(self):
        for i in range(0,len(self.Ladrillos),1):
            self.Ladrillos[i].close()
            print("Desconectado")
        return None   

    def configurar_torque(self, Torques):
        for j in range(0,len(self.Puerto),1):
            self.Servo(0, j, Torques[j])
            self.Servo(1, j, Torques[j])
        return None    

    def Obtener_angulos(self):
        Angulos=[]
        for i in range(0,len(self.Ladrillos),1):
            for j in range(0,len(self.Puerto),1):
                Angulos.append(self.Encoder(i, j))   
        return Angulos




#Uno=NXTS()
#while(True):
#    print(Uno.Bateria(0),Uno.Bateria(1))
#print('listo')

