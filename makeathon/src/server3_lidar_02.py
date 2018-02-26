#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

import sys
sys.path.insert(0, "..")
import time
from opcua import ua, Server


float distance

def callback(data):
    global distance
    distance=min(data.ranges[1],data.ranges[2],data.ranges[3],data.ranges[4],data.ranges[5],data.ranges[6],data.ranges[7],data.ranges[8],data.ranges[9],data.ranges[10],data.ranges[11],data.ranges[12],data.ranges[13],data.ranges[14],data.ranges[15])
    rospy.loginfo(rospy.get_caller_id() + "The distance is %f", distance)
    
def listener():

    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("scan", LaserScan, callback)
    rospy.spin()


if __name__ == "__main__":

    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://localhost:4841/freeopcua/server/")

    # setup our own namespace, not really necessary but should as spec
    uri = "Lidar"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()

    # AMK - Here we declare our objects and data!
    # populating our address space
    myobj = objects.add_object(idx, "Data")
    myvar = myobj.add_variable(idx, "Distance", -1)
    #myvar.set_writable()    # Set MyVariable to be writable by clients

    # starting!
    server.start()

    try:
        ### AMK - Here Goes our code!
        global distance

        while True:
            time.sleep(1)
            listener()
            myvar.set_value(distance)
    finally:
        #close connection, remove subcsriptions, etc
        server.stop()
