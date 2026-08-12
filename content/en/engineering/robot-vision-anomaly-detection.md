---
title: "Robot Vision and PatchCore Anomaly Detection"
description: "DOPE validation in Isaac Sim, physical perception with RealSense and AprilTag, and a PatchCore prototype not yet deployed to formal inspection."
featured_image: "/images/projects/default-project.svg"
tags: ["RealSense", "DOPE", "OpenCV", "AprilTag", "PatchCore", "ROS 2"]
weight: 9
---

This project covers both the 3D vision required for robot manipulation and image anomaly detection for inspection. The focus was turning model outputs into traceable, testable, and integrable engineering workflows.

## Robot Vision

- Evaluated DOPE pose prediction and its ROS 2 image-to-pose and TF flow in Isaac Sim using official data; this is not presented as a physical-robot result.
- Built Eye-in-Hand and Eye-to-Hand hand-eye calibration workflows.
- Tested checkerboards and OpenCV calibration algorithms to analyze translation and rotation error sources.
- Used RealSense, AprilTag, and OpenCV for image acquisition, localization, and coordinate conversion.

## Anomaly Detection

- Developed a PatchCore API server and PyQt interface.
- Added ROI extraction, resize, crop, normalize, clip, template replacement, and anomaly-score evaluation.
- Compared normal images, reflections, small defects, and different scenes to identify false-positive conditions and tune preprocessing.

PatchCore remains a development prototype. It has not been integrated into a formal inspection or production flow, and unmeasured AUROC, F1, or per-image inference time are not published.
