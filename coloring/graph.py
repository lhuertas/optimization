from collections import namedtuple

class Graph(object):
    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict
        self.list_vtx = self.get_vertex_degree()

    def get_vertex_degree(self):
        vtx_array = []
        vtx_tuple = namedtuple("vtx", ['vtx','degree'])
        for vtx in self.__graph_dict.keys():
            adj_vertices = self.__graph_dict[vtx]
            degree = len(adj_vertices) + adj_vertices.count(vtx)
            vtx_array.append(vtx_tuple(vtx, degree))

        return sorted(vtx_array, key=lambda x: x.degree, reverse=True)

    def coloring(self):
        color_dict = {}
        for key in self.__graph_dict.keys():
            color_dict[key] = []

        for vtx, _ in self.list_vtx:
            c=1
            adj_vertices = self.__graph_dict[vtx]
            for adj_vtx in adj_vertices:
                 if c in color_dict[str(adj_vtx)]:
                    c += 1
            color_dict[vtx].append(c)

        return color_dict



if __name__ == '__main__':

    file = "data/gc_20_1"
    with open(file, 'r') as input_data_file:
        input_data = input_data_file.read()

    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    graph = dict()
    nodes = list()
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        print(parts)
        if parts[0] not in graph.keys():
            graph[parts[0]] = []
            nodes.append(parts[0])
        if parts[1] not in graph.keys():
            graph[parts[1]] = []
            nodes.append(parts[1])

        if int(parts[1]) not in graph[parts[0]]:
            graph[parts[0]].append(int(parts[1]))
        if int(parts[0]) not in graph[parts[1]]:
            graph[parts[1]].append(int(parts[0]))
    print(graph)

    net = Graph(graph)
    color_dist = net.coloring()
    color_dist_sorted = {}
    for node in nodes:
        for key in color_dist.keys():
            if key == node:
                color_dist_sorted[key] = color_dist[key]
    solution = [item for sublist in color_dist.values() for item in sublist]



#    for vtx in graph.keys():
#        print(net.vertex_degree(vtx))
