---
title: "TM5S Web Remote Control and Live Monitoring"
description: "A ROS 2, FastAPI, React, and WebSocket platform for TM5S remote control and live monitoring."
featured_image: "/images/projects/default-project.svg"
tags: ["TM5S", "ROS 2", "FastAPI", "React", "WebSocket"]
weight: 6
---

This platform exposes TM5S remote control and live monitoring in a browser, focusing on robot operation, camera streams, and system status. Automated script orchestration is handled by a separate workflow platform.

## Scope and Architecture

- Independently developed and connected to a physical TM5S.
- Built the frontend with React, TypeScript, Vite, and Material UI, and connected the backend to ROS 2 through FastAPI, `rclpy`, and WebSocket.
- Used Docker and Nginx to organize service boundaries and deployment.

## Control Capabilities

- Robot control, reusable actions, and control-command integration.
- MoveIt trajectory planning and execution.

## Live Monitoring

- Robot feedback, control state, and connection status.
- Camera streams and ROS 2 runtime information for operation and troubleshooting.

The platform combines browser-based robot control, camera streams, feedback, and ROS 2 runtime information in one operational interface.
