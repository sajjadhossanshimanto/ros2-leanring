## Build a package
<font color="#c00000">must</font> run in the workspace
```
colcon build 
```
- or just a specific package
```
colcon  build --packages-select my_py_pkg
```
### symlink
- specific to python only
```
colcon build --symlink-install
```
- with this our file is directed runed without compelling
- sometime this might not work. then we have to follow the build-> source -> run 
- <font color="#ff0000">note</font>: symlink is only for developmennt phase
## Create a package

```
ros2 pkg create my_py_pkg --build-type ament_python --dependencies rclpy
```
- run this command in in <font color="#00b050">src</font> directory
## ros2 pkg
- `ros2 pkg -h`
```
Commands:
  create       Create a new ROS 2 package
  executables  Output a list of package specific executables
  list         Output a list of available packages
  prefix       Output the prefix path of a package
  xml          Output the XML of the package manifest or a specific tag
```
### list
- `ros2 pkg list`
```
action_msgs
action_tutorials_cpp
action_tutorials_interfaces
action_tutorials_py
actionlib_msgs
ament_cmake
ament_cmake_auto
....
angles
builtin_interfaces
class_loader
common_interfaces
composition
composition_interfaces
console_bridge_vendor
cv_bridge
demo_nodes_cpp
demo_nodes_cpp_native
demo_nodes_py
depthimage_to_laserscan
desktop
diagnostic_msgs
domain_coordinator
dummy_map_server
dummy_robot_bringup
dummy_sensors
eigen3_cmake_module
example_interfaces
examples_rclcpp_minimal_action_client
....
rcl_action
rcl_interfaces
rcl_lifecycle
rcl_logging_interface
rcl_logging_spdlog
rcl_yaml_param_parser
...
...
```
### executables
- `ros2 pkg executables my_py_pkg`
```
my_py_pkg py_node
my_py_pkg py_oop_node
my_py_pkg robot_news_station
```
### prefix
- `ros2 pkg prefix my_py_pkg`
```
/mnt/d/coding/ros2_ws/install/my_py_pkg
```
## Minimal Node code
- maybe nothing to add here
## ros2 node
- `ros2 node -h `-> has only 2 commands 
```
usage: ros2 node [-h] Call `ros2 node <command> -h` for more detailed usage. ...

Various node related sub-commands

options:
  -h, --help            show this help message and exit

Commands:
  info  Output information about a node
  list  Output a list of available nodes

  Call `ros2 node <command> -h` for more detailed usage.
```
- `ros2 node list` -> lists only the <font color="#00b050">running</font> nodes
```
/py_test_oop
```
- `ros2 node info /py_test_oop` -> don't forget the <font color="#00b050">/</font> 
```
/py_test_oop
  Subscribers:

  Publishers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /rosout: rcl_interfaces/msg/Log
  Service Servers:
    /py_test_oop/describe_parameters: rcl_interfaces/srv/DescribeParameters
    /py_test_oop/get_parameter_types: rcl_interfaces/srv/GetParameterTypes
    /py_test_oop/get_parameters: rcl_interfaces/srv/GetParameters
    /py_test_oop/list_parameters: rcl_interfaces/srv/ListParameters
    /py_test_oop/set_parameters: rcl_interfaces/srv/SetParameters
    /py_test_oop/set_parameters_atomically: rcl_interfaces/srv/SetParametersAtomically
  Service Clients:

  Action Servers:

  Action Clients:

```
## Remap node
- let's us run the same node without modifing code or re-compiling
```
ros2 run my_py_pkg py_oop_node --ros-args -r __node:=temperature_sensor_1
```
- `-r`  -> `--remap` can also re replaced with this
-  `ros2 node list`
```
/temperature_sensor_1
/temperature_sensor_2
```

## Turtlesim
- controller
```
ros2 run turtlesim turtle_teleop_key
```
- robo
```
ros2 run turtlesim turtlesim_node
```

## ros2 interface
- ` ros2 interface -h`
```
Commands:
  list      List all interface types available
  package   Output a list of available interface types within one package
  packages  Output a list of packages that provide interfaces
  proto     Output an interface prototype
  show      Output the interface definition
```
- `ros2 interface packages`
```
action_msgs
action_tutorials_interfaces
actionlib_msgs
builtin_interfaces
composition_interfaces
diagnostic_msgs
example_interfaces
geometry_msgs
lifecycle_msgs
logging_demo
map_msgs
nav_msgs
pcl_msgs
pendulum_msgs
rcl_interfaces
rmw_dds_common
rosbag2_interfaces
rosgraph_msgs
sensor_msgs
shape_msgs
statistics_msgs
std_msgs
std_srvs
stereo_msgs
tf2_msgs
trajectory_msgs
turtlesim
unique_identifier_msgs
visualization_msgs
```
- `ros2 interface package example_interfaces `
```
example_interfaces/msg/Float64MultiArray
example_interfaces/msg/MultiArrayDimension
example_interfaces/msg/Byte
example_interfaces/msg/Float32
example_interfaces/msg/UInt64MultiArray
example_interfaces/msg/Int8
example_interfaces/srv/SetBool
example_interfaces/msg/UInt8
example_interfaces/msg/Int32
example_interfaces/msg/Int64
example_interfaces/msg/ByteMultiArray
example_interfaces/msg/Float32MultiArray
example_interfaces/msg/UInt32
example_interfaces/msg/Int64MultiArray
example_interfaces/msg/UInt64
example_interfaces/msg/UInt16
example_interfaces/msg/UInt16MultiArray
example_interfaces/msg/UInt32MultiArray
example_interfaces/msg/Int16
example_interfaces/msg/Char
example_interfaces/msg/Int32MultiArray
example_interfaces/msg/Float64
example_interfaces/srv/AddTwoInts
example_interfaces/msg/WString
example_interfaces/action/Fibonacci
example_interfaces/msg/Int8MultiArray
example_interfaces/msg/MultiArrayLayout
example_interfaces/msg/Bool
example_interfaces/msg/UInt8MultiArray
example_interfaces/msg/Int16MultiArray
example_interfaces/msg/String
example_interfaces/srv/Trigger
example_interfaces/msg/Empty
```
- `ros2 interface show example_interfaces/msg/String`
```
# This is an example message of using a primitive datatype, string.
# If you want to test with this that's fine, but if you are deploying
# it into a system you should create a semantically meaningful message type.
# If you want to embed it in another message, use the primitive data type instead.
string data
```
- `ros2 interface proto example_interfaces/msg/String`
```
"data: ''
"
```
```
