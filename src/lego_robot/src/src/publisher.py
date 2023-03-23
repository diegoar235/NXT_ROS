#!/usr/bin/env python3
import sys
import rospy
import moveit_commander
import moveit_msgs.msg
from moveit_commander.conversions import pose_to_list
from geometry_msgs.msg import Pose, PoseStamped, PoseArray, Quaternion
from moveit_msgs.msg import DisplayTrajectory, RobotState
from std_msgs.msg import ColorRGBA


import copy


class MoveGroupPython(object):
  robot = None
  group_names = None
  group = None
  File = None
  display_trajectory_publisher = None
  def __init__(self):
    super(MoveGroupPython, self).__init__()

    #Inicializo moveit creo e inicializo nodo
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('move_group_python_interface_tutorial', anonymous=True)
    
    self.robot = moveit_commander.RobotCommander() #cargo infomacion sobre el manipulador
    self.group_names = self.robot.get_group_names()     #Obtengo todos los grupos (en este caso 2)
    print(self.group_names)
    self.group = moveit_commander.MoveGroupCommander(self.group_names[0])
    self.display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   moveit_msgs.msg.DisplayTrajectory,
                                                    queue_size=20)


  def Trayectoria(self):

    waypoints = []
    wpose = self.group.get_current_pose().pose
    wpose.position.z += 0.1
    wpose.position.x += 0.1
    wpose.position.y -= 0.1
    waypoints.append(copy.deepcopy(wpose))    

    (plan, fraction) = self.group.compute_cartesian_path(
                                waypoints,   # puntos de destino
                                0.01,        # tamaño máximo de paso
                                0.0,         # distancia máxima permitida entre posiciones
                                True)        # evitar colisiones 
    self.group.execute(plan, wait=True)
    
def main():
    try:
        control = MoveGroupPython()
        control.Trayectoria()
       
    except rospy.ROSInterruptException:
        return
    except KeyboardInterrupt:
        return


if __name__ == '__main__':
  main()