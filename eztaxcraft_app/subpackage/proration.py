# #!/usr/bin/env python3
# # -*- cording: utf-8 -*-

class Proration:
    """按分クラス
    """
    def calc_expenses(self, source_value: float, target_value: float, cost: int) -> int:
        """経費按分計算

        Args:
            source_value (float): ベースの値
            target_value (float): 経費精算したい部分の値
            cost (int): 1か月の経費

        Returns:
            int: 必要経費額
        """
        # 按分用比率計算
        ratio = target_value / source_value
        # 比率の表示
        print(f'按分用比率: {ratio:.2%}')
        # 必要経費計算
        required_expenses = cost * ratio

        return int(required_expenses)
