#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ベース画面クラス

Author: Shimizu
Date: 2024/5/26
"""

import tkinter as tk
from abc import abstractmethod
from tkinter import ttk
from controllers.base_controller import BaseController


class BaseView(ttk.Frame):
    """ベース画面クラス
        NOTE:全画面クラスが継承すべき基底クラス
    """

    def __init__(self, controller: BaseController) -> None:
        """コンストラクタ

        Args:
            master (tk.Tk): ルート画面オブジェクト
            controller (BaseController): ベース制御クラスを継承した画面制御インスタンス
        """
        ### 画面のルートインスタンスを生成
        self.root = tk.Tk()
        ### コントロールオブジェクト格納
        self.controller = controller
        ### 画面のタイトル情報、サイズ情報を取得
        title, _ = self.controller.get_window_title()
        width, _ = self.controller.get_window_width()
        height, _ = self.controller.get_window_height()
        pos_x, _ = self.controller.get_window_position_x()
        pos_y, _ = self.controller.get_window_position_y()
        # NOTE:画面のタイトル文字を削除
        self.root.title(title)
        # NOTE:画面のジオメトリを設定
        self.root.geometry(f'{width}x{height}+{pos_x}+{pos_y}')
        ### 親クラスのコンストラクタ呼び出し
        super().__init__(self.root)
        ### ウィジェットを生成
        self.create_widget()
        ### 画面のリサイズイベント処理のコールバックを格納
        self.resize_event_cb_list: list = []
        self.event_bind()

    @abstractmethod
    def run(self) -> None:
        """画面処理を開始する
        """
        # NOTE:派生先のクラスで本メソッドをオーバーライドして必ず実装する
        raise NotImplementedError()

    @abstractmethod
    def create_widget(self) -> None:
        """ウィジェットを生成する
        """
        # NOTE:派生先のクラスで本メソッドをオーバーライドして必ず実装する
        raise NotImplementedError()

    def event_bind(self) -> None:
        """ルート画面のイベント処理をバインドする
        """
        self.root.bind("<Configure>", self.resize_event)

    def resize_event(self, event) -> None:
        """画面のリサイズイベント処理
        """
        ### バッファに格納されたコールバック実行
        for func in self.resize_event_cb_list:
            func()

    def regist_resize_cb(self, func) -> None:
        """リサイズイベントのコールバック登録

        Args:
            func (Function|Method): 関数(メソッド)のポインタ
        """
        ### バッファにコールバックを登録する
        self.resize_event_cb_list.append(func)
