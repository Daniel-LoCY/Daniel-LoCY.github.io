---
title: "NVIDIA Isaac GR00T N1.7 Digital-Twin Data Platform"
description: "A multi-source data pipeline for robot, camera, gripper, and action data prepared for NVIDIA Isaac GR00T N1.7 training."
featured_image: "/images/projects/default-project.svg"
tags: ["Isaac Sim", "ROS 2", "RGB / Depth", "Robot State", "Action"]
weight: 6
---

This platform organizes multi-source data from simulated and physical robot tasks. It turns synchronization, quality checks, task segmentation, and format conversion into a repeatable workflow for Isaac GR00T N1.7 training and inference experiments.

## Data Covered

- Robot joint state, end-effector position, and pose.
- Gripper state, camera RGB/depth images, and control actions.
- Task, scene, and recording metadata from simulated and physical environments.

## My Contributions

- Built synchronization, quality-checking, task-segmentation, image-preprocessing, and structured-data export workflows.
- Aligned data formats and action definitions with the training requirements of Isaac GR00T N1.7.
- Handled Rotation 6D, ABSOLUTE/RELATIVE Action, and Base/Tool Frame differences.
- Supported data collection across tasks and scenes for later model training, inference testing, and sim-to-real validation.
