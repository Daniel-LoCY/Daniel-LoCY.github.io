---
title: "NVIDIA Isaac GR00T N1.7: VLA Policy Training and Physical-Robot Inference"
description: "An end-to-end workflow covering robot-data conversion, GR00T N1.7 training, policy inference, and physical-robot control integration."
featured_image: "/images/projects/default-project.svg"
tags: ["NVIDIA Isaac GR00T", "VLA", "Digital Twin Data", "Robot Data", "Policy Inference"]
weight: 1
---

This project connects robot data collected separately from simulated and physical environments to NVIDIA Isaac GR00T N1.7 data conversion, model training, policy inference, and physical-robot execution. My core responsibility was robot control and end-to-end system integration rather than only one data or modeling step.

The project separately validates two workflows: training with simulated data followed by inference in the physical environment, and training plus inference with physical-environment data. These were not run as one simultaneous mixed-data training process.

## Scope and Ownership

- Completed the end-to-end path from data conversion and model training to inference and physical-robot testing.
- Owned robot control, policy-service integration, action mapping, and the physical inference path.
- The recording platform was a separate system; I contributed to its development and integrated robot control and workflow automation with it.

## End-to-End Data and Inference Flow

1. Build episodes from dual-camera images, robot state, gripper state, and control actions.
2. Record images at 30 FPS and robot state/actions at 60 Hz, align them by timestamp, and organize episodes of approximately 100–600 timesteps.
3. Convert position, pose, Rotation 6D, and action definitions into the GR00T N1.7 training format, then train and evaluate checkpoints through inference.
4. Send observations to a policy service, map returned model actions into executable robot commands, and validate the physical-robot path.

## Engineering Focus

- Defined explicit contracts for images, robot state, actions, and timestamps to handle synchronization across sources with different rates.
- Reconciled ABSOLUTE/RELATIVE actions, Base/Tool frames, and Rotation 6D so training data and physical control retain the same semantics.
- Separated policy inference from robot output behind inspectable service boundaries, with a no-motion test mode before physical execution.
- Completed the full path for pick-and-place tasks. GR00T task development and stability validation are ongoing, so no unmeasured success-rate claim is presented.
