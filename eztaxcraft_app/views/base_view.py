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

    def __init__(self, master: tk.Tk, controller: BaseController) -> None:
        """コンストラクタ

        Args:
            master (tk.Tk): ルート画面オブジェクト
            controller (BaseController): ベース制御クラスを継承した画面制御インスタンス
        """
        ### 画面の最上位オブジェクト(root[master])を格納
        self.root = master
        ### 親クラスのコンストラクタ呼び出し
        super().__init__(self.root)
        ### 画面制御インスタンスを格納
        self.controller = controller
        ### ウィジェットを生成
        self.create_widget()
        ### 画面のリサイズイベント処理のコールバックを格納
        self.resize_event_cb_list: list = []
        self.event_bind()

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
