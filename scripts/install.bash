#! /bin/bash
# Note: Use this script as a regular user. It will request sudo on demand

if [[ $# -ne 1 ]]
then
    echo "Use: $0 <root target catkin workspace location>"
    exit -1
fi

# Install the rosinstall stuff in the workspace
cd $1/src
rosinstall . file:robotics_challenge/robotics_challenge.rosinstall


## Install yocs stuff
P=ros-melodic-yocs-
sudo aptitude install ${P}ar-marker-tracking ${P}ar-pair-approach ${P}ar-pair-tracking ${P}cmd-vel-mux ${P}controllers \
${P}joyop ${P}keyop ${P}localization-manager ${P}math-toolkit ${P}msgs ${P}navi-toolkit ${P}navigator ${P}rapps ${P}safety-controller ${P}velocity-smoother ${P}virtual-sensor ${P}waypoint-provider ${P}waypoints-navi -y

# Install kobuki stuff
sudo apt install ros-melodic-kobuki-core ros-melodic-kobuki-dock-drive ros-melodic-kobuki-driver ros-melodic-kobuki-ftdi ros-melodic-kobuki-msgs -y

# Install turtlebot3 packages
sudo apt install ros-melodic-turtlebot3-gazebo -y

# Additional utils
sudo apt install pyqt5-dev-tools ros-melodic-ecl-core -y


# Compile the stuff
cd ..
catkin_make
