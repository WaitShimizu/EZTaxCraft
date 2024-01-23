# #!/usr/bin/env python3
# # -*- cording: utf-8 -*-

import math

class Proration:
    """按分クラス
    """
    def calc_expenses(self, source_value: float, target_value: float, _per_month: int) -> int:
        """経費按分計算

        Args:
            source_value (float): ベースの値
            target_value (float): 経費精算したい部分の値
            _per_month (int): 1か月の経費

        Returns:
            int: 必要経費額
        """
        # 按分用比率計算
        ratio = target_value / source_value
        # 比率の表示(切り上げ)
        round_up = math.ceil(ratio*100)
        print(f'按分元データ：[{ratio:.2%}],按分用比率:[{round_up}%]')
        # 必要経費計算
        required_expenses = math.ceil(_per_month * ratio)
        # 変数のタイプチェック用
        print(type(required_expenses))

        return required_expenses
    
if __name__ == '__main__':
    # インスタンスの生成
    proration = Proration()

    source_str, target_str, cost_str = input().split()
    source_val = float(source_str)
    target_val = float(target_str)
    cost_val = int(cost_str)

    result_val = proration.calc_expenses(source_val, target_val, cost_val)
    print(f'経費：{result_val:,.0f}円')
