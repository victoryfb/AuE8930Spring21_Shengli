#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist


class TurtleBot:
    def __init__(self, node_name, topic):
        rospy.init_node(node_name, anonymous=True)

        # Publisher which will publish to the given topic.
        self.velocity_publisher = rospy.Publisher(topic, Twist, queue_size=10)

        # Init the velocity message
        self.vel_msg = Twist()

        # Init the publish rate
        self.rate = rospy.Rate(10)

    def move_circle(self):
        """ Move the turtle in a circle. """
        self.vel_msg.linear.y = 0

        # Get the input from the user.
        self.vel_msg.linear.x = rospy.get_param('~x')
        self.vel_msg.angular.z = rospy.get_param('~z')
        num_turms = rospy.get_param('~n')

        # Calculate the moving time according to the angular velocity
        # and the number of turms
        moving_time = num_turms * 2 * 3.14159 / self.vel_msg.angular.z

        # Record the start time
        start = rospy.Time.now()

        while rospy.Time.now() - start < rospy.Duration.from_sec(moving_time):
            # Publish the vel_msg
            self.velocity_publisher.publish(self.vel_msg)

            # Publish at the desired rate.
            self.rate.sleep()

        # Stop the robot after the movement is over.
        self.vel_msg.linear.x = 0
        self.vel_msg.angular.z = 0
        self.velocity_publisher.publish(self.vel_msg)

        # If control + C is pressed, the node will stop.
        rospy.spin()


if __name__ == '__main__':
    try:
        x = TurtleBot('turtlebot_controller', '/turtle1/cmd_vel')
        x.move_circle()
    except rospy.ROSInterruptException:
        pass


