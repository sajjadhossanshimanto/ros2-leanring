import rclpy
from rclpy.node import Node


class MyNode(Node):
    def __init__(self):
        super().__init__("test_param_1")
        self.declare_parameter("name", "bob")# type of paramiter will be auto pick by type of default value

        self.create_timer(1.0, self.callback)
    
    def callback(self):
        self._logger.info(f"hello {self.get_parameter('name').value}")


def main(args=None):
    rclpy.init(args = args)
    
    node = MyNode()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=="__main__":
    main()
