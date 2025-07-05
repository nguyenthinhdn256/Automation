import tkinter as tk
from tkinter import ttk

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.create_widgets()
    
    def setup_window(self):
        """Thiết lập cửa sổ chính"""
        self.root.title("No-Code Automation Tool")
        self.root.geometry("800x600")
        self.root.configure(bg='#2b2b2b')  # Màu nền tối
        
        # Căn giữa cửa sổ
        self.root.eval('tk::PlaceWindow . center')
    
    def create_widgets(self):
        """Tạo các widget cho giao diện"""
        
        # Frame chính
        main_frame = tk.Frame(self.root, bg='#2b2b2b')
        main_frame.pack(expand=True, fill='both', padx=50, pady=50)
        
        # Tiêu đề
        title_label = tk.Label(
            main_frame,
            text="No-Code Automation Tool",
            font=('Arial', 24, 'bold'),
            fg='white',
            bg='#2b2b2b'
        )
        title_label.pack(pady=(0, 50))
        
        # Frame chứa các button
        button_frame = tk.Frame(main_frame, bg='#2b2b2b')
        button_frame.pack(expand=True)
        
        # Tạo 3 button
        self.create_button(button_frame, "Emulator", self.open_emulator_window)
        self.create_button(button_frame, "Phone", self.open_phone_window)
        self.create_button(button_frame, "Trình duyệt", self.open_browser_window)
    
    def create_button(self, parent, text, command):
        """Tạo button với style thống nhất"""
        button = tk.Button(
            parent,
            text=text,
            font=('Arial', 16),
            fg='white',
            bg='#404040',
            activebackground='#505050',
            activeforeground='white',
            width=15,
            height=2,
            command=command,
            relief='flat',
            bd=0
        )
        button.pack(pady=15)
        
        # Hiệu ứng hover
        button.bind("<Enter>", lambda e: button.config(bg='#505050'))
        button.bind("<Leave>", lambda e: button.config(bg='#404040'))
    
    def open_emulator_window(self):
        """Mở cửa sổ Emulator"""
        self.open_secondary_window("Emulator Automation")
    
    def open_phone_window(self):
        """Mở cửa sổ Phone"""
        self.open_secondary_window("Phone Automation")
    
    def open_browser_window(self):
        """Mở cửa sổ Browser"""
        self.open_secondary_window("Browser Automation")
    
    def open_secondary_window(self, title):
        """Mở cửa sổ phụ trống"""
        secondary_window = tk.Toplevel(self.root)
        secondary_window.title(title)
        secondary_window.geometry("600x400")
        secondary_window.configure(bg='#2b2b2b')
        
        # Label thông báo
        label = tk.Label(
            secondary_window,
            text=f"{title}\n(Chức năng sẽ được thêm sau)",
            font=('Arial', 14),
            fg='white',
            bg='#2b2b2b'
        )
        label.pack(expand=True)
    
    def run(self):
        """Chạy ứng dụng"""
        self.root.mainloop()
