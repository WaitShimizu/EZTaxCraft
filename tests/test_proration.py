# #!/usr/bin/env python3
# # -*- cording: utf-8 -*-

from eztaxcraft_app.subpackage.proration import Proration

def test_calc_expenses():
    """経費計算メソッドのテスト
    """
    # テストデータを作成
    test_data_list = [
        [159, 403, 8436],
        [154, 390, 10730],
        [174, 403, 11255],
        [167, 390, 9993],
        [165, 403, 8637]
    ]
    # 結果データを作成
    result_data_list = [
        3328,
        4237,
        4859,
        4279,
        3536
    ]
    print('')
    proration = Proration()
    for i, data in enumerate(test_data_list):
        result = proration.calc_expenses(data[0], data[1], data[2])
        print(f'経費計算テスト結果：{result}, 比較用結果データ：{result_data_list[i]}')
        assert result == result_data_list[i]
