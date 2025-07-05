import sys
import os

# Thêm src vào path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from gui.main_window import MainWindow

def main():
    """Hàm chính để chạy ứng dụng"""
    app = MainWindow()
    app.run()

if __name__ == "__main__":
    main()
