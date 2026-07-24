---
title: "YOLO OBB Visual-Guided HDMI Insertion"
description: "A TM5S insertion workflow using YOLO OBB and visual servoing to locate, align, and insert HDMI connectors."
featured_image: "/images/projects/default-project.svg"
tags: ["TM5S", "TM Flow", "TM API", "ROS 2", "YOLO OBB", "OpenCV"]
weight: 1
---

This workflow combines object detection, camera geometry, and robot control so that a wrist-mounted camera can iteratively align with an HDMI port before executing the insertion motion.

## My Contributions

- Used YOLO OBB to detect HDMI port centers and rotation poses.
- Controlled the TM5S wrist camera through translation, rotation, and synchronized multi-axis alignment.
- Estimated relative distance from camera intrinsics, principal-point offset, focal length, detected-box size, and the physical HDMI dimensions.
- Tuned motion increments and rotation-error thresholds to reduce repeated corrections and improve the insertion flow.

## Technical Focus

- Read focal length, image dimensions, camera matrix, and distortion coefficients through the EIH Camera API.
- Converted visual detections into executable robot-control targets.
- Connected TM Flow, TM API, and ROS 2 for perception, control, and workflow-state integration.
