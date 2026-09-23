---
title: "Robot Workflow Automation and Recording Integration"
description: "An AI and robotics workflow and recording platform built with ROS 2, WebSocket, React Flow, FastAPI, and Docker."
featured_image: "/images/projects/default-project.svg"
tags: ["Robot Workflow", "ROS 2", "WebSocket", "React Flow", "FastAPI", "Docker"]
weight: 5
---

This flow integrates automated task execution, robot control, and data recording through ROS 2, WebSocket, and related interfaces for AI / VLA data workflows. It is distinct from the separate web platform built for live control and monitoring.

## Scope and Ownership

- Owned requirements, architecture, frontend and backend implementation, robot-control integration, Docker deployment, testing, and maintenance.
- Integrated automated workflow execution, robot control, data recording, and cross-system interfaces.

## System Design

- Used Next.js and React Flow to compose and monitor robot-task workflows.
- Connected robot control, workflow state, and data recording through ROS 2, FastAPI, WebSocket, and Docker.
- Supported AI / VLA data collection through repeatable workflow execution.

## Tasks and Results

- Integrated multiple robot-task variants and recording flows, reaching approximately 3-4x the manual data volume in the same time window and reducing manual staffing needs by two operators.
- Provided repeatable execution and clear workflow status for later maintenance; cable-insertion success improved from 70% to 90% in a related robotics task.

The workflow demonstrates practical integration across robot control, task orchestration, and AI data collection.
