#!/usr/bin/env python3
from lego_class import*
import rospy
from sensor_msgs.msg import JointState

def callback(data):
    joint_names = data.name
    joint_positions = data.position
    print(joint_positions[0])

def listener():
    rospy.init_node('joint_state_listener', anonymous=True)
    rospy.Subscriber("/joint_states", JointState, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

"""
import math
import tkinter
from tkinter.messagebox import NO
from turtle import position
import rospy
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from tf.transformations import euler_from_quaternion
import moveit_commander
import sys
import rospy
from sensor_msgs.msg import JointState
from matplotlib.animation import FuncAnimation
import time


class Graficador():
    info = None
    dx = 0
    t=0
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x400")
        moveit_commander.roscpp_initialize(sys.argv)
        self.robot = moveit_commander.RobotCommander()
        self.group = moveit_commander.MoveGroupCommander("GropoBrazo")
        self.sub = rospy.Subscriber("/joint_states", JointState, self.callback)
        self.Canvas = tkinter.Canvas(self.root, bg="white", height=300, width=700)
        self.root.after(100, self.grafricador)
        self.root.mainloop()
    

    def callback(self, JointState):
        self.info=JointState

        return None
        
    def grafricador(self):
        x = self.info.position*100
        #print(x)
        valores_articulaciones = self.group.get_current_joint_values()
        print("Los valores actuales de las articulaciones son:", valores_articulaciones[1])

        self.t = self.t+1
        coord1 = 10+self.t, 100+x[3]*180/math.pi, 10.5+self.t, 100.5+x[3]*180/math.pi
        coord2 = 10+self.t, 100+x[4]*180/math.pi, 10.5+self.t, 100.5+x[4]*180/math.pi
        coord3 = 10+self.t, 100+x[5]*180/math.pi, 10.5+self.t, 100.5+x[5]*180/math.pi
        pos1 = self.Canvas.create_oval(coord1, fill="red")    
        pos2 = self.Canvas.create_oval(coord2, fill="red")    
        pos3 = self.Canvas.create_oval(coord3, fill="red")    
        self.Canvas.pack()
        self.root.after(100, self.grafricador)
        if self.t>360: 
            self.t = 0
            self.Canvas.delete('all')
        return None

    
if __name__ == "__main__":
    rospy.init_node('listener', anonymous=True)
    sensor = Graficador()
"""