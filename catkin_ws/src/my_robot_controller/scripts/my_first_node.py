#!/usr/bin/env python3
import rospy

if __name__ == '__main__':
    rospy.init_node("test_node")

    rospy.loginfo("test node has been started")

    rate = rospy.Rate(10) #rate of 10 Hz (0.1 seconds)

    while not rospy.is_shutdown():
        rospy.loginfo("hello")
        rate.sleep()

    # #this is a print and also saves to logs.
    # rospy.loginfo("Hello from test node")
    # rospy.logwarn("this is a warning :O")
    # rospy.logerr("this is an error")

    # rospy.sleep(1) #this is the equivalent of time.sleep
    # rospy.loginfo("end of program!")
    