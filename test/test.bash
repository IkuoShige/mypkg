#!/bin/bash
#SPDX-FileCopyrightText: 2022 Ikuo Shige                                                         
#SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。


cd $dir/ros2_ws
#cd $dir/robo_sys/ros2_ws
colcon build
source $dir/.bashrc
#timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log
#gnome-terminal -- bash -c "run.bash"
cd src/mypkg/test/
echo "read" > "option.txt"
ls option.txt
#gnome-terminal -- bash -c "bash run_1.bash"
#gnome-terminal -- bash -c "ros2 run mypkg hit_and_blow_B < 'input.txt' > '/tmp/mypkg.log'"
ros2 run mypkg hit_and_blow_B < 'input.txt' > '/tmp/mypkg.log'
sleep 1
ros2 run mypkg hit_and_blow < 'input.txt'
#gnome-terminal -- bash -c "ros2 run mypkg hit_and_blow < 'input.txt'"
#gnome-terminal -- bash -c 'bash run_2.bash'
#rm "option.txt"
#cat option.txt
sleep 10
cat /tmp/mypkg.log | grep 'you win'