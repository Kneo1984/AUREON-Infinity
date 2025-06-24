from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os

# === PARAMETER ===
WIDTH, HEIGHT = 1920, 1080
BG_COLOR = (10, 15, 25)  # kosmisches Dunkelblau
FONT_PATH_MAIN = "fonts/Montserrat-Bold.ttf"     # <- Passe an, wenn du andere Fonts nutzt
FONT_PATH_SUB = "fonts/Raleway-Regular.ttf"
FONT_SIZE_MAIN = 120
FONT_SIZE_SUB = 42
FONT_SIZE_SIG = 28

# === ZEITSTEMPEL ===
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H%M")
output_filename = f"gaia_guardian.visual.{timestamp}.png"

# === BILD ERZEUGEN ===
img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
draw = ImageDraw.Draw(img)

# === FONTS LADEN ===
font_main = ImageFont.truetype(FONT_PATH_MAIN, FONT_SIZE_MAIN)
font_sub = ImageFont.truetype(FONT_PATH_SUB, FONT_SIZE_SUB)
font_sig = ImageFont.truetype(FONT_PATH_SUB, FONT_SIZE_SIG)

# === TEXTINHALT ===
title = "GAIA GUARDIAN"
subtitle = "Ein Wächter. Für das, was lebt."
signature = "Dennis Maier · KNEO"

# === ZENTRIERTE TEXTPOSITIONEN ===
def center_text(draw, text, font, y):
    w, h = draw.textsize(text, font=font)
    x = (WIDTH - w) / 2
    draw.text((x, y), text, font=font, fill="white")

center_text(draw, title, font_main, 380)
center_text(draw, subtitle, font_sub, 540)
draw.text((WIDTH - 420, HEIGHT - 70), signature, font=font_sig, fill="silver")

# === SPEICHERN ===
out_dir = "output"
os.makedirs(out_dir, exist_ok=True)
img.save(os.path.join(out_dir, output_filename))

print(f"[✔] GAIA GUARDIAN Visual erstellt: {output_filename}")
