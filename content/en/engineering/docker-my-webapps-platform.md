---
title: "Dockerized Personal Multi-purpose Workspace"
description: "A private media and workflow platform built with React, FastAPI, and Docker."
featured_image: "/images/projects/default-project.svg"
tags: ["Docker", "React", "FastAPI", "FFmpeg", "yt-dlp", "SQLite"]
weight: 35
---

This is a Docker Compose-based personal workspace that brings media downloading, processing, document conversion, asset management, and private data features behind one Web entry point.

## System composition

- A React Web UI and PWA entry point with dark and light themes.
- A FastAPI backend for accounts, permissions, job orchestration, and feature APIs.
- yt-dlp for source resolution and FFmpeg for transcoding and media processing.
- Docker Compose services for the frontend, backend, and file browser, with separate dev and prod modes.

## Key capabilities

- Video downloads, playlist handling, format conversion, trimming, merging, frame extraction, thumbnails, and speed adjustment.
- Live visual adjustments and output, including temperature, brightness, contrast, saturation, blur, sharpening, background removal, and watermarks.
- HLS / DASH output, RTMP / SRT / UDP streaming, background jobs, and callback support.
- MarkItDown document conversion, GitHub image-asset management, and per-account SQLite finance data isolation.

## Engineering focus

- Scoped video workspaces and data isolation, with validation, authorization, and consistent error handling at API boundaries.
- Service-status checks so the home screen can detect whether other self-hosted services are available.
- Background media jobs that keep long-running processing separate from Web API responses.

## Showcase boundary

This is a private self-hosted platform. The portfolio exposes the architecture, technical decisions, and public feature summary without publishing internal URLs, accounts, files, or personal finance data.
