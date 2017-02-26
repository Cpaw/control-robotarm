## Preparation

* WebIOPiのインストール

    [DEVICE PLUSの記事](http://deviceplus.jp/hobby/raspberrypi_entry_030/)を参考に

* WebIOPiの設定ファイルの変更

    [hiramine.com](http://www.hiramine.com/physicalcomputing/raspberrypi/webiopi_callmacro.html)の「WebIOPiサービスの設定の変更」を参考に。「welcome-file」はindex.htmlでOK


## Usage

1. 「seigyo.py」で使用するピンのGPIO番号を設定

1. サービス開始

    ```bash
    sudo /etc/init.d/webiopi start
    ```
 
1. ブラウザで以下に接続

    ```
    WebIOPiのプログラムが走ってるpcのIPアドレス:8000
    ```

1.  認証は以下で通る

    | User |Password|
    |--------|------------|
    |webiopi|raspberry|

1. サービス終了

    ```bash
    sudo /etc/init.d/webiopi stop
    ```
