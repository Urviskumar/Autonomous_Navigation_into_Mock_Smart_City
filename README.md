# Autonomous Navigation
Autonomous navigation from scratch
More updates coming soon

# Introduction

<p align="justify">In this project, we advance one step ahead of our previous project, Autonomous Navigation Using Vision Only Mode. 
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

* Local obstacle avoidance

* Real-time video segmentation for lane tracking

* Traffic sign detection

* Indoor navigation and path planning using Nav2</P>

# Background

<p align="justify">In this project, we have presented a ROS-based autonomous navigation system for navigating a mock city. 
We aimed to replicate the complexities of real-world scenarios. Our setup includes traffic signs, both 
two-lane and single-lane roads, and the robot's ability to detect other robotic cars, making decisions 
based on the situation—such as stopping, turning, or moving straight when encountering traffic signs or other robots.</p>

## A Hardware Implementation
<p align="justify">Our robot is a wheeled-based Rosmaster R2 bot equipped with a differential drive system. 
We integrated the powerful Jetson Orin NX into our bot, and it is also equipped with an IMU, 2D YD LiDAR, 
and a ZED2 RGB-D camera with RGB-D data capture capability. </p>


## B. Software Implementation
<p align="justify">We utilized the following software libraries and tools:

* Yahboom car SDK: Ensures seamless integration with the Yahboom robotic hardware, providing necessary control functions and protocols.

* ZED SDK: Provided high-resolution images and depth data, crucial for object detection and distance estimation. 
Enabled accurate 3D mapping and environmental understanding.

* Jetson Orin NX with NVIDIA Jetpack 5.0: Served as the computational backbone, handling intensive data processing and
 model execution. Optimized for AI applications with GPU acceleration.

* YD LiDAR SDK: Facilitated precise distance measurements and environmental mapping, vital for obstacle detection and navigation.

* Ubuntu 20: Offered a stable and flexible operating system environment, compatible with ROS2 and other essential libraries.

* ROS2 Foxy: Enabled efficient system integration, data handling, and algorithm implementation. Provided a robust framework for robot control and communication.</p>
