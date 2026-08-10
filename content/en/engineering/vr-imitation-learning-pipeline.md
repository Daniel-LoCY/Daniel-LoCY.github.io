---
title: "VR Control and NVIDIA Isaac GR00T Imitation-Learning Pipeline"
description: "A virtual/physical robot data workflow combining Quest 2 control, robot state, and vision data for NVIDIA Isaac GR00T imitation learning."
featured_image: "/images/projects/default-project.svg"
tags: ["Quest 2", "PyOpenXR", "Rotation 6D", "NVIDIA Isaac GR00T", "ROS 2"]
weight: 5
---

This workflow uses VR controllers to operate a robot, record demonstrations, and test model inference while keeping control and data formats aligned between simulation and the physical environment.

## My Contributions

- Combined Quest 2 controller poses, button states, and robot end-effector state into control and training data.
- Built recording workflows for virtual and physical environments with RGB, depth, end-effector pose, gripper state, and action data.
- Increased control-box capture throughput from approximately 10 to 60 samples per second while improving data alignment and recording format.
- Built data-quality filtering, task segmentation, inference, and experiment-recording workflows to evaluate resolution, dataset size, and scene effects.
- Compared official, team, and custom action definitions, supporting RELATIVE Action and exploring RTRS real-time control.

## Control Constraints

VR poses and buttons are mapped to virtual and physical robot commands with speed and workspace limits to keep operation within the usable range.
