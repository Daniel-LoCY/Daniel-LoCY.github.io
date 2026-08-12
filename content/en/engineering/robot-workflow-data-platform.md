---
title: "Robot Workflow Automation and Recording Integration"
description: "A 34-node workflow platform for robot tasks, scene reset, and recording that collects 3–4× as much data as manual operation in the same time window."
featured_image: "/images/projects/default-project.svg"
tags: ["Robot Workflow", "ROS 2", "React Flow", "FastAPI", "Docker"]
weight: 5
---

This platform turns repetitive manual robot tasks into configurable and repeatable automation. Its purpose is automated script execution and data collection, which is distinct from the separate web platform built for live control and monitoring.

## Scope and Ownership

- Independently designed and developed from scratch, with the first usable version completed in approximately four weeks.
- Owned requirements, architecture, frontend and backend implementation, robot-control integration, Docker deployment, testing, and maintenance.
- The recording platform was an existing external system. I contributed to it and integrated workflow execution, robot control, and recording status.

## System Design

- Built a graph-based editor with Next.js and React Flow for composing actions, conditions, waits, retries, recording, and scene-reset steps.
- Used FastAPI for workflow definitions, the execution queue, runners, state events, and live WebSocket updates.
- Implemented 34 workflow node types spanning robot arms, grippers, task control, recording, and flow logic.
- Supported pause, stop, and retry during execution while reporting the active node, status, errors, and saved-data count to the interface.

## Tasks and Results

- Integrated four pick-and-place task variants plus scene reset before and after recording.
- Once a task is configured, later runs complete without continuous manual intervention.
- Collected approximately 3–4× as much data as manual operation in the same time window.
- Recording covered 30 FPS images and 60 Hz robot state/actions, with episodes of approximately 100–600 timesteps depending on the task.

Task success rate and cumulative run count have not been formally measured, so the public result is limited to the observed and confirmed data-collection multiplier.
