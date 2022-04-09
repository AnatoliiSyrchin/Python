import tkinter as tk
from traffic_light import TrafficLight


class Window:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Duration time')
        self.root.geometry('300x120+300+300')
        self.root.resizable(False, False)

        # запрос времени задержки светофора
        self.red = tk.Label(self.root, text="Enter red light duration:", width=20)
        self.red_time = tk.Entry(self.root, width=5)
        self.red_time.insert(string='7', index='0')

        self.yellow = tk.Label(self.root, text="Enter yellow light duration:", width=20)
        self.yellow_time = tk.Entry(self.root, width=5)
        self.yellow_time.insert(string='2', index='0')

        self.green = tk.Label(self.root, text="Enter green light duration:", width=20)
        self.green_time = tk.Entry(self.root, width=5)
        self.green_time.insert(string='3', index='0')

        # button
        self.start_button = tk.Button(
            self.root, text='Turn the lights on!', width=38, bg='white', command=self.start_traffic)

    # собираем все прорисовки
    def draw_widgets(self):
        self.red.grid(row=0, column=0)
        self.red_time.grid(row=0, column=1, padx=10, pady=5)

        self.yellow.grid(row=1, column=0)
        self.yellow_time.grid(row=1, column=1, padx=10, pady=5)

        self.green.grid(row=2, column=0)
        self.green_time.grid(row=2, column=1, padx=10, pady=5)

        self.start_button.grid(row=3, columnspan=3, padx=10, pady=5)

    # запуск просрисовки
    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    # собираем время задержки и передаем светофору
    def start_traffic(self):
        red_seconds = int(self.red_time.get())
        yellow_seconds = int(self.yellow_time.get())
        green_seconds = int(self.green_time.get())
        window.create_traffic_light(red_seconds, yellow_seconds, green_seconds)

    # запускаем второе окно со светофором
    def create_traffic_light(self, red_seconds, yellow_seconds, green_seconds):
        traffic = TrafficLight(self.root, red_seconds, yellow_seconds, green_seconds)
        traffic.run()


if __name__ == '__main__':
    window = Window()
    window.run()

