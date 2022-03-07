# Launch File Explanations

## multi_range.launch 

This launch file will set up a boolean-value object detection in 4 ranges within a 90 degree cone in front of the RPLIDAR. You can set the r_value (in meters) to determine how far away you want the robot to stay away from an obstacle (default .5 m).

## test.launch

This is the launch file which will lead to one method of autonomy, will write more later.
<img src="https://lh3.googleusercontent.com/SmbnTsUosFNbEJGCA40CqwkWQteKnpj2H7qH9ltxtDqeIQh7Mgd5uFTLHnjccB8nZtqFFb738ioU71A9ZFl2xqX_VhHi8MxV_S5R4uclaVoo6YDSBrdDSuOzDtmYDdvDW_xh8laR-K5b--Rglo12wcY78azxOufZDX_Zku6ST2kjQReIR4W89Y9dX6Lr384DLnO85Hbf1gvbIL6AU5gZarDSowIAdZzdsHbCuEK2oYsZ5XCgfM6KdlvT1vlLdPM2esVDRWwJ8ShTj0pi4wMrKS6xqE6FupFlhUxzEGGtt6kDYSELcARMTYXZvk3typOwLD1kGiQMLxxcGrdRIOcXOBW49j4TaHX175Qe-KESGUnKJogGBtit7sFwQ_ktx7KEt96nWndI-T75laUrHbVFgxf-aBM7xHXo6Fxb3wG6YaF5Nj52j4se1o_OtEzgKvWbnkoix5EAPGRjmCfg6MF0RGtvhD9gRBfDTQ2CHDDRzUBw1fIbwJt6URr81ZdCMJpuzuJxTexMtawKAFNZzvjLF9-tQfSU_SPKuMgjfzt9gGAoOq-3uOxUkVFfqDWvb6bYqJwxfX4YLUOweEcUtdwkyIY0Epyx14F3pp70LJNHvarNL3uWagYx_2etckmnzSEy4egCxsRW1Xi-jO8WGuE53h3ZM2sG7anpsDqqHlqYt118vIs1H0Ftg52zSkcsb44ITFtk4OWwflykBLBOyaNn-JZKBQ=w818-h786-no?authuser=0" width=410, height=394/>
<img src="https://lh3.googleusercontent.com/AD9j4HJrWLqfbWlCdmkDjDGa8BY6ZEVVDf_K3KVz7J4j7-NONBi87nR54AGy8Oq29UAVlQuyBFnFmDxH5701AGYQ9aDY3iNtDNUO9Ys6L3JeW6X4WGGr4YIrsGsfkzmdNNfg7OcJJ5xOy2YPNLCqkfVy-aiIAxfds9OphfF0m2X-uA3kc3Ac8WNl7w3hq76MJMNK8Pm1Bi60N3W8cZpdlCGdqIHBaVrIMCwvGbswKS21YI8LzyuXUgQXHt37p3LGnQOXRVLdu225kOUts7GzDFxLUq4Q_kUwnSEOcWIsUWaCvZ9s1bWWq6eHrEvwgvfG8GcG2glzGoA8xvPIJ-3I64x8frfE7dZVcYk2brA1wq4ZOuXPYAi6rhY0lRfHnIu9L5fLPRthkvnHLKx_2R5dXW609kJv_aMV6mkIKNJZuB_rL-w0nLsuwsrbEAAce6jdYNDgQXtNVtDqOtZZL2AbP_f-Lv2bgCTmSPQl2Ydne9E_XD3qX0fbkiM9GM3AOw_QtPUtj0YwHOBVntBsNG9bbxORr65nIyRJxnkplHuK3FDaN3b9BmHpvxKeuGGm1uEgb27f0LyWiC4gk9o1-MXxA-ghXfAfjkNV7cLd3iKmlUef0xj2qHmACIopD39CuaAKqJY9PsCc9R61D0GpMJJNR4t5mj8Aq7ZLAFXGS4LIkJqApQofBImZKo_q_JgP8hn2mELPimXePbkk_8uf4BgESVvQjg=w916-h585-no?authuser=0" width=500, height=300/>

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

