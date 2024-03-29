#!/usr/bin/bash

#----------------------------------------------------------------------
#
#【注意】
# 本アプリケーションは内部でTkinterを利用する
# 動作環境がWSLの場合は本スクリプトを実行して環境を整備すること
# ※アプリケーションでは日本語文字列を利用しているため初回起動時のみ
#   本スクリプトを実行する必要がある
# 本スクリプトがサポートするWSLの動作環境は以下の通り
#   ・Ubuntu:22.04LTS
#   ・Python3.8.10以上
#
#----------------------------------------------------------------------

# 1. Windowsのフォントファイルを読み込むための設定ファイルを配置する
target_path="/etc/fonts/local.conf"
copy_path="../config/fonts/local.conf"

if [ ! -e "$target_path" ]; then
    sudo cp $copy_path $target_path
    echo "コピーしたフォント用設定ファイルを目標のパスへ配置しました。目標のパス-> [ $target_path ]"
else
    echo "既にフォント用設定ファイルは所定のディレクトリに配置されています。"
fi
