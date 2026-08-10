---
title: "Multi-stack Docker Self-hosted Service Platform"
description: "A private service platform integrating deployment scripts, Nginx, Authelia, and Tailscale."
featured_image: "/images/projects/default-project.svg"
tags: ["Docker", "Nginx", "Authelia", "Tailscale", "n8n", "Portainer"]
weight: 37
---

This Docker workspace organizes multiple self-hosted services into an operable multi-stack platform. A unified deployment entry point, reverse proxy, and authorization checks connect workflow automation with personal Web tools.

## Platform composition

- Root-level `deploy.sh` and `Makefile` handle up, down, restart, build, logs, and ps operations.
- Authelia and Nginx provide a protected service entry point that routes requests to n8n, Portainer, OXWU, THSRC, and other internal services.
- A route registry and generator keep Nginx routing decisions centralized and reduce drift between hand-written configurations.
- Tailscale separates a public Funnel gateway from private Serve listeners, preserving different access boundaries for each service.

## Operations and reliability

- Dev / prod modes and targeted Stack / service operations are supported.
- Host ports are checked before startup; if a preferred port is occupied, an available port is selected and recorded for subsequent Compose runs.
- Deployment output reports the effective service entry points and status, while per-stack logs, restart, and rollback paths remain available.
- Home Assistant, the media platform, the ticket-booking Web UI, Portainer, n8n, and OXWU follow the same operational workflow.

## Engineering focus

- Clear boundaries between container lifecycle, network entry, authorization, routing, and service status.
- Configuration and scripts reduce manual deployment errors without hard-coding sensitive values into public content.
- Explicit fallback and verification points for the exposure, Tailnet access, and authentication of internal services.

## Verifiable engineering evidence

- Route output is validated through a route registry, generator, and Nginx syntax checks; services not present in the allowlist are not automatically exposed through the public gateway.
- The August 2026 operations audit added reproducibility and security evidence: Docker images with trusted digests were pinned where verifiable, while dynamic Docker DNS upstreams, Compose config, health checks, and HTTP smoke tests were validated.
- A concrete rollback path remains available through per-stack or per-service rebuild, logs, and restoration of route / port configuration instead of manual edits inside containers.

## Showcase boundary

This is private self-hosted infrastructure. The portfolio presents the architecture and operational practices without publishing the actual hostname, internal ports, accounts, tokens, or service data.
