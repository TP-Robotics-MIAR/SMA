#!/bin/bash

counter=1

source /opt/ros/noetic/setup.bash
source /home/michael/Documents/AIROB/catkin_ws_turtlebot/devel/setup.bash
echo "Launching empty world, please wait!"
roslaunch sma empty_gazebo.launch &

read -p "Enter Number of Turtlebots: " bots
while [ $counter -le $bots ] 
do
    $next_count = $counter + 1
    roslaunch sma n_robots_gazebo.launch counter:=$counter x_pos:=$(seq -6 6 | shuf -n 1) y_pos:=$(seq -6 6 | shuf -n 1) --wait &
    ((counter++))
done
counter=0

read -p "Enter Sequence of Robots: " -a array

while [ $counter -le ${#array[@]} ] 
do
    
    rosrun sma follow_node.py ${array[counter]} ${array[counter + 1]} &
    ((counter++))
done
counter=0
while [ $counter -le $((${#array[@]} -1)) ] 
do

    rosrun sma multipleBroadcaster.py ${array[counter]} ${array[counter + 1]} &
    ((counter++))
done


echo All done
