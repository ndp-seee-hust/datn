import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import xacro


def generate_launch_description():
	
    lidar = IncludeLaunchDescription(PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('ydlidar_ros2_driver'), 'launch'),'/x3.py']))

    slam = IncludeLaunchDescription(PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('slam_gmapping'), 'launch'),'/x3_slam.py']))

    gmapping = IncludeLaunchDescription(PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('slam_gmapping'), 'launch'),'/gmapping_x3_launch.py']))

    robot = IncludeLaunchDescription(PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('my_bot'),'launch'),'/rsp.launch.py']))


    return LaunchDescription([

        lidar,
        slam,
        #gmapping,
		robot
    ])