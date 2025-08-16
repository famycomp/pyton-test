import tkinter as tk
from tkinter import messagebox

def calculate_sum():
    try:
        num_str = entry.get()
        num = int(num_str)
        if num < 1:
            messagebox.showinfo("결과", "1 이상의 숫자를 입력해주세요.")
        else:
            total = sum(range(1, num + 1))
            messagebox.showinfo("결과", f"1부터 {num}까지의 합은 {total}입니다.")
    except ValueError:
        messagebox.showerror("오류", "잘못된 입력입니다. 숫자를 입력해주세요.")

# GUI 생성
window = tk.Tk()
window.title("합계 계산기")
window.geometry("300x150")

label = tk.Label(window, text="숫자를 입력하세요:")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=5)

button = tk.Button(window, text="계산", command=calculate_sum)
button.pack(pady=10)

window.mainloop()