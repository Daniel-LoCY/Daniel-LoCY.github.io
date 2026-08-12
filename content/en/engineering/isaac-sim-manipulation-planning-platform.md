---
title: "TM5S Robot Control and Isaac Sim-to-Real Platform"
description: "A control, planning, and physical-validation environment connecting TM5S, Isaac Sim and Isaac Lab, ROS 2, MoveIt 2, and cuMotion."
featured_image: "/images/projects/default-project.svg"
tags: ["Isaac Sim", "ROS 2", "MoveIt 2", "cuMotion", "OMPL", "TRAC-IK"]
weight: 3
---

This sim-to-real environment centers on TM5S control and connects Isaac Sim and Isaac Lab, ROS 2, MoveIt 2, and cuMotion for target poses, motion planning, collision handling, manipulation, and real-robot tasks.

## My Contributions

- Implemented target-pose control, fixed-object grasping/placement, collision scenes, and dynamic collision-object updates.
- Implemented `Attach Object` so grasped objects become part of the planning collision model and do not cause later plans to fail around the gripper.
- Worked around the limitation of attaching Mesh objects by creating approximate collision spheres from the objects' actual poses.
- Built TM5S and Isaac Sim control and coordinate-conversion flows for pick-and-place, cable insertion/removal, and GR00T-related system integration.
- Moved arm and gripper parameters from hard-coded values into configuration files to reduce repeated setup across control, planning, and physical environments.

## Technical Focus

Used URDF/USD/XRDF, OMPL, TRAC-IK, and KDL for robot models, kinematics, planning, and collision configuration. MoveIt 2 and cuMotion were existing planning tools; my primary contribution was the control layer and end-to-end task integration.
