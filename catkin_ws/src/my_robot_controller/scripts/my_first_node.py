#!/usr/bin/enc python3
import rospy

if __name__ == '__main__':
    rospy.init_node("test_node")

    #this is a print and also saves to logs.
    rospy.loginfo("Hello from test node")
    rospy.logwarn("this is a warning :O")
    rospy.logerr("this is an error")

    rospy.sleep(1) #this is the equivalent of time.sleep
    rospy.loginfo("end of program!")
    