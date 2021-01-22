#!/usr/bin/env python3

from threading import current_thread
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
        self.rate = rospy.Rate(20)

    def move_sqaure(self):
        """ Move the turtle in a square. """
        # Since the robot is moving just in x-axis
        self.vel_msg.linear.y = 0
        self.vel_msg.linear.z = 0
        self.vel_msg.angular.x = 0
        self.vel_msg.angular.y = 0

        # Get the input from the user.
        square_size = rospy.get_param('~l')
        speed = rospy.get_param('~x')
        angular_velocity = rospy.get_param('~z')

        # Keep moving until shutdown
        while not rospy.is_shutdown():
            # Get the current time for distance calculus
            t0 = rospy.Time.now().to_sec()
            current_distance = 0

            # Set moving speed
            self.vel_msg.linear.x = speed
            self.vel_msg.angular.z = 0

            # Move forward
            while current_distance < square_size:
                # Publish the vel_msg
                self.velocity_publisher.publish(self.vel_msg)

                # Calculate the current distance
                t1 = rospy.Time.now().to_sec()
                current_distance = speed * (t1 - t0)

                # Publish at the desired rate.
                self.rate.sleep()

            # Make a 90 degree turn
            self.vel_msg.linear.x = 0
            self.vel_msg.angular.z = angular_velocity
            t = (3.14159 / 2) / angular_velocity    # the turning time
            for _ in range(int(t*20)):
                # Publish the vel_msg
                self.velocity_publisher.publish(self.vel_msg)
                # Publish at the desired rate.
                self.rate.sleep()

        # If control + C is pressed, the node will stop.
        rospy.spin()


if __name__ == '__main__':
    try:
        x = TurtleBot('turtlebot_controller', '/turtle1/cmd_vel')
        x.move_sqaure()
    except rospy.ROSInterruptException:
        pass


