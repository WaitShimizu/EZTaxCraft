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

def get_icon(file_name: str, width: int = 100, height: int = 50) -> ImageTk.PhotoImage:
    """アイコン画像を取得する
        NOTE:取得先のパスは「eztaxcraft_app」ディレクトリ直下の「/data/icon」固定

    Args:
        file_name (str): 取得するアイコン画像ファイル名
        width (int, optional): 画像横幅サイズ. Defaults to 100.
        height (int, optional): 画像高さサイズ. Defaults to 50.

    Returns:
        ImageTk.PhotoImage: 画像データ
    """
    ### バッファチェック
    # NOTE:既にファイル名の画像データをバッファに保持している場合はそれを応答する
    # if file_name in images:
    #     data = images[file_name]
    #     # バッファの画像データサイズチェック
    #     if data["width"] == width and data["height"] == height:
    #         return images[file_name]

    ### 画像データを取得してバッファに格納する
    file_path = f"data/icon/{file_name}"
    image = Image.open(file_path)
    resized_image = image.resize((width, height))
    logo_image = ImageTk.PhotoImage(resized_image)
    # # NOTE:バッファに格納するデータを生成
    # save_image = {
    #     "image_data": logo_image,
    #     "width": width,
    #     "height": height
    # }
    # images[f"{file_name}"] = save_image
    # return images[f"{file_name}"]["image_data"]
    return logo_image
