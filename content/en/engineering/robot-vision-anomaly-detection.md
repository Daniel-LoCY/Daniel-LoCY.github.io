---
title: "Robot Vision and PatchCore Anomaly Detection"
description: "A perception and inspection workflow integrating RealSense, DOPE, AprilTag, hand-eye calibration, and PatchCore."
featured_image: "/images/projects/default-project.svg"
tags: ["RealSense", "DOPE", "OpenCV", "AprilTag", "PatchCore", "ROS 2"]
weight: 4
---

This project covers both the 3D vision required for robot manipulation and image anomaly detection for inspection. The focus was turning model outputs into traceable, testable, and integrable engineering workflows.

## Robot Vision

- Integrated DOPE pose prediction with ROS 2 from image input and pose output through TF conversion and grasp-target calculation.
- Built Eye-in-Hand and Eye-to-Hand hand-eye calibration workflows.
- Tested checkerboards and OpenCV calibration algorithms to analyze translation and rotation error sources.
- Used RealSense, AprilTag, and OpenCV for image acquisition, localization, and coordinate conversion.

## Anomaly Detection

- Developed a PatchCore API server and PyQt interface.
- Added ROI extraction, resize, crop, normalize, clip, template replacement, and anomaly-score evaluation.
- Compared normal images, reflections, small defects, and different scenes to identify false-positive conditions and tune preprocessing.
