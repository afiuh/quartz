import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCH_DIR = "content"
DEBOUNCE_SECONDS = 5
GIT_BRANCH = "v4"  # 改成你的分支名

class ChangeHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_trigger = 0
        self.timer = None

    def on_any_event(self, event):
        # 忽略目录事件和自身临时文件
        if event.is_directory:
            return
        # 触发防抖：记录最后事件时间，5秒无新事件才执行
        self.last_trigger = time.time()
        if self.timer:
            self.timer.cancel()
        self.timer = threading.Timer(DEBOUNCE_SECONDS, self.do_git_sync)
        self.timer.start()

    def do_git_sync(self):
        print("\n检测到文件变动，准备自动提交...")
        # 检查是否有更改
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True, text=True
        )
        if not result.stdout.strip():
            print("没有需要提交的更改。")
            return

        # 添加所有更改
        subprocess.run(["git", "add", "."], check=True)

        # 提交
        commit_msg = "auto: 内容更新"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)

        # 推送
        subprocess.run(["git", "push", "origin", GIT_BRANCH], check=True)
        print("推送成功！")

def main():
    import threading  # 放到这里确保可用
    global threading
    import threading as th
    threading = th

    print(f"正在监听 {WATCH_DIR} 文件夹...")
    print("修改文件后，等待 5 秒无新变动即自动提交并推送。")
    print("按 Ctrl+C 停止监听。")

    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_DIR, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n监听已停止。")
    observer.join()

if __name__ == "__main__":
    main()