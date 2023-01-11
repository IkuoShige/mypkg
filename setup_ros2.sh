cd
git clone https://github.com/ryuichiueda/ros2_setup_scripts
cd ros2_setup_scripts
./setup.bash
echo "source ~/ros2_ws/install/setup.bash" >> ~/.bashrc
echo "source ~/ros2_ws/install/local_setup.bash" >> ~/.bashrc
source ~/.bashrc
cd
mkdir -p ros2_ws/src
cd ~/ros2_ws/src/
git clone https://github.com/IkuoShige/mypkg.git
git clone https://github.com/IkuoShige/hit_and_blow_msgs.git
cd ~/ros2_ws/
sudo rosdep install -i --from-path src --rosdistro foxy -y
rosdep update
colcon build
