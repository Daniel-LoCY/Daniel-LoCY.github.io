---
title: "Credit Card Reward Comparison PWA"
description: "A live Taiwan credit-card reward comparison product built with Flutter, FastAPI, and PostgreSQL."
featured_image: "/images/projects/default-project.svg"
tags: ["Flutter", "Dart", "FastAPI", "PostgreSQL", "PWA", "Docker"]
weight: 25
---

This is a live Taiwan credit-card reward comparison product. Users enter a spending amount, merchant, and payment conditions; the system evaluates current-date card and campaign rules, exposes official sources, and ranks estimated rewards.

## Live Demo

[Open Card Guide](https://card.lolo-lab.com/)

## System composition

- Flutter provides shared Android, iOS, and Web interfaces. The Web build supports a PWA manifest, service worker, standalone display mode, and install prompt.
- A modular FastAPI monolith separates bank, credit-card, merchant, payment-method, reward-rule, recommendation, and user-report domains.
- PostgreSQL, SQLAlchemy, and Alembic manage the data model, migrations, and official-data synchronization results.
- Docker Compose manages the database, API, and Flutter Web. Nginx serves the Web app and proxies same-origin `/api` requests to the backend; production exposure uses Cloudflare Tunnel.

## Product capabilities

- Filter available rewards by spending amount, merchant, bank, card, and payment method.
- Calculate base rewards and campaigns with thresholds, dates, registration, or plan-specific conditions while preserving original units such as cash, points, and miles.
- Merge duplicate merchant campaigns while preserving card-specific conditions and official source links.
- Store “My Cards” and plan preferences locally with `shared_preferences`, without requiring an account.
- Provide an about / report page where users can report data issues; the backend stores the issue description and non-personal data-count snapshot only.

## Data reliability design

- The synchronization flow requires HTTPS official sources, fixed JSON schemas, date and condition validation, and bank / card / payment / merchant consistency checks.
- The LLM Collector is bounded to source retrieval and fixed-format validation; unvalidated model output is not published directly as public reward data.
- Campaign details and recommendation results expose official source URLs so users can verify terms with the issuing bank or campaign owner.

## Engineering focus

- Maintaining a consistent data flow across Flutter UI, FastAPI contracts, PostgreSQL schema, and Docker production deployment.
- Keeping clear domain boundaries in a modular monolith without prematurely splitting an MVP into microservices.
- Combining same-origin API proxying, PWA delivery, source disclosure, and product disclaimers so the tool can serve real users instead of remaining a demo.

## Verifiable engineering evidence

- Verification snapshot from 2026-08-08: Flutter `analyze`, 22 Flutter tests, Web release build, SEO contract verification, Nginx configuration checks, and HTTP smoke tests passed; backend pytest reported 40 passed.
- Data synchronization snapshot from 2026-07-21: 151 active cards and 413 active official campaign rules across 24 banks. This is a dated verification snapshot, not a current live count.
- The Web entry includes canonical, Open Graph, JSON-LD, indexable product, data-source, and privacy pages, with Docker rebuild verification for deployment behavior.

## Product limitations

The product provides a quick reward estimate, not a guarantee of final bank settlement. Campaign quotas, already-used caps, MCC classification, and changing terms can affect the result. The tool does not require login or collect card numbers or transaction records; the portfolio presents only public product behavior and engineering design.
