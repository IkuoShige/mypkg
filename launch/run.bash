#!/bin/bash
gnome-terminal -- bash -c "ros2 run mypkg hit_and_blow_B; echo Press a key... close the window; read -n1"
gnome-terminal -- bash -c "ros2 run mypkg hit_and_blow; echo Press a key... close the window; read -n1"
