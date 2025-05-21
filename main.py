import random
import time
import tkinter as tk
from tkinter import messagebox

# Символи для барабанів
symbols = ["🍒", "🍋", "🔔", "💎", "7️⃣", "⭐"]

# Налаштування гри
START_BALANCE = 100
BET = 10
SPIN_DELAY = 100  # мс між змінами символів під час "анімації"

class SlotMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎰 Слоти Казино")
        self.balance = START_BALANCE

        self.setup_ui()

    def setup_ui(self):
        self.root.configure(bg="#222")

        self.balance_label = tk.Label(self.root, text=f"💰 Баланс: {self.balance}", font=("Arial", 16),
                                      fg="white", bg="#222")
        self.balance_label.pack(pady=10)

        self.reel_frame = tk.Frame(self.root, bg="#222")
        self.reel_frame.pack(pady=20)

        self.reels = [tk.Label(self.reel_frame, text="❔", font=("Arial", 50), fg="white", bg="#333", width=2)
                      for _ in range(3)]
        for reel in self.reels:
            reel.pack(side=tk.LEFT, padx=10)

        self.spin_button = tk.Button(self.root, text="Крутити 🎲", font=("Arial", 16), command=self.start_spin,
                                     bg="#28a745", fg="white", width=15)
        self.spin_button.pack(pady=20)

    def start_spin(self):
        if self.balance < BET:
            messagebox.showwarning("Недостатньо коштів", "У вас недостатньо монет для нової ставки.")
            return

        self.balance -= BET
        self.update_balance()

        self.spin_button.config(state=tk.DISABLED)
        self.animate_reels(0, 10)  # 10 кроків "анімації"

    def animate_reels(self, step, max_steps):
        if step < max_steps:
            for reel in self.reels:
                reel.config(text=random.choice(symbols))
            self.root.after(SPIN_DELAY, lambda: self.animate_reels(step + 1, max_steps))
        else:
            final_symbols = [random.choice(symbols) for _ in range(3)]
            for i in range(3):
                self.reels[i].config(text=final_symbols[i])
            self.check_result(final_symbols)
            self.spin_button.config(state=tk.NORMAL)

    def check_result(self, symbols_result):
        if symbols_result[0] == symbols_result[1] == symbols_result[2]:
            winnings = BET * 10
            self.balance += winnings
            messagebox.showinfo("🎉 Виграш!", f"Ви виграли {winnings} монет!")
        else:
            messagebox.showinfo("😢 Програш", "Спробуйте ще раз!")
        self.update_balance()

    def update_balance(self):
        self.balance_label.config(text=f"💰 Баланс: {self.balance}")

# Запуск програми
root = tk.Tk()
app = SlotMachineApp(root)
root.mainloop()
