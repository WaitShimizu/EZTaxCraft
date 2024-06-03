#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
共通利用する関数群を定義

Author: Shimizu
Date: 2024/5/23
"""

from PIL import Image, ImageTk

### GCによるデータ削除回避のためグローバルに定義
images: dict = {}

def get_icon(file_name: str) -> ImageTk.PhotoImage:
    """アイコン画像を取得する
        NOTE:取得先のパスは「eztaxcraft_app」ディレクトリ直下の「/data/icon」固定

    Args:
        file_name (str): 取得するアイコン画像ファイル名

    Returns:
        ImageTk.PhotoImage: 画像データ
    """
    ### グローバル変数データチェック
    # NOTE:既にファイル名の画像データをグローバルで保持している場合はそれを応答する
    if file_name in images:
        return images[file_name]

    ### 画像データを取得してグローバル変数に格納
    file_path = f"data/icon/{file_name}"
    image = Image.open(file_path)
    resized_image = image.resize((193, 51))
    logo_image = ImageTk.PhotoImage(resized_image)
    images[f"{file_name}"] = logo_image
    return images[f"{file_name}"]
