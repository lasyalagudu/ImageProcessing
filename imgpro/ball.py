import tkinter as tk

class BouncingBallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bouncing Ball with Count")

        self.canvas = tk.Canvas(root, width=400, height=300, bg="white")
        self.canvas.pack()

        self.ball = self.canvas.create_oval(175, 10, 225, 50, fill="blue")

        self.dy = 3

        self.bounce_count = 0
        self.bounce_label = tk.Label(root, text="Bounces: 0")
        self.bounce_label.pack()

        self.update_bounce_count()
        self.animate_ball()

    def animate_ball(self):
        coords = self.canvas.coords(self.ball)
        if coords[1] <= 0 or coords[3] >= self.canvas.winfo_height():
            self.dy = -self.dy
            self.bounce_count += 1
            self.update_bounce_count()

        self.canvas.move(self.ball, 0, self.dy)
        self.root.after(20, self.animate_ball)

    def update_bounce_count(self):
        self.bounce_label.config(text=f"Bounces: {self.bounce_count-2}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BouncingBallApp(root)
    root.mainloop()
