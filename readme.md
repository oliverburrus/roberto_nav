# Launch File Explanations

## multi_range.launch 

This launch file will set up a boolean-value object detection in 4 ranges within a 90 degree cone in front of the RPLIDAR. You can set the r_value (in meters) to determine how far away you want the robot to stay away from an obstacle (default .5 m).
<img src="https://lh3.googleusercontent.com/pw/AM-JKLV3EibqC1AEUmjvsQnpU55opvjySuAICHiBi0ocyqEG0bqpKUwbJl1gLrZtqBjCcOF3KQNt6Cp29-h46xTvx4GhL6pU-_BJ11kZAfAs99wtV4JlbNR_e7UWNVfWX978VoKkM2HXXeWoUVhi9rcN1U8uXQ=w960-h720-no?authuser=0" width=400, height=300/>

# Setup and Launch
```
# Make sure the RPLIDAR is connected
ls -l /dev | grep ttyUSB0

# Set permissions for the RPLIDAR
sudo chmod 666 /dev/ttyUSB0

# catkin_make and launch
cd catkin_ws
catkin_make
roslaunch rplidar_ros rplidar.launch
roslaunch check_obstacle {multi_range/detector}.launch
```

# Installation
## With prior install of rplidar_ros
```
cd catkin_ws/src
sudo git clone https://github.com/oliverburrus/obstacle_detector.git
```
## Without prior install of rplidar_ros
```
# Install dependencies.
sudo apt-get update
sudo apt-get install cmake python-catkin-pkg python-empy python-nose python-setuptools libgtest-dev python-rosinstall python-rosinstall-generator python-wstool build-essential git

cd ~/catkin_ws/

gedit ~/.bashrc
#Add the following at the END of the .bashrc file

source /opt/ros/melodic/setup.bash
source ~/catkin_ws/devel/setup.bash

# Save and close

source ~/catkin_ws/devel/setup.bash
cd src
sudo git clone https://github.com/Slamtec/rplidar_ros.git
sudo git clone https://github.com/oliverburrus/obstacle_detector.git
```

