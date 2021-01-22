#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt


class TurtleBot:
    def __init__(self):
        # Creates a node with name 'turtlebot_controller' and make sure it is a
        # unique node (using anonymous=True).
        rospy.init_node('turtlebot_controller', anonymous=True)

        # Publisher which will publish to the topic '/turtle1/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',
                                                  Twist, queue_size=10)

        # A subscriber to the topic '/turtle1/pose'. self.update_pose is called
        # when a message of type Pose is received.
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose',
                                                Pose, self.update_pose)

        # Init the velocity message
        self.vel_msg = Twist()

        self.pose = Pose()
        self.rate = rospy.Rate(20)

    def update_pose(self, data):
        """Callback function which is called when a new message of type Pose is
        received by the subscriber."""
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def euclidean_distance(self, goal_pose):
        """Euclidean distance between current pose and the goal."""
        return sqrt(pow((goal_pose.x - self.pose.x), 2) +
                    pow((goal_pose.y - self.pose.y), 2))

    def linear_vel(self, goal_pose, constant=1.5):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return constant * self.euclidean_distance(goal_pose)

    def steering_angle(self, goal_pose):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)

    def angular_vel(self, goal_pose, constant=6):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return constant * (self.steering_angle(goal_pose) - self.pose.theta)

    def move2goal(self, goal_pose, distance_tolerance):
        """ Moves the turtle to the goal. """
        # Oritent the robot to the target
        while abs(self.pose.theta - self.steering_angle(goal_pose)) > 0.00001:
            self.vel_msg.angular.z = self.angular_vel(goal_pose)

            # Publishing our vel_msg
            self.velocity_publisher.publish(self.vel_msg)

            # Publish at the desired rate.
            self.rate.sleep()
        self.vel_msg.angular.z = 0

        # Move the turtle to the goal
        while self.euclidean_distance(goal_pose) > distance_tolerance:
            # Linear velocity in the x-axis.
            self.vel_msg.linear.x = self.linear_vel(goal_pose)
            self.vel_msg.linear.y = 0
            self.vel_msg.linear.z = 0

            # Publishing our vel_msg
            self.velocity_publisher.publish(self.vel_msg)

            # Publish at the desired rate.
            self.rate.sleep()

        # Stopping our robot after the movement is over.
        self.vel_msg.linear.x = 0
        self.vel_msg.angular.z = 0
        self.velocity_publisher.publish(self.vel_msg)

    def move_square(self):
        # Get the input from the user.
        distance_tolerance = rospy.get_param('~tol')

        # Define the path
        path = [(5, 5), (8, 5), (8, 8), (5, 8), (5, 5)]

        # Init the goal position
        goal_pose = Pose()

        # Move along the path
        for point in path:
            goal_pose.x, goal_pose.y = point
            self.move2goal(goal_pose, distance_tolerance)


if __name__ == '__main__':
    try:
        x = TurtleBot()
        x.move_square()
    except rospy.ROSInterruptException:
        pass
