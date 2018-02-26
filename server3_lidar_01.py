import sys
sys.path.insert(0, "..")
import time


from opcua import ua, Server


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
        count = 0
        while True:
            time.sleep(1)
            count += 0.1
            myvar.set_value(count)
    finally:
        #close connection, remove subcsriptions, etc
        server.stop()
