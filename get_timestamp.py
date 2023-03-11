import time
###
# 2か月に1度コミットしないとRSS取得が停止してしまうので、timestampをコミットしてpushするためのプログラム
###
# 現在のタイムスタンプを取得
timestamp = int(time.time())
print(f"update timestamp... {timestamp}")

# タイムスタンプを文字列に変換
timestamp_str = str(timestamp)

# ファイルに書き込む
with open('timestamp.txt', 'w') as f:
    f.write(timestamp_str)