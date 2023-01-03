#!/bin/bash
#SPDX-FileCopyrightText: 2022 Ikuo Shige                                                         
#SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
#timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log
#gnome-terminal -- bash -c "run.bash"
echo "read" > "option.txt"
gnome-terminal -- bash -c "bash run_1.bash"
gnome-terminal -- bash -c "bash run_2.bash"
sleep 10
cat /tmp/mypkg.log | grep 'you win'