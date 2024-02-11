# #!/usr/bin/env python3
# # -*- cording: utf-8 -*-

class Proration:
    """按分クラス
    """
    def calc_expenses(self, comparison_value: float, comparison_original_value: float, cost_per_month: int) -> int:
        """経費計算

        Args:
            comparison_value (float): 比較値
            comparison_original_value (float): 比較元値
            cost_per_month (int): 1カ月当たりの費用

        Returns:
            int: 必要経費額
        """
        # 按分詳細比率(小数点以下第9位まで)
        proration_detail_rate = self.__get_proration_detail_rate(comparison_value, comparison_original_value)
        # 按分比率(整数)
        proration_rate = self.__get_proration_rate(proration_detail_rate)
        print(f'按分詳細比率：[{proration_detail_rate}],按分比率:[{proration_rate}%]')
        # 必要経費計算
        required_expenses = round(cost_per_month * proration_detail_rate, 1)
        return int(required_expenses)

    def __get_proration_detail_rate(self, comparison_value: float, comparison_original_value: float) -> float:
        """按分詳細比率を取得する [内部処理用]
            NOTE:小数点以下第9位まで

        Args:
            comparison_value (float): 比較値
            comparison_original_value (float): 比較元値

        Returns:
            float: 按分詳細比率
        """
        result = round(comparison_value / comparison_original_value, 9)
        return result

    def __get_proration_rate(self, proration_detail_rate: float) -> int:
        """按分比率を取得する [内部処理用]
            NOTE:整数で算出する

        Args:
            proration_detail_rate (float): 按分詳細比率

        Returns:
            int: 按分比率
        """
        result = int(round(round(proration_detail_rate,3)*100, 0))
        return result
