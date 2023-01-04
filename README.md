# mypkg
![test](https://github.com/IkuoShige/mypkg/actions/workflows/test.yml/badge.svg)

こちらは、千葉工業大学先進工学部未来ロボティクス学科2年後期のロボットシステム学の講義で扱っているROS2のパッケージのリポジトリです。

# リポジトリの概要

talker.py, listener.py

* クラスやメソッドを用いて整理し、publisherとsubscriberを実装

talker_before_lesson_11.py, listener_before_lesson_11.py

* 講義のlesson_11までのtalkerとlistener

talk_listen.launch.py

* talker.py と listener.py の launchファイル

hit_and_blow.py, hit_and_blow_B.py

* 一般的にHit&Blowと呼ばれるゲームをpythonを用いて実装

# リポジトリの使用方法

ターミナルで以下のコマンドを実行する
```
$ cd ~/ros2_ws/src/
$ git clone https://github.com/IkuoShige/mypkg.git
$ git clone https://github.com/IkuoShige/hit_and_blow_msgs.git
$ cd ~/ros2_ws/
$ colcon build
```

# talker と listener

## 機能

talker.py で１ずつ加算したnをpublishし、listener.py でnをsubscribeする

## 使いかた

先述したlaunchファイルを実行する

```
$ cd ~/ros2_ws/
$ ros2 launch mypkg talk_listen.launch.py
```

出力結果は以下のようになります
```
[INFO] [launch]: All log files can be found below /home/ikuo/.ros/log/2022-12-31-22-38-47-736373-ikuo-CFSV1-1-116125
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [116127]
[INFO] [listener-2]: process started with pid [116129]
[listener-2] [INFO] [1672493928.746150294] [listener]: Listen: 0
[listener-2] [INFO] [1672493929.230498671] [listener]: Listen: 1
[listener-2] [INFO] [1672493929.730591909] [listener]: Listen: 2
[listener-2] [INFO] [1672493930.230547673] [listener]: Listen: 3
...
...
```

# hit_and_blow

## 機能

pythonを用いてHit&Blowを行う

Hit&Blowとは
* はじめにプレイヤーは3桁の整数であり、かつ百の位と十の位と一の位の数字にかぶりのないものを用意する(今回はランダムで設定する)
* ターン制で3桁の整数を選択する
* 数字と場所があっていればHitのカウントが1増加する
* 数字はあっているが場所はあっていないならBlowのカウントが1増加する
* このときに相手の3桁の整数を当てれば(Hitのカウントが3になれば)勝利
* 両方が同じターンで当てた場合は引き分けとなる

## 使いかた

以下のコマンドで実行が可能

```
$ bash ~/ros2_ws/src/mypkg/launch/run.bash
```

それぞれのターミナルでゲームを進めていく
先手は誘導のある方のターミナルから

上記コマンド実行時点での出力(例)
```
(player A)
player_B answer: [1, 6, 4]
1番目の数を入力してください:

(player B)
player_A answer: [2, 1, 6]
```

プログラムの誘導に沿ってゲームを進める

決着時の出力(例)
```
(player A)
1番目の数を入力してください: 1
2番目の数を入力してください: 2
3番目の数を入力してください: 3
hit :0, blow :2
answer_B: [1, 6, 4]
hit_B: 3, blow_B: 0
you lose
Press a key... close the window

(player B)
answer_A: [1, 2, 3]
hit_A: 0, blow_A: 2
1番目の数を入力してください: 1
2番目の数を入力してください: 6
3番目の数を入力してください: 4
hit :3, blow :0
clear!
you win
Press a key... close the window
```

## ノードとトピック
![Test Image 6](https://github.com/IkuoShige/mypkg/blob/main/image/rqt_graph_mypkg.png)

/hit_and_blow_AのノードからA側のプレイヤーの答案の情報が含まれているトピックである/Aをlistener_Bのノードに渡している

/hit_and_blow_BのノードからB側のプレイヤーの答案の情報が含まれているトピックである/Bをlistener_Aのノードに渡している

トピックの内容
* プレイヤーの答案
* hitのカウント
* blowのカウント
* 勝利のカウント
* ターンのカウント

# テスト環境
* Ubuntu 20.04.5 LTS
* ROS2 noetic

* Python
    3.7~3.10

# LICENSE

* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    * [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* © 2022 Ikuo Shige