#!/usr/bin/env bash

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
image_name="daniel-resume-builder"
user_id="$(id -u):$(id -g)"

docker build --pull=false -f "$repo_root/resume/Dockerfile" -t "$image_name" "$repo_root"
docker run --rm --user "$user_id" -v "$repo_root:/workspace" \
  "$image_name" python /workspace/resume/generate_resume.py
docker run --rm --user "$user_id" -v "$repo_root:/workspace" \
  "$image_name" python -m unittest discover -s /workspace/resume/tests -v
