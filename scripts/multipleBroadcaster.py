#! /home/michael/.local/share/virtualenvs/DeepLearningProject-WE2UAgWf/bin/python

import rospy
import time
import tf
from tf3D import GazeboModel
import sys

def handle_turtle_pose (pose_msg, robot_name):
	br = tf.TransformBroadcaster()
	br.sendTransform((pose_msg.position.x,pose_msg.position.y,pose_msg.position.z),
		(pose_msg.orientation.x,pose_msg.orientation.y,pose_msg.orientation.z,pose_msg.orientation.w),
		rospy.Time.now(),
		robot_name,
		"/world")

def publisher_of_tf():
	rospy.init_node('publisher_of_tf_node', anonymous=True)
	robot_name_list=["turtlebot3_waffle_pi_fol_" + sys.argv[1],"turtlebot3_waffle_pi_fol_" + sys.argv[2]]
	gazebo_model_object = GazeboModel(robot_name_list)

	for robot_name in robot_name_list:
		pose_now = gazebo_model_object.get_model_pose(robot_name)

	time.sleep(1)
	rospy.loginfo("Ready .. Starting to Publish TF data now ...")

	rate = rospy.Rate(5)
	while not rospy.is_shutdown():
		for robot_name in robot_name_list:
			pose_now = gazebo_model_object.get_model_pose(robot_name)
			if not pose_now:
				print("The pose of " + str(robot_name) + " is not yet availble.")
			else:
				handle_turtle_pose(pose_now, robot_name)
		rate.sleep()

if __name__=='__main__':
	try:
		publisher_of_tf()
	except rospy.ROSInterruptException:
		pass
