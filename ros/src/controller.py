# Placeholder — replace with the real controller once this section is underway.
# Shown in pages/ros/01-fundamentals.md via: {{#include ../../ros/src/controller.py:1:25}}

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, qos_profile_sensor_data
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

DEFAULT_KP = 0.8


class Controller(Node):
    def __init__(self):
        super().__init__("controller")
        self.target = 0.0
        self.current = 0.0
        self.kp = DEFAULT_KP

        reliable_qos = QoSProfile(depth=10, reliability=ReliabilityPolicy.RELIABLE)
        self.publisher_ = self.create_publisher(Twist, "cmd_vel", reliable_qos)

        self.subscription_ = self.create_subscription(
            Odometry, "odom", self._on_odom, qos_profile_sensor_data
        )

    def _on_odom(self, msg: Odometry) -> None:
        self.current = msg.pose.pose.position.x

    def update(self) -> None:
        # P-controller: steer toward self.target using proportional error.
        error = self.target - self.current
        cmd = Twist()
        cmd.linear.x = self.kp * error
        self.publisher_.publish(cmd)
