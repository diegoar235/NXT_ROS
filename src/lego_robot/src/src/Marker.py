#! /usr/bin/env python3

import rospy
from visualization_msgs.msg import Marker



class FixedTFBroadcaster:

    def __init__(self):
        self.pub_tf = rospy.Publisher("/visualization_marker", Marker, queue_size=1)

        while not rospy.is_shutdown():
            # Run this loop at about 10Hz
            rospy.sleep(0.1)

            marker = Marker()
            marker.header.frame_id = "base_link"
            marker.header.stamp = rospy.Time.now()

        # set shape, Arrow: 0; Cube: 1 ; Sphere: 2 ; Cylinder: 3
            marker.type = 0
            marker.id = 0

        # Set the scale of the marke
            marker.scale.x = 0.1
            marker.scale.y = 0.1
            marker.scale.z = 0.05

        # Set the color
            marker.color.r = 0.0
            marker.color.g = 1.0
            marker.color.b = 0.0
            marker.color.a = 1.0

        # Set the pose of the marker
            marker.pose.position.x = 0.1 + marker.pose.position.x
            marker.pose.position.y = 0
            marker.pose.position.z = 0
            marker.pose.orientation.x = 0.0
            marker.pose.orientation.y = 0.0
            marker.pose.orientation.z = 0.0
            marker.pose.orientation.w = 1.0

            self.pub_tf.publish(marker)

if __name__ == '__main__':
    rospy.init_node('rviz_marker')
    tfb = FixedTFBroadcaster()
    rospy.spin()