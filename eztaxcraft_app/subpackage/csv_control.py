# #!/usr/bin/env python3
# # -*- cording: utf-8 -*-

import csv

class CsvCtrl:
    """CSV制御クラス
    """
    def __check_file(self, file_path: str):
        """ファイル存在とアクセス権チェック

        Args:
            file_path (str): チェックするファイルのパス

        Returns:
            bool: ファイルが存在し、かつアクセス権がある場合はTrue、それ以外はFalse
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                pass
            return True
        except FileNotFoundError as e:
            print(f"Error: ファイル '{file_path}' が存在しません。詳細: {e}")
            return False
        except PermissionError as e:
            print(f"Error: ファイル '{file_path}' にアクセス権がありません。詳細: {e}")
            return False
        except IsADirectoryError as e:
            print(f"Error: パス '{file_path}' はディレクトリです。ファイルを指定してください。詳細: {e}")
            return False
        except UnicodeDecodeError as e:
            print(f"Error: ファイル '{file_path}' のエンコーディングが無効です。詳細: {e}")
            return False
        except Exception as e:
            print(f"Error: ファイル '{file_path}' のチェック中にエラーが発生しました。詳細: {e}")
            return False
        

    def read_data(self, file_path: str):
        """読み込み

        Args:
            file_path (str): 読み込むCSVファイルパス
        """
        # ファイル存在チェック
        if not self.__check_file(file_path):
            return None
        
        # 結果格納リスト
        result_rows = []

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    result_rows.append(row)
        except csv.Error as e:
            print(f"Error: ファイル '{file_path}' の読み込み中にCSVエラーが発生しました。詳細: {e}")
            return None

        return result_rows

    def write_data(self, file_path: str, data: list):
        """書き込み(上書き)

        Args:
            file_path (str): 書き込むCSVファイルパス
            data (list): CSVに書き込むデータリスト
        """
        ### CSVファイルの中身をすべて上書き
        self.__write(file_path, data, False)

    def add_data(self, file_path: str, data: list):
        """書き込み(末尾に追加)

        Args:
            file_path (str): 書き込むCSVファイルパス
            data (list): CSVに書き込むデータリスト
        """
        ### CSVファイルの中身をすべて上書き
        self.__write(file_path, data)

    def __write(self, file_path: str, data: list, append=True):
        """書き込み [内部処理用]

        Args:
            file_path (str): 書き込むCSVファイルパス
            data (list): CSVに書き込むデータリスト
            append (bool): Trueの場合、既存のデータに追記。Falseの場合、上書き。
        """
        if append:
            mode = 'a'
        else:
            mode = 'w'

        if not self.__check_file(file_path) and append:
            print(f"Warning: ファイル '{file_path}' が存在しないため、新しく作成します。")

        with open(file_path, mode, encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            for row in data:
                writer.writerow(row)


if __name__ == '__main__':
    # インスタンスの生成
    csv_ctrl = CsvCtrl()

    # サンプルデータ
    sample_data = [
       ['inu','10','guamu']
    ]

    # 書き込み
    csv_ctrl.add_data('/home/ubuntu/project/csv_study/venv/sample2.csv', sample_data)
    # 読み込み
    result = csv_ctrl.read_data('/home/ubuntu/project/csv_study/venv/sample2.csv')
    print(result)
