# ROS 2 Foxy installation
1. follow the tutorial : https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html
2. install also the following dependencies:
```
sudo apt update && sudo apt install -y \
  build-essential \
  cmake \
  git \
  libbullet-dev \
  python3-colcon-common-extensions \
  python3-flake8 \
  python3-pip \
  python3-pytest-cov \
  python3-rosdep \
  python3-setuptools \
  python3-vcstool \
  wget

python3 -m pip install -U \
  argcomplete \
  flake8-blind-except \
  flake8-builtins \
  flake8-class-newline \
  flake8-comprehensions \
  flake8-deprecated \
  flake8-docstrings \
  flake8-import-order \
  flake8-quotes \
  pytest-repeat \
  pytest-rerunfailures \
  pytest

sudo apt install --no-install-recommends -y \
  libasio-dev \
  libtinyxml2-dev

sudo apt install --no-install-recommends -y \
  libcunit1-dev
   ```

# ROS2_ortopillar_packages

1. clone this pkgs into your ros 2 workspace

2. Copy the folder *meshes* in orthopillar_robot_spawner_pkg/model/orto_meshes into a new folder called *orthopillar* to be placed in /.gazebo/models 

3. Put in ./gazebo/models/orthopillar also the file.config that you can find in orthopillar_robot_spawner_pkg/model/orthopillar
4. install: 
   ```
   pip3 install xacro
   sudo apt install ros-foxy-joint-state-publisher-gui
   ```

5. colcon build at the root of the workspace
## Run 

1. run the command: ros2 launch orthopillar_robot_spawner_pkg gazebo_world.launch.py (spawn the model in gazebo).

2. in another shell: ros2 launch orthopillar_robot_controller_pkg controller_estimator.launch.py (make the robot move using odometry and lidar).

3.  in another shell type < rviz2 > and load the configuration or create a new one.

# Nav2 installation
1. install
   ```
   sudo apt install ros-foxy-navigation2 ros-foxy-nav2-bringup
   cd /ros2_slam
   colcon build
   ```
2. Source the workspace: 
   ``` 
   . install/local_setup.bash
   ```
   ## Run 
   1. launch the ortopillar simulation:
   ```
   ros2 launch orthopillar_robot_spawner_pkg gazebo_world.launch.py
   ```
   In Rviz, correct the path of the robotModel by opening the model.urdf file.

   2. In another __sourced__ terminal launch the navigation node:
   ```
   ros2 launch nav2_bringup navigation_launch.py
   ```
   3. In the final terminal (__sourced__) launch the slam:
   ```
   ros2 launch slam_toolbox online_async_launch.py
   ```
   4. In Rviz you should be able to add the cost_map (local and global), the path ....
   5. Finally in another terminal you can give a goal position to the robot using the nav2 action server:
   ```
   ros2 topic pub /goal_pose geometry_msgs/PoseStamped "{header: {stamp: {sec: 0}, frame_id: 'map'}, pose: {position: {x: 0.2, y: 0.0, z: 0.0}, orientation: {w: 1.0}}}"
   ```

  



 
