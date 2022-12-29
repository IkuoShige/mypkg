#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2022 Ikuo Shige                                                                                                           
# SPDX-License-Identifier: BSD-3-Clause
"""
BSD 3-Clause License
Copyright (c) 2020, Ryo Nakamura & Ryuichi Ueda.
All rights reserved.
"""
import time
import rclpy
from rclpy.node import Node
import random
from std_msgs.msg import Int32

rclpy.init()
node = Node("game")
#pub = node.create_publisher("game", Int32, queue_size=1)
pub = node.create_publisher(Int32, "game", 1)
#rate = rclpy.Rate(10)
rate = node.create_rate(10)

x = 0   # 変数定義
a = 0   # 変数定義
b = 0   # 変数定義

round = 0   # 現在のラウンド
miss = 0    # ミスした回数
flag = 0    # 0なら線形、1なら二乗の計算

a_range_factor = 10 # aの範囲を決  めるための補正値
b_range_factor = 25 # bの範囲を決めるための補正値
x_range_factor = 35 # xの範囲を決めるための補正値

max_round = 4   # ゲームをやる回数
mul_round = 2   # 2乗が出てくるタイミング

# ax + b
def x_linear(tmp):
    return a * tmp + b

# ax² + b
def x_square(tmp):
    # -ax² + b
    if(tmp < 0):
        return -1 * a * tmp * tmp + b
    # +ax² + b
    else:
        return a * tmp * tmp + b

print("説明")
print("数当てゲームを", max_round, "回やります。")
print(max_round, "回のやった際の入力回数が少ないほど高スコアになります。")
print("入力する数値は特定の規則に乗っ取り変化します。")

#rospy.sleep(2)
time.sleep(2)

print("例 目標が61のとき")
print("1 → 5, 2 → 7, 3 → 9 ならば2x + 3という規則に乗っ取っている。")
print("なので29を入力すれば61になるのでクリア！")
print("")

#rospy.sleep(2)
time.sleep(2)

# a, b, 答えを決める
while(round < max_round):
    
    # 始まるタイミングでラウンドを増やす
    round = round + 1
    print()
    print("ステージ" , end="")
    print(round, "!")

    #rospy.sleep(1)
    time.sleep(1)

    # 乱数でa, bの値を決める
    a = random.randint(-1 * round * a_range_factor, round * a_range_factor)
    b = random.randint(-1 * round * b_range_factor, round * b_range_factor)
    
    print("以下の答えになる整数を探してください。")
    
    # 二乗が出てもよいなら乱数でどっちを出題するか決める
    if(round >= mul_round):
        flag = random.randint(0, 1)
    
    # 作成した式に範囲内で代入を行い
    if(flag):
        answer = x_square(random.randint(0, round * x_range_factor))
    else:
        answer = x_linear(random.randint(-1 * round * x_range_factor, round * x_range_factor))
    
    print(answer)
    print()

    #rospy.sleep(1)
    time.sleep(1)

    print("xを入力してください。")
    print("今回のステージでのxの取る範囲は", -1 * round * x_range_factor , "≦ x ≦ ", round * x_range_factor, "です。")
    
    # 入力部
    while rclpy.ok():
    #while not rospy.is_shutdown():
        
        tmp = ""
        print("整数を入力してください。")
        tmp = input()

        # 入力された文字が数字か否か判別
        try:
            int(tmp)
            x = int(tmp)
        except ValueError:
            print("\033[31m数字以外が含まれています。\033[0m")
            print("\033[31m半角数字になっているか確認後再入力をしてください。\033[0m")
            continue

        if(flag):
            x = x_square((int)(x))
        else:
            x = x_linear((int)(x))
        
        if(x == answer):
            print("クリア")
            print("")
            break
        else:
            print("else !")
            miss = miss + 1

        print(x)
        miss_32 = miss
        miss_32 = Int32()
        pub.publish(miss_32)
        #rate.sleep()
        #rclpy.spin(node)


# スコアを決める
# バグ利用時
if(miss == 0):
    print("\033[31mスコア : SSS!\033[0m")
# 平均3回以内
elif(max_round * 3 >= miss):
    print("\033[32mスコア : SS!\033[0m")
# 平均4回以内
elif(max_round * 4 >= miss):
    print("\033[33mスコア : S!\033[0m")
# 平均6回以内
elif(max_round * 6 >= miss):
    print("\033[34mスコア : A!\033[0m")
# 平均10回以内
elif(max_round * 10 >= miss):
    print("\033[35mスコア : B!\033[0m")
# 平均15回以内
elif(max_round * 15 >= miss):
    print("\033[36mスコア : C!\033[0m")
# それ以外
else:
    print("スコア : D!")

print("入力回数 : ", miss, "回")