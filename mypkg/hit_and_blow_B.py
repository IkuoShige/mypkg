#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2022 Ikuo Shige                                                                                                           
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
import geometry_msgs
from geometry_msgs.msg import Pose2D
import random
#from person_msgs.msg import Person
from mypkg.msg import Answer
import time



class Subscribe_publishers():
    def __init__(self, node):
        # Subscriberを作成
        self.subscriber_enemy_answer = node.create_subscription(Answer, "first_number_b", self.callback_first_answer, 8)
        self.subscriber_b = node.create_subscription(Answer, "a", self.callback_answer, 10)
        self.publisher_b = node.create_publisher(Answer, "first_number_a", 9)
        #print("a")
        #self.subscriber_r = rclpy.create_subscription(Pose2D, 'red', self.callback_red)
        #self.subscriber_g = rclpy.create_subscription(Pose2D, 'green', self.callback_green)
        # messageの型を作成
        self.message = Answer()
        time.sleep(2)
        self.publish_first_answer()

    def publish_first_answer(self):
        self.enemy_answer = Answer(answer=[a[0], a[1], a[2], 0, 0, 0, 0])
        #print("enemy_answer: "+str(self.enemy_answer))
        self.publisher_b.publish(self.enemy_answer)
        time.sleep(1)
        self.publisher_b.publish(self.enemy_answer)

    def callback_first_answer(self, message):
        first_answer = message
        #print("message: "+str(first_answer))
        global answer_A, hit_A, blow_A, clear_A, turn
        answer_A = [first_answer.answer[0],first_answer.answer[1],first_answer.answer[2]]
        #print("first_answer_: "+str(answer_A))
        hit_A, blow_A = first_answer.answer[3], first_answer.answer[4]
        clear_A = first_answer.answer[5]
        turn = first_answer.answer[6]
        global a
        a = answer_A

    def callback_answer(self, message):
        #print("callback!!!!!!!!!!!")
        #global sub_blue
        sub_answer = message
        global answer_A, hit_A, blow_A, clear_A, turn
        answer_A = [sub_answer.answer[0],sub_answer.answer[1],sub_answer.answer[2]]
        hit_A, blow_A = sub_answer.answer[3],sub_answer.answer[4]
        clear_A = sub_answer.answer[5]
        turn = sub_answer.answer[6]
        print("answer_A: "+str(answer_A))
        print("hit_A: "+str(hit_A)+", blow_A: "+str(blow_A))
        #print(clear_A)
        #print(turn)
        # callback時の処理
        #self.pub.make_msg(message)
        # publish
        #self.pub.send_msg()

class Hit_And_Blow():
    def __init__(self, node):
        self.pub_answer = node.create_publisher(Answer, "b", 10)
        self.n = 0
        #node.create_timer(0.5, self.call_back)
        #self.main()
        #first = Person(answer=[a[0], a[1], a[2], 0, 0, 0, 0])
        #print(first)
        #self.pub_answer.publish(first)

    def call_back(self):
        msg = Answer()
        #self.pub.publish(msg)

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
        global clear_B
        self.n = 0
        clear_B = 0
        global turn
         
        #a = [random.randint(0, 10) for i in range(3)]
        

        while self.n != 1:
            hit = 0
            blow = 0
            #print("turn_1"+str(turn))
            if turn == 1:
                tmp_1 = int(input("1番目の数を入力してください: "))
                #print(tmp_1)1
                tmp_2 = int(input("2番目の数を入力してください: "))
                #print(tmp_2)
                tmp_3 = int(input("3番目の数を入力してください: "))
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
                    clear_B = 1
                turn = 0
                self.n = 1
                answer = Answer(answer=[tmp_1, tmp_2, tmp_3, hit, blow, clear_B, turn])
                #print(answer)
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
    global a
    global clear_A
    global turn
    clear_A = 0
    a = rand_ints_nodup(0, 9, 3)
    #a = [4, 5, 6]
    #a = answer_A
    print("player_A answer: "+str(a))
    rclpy.init()
    node = Node("listener_b")
    sub = Subscribe_publishers(node)
    time.sleep(0)
    rclpy.spin_once(node)
    #rclpy.spin_once(node)
    #print("enemy: "+str(a))
    #rclpy.init()
    node_B = Node("hit_and_blow_b")
    player = Hit_And_Blow(node_B)
    while clear_A != 1 or clear_B == 1:
        #print("clear: "+str(clear_A))
        #if cnt != 0:
        time.sleep(1)
        rclpy.spin_once(node)#ここでsubしてる
        player.main()
        #sub = Subscribe_publishers(node)
        #if turn == 0:
        #    rclpy.spin_once(node)
        #time.sleep(10)
        if clear_A == 1 or clear_B == 1:
            #print("you lose")
            break
        #else:
        #    print("draw")
        #    break
        #print("finish spin")
    #rclpy.shutdown()
    #print("test")
    #start hit and blow
    #対戦型でros2のpubsubを使う
    #最初にランダムで数字を決定する(3桁同じ数字は使えない)
    #数字と場所があっていればHit
    #数字はあっているが場所はあっていないならBlow
    #先に相手の設定した数字を当てることができれば勝ち
    #Bが当てた場合、Aは即負け、即勝ち
    #Aが当てた場合、Bが入力するまで待つ必要がある

    if clear_A == 1 and clear_B == 1:
        print("draw")
    elif clear_B == 1:
        print("you win")
    elif clear_A == 1:
        print("you lose")

if __name__ == '__main__':
    main()