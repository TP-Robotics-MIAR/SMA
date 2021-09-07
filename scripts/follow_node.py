#! /home/michael/.local/share/virtualenvs/DeepLearningProject-WE2UAgWf/bin/python

import rospy
import time
import tf, math
import geometry_msgs.msg
import sys

if __name__ == '__main__':
	rospy.init_node('tf_listener_turtle',anonymous=True)
	listener = tf.TransformListener()

	follower = 'turtlebot3_waffle_pi_fol_' + sys.argv[2]
	followed = 'turtlebot3_waffle_pi_fol_' + sys.argv[1]
	cmd_vel = '/fol_' + sys.argv[2] + '/cmd_vel'

	turtle_vel = rospy.Publisher(cmd_vel, geometry_msgs.msg.Twist, queue_size = 1)

	rate = rospy.Rate(10.0)
	ctrl_c = False

	follower_frame = '/'+follower
	followed_frame = '/'+followed

	def shutdownhook():
		global ctrl_c
		print("shut down")
		cmd = geometry_msgs.msg.Twist()
		cmd.linear.x = 0
		cmd.angular.z = 0
		turtle_vel.publish(cmd)
		ctrl_c = True

	while not ctrl_c:
		try:
			(tran,rot) = listener.lookupTransform(follower_frame,followed_frame, rospy.Time(0))
		except:
			continue

		angular = 0.4 * math.atan2(tran[1],tran[0])
		linear = 0.1 * math.sqrt(tran[0]**2 + tran[1]**2)
		cmd = geometry_msgs.msg.Twist()
		cmd.linear.x = linear
		cmd.angular.z = angular
		turtle_vel.publish(cmd)
		rate.sleep()
