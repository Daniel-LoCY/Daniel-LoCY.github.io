---
title: "Home Assistant / ESPHome IoT Stack"
description: "A Docker-managed IoT platform combining Home Assistant, ESPHome, MQTT, and configuration consistency tooling."
featured_image: "/images/projects/default-project.svg"
tags: ["Docker", "Home Assistant", "ESPHome", "MQTT", "ESP32", "Python"]
weight: 36
---

This is a Docker-managed smart-home and IoT environment that combines Home Assistant, ESPHome, and the Mosquitto MQTT broker into a persistent service stack.

## System composition

- Home Assistant for device integration, automation, and state management.
- ESPHome for ESP-device configuration, compilation, and management.
- Mosquitto for MQTT messaging between sensors and automation workflows.
- Compose bind mounts that preserve Home Assistant, ESPHome, and MQTT configuration, data, and logs.

## Reliability design

- Host networking supports local-network discovery and IoT scenarios that require same-network communication.
- `ha_esphome_config_guard.py` continuously checks Home Assistant ESPHome config entries.
- Host / port drift is reconciled automatically, with a restart cooldown to reduce repeated restarts.
- Backup, container startup, syntax checks, and troubleshooting steps are documented as a reproducible rebuild workflow.

## Engineering focus

- Managing the boundaries between containers, local networking, device services, and persistent configuration.
- Turning real-world IP / port drift into an observable and recoverable reconciliation flow.
- Treating IoT automation as an operable system that can be rebuilt and maintained, not only a one-off demo.

## Showcase boundary

This is a private hardware and home-service environment. The portfolio describes the system design and engineering approach without publishing device identifiers, private network addresses, credentials, or personal automation data.
