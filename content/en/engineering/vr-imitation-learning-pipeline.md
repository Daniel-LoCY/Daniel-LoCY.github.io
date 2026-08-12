---
title: "Quest 2 Teleoperation and VLA Demonstration-Data Pipeline"
description: "Quest 2 control for Isaac Sim and TM5S, integrated with robot state, images, and action recording for GR00T and VLA demonstrations."
featured_image: "/images/projects/default-project.svg"
tags: ["Quest 2", "PyOpenXR", "Rotation 6D", "NVIDIA Isaac GR00T", "ROS 2"]
weight: 2
---

This system uses Quest 2 controllers to teleoperate robot arms in both Isaac Sim and on a physical TM5S. It then connects to a separate recording platform to produce demonstration data for imitation learning and NVIDIA Isaac GR00T.

## Control Flow

- Captured controller poses and button states through Quest 2, ALVR, SteamVR, and PyOpenXR.
- Converted VR coordinates into robot end-effector targets at a 60 Hz control rate, with speed, workspace, and operating-state limits.
- Connected the same teleoperation concept to both Isaac Sim and TM5S and validated it on pick-and-place tasks.

## Recording Integration

- Integrated control actions with camera images, robot state, end-effector pose, and gripper state in the recording platform.
- Supported demonstrations from simulated and physical environments for imitation learning and GR00T/VLA training.
- Recorded images at 30 FPS and robot state/actions at 60 Hz, aligning multi-source data by timestamp.

## Validation Status

Approximately five people operated or tested the system, and pick-and-place was completed in both simulated and physical environments. Latency and task success rate have not been formally measured, so subjective impressions are not presented as quantitative results.
