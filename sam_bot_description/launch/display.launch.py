import launch
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os
# MODULE IMPORTED TO CHECK
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    pkg_share = launch_ros.substitutions.FindPackageShare(package='sam_bot_description').find('sam_bot_description')
    #default_model_path = os.path.join(pkg_share, 'models/sam_bot_description.urdf')
    # CREARE UNA CARTELLA WORLD NEL PKG NOSTRO CON DENTRO VOLENDO dolly_city.world o un world più legger
    #default_world_path = os.path.join(pkg_share, '~/Desktop/dev_ws/src/navigation2_tutorials/sam_bot_description/worlds/sam_empty.world')
    default_world_path = os.path.join(pkg_share, 'worlds/sam_empty.world')
    default_rviz_config_path = os.path.join(pkg_share, 'rviz/urdf_config.rviz')
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')#FORSE DOBBIAMO CAMBIARE IL PATH 
    use_sim_time = LaunchConfiguration('use_sim_time')
    lidar_pkg_dir = LaunchConfiguration('lidar_pkg_dir',
        default=os.path.join(get_package_share_directory('hls_lfcd_lds_driver'), 'launch'))

    urdf_file = os.path.join(pkg_share, 'models/sam', 'sam_bot_description.urdf')
    
    doc = xacro.parse(open(urdf_file))
    xacro.process_doc(doc)
    robot_description = {'robot_description': doc.toxml()}
    
    declare_use_sim_time_argument = DeclareLaunchArgument(
        'use_sim_time',
        default_value='false',
        description='Use simulation/Gazebo clock')

    robot_state_publisher_node = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen', 
        parameters=[robot_description]
    )
    joint_state_publisher_node = launch_ros.actions.Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        condition=launch.conditions.UnlessCondition(LaunchConfiguration('gui'))
    )
    joint_state_publisher_gui_node = launch_ros.actions.Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        condition=launch.conditions.IfCondition(LaunchConfiguration('gui'))
    )
    rviz_node = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', LaunchConfiguration('rvizconfig')],
    )
    #### tf2 static transforms

    ## tf2 - base_footprint to laser
    node_tf2_fp2laser = Node(
        name='tf2_ros_fp_laser',
        package='tf2_ros',
        executable='static_transform_publisher',
        output='screen',
        arguments=['0', '0', '0', '0.0', '0.0', '0.0', 'base_footprint', 'laser'],   
    )

    ## tf2 - base_footprint to map
    node_tf2_fp2map = Node(
        name='tf2_ros_fp_map',
        package='tf2_ros',
        executable='static_transform_publisher',
        output='screen',
        arguments=['0', '0', '0', '0.0', '0.0', '0.0', 'base_footprint', 'map'], 
    )

    ## tf2 - base_footprint to odom
    node_tf2_fp2odom = Node(
        name='tf2_ros_fp_odom',
        package='tf2_ros',
        executable='static_transform_publisher',
        output='screen',
        arguments=['0', '0', '0', '0.0', '0.0', '0.0', 'base_footprint', 'odom'],
    )
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py'),
        )
    )

    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'sam_bot_description'],
                        output='screen')

    joint = Node(package='dummy_sensors', executable='dummy_joint_states', output='screen')

    laser = Node(package='dummy_sensors', executable='dummy_laser', output='screen')

    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(name='gui', default_value='True',
                                            description='Flag to enable joint_state_publisher_gui'),
        launch.actions.DeclareLaunchArgument(name='model', default_value=urdf_file,
                                            description='Absolute path to robot urdf file'),
        launch.actions.DeclareLaunchArgument(name='rvizconfig', default_value=default_rviz_config_path,
                                            description='Absolute path to rviz config file'),
        launch.actions.DeclareLaunchArgument(name='world', default_value=default_world_path, description='SDF world file'),
        
        joint_state_publisher_node,
        joint_state_publisher_gui_node,
        robot_state_publisher_node,
        rviz_node,
        gazebo,
        spawn_entity,
        laser,
        joint,
        declare_use_sim_time_argument,
        node_tf2_fp2laser,
        node_tf2_fp2map,
        node_tf2_fp2odom 
    ])

