import tkinter as tk
from PIL import Image, ImageTk # type: ignore
import pyttsx3 # type: ignore
import threading
import time

from parking_logic import calculate_distance


WINDOW_W = 1200
WINDOW_H = 700

# Center of Slot 22
SLOT_X = 900
SLOT_Y = 280

# Virtual car position
view_x = 0
view_y = 80
zoom = 1.0

engine = pyttsx3.init()
last_voice = ""


class SmartParking:

    def __init__(self, root):
        self.root = root
        self.root.title("Smart Parking Assistance System")
        self.canvas = tk.Canvas(
            root,
            width=WINDOW_W,
            height=WINDOW_H
        )
        self.canvas.pack()
        root.bind("t", self.run_test)

        # Dashboard Overlay
        overlay = Image.open("dashboard_overlay.png").convert("RGBA")
        overlay = overlay.resize((WINDOW_W, WINDOW_H))
        self.overlay_photo = ImageTk.PhotoImage(overlay)
        self.bg_item = self.canvas.create_image(0, 0, anchor="nw")
        self.draw_scene()
    
        overlay = Image.open("dashboard_overlay.png").convert("RGBA")
        overlay = overlay.resize((WINDOW_W, WINDOW_H))
        self.overlay_photo = ImageTk.PhotoImage(overlay)
        self.overlay_item = self.canvas.create_image(0, 0, image=self.overlay_photo, anchor="nw")
       
        self.distance_text = self.canvas.create_text(
            1084,148,
            text="0",
            fill="#00FFFF",
            font=("Arial",18,"bold")
        )

        self.direction_text = self.canvas.create_text(
            1108,208,
            text="",
            fill="#00FFFF",
            font=("Arial",14,"bold")
        )

        self.zone_text = self.canvas.create_text(
            1110,265,
            text="",
            fill="white",
            font=("Arial",15,"bold")
        )

        self.status_text = self.canvas.create_text(
            1085,320,
            text="",
            fill="#00FFFF",
            font=("Arial",14,"bold")
        )

        self.score_text = self.canvas.create_text(
            1115,375,
            text="",
            fill="#00FFFF",
            font=("Arial",20,"bold")
        )
        root.bind("<Left>", self.left)
        root.bind("<Right>", self.right)
        root.bind("<Up>", self.up)
        root.bind("<Down>", self.down)

        self.update_dashboard()
        self.voice_message = "Move towards slot twenty two"
        self.voice_loop()   
        
    
    
    # Draw the parking scene based on current view and zoom level
    def draw_scene(self):
        img = Image.open("camera_scene.png")
        crop_w = int(1200 / zoom)
        crop_h = int(700 / zoom)
        max_x = img.width - crop_w
        max_y = img.height - crop_h
        x = max(0, min(view_x, max_x))
        y = max(0, min(view_y, max_y))
        img = img.crop(
            (
                x,
                y,
                x + crop_w,
                y + crop_h
            )
        )
        img = img.resize(
            (1200,700),
            Image.LANCZOS
        )
        self.bg_photo = ImageTk.PhotoImage(img)
        self.canvas.itemconfig(
            self.bg_item,
            image=self.bg_photo
        )
        
    # Periodically update voice feedback
    def voice_loop(self):
        if self.voice_message:
            self.speak(self.voice_message)
        self.root.after(
            4000,
            self.voice_loop
        )

    # Voice feedback for parking status and direction
    def speak(self, text):
        def run():
            try:
                engine = pyttsx3.init()
                engine.setProperty("rate", 160)
                engine.say(text)
                engine.runAndWait()
            except:
                pass
        threading.Thread(
            target=run,
            daemon=True
        ).start()
        
    
    # Simulate car movement and view adjustment
    def left(self,event):
        global view_x
        view_x -= 40
        self.draw_scene()
        self.update_dashboard()

    def right(self,event):
        global view_x
        view_x += 40
        self.draw_scene()
        self.update_dashboard()

    def up(self,event):
        global zoom
        zoom -= 0.15
        zoom = max(zoom,1.0)
        self.draw_scene()
        self.update_dashboard()

    def down(self,event):
        global zoom
        global view_x
        zoom += 0.15
        zoom = min(zoom,4.0)
        view_x += 20
        self.draw_scene()
        self.update_dashboard()

    def update_dashboard(self):
        global zoom
        distance = int(
                max(
                    0,
                    1600 - (zoom * 400)
                )
            )

        if zoom < 1.5:
            direction = "TURN RIGHT"
        elif zoom < 2.5:
            direction = "ALIGN SLOT"
        else:
            direction = "STRAIGHT"
            
        if zoom >= 3.5:
            status = "PARKED"
        elif zoom >= 2.8:
            status = "ALIGN SLOT"
        elif zoom >= 1.8:
            status = "APPROACHING"
        else:
            status = "SEARCHING"

        if zoom >= 3.0:
            zone = "GREEN"
        elif zoom >= 2.0:
            zone = "YELLOW"
        else:
            zone = "RED"

        score = min(
            100,
            int((zoom - 1.0) * 33)
        )

        self.canvas.itemconfig(
            self.distance_text,
            text=f"{distance}px"
        )

        self.canvas.itemconfig(
            self.direction_text,
            text=direction
        )

        zone_color = "green"
        if zone == "RED":
            zone_color = "red"
        elif zone == "YELLOW":
            zone_color = "yellow"
        elif zone == "GREEN":
            zone_color = "#00ff00"
        self.canvas.itemconfig(
            self.zone_text,
            text=zone,
            fill=zone_color
        )

        self.canvas.itemconfig(
            self.status_text,
            text=status
        )

        self.canvas.itemconfig(
            self.score_text,
            text=f"{score}%"
        )

        if status == "PARKED":
            self.voice_message = "Parking complete"
            if not hasattr(self, "parking_announced"):
                self.parking_announced = False
            if not self.parking_announced:
                self.parking_announced = True
                self.speak("Parking complete")
        else:
            self.parking_announced = False
          
            
        if status == "PARKED":
            self.voice_message = "Parking complete"
        elif status == "ALIGN SLOT":
            self.voice_message = "Slow down. Align with slot twenty two."
        elif direction == "TURN RIGHT":
            self.voice_message = "Turn right"
        elif direction == "TURN LEFT":
            self.voice_message = "Turn left"
        elif status == "APPROACHING":
            self.voice_message = "Continue reversing"
        else:
            self.voice_message = "Move towards slot twenty two"
            
    
    def run_test(self, event=None):
        distance = calculate_distance(900,280,900,280)
        print("Distance Test:", distance)
        if distance == 0:
            print("PASS")
        else:
            print("FAIL")



root = tk.Tk()
app = SmartParking(root)
root.mainloop()