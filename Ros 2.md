## Build a package
<font color="#c00000">must</font> run in the workspace
```
colcon build 
```
- or just a specific package
```
colcon  build --packages-select my_py_pkg
```

## Create a package

```
ros2 pkg create my_py_pkg --build-type ament_python --dependencies rclpy
```
- run this command in in <font color="#00b050">src</font> directory
- 
## Minimal Node code

## Inspect Node
### ros2 node
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
