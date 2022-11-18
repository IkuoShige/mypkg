import rclpy
from rclpy.node import Node
#from std_msgs.msg import Int16
#from person_msgs.msg import Person#add msg
from person_msgs.srv import Query#add query

"""
def cb(msg):
    global node
    #node.get_logger().info("Listen: %d" % msg.data)
    node.get_logger().info("Listen: %s" % msg)

rclpy.init()
node = Node("listener")
#pub = node.create_subscription(Int16, "countup", cb, 10)
pub = node.create_subscription(Person, "person", cb, 10)

rclpy.spin(node)
"""

def main():
    rclpy.init()
    node = Node("listener")
    client = node.create_client(Query, 'query')
    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('待機中')

    req = Query.Request()
    req.name = "茂郁良"
    future = client.call_async(req)

    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('呼び出し失敗')
            else:
                node.get_logger().info("age; {}".format(response.age))

            break

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
