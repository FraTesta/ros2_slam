# ROS2_ortopillar_packages

1. clone this pkgs into your ros 2 workspace

2. colcon build at the root of the workspace

3. run the command: ros2 launch orthopillar_robot_spawner_pkg gazebo_world.launch.py (spawn the model in gazebo).

4. in another shell: ros2 launch orthopillar_robot_controller_pkg controller_estimator.launch.py (make the robot move using odometry and lidar).

5. in another shell type < rviz2 > and load the configuration or create a new one.

WARNING! the rviz config is not in the launch file (mi ero rotto il cazzo) quindi aggiungerla una volta trovata una decente / CHECK URDF CONVERTITO 
