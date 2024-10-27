# Autonomous Navigation
Autonomous navigation from scratch
More updates coming soon

# Introduction

In this project, we advance one step ahead of our previous project, Autonomous Navigation Using Vision Only Mode. 
Previously, we discussed the crucial role of Visual Odometry (VO) in autonomous robotic navigation, especially in 
GPS-denied environments such as planetary terrains or indoor robotic applications. Here, we implement autonomous 
navigation using sensor fusion techniques within a mock smart city that we built from scratch.

The main focus is to navigate the robot in indoor environments using built-in sensors such as cameras,
 LiDAR, and IMU. We have constructed a 3D mock smart city and developed our own custom-trained dataset 
 for lanes and traffic signs. Real-time video segmentation feeds are directly sourced from the ZED2 RGB-D data. 
 All setups have been implemented using ROS2 Foxy. Currently, we are working on implementing the path-planning 
 algorithm once we save the map inside the robot using SLAM. For this, we have employed the Cartographer SLAM 
 technique originally developed by Google.

We have introduced four typical application scenarios:

Local obstacle avoidance

Real-time video segmentation for lane tracking

Traffic sign detection

Indoor navigation and path planning