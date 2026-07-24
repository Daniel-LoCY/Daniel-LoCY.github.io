---
title: "AprilTag HDMI and Power-Cable Unplugging"
description: "An AprilTag-guided TM5S workflow integrating grippers, TM APIs, and ROS 2 across multiple unplugging orientations and device models."
featured_image: "/images/projects/default-project.svg"
tags: ["TM5S", "TM Flow", "TM API", "ROS 2", "AprilTag", "PyQt"]
weight: 2
---

This real-robot workflow covers HDMI and power-cable connectors from visual detection and pose estimation through robot approach, gripping, unplugging, and error handling, with configurable device and cable settings.

## My Contributions

- Used AprilTag to detect connector position and pose, then controlled the robot to approach and unplug the target.
- Supported rear-, side-, and bottom-inserted connectors, power cables, and multiple device models; tested up to four AprilTags in one frame.
- Measured the stable detection range of the robot's built-in camera, with a tested limit of approximately 50 cm and 80 pixels.
- Tuned robot poses and gripping locations by device and connector orientation to reduce collision risk.
- Moved the latch/gripping position away from the connector to address the limited vertical approach available on rear-inserted devices.

## Control Interface

Designed a PyQt/PyQt6 UI to manage device and cable settings, tag IDs, image display, workflow state, error handling, and robot control while separating vision, PLC, gripper, ROS 2, and workflow-execution modules.
