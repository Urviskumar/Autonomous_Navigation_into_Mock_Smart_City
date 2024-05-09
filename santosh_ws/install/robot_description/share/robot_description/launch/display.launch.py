import launch
import launch_ros
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
import os


def generate_launch_description():

    pkg_path = launch_ros.substitutions.FindPackageShare(package='robot_description').find('robot_description')
    urdf_model_path = os.path.join(pkg_path, 'urdf/robot.urdf')
    rviz_config_path = os.path.join(pkg_path, 'config/config.rviz')

    with open(urdf_model_path) as urdffile:
        robot_description = urdffile.read()

    params = {'robot_description': robot_description}

    return launch.LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[params],
            arguments=[urdf_model_path]),
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            parameters=[params],
            arguments=[urdf_model_path]),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            arguments=[urdf_model_path]),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config_path]),
  ])