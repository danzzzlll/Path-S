from fastapi import FastAPI
from main import PathFinder
from typing import Optional
import json

cams_path = 'cams.csv'
boarders = [55.756216, 55.768715, 37.596696, 37.628496]
G_path = 'editedgraph.graphml'
pf = PathFinder(boarders, cams_path, G_path)

app = FastAPI()

@app.get("/route/{mode}/{pts}")
def read_item(mode: str, pts, i: Optional[float] = 0.5):
    pf.set_weights(mode, i)
    points = json.loads(pts)
    path = pf.get_path_by_points(points)
    return json.dumps(path)
