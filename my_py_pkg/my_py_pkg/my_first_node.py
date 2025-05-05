import rclpy
from rclpy.node import Node


def main(args=None):
    rclpy.init(args = args)
    
    ## do stuf
    node = Node("py_test")
    node.get_logger().info("Hello world")
    rclpy.spin(node)# loop a node

    rclpy.shutdown()

if __name__=="__main__":
    # if we want to directly wants to run the file
    main()
