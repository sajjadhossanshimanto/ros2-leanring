import rclpy
from rclpy.node import Node


class MyNode(Node):
    def __init__(self):
        super().__init__("test_param_2")
        self.declare_parameter("start_from", 0)# type of paramiter will be auto pick by type of default value
        self.declare_parameter("time_period", 1.0)

        # here we are not constantly seeking value from get_parameter.
        # so to get effect we need to change the param at the begenning
        self.counter = self.get_parameter("start_from").value
        self.create_timer(self.get_parameter("time_period").value, self.callback)
    
    def callback(self):
        self._logger.info(f"hello {self.counter}")
        self.counter += 1

def main(args=None):
    rclpy.init(args = args)
    
    node = MyNode()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=="__main__":
    main()
