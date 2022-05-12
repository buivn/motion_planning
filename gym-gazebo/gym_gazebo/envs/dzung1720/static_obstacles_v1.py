# In this environment, there are two kind of reset functions.
    # self.reset: the robot is still the same predefined position after resetting
    # self.reset_2:  robot's pose will be changed after resetting

import gym
import rospy
import roslaunch
import time
import numpy as np

from gym import utils, spaces
from gym_gazebo.envs import gazebo_env
from gym.utils import seeding

from std_srvs.srv import Empty
from std_msgs.msg import Empty as empty1
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry


import tf
# for the ground truth
from gazebo_msgs.srv import GetModelState
from gazebo_msgs.srv import SetModelState
from gazebo_msgs.msg import ModelState


class Static_Obstacles_Env_v1(gazebo_env.GazeboEnv):

    def __init__(self):
        # Launch the simulation with the given launchfile name
        gazebo_env.GazeboEnv.__init__(self, "Static_Obstacles_Env_v1.launch")
        self.vel_pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=5)
        self.reset_odom_pub = rospy.Publisher('/mobile_base/commands/reset_odometry', empty1, queue_size=10)
        self.unpause = rospy.ServiceProxy('/gazebo/unpause_physics', Empty)
        self.pause = rospy.ServiceProxy('/gazebo/pause_physics', Empty)
        self.reset_proxy = rospy.ServiceProxy('/gazebo/reset_simulation', Empty)
        self.set_model_state = rospy.ServiceProxy("gazebo/set_model_state", SetModelState)
        self.get_ground_truth = rospy.ServiceProxy("gazebo/get_model_state", GetModelState)
        self.target = [4.0, -3.2]
        self.reward_range = (-np.inf, np.inf)

        self._seed()

    def calculate_observation(self, data, pos):
        min_range = 0.2
        done1 = False  # check for collision
        done2 = False   # check of reaching the target
        # done =False
        # if the robot is too close to any point around, terminate/done=True
        for i, item in enumerate(data.ranges):
            if (min_range > data.ranges[i] > 0):
                done1 = True

        delta_x = self.target[0] - pos.pose.pose.position.x
        delta_y = self.target[1] - pos.pose.pose.position.y
        # reach the target
        if (abs(delta_x) < 0.3) and (abs(delta_y) < 0.3):
            done2 = True

        # if done1 or done2:
        #     done = True
        data1 = list(data.ranges)
        # data1 = data1 +delta_x
        # for ii in range(2):
        # data1.append(delta_x)
        # data1.append(delta_y)
        # data1.append(abs(delta_x))
        # data1.append(abs(delta_y))
                       
        # data1 = data1 +delta_y
        return data1, done1, done2

    def _seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        # block until a service is available
        # print ("/gazebo/unpause_physics service call failed----------------")
        rospy.wait_for_service('/gazebo/unpause_physics')
        try:
            self.unpause()
        except (rospy.ServiceException) as e:
            print ("/gazebo/unpause_physics service call failed")

        max_ang_speed = 0.3
        ang_vel = (action-10)*max_ang_speed*0.1 #from (-0.33 to + 0.33)

        vel_cmd = Twist()
        vel_cmd.linear.x = 0.2
        vel_cmd.angular.z = ang_vel
        self.vel_pub.publish(vel_cmd)

        data = None
        pos = None
        while data is None:
            try:
                # create a new subscription to the topic, receive one message, then unsubscribe
                data = rospy.wait_for_message('/scan', LaserScan, timeout=5)
            except:
                pass

        while pos is None:
            try:
                # create a new subscription to the topic, receive one message, then unsubscribe
                pos = rospy.wait_for_message('/odom', Odometry, timeout=5)
            except:
                pass
        # block until a service is available
        rospy.wait_for_service('/gazebo/pause_physics')
        try:
            #resp_pause = pause.call()
            self.pause()
        except (rospy.ServiceException) as e:
            print ("/gazebo/pause_physics service call failed")

        state, done1, done2 = self.calculate_observation(data, pos)

        if done1:
            reward = -200.0
        elif done2:
            reward = 100.0
        else:
            reward = -0.5
            
        done = done1 or done2

        return np.asarray(state), reward, done, {}

    def reset(self):
        # Reset odometry
        
        # self.reset_odom_pub.publish(empty1())
        # Resets the state of the environment and returns an initial observation.
        rospy.wait_for_service('/gazebo/reset_simulation')
        try:
            #reset_proxy.call()
            self.reset_proxy()
            self.reset_odom_pub.publish(empty1())
        except (rospy.ServiceException) as e:
            print ("/gazebo/reset_simulation service call failed")

        
        # Unpause simulation to make observation
        rospy.wait_for_service('/gazebo/unpause_physics')
        try:
            #resp_pause = pause.call()
            self.unpause()
        except (rospy.ServiceException) as e:
            print ("/gazebo/unpause_physics service call failed")
        #read laser data
        data = None
        while data is None:
            try:
                data = rospy.wait_for_message('/scan', LaserScan, timeout=5)
            except:
                pass
        pos = None
        while pos is None:
            try:
                # create a new subscription to the topic, receive one message, then unsubscribe
                pos = rospy.wait_for_message('/odom', Odometry, timeout=5)
                # ROS_INFO("the current position is: ", pos.pose)
            except:
                pass
        rospy.wait_for_service('/gazebo/pause_physics')
        try:
            #resp_pause = pause.call()
            self.pause()
        except (rospy.ServiceException) as e:
            print ("/gazebo/pause_physics service call failed")

        state, done1, done2 = self.calculate_observation(data, pos)

        return np.asarray(state)

    def reset_2(self):
        print("Wait for GET service ....")
        rospy.wait_for_service("gazebo/get_model_state")

        # # Resets the state of the environment and returns an initial observation.
        rospy.wait_for_service('/gazebo/reset_simulation')
        try:
            self.reset_proxy()
            
        except (rospy.ServiceException) as e:
            print ("/gazebo/reset_simulation service call failed")

        # Pause simulation to adjust the robot
        # rospy.wait_for_service('/gazebo/pause_physics')
        # try:
        #     self.pause()
        # except (rospy.ServiceException) as e:
        #     print ("/gazebo/unpause_physics service call failed")
        
        rospy.wait_for_service("gazebo/set_model_state")
        self.model_state = ModelState()
        self.model_state.model_name = "mobile_base"
        self.model_state.pose.position.x = 1.0
        self.set_model_state(self.model_state)
        self.reset_odom_pub.publish(empty1())

        # Unpause simulation to make observation
        # rospy.wait_for_service('/gazebo/unpause_physics')
        # try:
        #     self.unpause()
        # except (rospy.ServiceException) as e:
        #     print ("/gazebo/unpause_physics service call failed")
        
        # data = None
        # while data is None:
        #     try:
        #         data = rospy.wait_for_message('/scan', LaserScan, timeout=5)
        #     except:
        #         pass
        # pos = None
        # while pos is None:
        #     try:
        #         # create a new subscription to the topic, receive one message, then unsubscribe
        #         pos = rospy.wait_for_message('/odom', Odometry, timeout=5)
        #         # ROS_INFO("the current position is: ", pos.pose)
        #     except:
        #         pass
        # rospy.wait_for_service('/gazebo/pause_physics')
        # try:
        #     #resp_pause = pause.call()
        #     self.pause()
        # except (rospy.ServiceException) as e:
        #     print ("/gazebo/pause_physics service call failed")

        # state, done1, done2 = self.calculate_observation(data, pos)

        # return np.asarray(state)
