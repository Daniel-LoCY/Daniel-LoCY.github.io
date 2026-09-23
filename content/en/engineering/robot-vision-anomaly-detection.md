---
title: "Robot Vision and PatchCore Anomaly Detection"
description: "DOPE validation in Isaac Sim, physical perception with RealSense and AprilTag, and a PatchCore anomaly-detection workflow with API and PyQt interfaces."
featured_image: "/images/projects/default-project.svg"
tags: ["RealSense", "DOPE", "OpenCV", "AprilTag", "PatchCore", "ROS 2"]
weight: 9
---

This project covers both the 3D vision required for robot manipulation and image anomaly detection for inspection. The focus was turning model outputs into traceable, testable, and integrable engineering workflows.

## Robot Vision

- Evaluated DOPE pose prediction and its ROS 2 image-to-pose and TF flow in Isaac Sim using official data.
- Built Eye-in-Hand and Eye-to-Hand hand-eye calibration workflows.
- Tested checkerboards and OpenCV calibration algorithms to analyze translation and rotation error sources.
- Used RealSense and OpenCV for image acquisition and preprocessing, with AprilTag for unplugging-connector localization and coordinate conversion.

## Anomaly Detection

- Developed a PatchCore API server and PyQt interface.
- Added ROI extraction, resize, crop, normalize, clip, template replacement, and anomaly-score evaluation.
- Compared normal images, reflections, small defects, and different scenes to identify false-positive conditions and tune preprocessing.

The PatchCore implementation provides a traceable anomaly-detection workflow with API serving, PyQt interaction, ROI preprocessing, template replacement, and anomaly-score evaluation.
