import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class MyNode(Node):
    def __init__(self):
        super().__init__("add_num_oop")

        self.clint = self.create_client(AddTwoInts, "add_two_number")
    
    def call_add_num(self, a, b):
        # wait for service
        while not self.clint.wait_for_service(1.0):
            self._logger.warn("waiting for service...")
        
        request = AddTwoInts.Request(a=a, b=b)
        feature = self.clint.call_async(request)
        # this only works if the node is already spinning. no need further spinning
        feature.add_done_callback(self.callback_add_number)
    
    def callback_add_number(self, future):
        response = future.result()
        self._logger.info(f"got sum = {response.sum}")




def main(args=None):
    rclpy.init(args=args)

    node = MyNode()
    node.call_add_num(5, 7)
    node.call_add_num(10, 20)
    node.call_add_num(10, 22)

    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()