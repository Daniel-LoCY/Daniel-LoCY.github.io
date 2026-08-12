---
title: "TM5S Web Remote Control and Live Monitoring"
description: "A ROS 2, FastAPI, and WebSocket platform integrating TM5S operation, robot feedback, camera streams, and MoveIt trajectories."
featured_image: "/images/projects/default-project.svg"
tags: ["TM5S", "ROS 2", "FastAPI", "React", "WebSocket"]
weight: 6
---

This platform lowers the barrier to live TM5S operation and status inspection by exposing remote control and monitoring in a browser. It handles interactive control and telemetry, not the automated script orchestration provided by the separate workflow platform.

## Scope and Architecture

- Independently developed from scratch, with the first version completed in approximately one week and connected to one physical TM5S.
- Built the frontend with React, TypeScript, Vite, and Material UI, and connected the backend to ROS 2 through FastAPI, `rclpy`, and WebSocket.
- Used Docker and Nginx to define deployment boundaries between the browser interface and robot-control process.

## Control Capabilities

- Joint-angle and Cartesian-target control.
- TM Script, I/O, events, and reusable pose or motion presets.
- MoveIt trajectory planning and execution, plus direct access to required TM control commands.

## Live Monitoring

- Robot feedback, joint state, tool pose, control state, and connection status.
- Camera streams, FPS, resolution, and image-source information.
- ROS 2 nodes, topics, and related runtime information for checking control and data paths.

The core value is simpler remote control and monitoring. It is currently used mainly by me, and control latency, time savings, and long-duration stability have not been formally measured, so no speculative metric is presented.
