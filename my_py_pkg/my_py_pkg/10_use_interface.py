import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from custom_interfaces.msg import HardwareStatus

class MyNode(Node):
    def __init__(self):
        super().__init__("robot_news_station")

        self.publisher = self.create_publisher(HardwareStatus, "robot_news_cinterface", 10)
        self.create_timer(1.0, self.publish_news)
        self.get_logger().info("Robot station has been stated.")
    
    def publish_news(self):
        " create and publish a string"
        msg = HardwareStatus(
            temperature = 67.0,
            are_motors_ready = True,
            debuf_msg = "condition is perfect"
        )

        self.publisher.publish(msg)
        self.get_logger().info(str(msg))

def main(args=None):
    rclpy.init(args = args)
    
    ## do stuf
    node = MyNode()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=="__main__":
    # if we want to directly wants to run the file
    main()
