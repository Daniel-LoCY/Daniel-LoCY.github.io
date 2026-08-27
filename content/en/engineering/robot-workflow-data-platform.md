---
title: "Robot Workflow Automation and Recording Integration"
description: "A two-part automation and recording flow using ROS 2, WebSocket, and related interfaces to collect imitation-learning / GR00T / VLA training data fully automatically at 3–4× the manual volume, reducing manual staffing needs by two operators."
featured_image: "/images/projects/default-project.svg"
tags: ["Robot Workflow", "ROS 2", "WebSocket", "React Flow", "FastAPI", "Docker"]
weight: 5
---

This flow has two cooperating parts: an automated workflow that runs scripts and controls the robot arm and task sequence, plus a recording system that captures actions, images, robot state/actions, and timestamps. They exchange control, state, and recording events through ROS 2, WebSocket, and related interfaces, enabling fully automated recording of multiple imitation-learning / GR00T / VLA training episodes. This is distinct from the separate web platform built for live control and monitoring.

## Scope and Ownership

- Independently designed and developed from scratch, with the first usable version completed in approximately four weeks.
- Owned requirements, architecture, frontend and backend implementation, robot-control integration, Docker deployment, testing, and maintenance.
- The recording platform was an existing external system. I contributed to it and integrated automated workflow execution, robot control, recording status, and the cross-system interfaces.

## System Design

- The automation side used Next.js and React Flow to compose scripts, actions, conditions, waits, retries, and scene-reset steps for robot-arm control.
- The recording side captured actions, images, robot state/actions, and timestamps as multiple episodes for imitation-learning / GR00T / VLA training.
- Connected robot control, workflow state, and recording events through ROS 2, FastAPI, WebSocket, and configurable workflow steps.
- Supported pause, stop, and retry during execution while reporting the active node, status, errors, and saved-data count to the interface.

## Tasks and Results

- Integrated four pick-and-place task variants plus scene reset before and after recording.
- Once a task is configured, later runs complete without continuous manual intervention.
- Collected approximately 3–4× as much data as manual operation in the same time window, reducing manual staffing needs by two operators.
- Recording covered 30 FPS images and 60 Hz robot state/actions, with episodes of approximately 100–600 timesteps depending on the task.

Task success rate and cumulative run count have not been formally measured, so the public result is limited to the observed and confirmed data-collection multiplier.
