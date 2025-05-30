import rclpy
from rclpy.node import Node

# oop implimentation
class MyNode(Node):
    def __init__(self):
        super().__init__("py_test_oop")# pass the node name

        # self.get_logger().info("Hello world for oop")

        self.counter = 0
        self.create_timer(1.0, self.callback)
    
    def callback(self):
        self.get_logger().info(f"hello {self.counter}")
        self.counter += 1

def main(args=None):
    rclpy.init(args = args)
    
    ## do stuf
    node = MyNode()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=="__main__":
    # if we want to directly wants to run the file
    main()
