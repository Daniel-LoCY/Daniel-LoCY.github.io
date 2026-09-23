---
title: "Virtual and Physical Robot VR Teleoperation and Digital Twin Data Pipeline"
description: "A VR teleoperation and Digital Twin workflow for virtual / physical robot operation and GR00T / VLA data collection."
featured_image: "/images/projects/default-project.svg"
tags: ["VR Teleoperation", "Digital Twin", "NVIDIA Isaac GR00T", "ROS 2"]
weight: 2
---

This system provides VR teleoperation and a Digital Twin data flow for robot arms in Isaac Sim and on physical robot hardware. It then connects to a recording platform to produce demonstration data for imitation learning and NVIDIA Isaac GR00T.

## Control Flow

- Converted VR control input into robot operation targets.
- Connected the teleoperation workflow to both Isaac Sim and physical robot hardware for simulation and physical validation.

## Recording Integration

- Integrated teleoperation data and camera images in the recording platform.
- Supported demonstrations from simulated and physical environments for imitation learning and GR00T / VLA training.
- Established a repeatable multi-source recording workflow.

## Validation Status

The system was validated in both simulated and physical environments and supports repeatable data collection and analysis.
