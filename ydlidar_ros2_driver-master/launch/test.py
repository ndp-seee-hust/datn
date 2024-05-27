
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import LifecycleNode
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.actions import LogInfo

import lifecycle_msgs.msg
import os


def generate_launch_description():
    share_dir = get_package_share_directory('ydlidar_ros2_driver')
    parameter_file = LaunchConfiguration('params_file')
    node_name = 'ydlidar_ros2_driver_node'
    slam_parameter_file = LaunchConfiguration('slam_params_file')

    params_declare = DeclareLaunchArgument('params_file',
                                           default_value=os.path.join(
                                               share_dir, 'params', 'ydlidar_x3.yaml'),
                                           description='FPath to the ROS2 parameters file to use.')
    params = DeclareLaunchArgument('slam_params_file',
                                           default_value=os.path.join(
                                               share_dir, 'params', 'mapper_params_online_async.yaml'),
                                           description='FPath to the ROS2 parameters file to use.')

    driver_node = LifecycleNode(package='ydlidar_ros2_driver',
                                executable='ydlidar_ros2_driver_node',
                                name='ydlidar_ros2_driver_node',
                                output='screen',
                                emulate_tty=True,
                                parameters=[parameter_file],
                                namespace='/',
                                )
    tf2_node = Node(package='tf2_ros',
                    executable='static_transform_publisher',
                    name='static_tf_pub_laser',
                    arguments=['0', '0', '0.02','0', '0', '0', '1','base_link','laser'],
                    )
    slam_toolbox = Node(package='slam_toolbox',
                        executable='async_slam_toolbox_node',
                        name='slam_toolbox',
                        output='screen',
                        parameters=[slam_parameter_file],
                        namespace='')

    return LaunchDescription([
        params_declare,
        params,
        driver_node,
        tf2_node,
        slam_toolbox,
    ])