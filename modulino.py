from modulino import ModulinoButtons, ModulinoPixels
import time

buttons = ModulinoButtons()
pixels = ModulinoPixels()

buttons.set_led_status(True, True, True)

# Zustände für jede Farbe
leds_blue_on = False
leds_red_on = False
leds_green_on = False

# Funktion: LEDs langsam einschalten
def fade_in(color):
    for i in range(8):
        pixels.set_rgb(i, *color)
        pixels.show()
        time.sleep(0.2)

# Funktion: LEDs langsam ausschalten
def fade_out():
    for i in reversed(range(8)):
        pixels.set_rgb(i, 0, 0, 0)
        pixels.show()
        time.sleep(0.2)

# ---------- BUTTON A (Blau) ----------
def button_function_a ():
    global leds_blue_on, leds_red_on, leds_green_on   # Global um den Zustand von der Variable led zu ändern (oben definiert)
    if not leds_blue_on:
        print("Button A gedrückt – Blau an")
        fade_in((0, 0, 255))                          # fade_in = Funktionsaufruf led einschalten
        leds_blue_on = True
        leds_red_on = leds_green_on = False
    else:
        print("Button A gedrückt – Blau aus")
        fade_out()                                    # fade_out = Funktionsaufruf led ausschalten
        leds_blue_on = False

# ---------- BUTTON B (Rot) ----------
def button_function_b ():
    global leds_blue_on, leds_red_on, leds_green_on   # Global um den Zustand von der Variable led zu ändern (oben definiert)
    if not leds_red_on:
        print("Button B gedrückt – Rot an")
        fade_in((255, 0, 0))                          # fade_in = Funktionsaufruf led einschalten
        leds_red_on = True
        leds_blue_on = leds_green_on = False
    else:
        print("Button B gedrückt – Rot aus")
        fade_out()                                    # fade_out = Funktionsaufruf led ausschalten
        leds_red_on = False

# ---------- BUTTON C (Grün) ----------
def button_function_c ():
    global leds_blue_on, leds_red_on, leds_green_on   # Global um den Zustand von der Variable led zu ändern (oben definiert)
    if not leds_green_on:
        print("Button C gedrückt – Grün an")
        fade_in((0, 255, 0))                          # fade_in = Funktionsaufruf led einschalten
        leds_green_on = True
        leds_blue_on = leds_red_on = False
    else:
        print("Button C gedrückt – Grün aus")
        fade_out()                                    # fade_out = Funktionsaufruf led ausschalten
        leds_green_on = False

# Button-Funktions zuweisung
buttons.on_button_a_press = button_function_a         # buttons.on_button_a_press ist das modulino vordefinierte Attribute um Aktionen wahrzunehmen an diesem Button.
buttons.on_button_b_press = button_function_b 
buttons.on_button_c_press = button_function_c 

# Hauptloop
while True:
    buttons.update()         # Prüft ständig ob eine neuer Button gedrückt wurde

