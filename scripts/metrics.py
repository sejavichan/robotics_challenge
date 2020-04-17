#!/usr/bin/env python

# A very basic TurtleBot script that moves TurtleBot forward indefinitely. Press CTRL + C to stop.  To run:
# On TurtleBot:
# roslaunch turtlebot_bringup minimal.launch
# On work station:
# python goforward.py

import sys
import math
import rospy
import tf
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PointStamped

class Metrics:
    def __init__(self):
       
        self.listener = tf.TransformListener()
    
        if not(rospy.has_param('~goal')):
            rospy.logfatal("You must specify the goal to this module via parameter server")
            
        self.base_frame = rospy.get_param('base_frame', default='base_link')
        self.global_frame = rospy.get_param('global_frame', default='map')
            
        self.goal_x = rospy.get_param('~goal/x', default=5)
        self.goal_y = rospy.get_param('~goal/y', default=5)  
        
        self.goal_tolerance = 0.25  // We will allow a 25 cm deviation from the goal
        
        self.has_transform = False
        
        while not(self.has_transform):
            (self.init_x, self.init_y) = self.getTransform()
        
        self.distance = 0
        self.init_time = rospy.now()
        
        
    def getTransform(self):
        try:
            (t,r) = self.listener.lookupTransform('map','base_link', rospy.Time(0))
            self.has_transform = True
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            return
        return (t[0], t[1])
        
	        
            
      
    def update(self):
	    rospy.loginfo("Metrics node. Acquiring new data")
        px,py = self.getTransform()
        self.distance += math.sqrt( (px-self.px)**2 + (py-self.py)**2)
        
        #Check for the goal:
        dist_goal = math.sqrt( (px-self.goal_x)**2 + (py-self.goal_y)**2)
        rospy.loginfo("Traveled distance %f. Distance to goal: %f", self.distance,dist_goal)
        
        self.px = px
        self.py = py
        
        if dist_goal_< self.goal_gap:
            self.elapsed_time = rospy.Time.now() - self.init_time
            rospy.loginfo("Goal time. Elapsed time: %f")

        

        
    def shutdown(self):
        # stop turtlebot
        rospy.loginfo("Stopped Metrics node. Generating statistics")
        (px, py) = self.getTransform()
        
	    
 
if __name__ == '__main__':
    try:
	    # initiliaze
        rospy.init_node('robotcontrol', anonymous=False)

	    # tell user how to stop TurtleBot
	    rospy.loginfo("To stop TurtleBot CTRL + C")

        metrics=Metrics()
	    # What function to call when you ctrl + c    
        rospy.on_shutdown(metrics.shutdown)

        #TurtleBot will stop if we don't keep telling it to move.  How often should we tell it to move? 10 HZ
        r = rospy.Rate(10);

        # as long as you haven't ctrl + c keeping doing...
        while not rospy.is_shutdown():
            rospy.loginfo("Loop")
                # publish the velocity
                metrics.update()
                # wait for 0.1 seconds (10 HZ) and publish again
                r.sleep()
    except:
        rospy.loginfo("Metrics node terminated.")
