#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2022 Ikuo Shige                                                                                                           
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray, Int32
import geometry_msgs
from geometry_msgs.msg import Pose2D
import random
from person_msgs.msg import Person
import time

"""
class Subscribe_publishers():
    def __init__(self):
        # Subscriberを作成
        self.subscriber_b = rclpy.create_subscription(Pose2D, 'blue', self.callback_blue)
        #self.subscriber_r = rclpy.create_subscription(Pose2D, 'red', self.callback_red)
        #self.subscriber_g = rclpy.create_subscription(Pose2D, 'green', self.callback_green)
        # messageの型を作成
        self.message = Pose2D()

    def callback_blue(self, message):
        #print("callback!!!!!!!!!!!")
        global sub_blue
        sub_blue = message
        #print("sub_blue_x: "+str(sub_blue.x) + "sub_blue_y: "+ str(sub_blue.y))
        # callback時の処理
        #self.pub.make_msg(message)
        # publish
        #self.pub.send_msg()
"""
class Subscribe_publishers():
    def __init__(self, node):
        # Subscriberを作成
        self.subscriber_b = node.create_subscription(Person, "B", self.callback_answer, 10)
        print("sub")
        #self.subscriber_r = rclpy.create_subscription(Pose2D, 'red', self.callback_red)
        #self.subscriber_g = rclpy.create_subscription(Pose2D, 'green', self.callback_green)
        # messageの型を作成
        self.message = Person()

    def callback_answer(self, message):
        #print("callback!!!!!!!!!!!")
        global sub_blue
        sub_answer = message
        global answer_B, hit_B, blow_B, clear_B, turn
        answer_B = [sub_answer.answer[0],sub_answer.answer[1],sub_answer.answer[2]]
        hit_B, blow_B = sub_answer.answer[3],sub_answer.answer[4]
        clear_B = sub_answer.answer[5]
        turn = sub_answer.answer[6]
        print(answer_B)
        print(str(hit_B)+str(blow_B))
        print(clear_B)
        print(turn)
        # callback時の処理
        #self.pub.make_msg(message)
        # publish
        #self.pub.send_msg()

class Hit_And_Blow():
    def __init__(self, node):
        #self.pub = node.create_publisher(Int32MultiArray, "A", 10)
        self.pub_answer = node.create_publisher(Person, "A", 10)
        #self.pub_hit_and_blow = node.create_publisher(Person, "A", 10)
        self.n = 0
        #node.create_timer(0.5, self.call_back)
        #self.main()
        first = Person(answer=[a[0], a[1], a[2], 0, 0, 0, 0])
        print(first)
        self.pub_answer.publish(first)

    #def call_back(self):
    #    global msg
    #    msg = Person()
    #    #self.pub.publish(msg)

    def rand_ints_dup(self, a, b, k):
        return [random.randint(a, b) for i in range(k)]

    def rand_ints_nodup(self, a, b, k):
        ns = []
        while len(ns) < k:
            n = random.randint(a, b)
            if not n in ns:
                ns.append(n)
        return ns

    def main(self):
        global clear_A
        self.n = 0
        clear_A = 0
        global turn
        #time.sleep(5)
        #turn = 0
        #answer = Person()
        #a = [random.randint(0, 10) for i in range(3)]
        #a = self.rand_ints_nodup(0, 9, 3)
        #print(a)

        while self.n != 1:
            hit = 0
            blow = 0
            print("turn: "+ str(turn))
            if turn == 0:
                tmp_1 = int(input("1番目の数を入力してください: "))
                #print(Int32(tmp_1))
                #print(tmp_1)
                tmp_2 = int(input("2番目の数を入力してください: "))
                #answer.data[1] = tmp_2
                #print(tmp_2)
                tmp_3 = int(input("3番目の数を入力してください: "))
                #answer.data[2] = tmp_3
                #print(tmp_3)

                if a[0] == tmp_1:
                    hit+=1
                elif a[0] == tmp_2:
                    blow+=1
                elif a[0] == tmp_3:
                    blow+=1

                if a[1] == tmp_2:
                    hit+=1
                elif a[1] == tmp_1:
                    blow+=1
                elif a[1] == tmp_3:
                    blow+=1

                if a[2] == tmp_3:
                    hit+=1
                elif a[2] == tmp_1:
                    blow+=1
                elif a[2] == tmp_2:
                    blow+=1


                print("hit :"+str(hit)+", blow :"+str(blow))
                if hit == 3:
                    print("clear!")
                    clear_A = 1
                    #print("clear: "+str(clear))
                turn = 1
                self.n = 1
            answer = Person(answer=[tmp_1, tmp_2, tmp_3, hit, blow, clear_A, turn])
            print(answer)
            self.pub_answer.publish(answer)
        #print("stop clear")

def rand_ints_nodup(a, b, k):
    ns = []
    while len(ns) < k:
        n = random.randint(a, b)
        if not n in ns:
            ns.append(n)
    return ns

def main():
    #time.sleep(5)
    global a
    global clear_B
    global clear_A
    global turn
    cnt = 0
    turn = 0
    print(turn)
    clear_B = 0
    clear_A = 0
    a = rand_ints_nodup(0, 9, 3)
    print(a)
    rclpy.init()
    node = Node("listener_A")
    sub = Subscribe_publishers(node)
    #rclpy.init()
    node_A = Node("hit_and_blow_A")
    #print(node)
    player = Hit_And_Blow(node_A)
    #rclpy.spin_once(node)
    print("a!")
    while clear_B != 1 or clear_A == 1:
        print("clear_B: "+str(clear_B))
        print("clear_A: "+str(clear_A))
        if cnt != 0:
            rclpy.spin_once(node)
            #ここでsubしてる
            if clear_B == 1:
                #you lose
                break
        print("aaa")
        player.main()
        #sub = Subscribe_publishers(node)
        #if turn == 1:
        #    rclpy.spin_once(node)
        #time.sleep(10)
        if clear_A == 1:
            #print("you win")
            break
        #else:
        #    print("draw")
        #    break
        print("finish spin")
        cnt += 1
    #rclpy.spin_once(node)
    #rclpy.shutdown()
    #print("test")
    #start hit and blow
    #対戦型でros2のpubsubを使う
    #最初にランダムで数字を決定する(3桁同じ数字は使えない)
    #数字と場所があっていればHit
    #数字はあっているが場所はあっていないならBlow
    #先に相手の設定した数字を当てることができれば勝ち
    #両方が同じターンで当てた場合drawにする必要がある
    #Aが当てた場合、Bが入力するのを待つ必要がある
    #Bが当てた場合、即負けでいい

    if clear_A == 1:
        rclpy.spin_once(node)
        if clear_B == 1:
            print("draw")
            #draw
        else:
            print("you win")
    elif clear_B == 1:
        print("you lose")

if __name__ == '__main__':
    main()