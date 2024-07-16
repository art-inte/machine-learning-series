import networkx
import os
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
import rdkit.Chem
import rdkit.Chem.Draw

if __name__ == '__main__':
    # Cyclohexane (C6H12)
    # Melting point 6.47 °C
    # Boiling point 80.74 °C
    m = rdkit.Chem.MolFromSmiles('Cc1ccccc1')
    # Returns a Mol block for a molecule
    str(rdkit.Chem.MolToMolBlock(m))
    img = rdkit.Chem.Draw.MolToImage(m, size=(600, 600))

    canvas = PIL.Image.new('RGB', (2750, 1000), (255, 255, 255))
    draw = PIL.ImageDraw.Draw(canvas)
    canvas.paste(img, (0, 50))
    font = PIL.ImageFont.load_default().font_variant(size=48)
    draw.text((600, 0), rdkit.Chem.MolToMolBlock(m), fill=(0, 0, 0), font=font)

    draw.rectangle([1850, 400, 1950, 440], fill='cyan')
    draw.polygon([(1920, 360), (1960, 420), (1920, 480)], fill='cyan')

    draw.rectangle([2000, 100, 2400, 800], outline='black', width=3)
    graph = networkx.DiGraph()
    graph.add_nodes_from([str(num) for num in range(1, 6)])
    for input_node in [str(num) for num in range(1, 4)]:
        for output_node in [str(num) for num in range(4, 6)]:
            graph.add_edge(input_node, output_node)

    pos = {
        '1': (1, 3),
        '2': (1, 2),
        '3': (1, 1),
        '4': (2, 2.5),
        '5': (2, 1.5)
    }
    radius = 20
    offset_x = 1900
    offset_y = 60
    scale = 200
    for node in graph.nodes():
        center_x = pos[node][0] * scale + offset_x
        center_y = pos[node][1] * scale + offset_y
        bbox = (center_x - radius, center_y - radius, center_x + radius, center_y + radius)
        draw.ellipse(bbox, outline='green', width=20)
    for edge in graph.edges():
        start_pos = (pos[edge[0]][0] * scale + offset_x, pos[edge[0]][1] * scale + offset_y)
        end_pos = (pos[edge[1]][0] * scale + offset_x, pos[edge[1]][1] * scale + offset_y)
        draw.line([start_pos, end_pos], fill='green', width=2)

    draw.text((2450, 400), 'Output\n[6.47, 80.74]', fill='black', font=font)

    save_path = 'temp/molecules_c6h12.png'
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    canvas.save(save_path)
    canvas.show()
