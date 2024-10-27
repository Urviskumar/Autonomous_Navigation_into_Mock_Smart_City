# Autonomous Navigation
Autonomous navigation from scratch
More updates coming soon

# Introduction

In this project we are moving one more step ahed of our previous projcet Autonomus navigation using vision only mode. In that we discussed how Visual Odometry (VO) is crucial for autonomous
robotic navigation, especially in GPS-denied environments like
planetary terrains or inddor robotic applications. Here we are imlementing the autonoomous navigation usen sensor fusion techinique into mock smart city taht we built from scratch. The project main focus is to navigate the robot into indoor environmnet using built in sensors such as camera , lidar and IMU. Till we have built the 3D mock smart city, using our own custom trained dataset of the lanes and traffic signs we have real time video segmentation feed directly coming from the ZED2 rgbd data. All setup has been done is ROS2 foxy. Currently we are trying to implement the path planing algorithm once we save the map inside robot using SLAM. For that we have been used cartographer slam technique originally developed by the google.

We have introduced 
four typical application scenarios: local obstacle avoidance, real time video segmentation for lane tracking, traffic sign detection , indoor navigation, and path planning.

Make sure you use technical words take it from publically availble research papers related to autonomous navigatio projects.
navigation.
Copilot
Introduction
In this project, we advance one step ahead of our previous project, Autonomous Navigation Using Vision Only Mode. Previously, we discussed the crucial role of Visual Odometry (VO) in autonomous robotic navigation, especially in GPS-denied environments such as planetary terrains or indoor robotic applications. Here, we implement autonomous navigation using sensor fusion techniques within a mock smart city that we built from scratch.

The main focus is to navigate the robot in indoor environments using built-in sensors such as cameras, LiDAR, and IMU. We have constructed a 3D mock smart city and developed our own custom-trained dataset for lanes and traffic signs. Real-time video segmentation feeds are directly sourced from the ZED2 RGB-D data. All setups have been implemented using ROS2 Foxy. Currently, we are working on implementing the path-planning algorithm once we save the map inside the robot using SLAM. For this, we have employed the Cartographer SLAM technique originally developed by Google.

We have introduced four typical application scenarios:

Local obstacle avoidance

Real-time video segmentation for lane tracking

Traffic sign detection

Indoor navigation and path planning