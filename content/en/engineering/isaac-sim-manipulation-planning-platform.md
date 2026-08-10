---
title: "Isaac Sim Robot Manipulation and Motion Planning"
description: "A robot simulation, collision-avoidance, and manipulation platform integrating Isaac Sim, ROS 2, MoveIt 2, and cuMotion."
featured_image: "/images/projects/default-project.svg"
tags: ["Isaac Sim", "ROS 2", "MoveIt 2", "cuMotion", "OMPL", "TRAC-IK"]
weight: 3
---

This environment uses Isaac Sim as the simulation core and connects ROS 2 with MoveIt 2/cuMotion to validate target poses, motion planning, collision handling, and object manipulation.

## My Contributions

- Implemented target-pose control, fixed-object grasping/placement, collision scenes, and dynamic collision-object updates.
- Implemented `Attach Object` so grasped objects become part of the planning collision model and do not cause later plans to fail around the gripper.
- Worked around the limitation of attaching Mesh objects by creating approximate collision spheres from the objects' actual poses.
- Extended the UR5 control architecture to TM5S through configuration-driven robot and gripper integration, supporting multiple equipment configurations.
- Moved arm and gripper parameters from hard-coded values into configuration files to reduce the cost of hardware changes.

## Technical Focus

Used URDF/USD/XRDF, OMPL, TRAC-IK, and KDL for robot models, kinematics, motion planning, and collision-related configuration.
