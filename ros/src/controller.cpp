// Placeholder — replace with the real controller once this section is underway.
// Shown in pages/ros/01-fundamentals.md via: {{#include ../../ros/src/controller.cpp:1:25}}

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
