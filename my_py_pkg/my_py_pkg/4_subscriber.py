import rclpy
from rclpy.node import Node
from example_interfaces.msg import String


class MyNode(Node):
    def __init__(self):
        # NOTE: don't say the robot_news_node❌
        super().__init__("robot_news_listener")

        # NOTE: data_type and topic name must be the same
        self.subscriber = self.create_subscription(String, "robot_news", self.callback_robo_news, 10)
        "we can't set timer. we never know when the publisher will publish."
        "so smart solution is -> a callback is run each time a msg is received"
        self.get_logger().info("smartphon subscriber started")

    # we can name is anything but better to call "callback_topic"
    def callback_robo_news(self, msg: String):
        self.get_logger().info(f"reveived -> {msg.data}")


def main(args=None):
    rclpy.init(args = args)
    
    ## do stuf
    node = MyNode()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=="__main__":
    # if we want to directly wants to run the file
    main()
