// Placeholder — replace with the real controller once Chapter 1 is underway.
// Shown in pages/chapter-1.md via: {{#include ../01-ros-gazebo/src/controller.cpp:1:40}}

#include <memory>
#include <string>

#include "controller.hpp"

namespace sim::ros_gazebo
{

constexpr double kDefaultKp = 0.8;

Controller::Controller(const std::string& node_name)
    : rclcpp::Node(node_name), target_(0.0), current_(0.0), kp_(kDefaultKp)
{
    publisher_ = this->create_publisher<geometry_msgs::msg::Twist>(
        "cmd_vel", rclcpp::QoS(10).reliable());

    subscription_ = this->create_subscription<nav_msgs::msg::Odometry>(
        "odom", rclcpp::SensorDataQoS(),
        [this](const nav_msgs::msg::Odometry::SharedPtr msg) {
            current_ = msg->pose.pose.position.x;
        });
}

void Controller::update()
{
    // P-controller: steer toward target_ using proportional error.
    const double error = target_ - current_;
    cmd_vel_.linear.x = kp_ * error;
    publisher_->publish(cmd_vel_);
}

void Controller::set_target(double target)
{
    target_ = target;
}

}  // namespace sim::ros_gazebo
