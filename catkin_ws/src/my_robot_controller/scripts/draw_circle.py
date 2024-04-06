#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist #import the Twist message from the msg folder of the geometry pckg

if __name__ == '__main__':
    rospy.init_node("draw_circle")
    rospy.loginfo("node has been started")
    #queue_size = 10 message buffer
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10) #publish to the cmd_vel node (rostopic list to see names)

    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        #create the message
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0 #think angular momentum from physics haha
        #no need to populate other fields, the default value is 0
        pub.publish(msg)
        rate.sleep()