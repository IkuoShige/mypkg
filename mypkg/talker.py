import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16 #lesson8
#from person_msgs.msg import Person#add msg
#from person_msgs.srv import Query#add query

"""
def cb(request, response):
    if request.name == "茂郁良":
        response.age = 44
    else:
        response.age = 255
    return response
#"""

class Talker():
    def __init__(self, node):
        self.pub = node.create_publisher(Int16, "countup", 10)
        self.n = 0
        node.create_timer(0.5, self.cb)

    def cb(self):
        #global n
        msg = Int16()#lesson8
        #msg = Person()#add msg
        #msg.name = "茂郁良"#add msg
        msg.data = self.n#lesson8
        #msg.age = n#add msg
        self.pub.publish(msg)
        self.n += 1

#rclpy.init()
#node = Node("talker")
#talker = Talker(node)
#pub = node.create_publisher(Int16, "countup", 10) #lesson8
#pub = node.create_publisher(Person, "person", 10)#add msg
#srv = node.create_service(Query, "query", cb)#add query
#n = 0

"""#lesson8
def cb():
    #global n
    msg = Int16()#lesson8
    #msg = Person()#add msg
    #msg.name = "茂郁良"#add msg
    msg.data = talker.n#lesson8
    #msg.age = n#add msg
    talker.pub.publish(msg)
    talker.n += 1
"""
#node.create_timer(0.5, cb)#lesson8
#rclpy.spin(node)

def main():
    rclpy.init()
    node = Node("talker")
    talker = Talker(node)
    rclpy.spin(node)

if __name__ == '__main__':
    main()
