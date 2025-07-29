# S&Path
## App to find most private and safe path

**Path‑S** is a small Python utility that finds a route between two geographic
points while weighting edges so the route is either

* **private** – minimises CCTV exposure;
* **safe** – prefers well‑lit/observed areas, with an adjustable weight factor.

It works on a pre‑built GraphML street graph (`editedgraph.graphml`)
and a CSV of camera coordinates (`cams.csv`).

---

## Features

* Shortest‑path search via **NetworkX**
* Two weighting modes: `private` and `safe`
* Optional safety factor (`pf.set_weights('safe', factor)`)
* Quick Matplotlib visualisation of the route
* Few external dependencies

---

## Installation

```bash
git clone https://github.com/danzzzlll/Path-S.git
cd Path-S
pip install -r requirements.txt
```

## Usage example

```python
#  example
from main import PathFinder

cams_path = 'cams.csv'
boarders = [55.756216, 55.768715, 37.596696, 37.628496]
G_path = 'editedgraph.graphml'
pf = PathFinder(boarders, cams_path, G_path)

origin = [55.764661, 37.604708]
end = [55.759570, 37.625882]

pf.set_weights('private')
path = pf.get_path_by_points([origin, end])
pf.plot_path(path)

pf.set_weights('safe')
path = pf.get_path_by_points([origin, end])
pf.plot_path(path)

pf.set_weights('safe', 0.2)
path = pf.get_path_by_points([origin, end])
pf.plot_path(path)
```
