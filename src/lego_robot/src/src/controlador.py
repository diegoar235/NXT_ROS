#!/usr/bin/env python3

from lego_class import*
import rospy
from sensor_msgs.msg import JointState
from pids import*
import math

class Controlador():
    info = None
    def __init__(self):
        rospy.init_node('listener', anonymous=True)
        self.lego = NXTS()
        self.PID = PIDController()
        self.listener()
        self.PID.self.set_point_=self.info.position[0]*180/math.pi
        self.lego.ResetEncoder()

    def callback(self, JointState):
        self.info = JointState
        self.PID.setTarget(float(self.info.position[0])*180/math.pi)
        M1_actual = self.lego.Encoder(0,0)/4.67
        timestamp = time.time()
        Torque = self.PID.update(M1_actual, timestamp)
        self.lego.Servo(0,0,int(Torque))
        print(M1_actual,self.PID.set_point_, Torque, self.lego.Bateria())

    def listener(self):
        rospy.Subscriber("/joint_states", JointState, self.callback)        
        rospy.spin()

if __name__ == '__main__':
    Controlador = Controlador()