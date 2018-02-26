#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

#float distancia

def callback(data):

    distancia=min(data.ranges[1],data.ranges[2],data.ranges[3],data.ranges[4],data.ranges[5],data.ranges[6],data.ranges[7],data.ranges[8],data.ranges[9],data.ranges[10],data.ranges[11],data.ranges[12],data.ranges[13],data.ranges[14],data.ranges[15])
    rospy.loginfo(rospy.get_caller_id() + "La distancia es %f", distancia)
    
def listener():

    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("scan", LaserScan, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()



