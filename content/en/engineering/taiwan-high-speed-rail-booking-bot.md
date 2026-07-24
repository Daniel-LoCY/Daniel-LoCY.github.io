---
title: "Taiwan High Speed Rail Ticket Booking Bot"
description: "An automation bot that simulates user actions to complete rail ticket booking."
featured_image: "/images/projects/default-project.svg"
tags: ["Python", "Selenium", "Browser Automation"]
weight: 100
---

An automation project designed to handle repetitive ticket booking steps through browser control.

## Highlights

- Automated login and ticket booking flows.
- Simulated user interactions with Selenium.
- Focused on reliable sequence control for web automation.

## Dockerized Deployment

- Wrapped the original booking project as an independently managed Web service with Docker Compose.
- Kept the original source mounted read-only while separating configuration and browser-extension state.
- Supported Headless and AutoVerify flows by default, with `/status.json` exposing the latest job and booking result.
