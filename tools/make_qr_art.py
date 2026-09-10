from pathlib import Path

import qrcode
from PIL import Image, ImageDraw

OUT = Path(r"d:\Projects\Arch\archsys-web\public\assets\screenshots\qr-identificacion.png")
NAVY = (10, 40, 64)
BLUE = (21, 111, 179)
MID = (18, 62, 106)
WHITE = (255, 255, 255)
INK = (12, 28, 65)


def elevator_icon(size=220):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    m = 18
    d.rounded_rectangle((m, 8, size - m, size - 10), 18, fill=NAVY)
    d.rounded_rectangle((m + 10, 22, size - m - 10, size - 28), 8, fill=(232, 238, 244))
    mid = size // 2
    d.rectangle((mid - 3, 22, mid + 3, size - 28), fill=BLUE)
    d.ellipse((mid - 9, size // 2 - 8, mid + 9, size // 2 + 10), fill=BLUE)
    d.rounded_rectangle((m + 56, 14, size - m - 56, 26), 4, fill=(56, 165, 255))
    return img


def main():
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=12, border=2)
    qr.add_data("https://www.archsys.com.ar")
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color=INK, back_color=WHITE).convert("RGBA")
    qr_img = qr_img.resize((420, 420), Image.Resampling.NEAREST)

    icon = elevator_icon(92)
    box = ((qr_img.width - icon.width) // 2, (qr_img.height - icon.height) // 2)
    pad = Image.new("RGBA", (icon.width + 16, icon.height + 16), WHITE)
    qr_img.paste(pad, (box[0] - 8, box[1] - 8))
    qr_img.paste(icon, box, icon)

    w, h = 720, 960
    canvas = Image.new("RGB", (w, h), WHITE)
    draw = ImageDraw.Draw(canvas)
    draw.rectangle((0, 0, w, 220), fill=NAVY)
    draw.polygon([(0, 180), (w, 140), (w, 240), (0, 260)], fill=MID)
    draw.ellipse((w - 260, -80, w + 80, 260), outline=(21, 111, 179, 40), width=18)

    card = Image.new("RGB", (560, 640), WHITE)
    cd = ImageDraw.Draw(card)
    cd.rounded_rectangle((0, 0, 559, 639), 28, outline=(228, 232, 236), width=2)
    card.paste(qr_img, ((560 - 420) // 2, 70), qr_img)
    cd.rounded_rectangle((150, 530, 410, 578), 20, fill=BLUE)
    try:
        from PIL import ImageFont
        font = ImageFont.truetype("arial.ttf", 22)
    except Exception:
        font = ImageDraw.ImageDraw(card).getfont()
    cd.text((280, 554), "E01  ·  ARCH", fill=WHITE, font=font, anchor="mm")
    cd.rectangle((0, 0, 8, 639), fill=BLUE)

    canvas.paste(card, ((w - 560) // 2, 240))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(OUT, "PNG")
    print("wrote", OUT, OUT.stat().st_size)


if __name__ == "__main__":
    main()
