---
title: "Virtual and Physical Robot VR Teleoperation and Digital Twin Data Pipeline"
description: "Quest 2 control for Isaac Sim and physical robot arms, integrated with robot state, images, and action recording for GR00T and VLA demonstrations."
featured_image: "/images/projects/default-project.svg"
tags: ["VR Teleoperation", "Digital Twin", "NVIDIA Isaac GR00T", "ROS 2"]
weight: 2
---

This system provides VR teleoperation and a Digital Twin data flow for robot arms in Isaac Sim and on physical robot hardware. It then connects to a recording platform to produce demonstration data for imitation learning and NVIDIA Isaac GR00T.

## Control Flow

- Converted VR control input into robot operation targets with speed, workspace, and operating-state limits.
- Connected the same teleoperation concept to both Isaac Sim and physical robot hardware for simulation and physical validation.

## Recording Integration

- Integrated control actions with camera images, robot state, end-effector pose, and gripper state in the recording platform.
- Supported demonstrations collected separately from simulated and physical environments for imitation learning and GR00T/VLA training.
- Established a repeatable multi-source recording and analysis workflow.

## Validation Status

The system was validated in both simulated and physical environments. The workflow records images, robot state/actions, end-effector pose, and gripper state for reproducible analysis.
