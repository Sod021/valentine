import random
import tkinter as tk
from tkinter import font


class ValentineApp(tk.Tk):
    """A lightweight Tkinter recreation of the Valentine interaction."""

    def __init__(self):
        super().__init__()
        self.title("Will you be my Valentine?")
        self.configure(bg="white")
        self.geometry("480x640")
        self.resizable(False, False)

        self.shake_count = 0
        self.no_click_count = 0
        self.shake_scale_step = 0.12
        self.no_scale_multiplier = 1.3

        self.yes_font = font.Font(family="Segoe UI", size=14, weight="bold")

        self.question_frame = tk.Frame(self, bg="white")
        self.celebration_frame = tk.Frame(self, bg="white")

        self._build_question_screen()
        self._build_celebration_screen()

        self.question_frame.pack(expand=True, fill="both")

    def _build_question_screen(self):
        heading = tk.Label(
            self.question_frame,
            text="Will you be my Valentine?",
            font=("Segoe UI", 22, "bold"),
            bg="white",
            fg="#1f1b2d",
        )
        heading.pack(pady=(40, 10))

        subtitle = tk.Label(
            self.question_frame,
            text="Click yes to make my heart skip a beat.",
            font=("Segoe UI", 12),
            bg="white",
            fg="#555",
        )
        subtitle.pack(pady=(0, 20))

        # Placeholder for the photo—swap the text with an actual PhotoImage if needed.
        thumb = tk.Label(
            self.question_frame,
            text="[Your photo here]",
            font=("Segoe UI", 10),
            bg="white",
            fg="#888",
            width=20,
            height=10,
            relief="groove",
        )
        thumb.pack(pady=(0, 30))

        button_row = tk.Frame(self.question_frame, bg="white")
        button_row.pack()

        self.yes_button = tk.Button(
            button_row,
            text="Yes",
            font=self.yes_font,
            bg="#ff4d6d",
            fg="white",
            activebackground="#ff9fcf",
            activeforeground="white",
            bd=0,
            padx=30,
            pady=10,
            command=self._on_yes,
        )
        self.yes_button.grid(row=0, column=0, padx=10)

        self.no_button = tk.Button(
            button_row,
            text="No",
            font=("Segoe UI", 12, "bold"),
            bg="#16121f",
            fg="#f7c5d6",
            activeforeground="#fff",
            bd=2,
            relief="ridge",
            padx=25,
            pady=10,
            command=self._on_no,
        )
        self.no_button.grid(row=0, column=1, padx=10)

    def _build_celebration_screen(self):
        banner = tk.Label(
            self.celebration_frame,
            text="Yay 🎉🎉🎉❤️❤️💕💕",
            font=("Segoe UI", 24, "bold"),
            bg="white",
            fg="#1f1b2d",
        )
        banner.pack(pady=(80, 10))

        message = tk.Label(
            self.celebration_frame,
            text="Love is in the air!",
            font=("Segoe UI", 14),
            bg="white",
            fg="#222",
        )
        message.pack(pady=(0, 20))

        self.confetti_canvas = tk.Canvas(
            self.celebration_frame,
            width=480,
            height=360,
            bg="white",
            highlightthickness=0,
        )
        self.confetti_canvas.pack()

    def _update_yes_scale(self):
        base_scale = 1 + self.shake_count * self.shake_scale_step
        scale = base_scale * (self.no_scale_multiplier ** self.no_click_count)
        new_size = max(12, int(14 * scale))
        self.yes_font.configure(size=new_size)
        self.yes_button.configure(font=self.yes_font)

    def _on_no(self):
        self.no_click_count += 1
        self._update_yes_scale()

    def _on_yes(self):
        self.shake_count += 2
        self._update_yes_scale()
        self._show_celebration()

    def _show_celebration(self):
        self.question_frame.pack_forget()
        self.celebration_frame.pack(expand=True, fill="both")
        self._launch_confetti(80)

    def _launch_confetti(self, amount=30):
        for _ in range(amount):
            x = random.randint(0, 480)
            y = random.randint(-200, 0)
            size = random.randint(6, 14)
            color = random.choice(
                ["#ff6fb1", "#ff4d6d", "#ffd6a5", "#f7c5d6", "#ffd8e0"]
            )
            piece = self.confetti_canvas.create_oval(
                x, y, x + size, y + size, fill=color, outline=""
            )
            self._animate_confetti(piece, size)
        self.celebration_frame.after(700, lambda: self._launch_confetti(15))

    def _animate_confetti(self, piece, size):
        def step():
            self.confetti_canvas.move(piece, 0, 10)
            coords = self.confetti_canvas.coords(piece)
            if coords and coords[1] < 360:
                self.confetti_canvas.after(40, step)
            else:
                self.confetti_canvas.delete(piece)

        step()


if __name__ == "__main__":
    app = ValentineApp()
    app.mainloop()
