import sys
sys.path.insert(0, "..")


from opcua import Client, ua
import motor


if __name__ == "__main__":

    opcv_client = Client("opc.tcp://AMKPi2:4841")
    motor_client = Client("opc.tcp://AMKPi:4841")
    lidar_client = Client("opc.tcp://AMKPi3:4841")
    # client = Client("opc.tcp://admin@localhost:4840/freeopcua/server/") #connect using a user
    try:
        opcv_client.connect()
        motor_client.connect()
        lidar_client.connect()

        # Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
        # root = client.get_root_node()
        # print("Objects node is: ", root)

        # Node objects have methods to read and write node attributes as well as browse or populate address space
        # print("Children of root are: ", root.get_children())

        # get a specific node knowing its node id
        #var = client.get_node(ua.NodeId(2002, 2))
        opcv_y = opcv_client.get_node("ns=1;i=2002")
        lidar_x = opcv_client.get_node("ns=1;i=2002")

        #var.get_data_value() # get value of node as a DataValue object
        y = var.get_value() # get value of node as a python builtin
        x = var.get_value()
        print("La distancia hacia el eje y es:", y , "medida")
        print("La distancia hacia el objeto es:", x , "medida")
        #var.set_value(ua.Variant([23], ua.VariantType.Int64)) #set node value using explicit data type
        #var.set_value(3.9) # set node value using implicit data type

        # Now getting a variable node using its browse path
        #myvar = root.get_child(["0:Objects", "2:MyObject", "2:MyVariable"])
        #obj = root.get_child(["0:Objects", "2:MyObject"])
        #print("myvar is: ", myvar)

    finally:
        client.disconnect()
