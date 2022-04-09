import tkinter as tk
import time


class TrafficLight:

    def __init__(self, parent, red_seconds, yellow_seconds, green_seconds):
        self.root = tk.Toplevel(parent)
        self.root.title('Traffic light')
        self.root.geometry('300x500+700+300')
        self.root.resizable(False, False)

        self.red_seconds = red_seconds
        self.yellow_seconds = yellow_seconds
        self.green_seconds = green_seconds

        self.canvas = tk.Canvas(self.root, width=160, height=380)
        self.circle_red = self.canvas.create_oval(30, 30, 130, 130, fill="red", width=2)
        self.circle_yellow = self.canvas.create_oval(30, 140, 130, 240, fill="yellow", width=2)
        self.circle_green = self.canvas.create_oval(30, 250, 130, 350, fill="green", width=2)


    # после паузы стираем предидущий кружок, рисуем следующий и обновляем
    def draw_red(self):
        self.circle_red = self.canvas.create_oval(30, 30, 130, 130, fill="red", width=2)
        self.canvas.update()

    # после паузы стираем предидущий кружок, рисуем следующий и обновляем
    def draw_yellow(self):
        time.sleep(self.red_seconds)
        self.canvas.delete(self.circle_red)
        self.circle_yellow = self.canvas.create_oval(30, 140, 130, 240, fill="yellow", width=2)
        self.canvas.update()

    # после паузы стираем предидущий кружок, рисуем следующий и обновляем
    def draw_green(self):
        time.sleep(self.yellow_seconds)
        self.canvas.delete(self.circle_yellow)
        self.circle_green = self.canvas.create_oval(30, 250, 130, 350, fill="green", width=2)
        self.canvas.update()

    # после паузы стираем предидущий кружок, рисуем кнопку выхода и обновляем
    def draw_button(self):
        time.sleep(self.green_seconds)
        self.canvas.delete(self.circle_green)
        exit_button = tk.Button(self.root, text='EXIT', width=20, height=2, bg='white', command=self.root.destroy)
        exit_button.pack()
        self.canvas.update()

    def run(self):
        self.canvas.pack()
        self.canvas.create_rectangle(20, 20, 140, 360, fill="black")
        self.draw_red()
        self.draw_yellow()
        self.draw_green()
        self.draw_button()


if __name__ == '__main__':
    window = TrafficLight(tk.Tk(), 2, 2, 2)
    window.run()
