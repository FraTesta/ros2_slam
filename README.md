# ROS2_ortopillar_packages

1. clone this pkgs into your ros 2 workspace

2. Copy the folder *meshes* in orthopillar_robot_spawner_pkg/model/orto_meshes into a new folder called *orthopillar* to be placed in /.gazebo/models 

3. Put in ./gazebo/models/orthopillar also the config file that you can find in orthopillar_robot_spawner_pkg/model/orthopillar

4. colcon build at the root of the workspace

5. run the command: ros2 launch orthopillar_robot_spawner_pkg gazebo_world.launch.py (spawn the model in gazebo).

6. in another shell: ros2 launch orthopillar_robot_controller_pkg controller_estimator.launch.py (make the robot move using odometry and lidar).

7. in another shell type < rviz2 > and load the configuration or create a new one.

 
