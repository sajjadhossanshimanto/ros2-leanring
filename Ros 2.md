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
ament_cmake_copyright
ament_cmake_core
ament_cmake_cppcheck
ament_cmake_cpplint
ament_cmake_export_definitions
ament_cmake_export_dependencies
ament_cmake_export_include_directories
ament_cmake_export_interfaces
ament_cmake_export_libraries
ament_cmake_export_link_flags
ament_cmake_export_targets
ament_cmake_flake8
ament_cmake_gen_version_h
ament_cmake_gmock
ament_cmake_gtest
ament_cmake_include_directories
ament_cmake_libraries
ament_cmake_lint_cmake
ament_cmake_pep257
ament_cmake_pytest
ament_cmake_python
ament_cmake_ros
ament_cmake_target_dependencies
ament_cmake_test
ament_cmake_uncrustify
ament_cmake_version
ament_cmake_xmllint
ament_copyright
ament_cppcheck
ament_cpplint
ament_flake8
ament_index_cpp
ament_index_python
ament_lint
ament_lint_auto
ament_lint_cmake
ament_lint_common
ament_package
ament_pep257
ament_uncrustify
ament_xmllint
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
examples_rclcpp_minimal_action_server
examples_rclcpp_minimal_client
examples_rclcpp_minimal_composition
examples_rclcpp_minimal_publisher
examples_rclcpp_minimal_service
examples_rclcpp_minimal_subscriber
examples_rclcpp_minimal_timer
examples_rclcpp_multithreaded_executor
examples_rclpy_executors
examples_rclpy_minimal_action_client
examples_rclpy_minimal_action_server
examples_rclpy_minimal_client
examples_rclpy_minimal_publisher
examples_rclpy_minimal_service
examples_rclpy_minimal_subscriber
fastrtps_cmake_module
geometry2
geometry_msgs
image_geometry
image_tools
image_transport
interactive_markers
intra_process_demo
joy
kdl_parser
keyboard_handler
laser_geometry
launch
launch_ros
launch_testing
launch_testing_ament_cmake
launch_testing_ros
launch_xml
launch_yaml
libcurl_vendor
libstatistics_collector
libyaml_vendor
lifecycle
lifecycle_msgs
logging_demo
map_msgs
message_filters
my_pacage
my_py_pkg
nav_msgs
orocos_kdl_vendor
osrf_pycommon
pcl_conversions
pcl_msgs
pendulum_control
pendulum_msgs
pluginlib
pybind11_vendor
python_cmake_module
python_orocos_kdl_vendor
python_qt_binding
qt_dotgraph
qt_gui
qt_gui_cpp
qt_gui_py_common
quality_of_service_demo_cpp
quality_of_service_demo_py
rcl
rcl_action
rcl_interfaces
rcl_lifecycle
rcl_logging_interface
rcl_logging_spdlog
rcl_yaml_param_parser
rclcpp
rclcpp_action
rclcpp_components
rclcpp_lifecycle
rclpy
rcpputils
rcutils
resource_retriever
rmw
rmw_dds_common
rmw_fastrtps_cpp
rmw_fastrtps_shared_cpp
rmw_implementation
rmw_implementation_cmake
robot_state_publisher
ros2action
ros2bag
ros2cli
ros2cli_common_extensions
ros2component
ros2doctor
ros2interface
ros2launch
ros2lifecycle
ros2multicast
ros2node
ros2param
ros2pkg
ros2run
ros2service
ros2topic
ros_base
ros_core
ros_environment
ros_workspace
rosbag2
rosbag2_compression
rosbag2_compression_zstd
rosbag2_cpp
rosbag2_interfaces
rosbag2_py
rosbag2_storage
rosbag2_storage_default_plugins
rosbag2_transport
rosgraph_msgs
rosidl_adapter
rosidl_cli
rosidl_cmake
rosidl_default_generators
rosidl_default_runtime
rosidl_generator_c
rosidl_generator_cpp
rosidl_generator_py
rosidl_parser
rosidl_runtime_c
rosidl_runtime_cpp
rosidl_runtime_py
rosidl_typesupport_c
rosidl_typesupport_cpp
rosidl_typesupport_fastrtps_c
rosidl_typesupport_fastrtps_cpp
rosidl_typesupport_interface
rosidl_typesupport_introspection_c
rosidl_typesupport_introspection_cpp
rpyutils
rqt_action
rqt_bag
rqt_bag_plugins
rqt_common_plugins
rqt_console
rqt_graph
rqt_gui
rqt_gui_cpp
rqt_gui_py
rqt_image_view
rqt_msg
rqt_plot
rqt_publisher
rqt_py_common
rqt_py_console
rqt_reconfigure
rqt_service_caller
rqt_shell
rqt_srv
rqt_topic
rttest
rviz2
rviz_assimp_vendor
rviz_common
rviz_default_plugins
rviz_ogre_vendor
rviz_rendering
sdl2_vendor
sensor_msgs
sensor_msgs_py
shape_msgs
shared_queues_vendor
spdlog_vendor
sqlite3_vendor
sros2
sros2_cmake
statistics_msgs
std_msgs
std_srvs
stereo_msgs
tango_icons_vendor
teleop_twist_joy
teleop_twist_keyboard
tf2
tf2_bullet
tf2_eigen
tf2_eigen_kdl
tf2_geometry_msgs
tf2_kdl
tf2_msgs
tf2_py
tf2_ros
tf2_ros_py
tf2_sensor_msgs
tf2_tools
tinyxml2_vendor
tinyxml_vendor
tlsf
tlsf_cpp
topic_monitor
tracetools
trajectory_msgs
turtlesim
uncrustify_vendor
unique_identifier_msgs
urdf
urdf_parser_plugin
visualization_msgs
yaml_cpp_vendor
zstd_vendor
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
## inspect Topic
- `ros2 topic -h`
```
Commands:
  bw     Display bandwidth used by topic
  delay  Display delay of topic from timestamp in header
  echo   Output messages from a topic
  find   Output a list of available topics of a given type
  hz     Print the average receiving rate to screen
  info   Print information about a topic
  list   Output a list of available topics
  pub    Publish a message to a topic
  type   Print a topic's type>)
```
- `ros2 topic list` -> list all the <font color="#00b050">active</font> topic
```
/parameter_events
/robot_news
/rosout
```
- `ros2 topic echo /topic_name` -> creates a <font color="#ff0000">instant</font> <font color="#00b050">subscriber</font> 
```
data: Hello
---
data: Hello
---
data: Hello
```
### ros2 service
```
 ros2 service call /add_two_number example_interfaces/srv/AddTwoInts "{a: 3, b: 7}"
```
- `/add_two_number` -> service name that we provided inside `create_service` method
## set param
- ` ros2 param list`
```
/test_param:
  start_from
  time_period
  use_sim_time
```
- `ros2 param set /test_param name shimanto` -> for this node should constantly use `get_parameter`
```
[INFO] [1746782895.420166075] [test_param]: hello bob
[INFO] [1746782896.426552644] [test_param]: hello bob
[INFO] [1746782897.424476770] [test_param]: hello shimanto
[INFO] [1746782898.426413431] [test_param]: hello shimanto
```
- change runtime at the start
```
ros2 run my_py_pkg test_param_2 --ros-args -p start_from:=1000 -p time_period:=2.0
```