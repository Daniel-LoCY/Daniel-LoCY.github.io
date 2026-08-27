---
title: "YOLO OBB Visual-Guided HDMI Insertion"
description: "A TM5S insertion workflow using YOLO OBB and visual servoing to locate, align, and insert HDMI connectors."
featured_image: "/images/projects/default-project.svg"
tags: ["TM5S", "TM Flow", "TM API", "ROS 2", "YOLO OBB", "OpenCV"]
weight: 4
---

This workflow combines YOLO OBB detection, OpenCV image and camera-geometry processing, and robot control so that a wrist-mounted camera can iteratively align with an HDMI port before executing the insertion motion.

## My Contributions

- Used YOLO OBB to detect HDMI port centers and rotation poses, with OpenCV handling image processing, camera intrinsics, and coordinate geometry.
- Controlled the TM5S wrist camera through translation, rotation, and synchronized multi-axis alignment.
- Estimated relative distance from camera intrinsics, principal-point offset, focal length, detected-box size, and the physical HDMI dimensions.
- Tuned motion increments and rotation-error thresholds to reduce repeated corrections and improve the insertion flow.

## Technical Focus

- Read focal length, image dimensions, camera matrix, and distortion coefficients through the EIH Camera API.
- Converted visual detections into executable robot-control targets.
- Connected TM Flow, TM API, and ROS 2 for perception, control, and workflow-state integration.

## Physical-Robot Validation

- Secondary visual calibration improved cable-insertion success from 70% to 90% across 10 trials in each stage.
- The recorded hand-eye calibration result was 6.82 mm mean position error and 0.40° mean angular error. This tracks calibration quality and is not presented as absolute accuracy for every scene.
