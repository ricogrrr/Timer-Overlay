import tkinter as tk
import keyboard
from datetime import datetime, timedelta

class TimerOverlay:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Timer Overlay")
        
        self.root.attributes('-alpha', 1.0)
        self.root.attributes('-topmost', True)
        
        self.root.overrideredirect(True)
        
        self.root.configure(bg='black')
        self.root.attributes('-transparentcolor', 'black')
        
        self.timer_label = tk.Label(
            self.root,
            text="0.00",
            font=('Arial', 32, 'bold'),
            fg='#00FF00',
            bg='black'
        )
        self.timer_label.pack(padx=25, pady=10)
        
        self.running = False
        self.start_time = None
        self.elapsed_time = timedelta()

        #Change the hotkeys here
        
        keyboard.on_press_key('f5', lambda _: self.start_timer())
        keyboard.on_press_key('f6', lambda _: self.stop_timer())
        keyboard.on_press_key('f7', lambda _: self.reset_timer())
        
        self.position_window()
        
        self.update_timer()
        
    def position_window(self):
        screen_width = self.root.winfo_screenwidth()
        
        window_width = 250
        window_height = 70
        
        x = screen_width - window_width - 20
        y = 20
        
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    def start_timer(self):
        if not self.running:
            self.running = True
            self.start_time = datetime.now() - self.elapsed_time
    
    def stop_timer(self):
        self.running = False
    
    def reset_timer(self):
        self.running = False
        self.elapsed_time = timedelta()
        self.timer_label.config(text="0.00")
    
    def update_timer(self):
        if self.running:
            self.elapsed_time = datetime.now() - self.start_time
            total_seconds = self.elapsed_time.total_seconds()
            
            if total_seconds < 60:
                seconds = int(total_seconds)
                milliseconds = int((total_seconds - seconds) * 100)
                self.timer_label.config(text=f"{seconds}.{milliseconds:02d}")
            else:
                minutes = int(total_seconds // 60)
                seconds = int(total_seconds % 60)
                milliseconds = int((total_seconds - int(total_seconds)) * 100)
                self.timer_label.config(text=f"{minutes}.{seconds:02d}.{milliseconds:02d}")
        
        self.root.after(10, self.update_timer)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    timer = TimerOverlay()
    timer.run() 