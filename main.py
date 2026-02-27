from shapely.geometry import Point, LineString
from core.render import save_svg
from core.geom import hidden_line_removal
import numpy as np
import random

def run(params, output_path):
    print("Running 001_hello_world sketch...")
    seed = params.get("seed", 0)
    random.seed(seed)
    np.random.seed(seed)
    
    width = params.get("width", 200)
    height = params.get("height", 200)
    num_lines = params.get("num_lines", 50)
    radius = params.get("circle_radius", 60)
    
    center = Point(width / 2, height / 2)
    # create a circular polygon with high resolution
    circle_poly = center.buffer(radius, resolution=64)
    
    # Generate some random lines that cross the canvas
    lines = []
    for _ in range(num_lines):
        x1 = random.uniform(-50, width+50)
        y1 = random.uniform(-50, height+50)
        x2 = random.uniform(-50, width+50)
        y2 = random.uniform(-50, height+50)
        lines.append(LineString([(x1, y1), (x2, y2)]))
    
    # Use HLR to remove the portions of the lines that fall inside the circle
    visible_lines = hidden_line_removal(lines, [circle_poly])
    
    # Draw the circle outline as well
    final_geometries = [circle_poly.boundary] + visible_lines
    
    save_svg(final_geometries, output_path, width, height)

if __name__ == "__main__":

    import json

    with open("example.json", 'r') as f:
        params = json.load(f)

    run(params, "test.svg")
