# Multi Agent System

This package can be used for a system of leader-followers. It extrapolates from the turtlebot3 package used for simulation in gazebo. Using this package, you can summon a number of turtlebots then select the sequence of how each are following each other.


## Usage

After making the bash script executable on your machine using;

```
chmod +x load_multiple_robots.sh
```

You will be able to run it. When at first glance the loading of messages seems to stop, write the number of turtlebots you want to summon. For example;

```
8
```

Then a second time the messages will seems to stop, there you will write the sequence which each turtlebot will follow each other;

For example using the 8 turtlebots above

```
4 5 6 7 8 1 3 2
```

## Explanation

From the shell script, all required python scripts will be loaded and executed so as to create the leader-follower system. As seen above in the commands the follower-leader will follow a sequence, similar to the image describe below.

![alt text](https://github.com/TP-Robotics-MIAR/SMA/blob/main/untitled.png)

The system works as this;

- The [broadcaster script](https://github.com/TP-Robotics-MIAR/SMA/blob/main/scripts/multipleBroadcaster.py) will take a list of two turtlebots;
- From this list, their relative pose (linear and angular) will be computed so as to get a comparison of their situation in the environment;
- Using this transform; their relative pose will be used to send a **cmd_vel** command to the follower turtlebot using;
![equation](http://www.sciweavers.org/download/Tex2Img_1632608553.jpg)
