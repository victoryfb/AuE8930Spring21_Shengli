# Assignments of AuE8930 Autonomy

This project is used to save assignments of AuE8930 Autonomy.

## About Me

I'm [Shengli Xu](https://www.linkedin.com/in/shengli-xu-8471a618b/), a Ph.D. student working with Dr. Rai at CU-ICAR. Intelligent control based on Deep Learning is my current research topic due to my academic background of Control Engineering.

## Description

A single **git_ws** folder which contains all assignments is maintained. The structure of the project is shown below.

```
📦git_ws
┣ 📂src
┃ ┣ 📂assignment2
┃ ┃ ┣ 📂screenshots
┃ ┃ ┃ ┣ 📜assignment2_circle.gif
┃ ┃ ┃ ┣ 📜assignment2_square_closedloop.gif
┃ ┃ ┃ ┗ 📜assignment2_square_openloop.gif
┃ ┃ ┣ 📂src
┃ ┃ ┃ ┣ 📂launch
┃ ┃ ┃ ┃ ┣ 📜circle.launch
┃ ┃ ┃ ┃ ┣ 📜square_closedloop.launch
┃ ┃ ┃ ┃ ┗ 📜square_openloop.launch
┃ ┃ ┃ ┗ 📂scripts
┃ ┃ ┃ ┃ ┣ 📜circle.py
┃ ┃ ┃ ┃ ┣ 📜square_closedloop.py
┃ ┃ ┃ ┃ ┗ 📜square_openloop.py
┃ ┃ ┣ 📂videos
┃ ┃ ┃ ┣ 📜assignment2_circle.mp4
┃ ┃ ┃ ┣ 📜assignment2_square_closedloop.mp4
┃ ┃ ┃ ┗ 📜assignment2_square_openloop.mp4
┃ ┃ ┣ 📜CMakeLists.txt
┃ ┃ ┣ 📜README.md
┃ ┃ ┗ 📜package.xml
┃ ┣ 📂assignment3_turtlebot3
┃ ┃ ┣ 📂screenshots
┃ ┃ ┃ ┣ 📜TurtleBot3_move_in_circle.gif
┃ ┃ ┃ ┣ 📜TurtleBot3_move_in_square.gif
┃ ┃ ┃ ┗ 📜emergency_braking.gif
┃ ┃ ┣ 📂src
┃ ┃ ┃ ┣ 📂launch
┃ ┃ ┃ ┃ ┣ 📜emergency_braking.launch
┃ ┃ ┃ ┃ ┗ 📜move.launch
┃ ┃ ┃ ┣ 📂scripts
┃ ┃ ┃ ┃ ┣ 📜circle.py
┃ ┃ ┃ ┃ ┣ 📜emergency_braking.py
┃ ┃ ┃ ┃ ┗ 📜square.py
┃ ┃ ┃ ┗ 📂worlds
┃ ┃ ┃ ┃ ┣ 📜empty.world
┃ ┃ ┃ ┃ ┗ 📜turtlebot3_wall.world
┃ ┃ ┣ 📂videos
┃ ┃ ┃ ┣ 📜TurtleBot3_move_in_circle.mp4
┃ ┃ ┃ ┣ 📜TurtleBot3_move_in_square.mp4
┃ ┃ ┃ ┗ 📜emergency_braking.mp4
┃ ┃ ┣ 📜CMakeLists.txt
┃ ┃ ┣ 📜README.md
┃ ┃ ┗ 📜package.xml
┗ 📜.catkin_workspace
```

## Getting started

### Prerequisites

- Ubuntu 20.04
- Ros Noetic
- ROS1
- TurtleBot3 packages
- Gazebo
- ROS Gazebo package
- Python3
- git

### Clone the project

```bash
$ git clone git@github.com:victoryfb/AuE8930Spring21_Shengli_Xu.git
```

### Build code in a catkin workspace `git_ws`

```bash
$ cd ./AuE8930Spring21_Shengli_Xu/git_ws
$ catkin_make
$ source ./git_ws/devel/setup.bash
```

### Run assignment

Details can be found in each assignment.
