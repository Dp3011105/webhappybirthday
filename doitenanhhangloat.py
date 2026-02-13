import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Các định dạng ảnh hỗ trợ
ALLOWED_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.webp', '.bmp')


def rename_images(folder_path):
    if not os.path.isdir(folder_path):
        messagebox.showerror("Lỗi", "Thư mục không tồn tại!")
        return

    # Lấy danh sách file ảnh
    files = [
        f for f in os.listdir(folder_path)
        if f.lower().endswith(ALLOWED_EXTENSIONS)
    ]

    if not files:
        messagebox.showinfo("Thông báo", "Không tìm thấy ảnh trong thư mục!")
        return

    # Sắp xếp theo tên cũ
    files.sort()

    # Đổi tên tạm để tránh trùng
    temp_files = []
    for i, filename in enumerate(files):
        old_path = os.path.join(folder_path, filename)
        temp_name = f"temp_{i}.tmp"
        temp_path = os.path.join(folder_path, temp_name)
        os.rename(old_path, temp_path)
        temp_files.append(temp_name)

    # Đổi sang tên mới
    for index, temp_name in enumerate(temp_files, start=1):
        temp_path = os.path.join(folder_path, temp_name)
        new_name = f"Anh ({index}).jpg"
        new_path = os.path.join(folder_path, new_name)
        os.rename(temp_path, new_path)

    messagebox.showinfo("Thành công", f"Đã đổi tên {len(temp_files)} ảnh!")


def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        rename_images(folder_selected)


# Tạo cửa sổ đơn giản
root = tk.Tk()
root.title("Đổi tên ảnh tự động")
root.geometry("300x150")

btn = tk.Button(root, text="Chọn thư mục và đổi tên", command=select_folder)
btn.pack(expand=True)

root.mainloop()
