# Path-S
## App to find most private and safe path

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
