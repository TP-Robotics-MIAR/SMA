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