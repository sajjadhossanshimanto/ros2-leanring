import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts



def main(args=None):
    rclpy.init(args = args)
    
    ## do stuf
    node = Node("add_num_clint")
    clint = node.create_client(AddTwoInts, "add_two_number")
    # wait for service to become active
    while not clint.wait_for_service(1.0):
        node._logger.warn("waiting for add two number service")

    request = AddTwoInts.Request()
    request.a = 3
    request.b = 8

    future = clint.call_async(request)
    rclpy.spin_until_future_complete(node, future)

    response = future.result()
    node._logger.info(f"{request.a} + {request.b} = {response.sum}")

    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    # if we want to directly wants to run the file
    main()
