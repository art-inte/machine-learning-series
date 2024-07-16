import os
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont

if __name__ == '__main__':
    canvas = PIL.Image.new('RGB', (2000, 1200), (255, 255, 255))
    draw = PIL.ImageDraw.Draw(canvas)

    center = (canvas.width // 2, canvas.height // 2)
    radius = 500
    draw.line((center[0] - radius, center[1], center[0] + radius, center[1]),
              fill='black', width=2)
    draw.ellipse((center[0] - radius, center[1] - radius,
                  center[0] + radius, center[1] + radius),
                  outline='blue',
                  width=30)
    draw.line((center[0] - radius - 300, center[1], center[0] - radius, center[1]),
              fill='black', width=20)
    draw.line((center[0] + radius, center[1], center[0] + radius + 300, center[1]),
              fill='black', width=20)
    draw.rectangle((center[0] - 300, center[1] - 100, center[0] - 100, center[1] + 100),
                   outline='black', fill='red', width=2)
    font = PIL.ImageFont.load_default().font_variant(size=96)
    draw.text((center[0] - 250, center[1] - 60), 'W', fill="white", font=font)
    draw.polygon([(center[0] + 100, center[1] + 100),
                  (center[0] + 200, center[1] - 100),
                  (center[0] + 300, center[1] + 100)],
                  outline='black', fill='green', width=2)
    draw.text((center[0] + 170, center[1] - 40), 'b', fill='white', font=font)
    draw.text((center[0] - radius - 200, center[1] - 150), 'x', fill='black', font=font)
    draw.text((center[0] + radius + 200, center[1] - 150), 'y', fill='black', font=font)
    draw.text((center[0] - 250, center[1] - 250), 'y = W * x + b', fill='black', font=font)
    save_path = 'temp/neuron.png'
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    canvas.save(save_path)
    canvas.show()
