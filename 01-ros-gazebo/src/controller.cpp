// Placeholder — replace with the real controller once Chapter 1 is underway.
// Shown in README.md via: {{#include src/controller.cpp:1:15}}

#include "controller.hpp"

void Controller::update()
{
    // P-controller: steer toward target_ using proportional error.
    auto error = target_ - current_;
    cmd_vel_.linear.x = kp_ * error;
    publisher_->publish(cmd_vel_);
}

void Controller::set_target(double target)
{
    target_ = target;
}
