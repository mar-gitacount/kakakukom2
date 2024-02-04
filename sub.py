import subprocess
# 任意の値をnumに代入
num = 23

# numが整数であるか確認
if isinstance(num, int):
    # 1からnumまでの範囲でループ
    for i in range(1, num + 1):
        # subprocessモジュールを使用して別のPythonスクリプトを呼び出す
        # 引数としてiの値を渡す
        process = subprocess.run(['python', 'webdrivertest.py', str(i)])
        # 子プロセスの終了コードを確認
        if process.returncode == 0:
            print(f"子プロセス {i} は正常に終了しました。")
        else:
            print(f"子プロセス {i} はエラー終了しました。終了コード: {process.returncode}")
else:
    print("Error: num should be an integer.")