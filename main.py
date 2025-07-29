import osmnx as ox
import networkx as nx
import folium
from folium.plugins import HeatMap
import pandas as pd

__all__ = ['PathFinder']

class PathFinder():
    def __init__(self, boarders, cams_path, G_path):
        ll, lh, lgl, lgh = boarders
        cams = pd.read_csv(cams_path)
        cams = cams[(cams['Latitude'] > ll).values & (cams['Latitude'] < lh).values & (cams['Longitude'] < lgh).values & (cams['Longitude'] > lgl).values]
        self.cams = cams.values.tolist()
        G = ox.io.load_graphml(G_path)
        for k, v in G.edges.items():
            if 'penalty' not in v:
                G.edges[k]['penalty'] = G.edges[k]['length']
            else:
                G.edges[k]['penalty'] = 0
        self.G = G
        self.weights_set = False
                
    def set_weights(self, mode='safe', mult=0.5):
        if mode == 'private':
            p = 1
        elif mode == 'safe':
            p = -1
        else:
            raise ValueError('Wrong mode chosen')
        for k, v in self.G.edges.items():
            self.G.edges[k]['weight'] = self.G.edges[k]['length'] ** (1.8 * (1 - mult)) * max(0.00001, self.G.edges[k]['penalty']) ** (1.8 * mult * p)
        self.weights_set = True
            
    def get_path_by_points(self, pts):
        if not self.weights_set:
            raise ValueError('weights not setted')
        path = []
        for i in range(len(pts) - 1):
            origin, end = pts[i], pts[i + 1]
            origin = ox.nearest_nodes(self.G, *origin[::-1])
            end = ox.nearest_nodes(self.G, *end[::-1])
            route = nx.shortest_path(self.G, origin, end, weight='weight')
            path += route[1:]
        path = [[self.G.nodes[loc]['y'], self.G.nodes[loc]['x']] for loc in path]
        return path
    
    def plot_path(self, path, pts):
        m = folium.Map(location=[55.754888, 37.618948])
        HeatMap(self.cams).add_to(m)
        m.add_child(folium.Marker(location=pts[0], icon=folium.Icon(color='red')))
        m.add_child(folium.Marker(location=pts[-1], icon=folium.Icon(color='red')))
        folium.PolyLine(path, color='black', weight=4, opacity=0.9).add_to(m)
        return m


if __name__ == '__main__':
    pass