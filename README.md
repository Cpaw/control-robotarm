## Preparation

* WebIOPiのインストール

    [DEVICE PLUSの記事](http://deviceplus.jp/hobby/raspberrypi_entry_030/)を参考に

* WebIOPiの設定ファイルの編集
    
    [hiramine.com](http://www.hiramine.com/physicalcomputing/raspberrypi/webiopi_callmacro.html)の「WebIOPiサービスの設定の変更」を参考に。


## Usage

1. 「seigyo.py」で使用するピンのGPIO番号を設定

1. 実行
    ```bash
    sudo /etc/init.d/webiopi start
    ```

    デバッグモードで実行
    ```bash
    sudo webiopi -d -c /etc/webiopi/config
    ```
 
1. スマホのブラウザで`WebIOPiのプログラムが走ってるpcのIPアドレス:8000`に接続

1. 認証は以下で通る

    | User |Password|
    |--------|------------|
    |webiopi|raspberry|
    
1. ボタンを押してロボットアームを操作

1. 停止
    ```bash
    sudo /etc/init.d/webiopi stop
    ```
    
    デバッグモードで実行してる場合はCtrl+Cで停止
    
