#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
イベント管理クラス定義

Author: Shimizu
Date: 2024/2/11
"""

import asyncio
from queue import Queue
from .event import Event
from .continuous_event import ContinuousEvent


class EventManager:
    """イベント管理クラス
        NOTE: イベント管理クラスが継承すべき親クラス
    """

    def __init__(self) -> None:
        """コンストラクタ
        """
        # イベント処理ループ待機時間(NOTE: デフォルトで1msの待機で設定)
        self.sleep_time = 1/1000
        # キューインスタンス生成
        self.event_queue: Queue = Queue()
        self.continuous_event_queue: Queue = Queue()

    def execute_events(self) -> None:
        """イベントキューに存在するイベントを実行
        """
        # イベントキューが空かどうかをチェック
        if self.event_queue.empty() is True:
            # イベントキューが空の場合は何もしない
            return

        # イベントループを作成してイベント処理開始
        event_loop = asyncio.get_event_loop()
        event_loop.run_until_complete(self.async_execute_event())

    def execute_continuous_events(self) -> None:
        """イベントキューに存在する継続イベントを実行
        """
        # イベントキューが空かどうかをチェック
        if self.continuous_event_queue.empty() is True:
            # イベントキューが空の場合は何もしない
            return

        # イベントループを作成してイベント処理開始
        event_loop = asyncio.get_event_loop()
        event_loop.run_until_complete(self.async_execute_continuous_event())

    async def async_execute_event(self) -> None:
        """イベントキューのイベント処理を非同期で実行
        """
        while not self.event_queue.empty():
            # イベントキューのイベントを取得
            event = self.event_queue.get()
            # 取り出したイベントを実行
            event.execute()
            # 他の非同期イベント・タスクのブロック回避のため待機する
            await asyncio.sleep(self.sleep_time)

    async def async_execute_continuous_event(self) -> None:
        """イベントキューの継続イベント処理を非同期で実行
        """
        while not self.continuous_event_queue.empty():
            # イベントキューのイベントを取得
            event = self.continuous_event_queue.get()
            # 取り出したイベントを実行
            event.execute()
            # 他の非同期イベント・タスクのブロック回避のため待機する
            await asyncio.sleep(self.sleep_time)

    def event_registration(self, event: Event) -> None:
        """イベント登録

        Args:
            event (Event): 登録するイベント
        """
        # イベント型チェック
        if self.check_event_type(event) is False:
            # イベント型でなければ何もしない
            return

        # イベントキューにイベントを追加
        self.event_queue.put(event)

    def continuous_event_registration(self, continuous_event: ContinuousEvent) -> None:
        """継続イベント登録

        Args:
            continuous_event (ContinuousEvent): 登録する継続イベント
        """
        self.continuous_event_queue.put(continuous_event)

    def event_notification(self, event: Event) -> None:
        """イベント通知

        Args:
            Event (_type_): _description_
        """
        self.event_registration(event)

    def check_event_type(self, event: Event) -> bool:
        """イベント型チェック

        Returns:
            bool: True: Event型 / False: Event型以外
        """
        return isinstance(event, Event)

    def check_continuous_event_type(self, event: ContinuousEvent) -> bool:
        """継続イベント型チェック

        Returns:
            bool: True: ContinuousEvent型 / False: ContinuousEvent型以外
        """
        return isinstance(event, ContinuousEvent)
