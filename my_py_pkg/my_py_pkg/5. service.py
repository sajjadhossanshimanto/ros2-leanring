import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class MyNode(Node):
    def __init__(self):
        # NOTE: don't say the robot_news_node❌
        super().__init__("add_num_server")

        self.server = self.create_service(AddTwoInts, "add_two_number", self.callback_add_number)
        self.get_logger().info("service started")

    # we can name is anything but better to call "callback_topic"
    def callback_add_number(self, request: AddTwoInts.Request, response: AddTwoInts.Response):
        response.sum = request.a + request.b
        self._logger.info(f"calculating {request.a} + {request.b} = {response.sum}")

        return response# NOTE: don't forget to return


def main(args=None):
    rclpy.init(args = args)
    
    ## do stuf
    node = MyNode()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=="__main__":
    # if we want to directly wants to run the file
    main()
