import rclpy
from rclpy.node import Node
from example_interfaces.msg import String


# oop implimentation
class MyNode(Node):
    def __init__(self):
        super().__init__("robot_news_station")# pass the node name

        # remember the topic name have to start with letters as like var
        self.publisher = self.create_publisher(String, "robot_news", 10)
        self.create_timer(1.0, self.publish_news)
        self.get_logger().info("Robot station has been stated.")
    
    def publish_news(self):
        " create and publish a string"
        msg = String(data = "Hello")
        # msg.data = "Hello"

        self.publisher.publish(msg)
        self.get_logger().info(f"hello ")

def main(args=None):
    rclpy.init(args = args)
    
    ## do stuf
    node = MyNode()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=="__main__":
    # if we want to directly wants to run the file
    main()
