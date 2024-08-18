#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ベースタブ画面クラス

Author: Shimizu
Date: 2024/6/9
"""

import tkinter as tk
from abc import abstractmethod
from PIL import ImageTk
from tkinter import ttk
from controllers.base_controller import BaseController


class BaseTabView(ttk.Frame):
    """ベースタブ画面クラス
        NOTE:全画面クラスが継承すべき基底クラス
    """

    def __init__(self, master: tk.Tk, style: str, controller: BaseController) -> None:
        """コンストラクタ

        Args:
            master (tk.Tk): ルート画面オブジェクト
            style (str): 適応するスタイル名
            controller (BaseController): ベース制御クラスを継承した画面制御インスタンス
        """
        ### 親クラスのコンストラクタ呼び出し
        super().__init__(master, style=style)
        ### 画面制御インスタンスを格納
        self.controller = controller
        ### ボディを生成
        self.create_body()

    @abstractmethod
    def create_body(self) -> None:
        """タブ画面のボディを生成する
        """
        # NOTE:派生先のクラスで本メソッドをオーバーライドして必ず実装する
        raise NotImplementedError()

    def create_menu(self, title_list: list) -> None:
        """タブ画面にメニューを生成する

        Args:
            title_info (list): メニューに設定するタイトル情報配列
        """
        # ボディ用フレーム生成
        frame = ttk.Frame(self)

        ### セルを生成
        # NOTE:セル数はタイトル数分生成する
        for title in title_list:
            cell = self.create_cell(frame, title)
            cell.pack(side=tk.LEFT, expand=True)

        # ウィジェットを配置
        frame.pack(padx=(5,5), pady=(0,0), fill="both")

    def create_cell(self, parent_frame: ttk.Frame, title_txt: str) -> ttk.Frame:
        """メニュー用のセルを生成する

        Args:
            parent_frame (ttk.Frame): 親フレーム
            title_txt (str): メニューに設定するタイトル文字列

        Returns:
            ttk.Frame: 生成したセルオブジェクト
        """
        ### 一つのセルの設定情報
        cell_width = 150
        cell_height = 35
        cell_bg_color = "white"
        # フォント設定情報
        font = "Arial"
        font_size = 12
        # 枠線の設定情報
        border_width = 1
        border_color = "#d3d3d3"

        ### セルとなるフレームを生成
        canvas = tk.Canvas(parent_frame, width=cell_width, height=cell_height, bg=cell_bg_color, highlightthickness=0)
        frame_id = canvas.create_rectangle(
            border_width, border_width,
            cell_width - (border_width // 2), cell_height - border_width,
            outline=border_color, width=border_width
        )

        # フレームサイズを固定
        # canvas.pack_propagate(False)
        # タイトルラベル生成
        label = tk.Label(canvas, text=title_txt, bg=cell_bg_color, font=(font, font_size))
        label_id = canvas.create_window((cell_width / 2, cell_height / 2), window=label, anchor="center")

        canvas.frame_id = frame_id
        # canvas.label_id = label_id
        canvas.label_widget = label

        # label.pack(side=tk.LEFT, padx=(2,2), pady=(2,2))
        # マウスカーソルイベント登録
        label.bind("<Enter>", lambda event: self.menu_cursor_event_cb(event, canvas, label, True))
        label.bind("<Leave>", lambda event: self.menu_cursor_event_cb(event, canvas, label, False))
        # セルオブジェクトを応答
        return canvas

    def cursor_event_cb(self, event, button: ttk.Button, image: ImageTk.PhotoImage) -> None:
        """カーソルイベント処理(コールバック)
            NOTE: マウスカーソルがボタン上に入ったときのイベント処理

        Args:
            event (_type_): イベントデータ
            button (ttk.Button): ボタンオブジェクト
            image (ImageTk.PhotoImage): 切り替える画像データ
        """
        button.config(image=image)

    def menu_cursor_event_cb(self, event, menu_cell: ttk.Frame, menu_cell_label: ttk.Label, is_enter: bool) -> None:
        """メニューカーソルイベント処理(コールバック)
            NOTE: マウスカーソルがメニューの各セル上に入ったときのイベント処理

        Args:
            event (_type_): イベントデータ
            menu_cell (ttk.Frame): セルフレームオブジェクト
            menu_cell_label (ttk.Label): セルラベルオブジェクト
            is_enter (bool): カーソルが入っているかの状態(True:入っている/False:入っていない)
        """
        ### マウスカーソルがセルに入っているかの状態判定
        if is_enter is True:
            # NOTE:入っている
            menu_cell.config(bg="lightgray")
            menu_cell_label.config(bg="lightgray")
            
        else:
            # NOTE:入っていない
            menu_cell.config(bg="white")
            menu_cell_label.config(bg="white")

    def resize_event_cb(self) -> None:
        """画面のリサイズイベント処理(コールバック)
        """
        pass