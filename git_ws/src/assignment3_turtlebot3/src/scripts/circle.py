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
        self.vel_msg.linear.x = 0.5
        self.vel_msg.angular.z = 0.5

        while not rospy.is_shutdown():
            # Publish the vel_msg
            self.velocity_publisher.publish(self.vel_msg)

            # Publish at the desired rate.
            self.rate.sleep()

        # If control + C is pressed, the node will stop.
        rospy.spin()


if __name__ == '__main__':
    try:
        x = TurtleBot('turtlebot_controller', '/cmd_vel')
        x.move_circle()
    except rospy.ROSInterruptException:
        pass


