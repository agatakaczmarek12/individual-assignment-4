# -*- coding: utf-8 -*-

#%% Excersise 1 & 2


graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["d"],
    "d": ["e"],
    "e": [],
    "f": []
}

import requests

url = 'http://127.0.0.1:5000/{}'

def upload_graph(graph): 
    data = graph
    request = requests.post(url .format('upload-graph'), json=data)
    
    return request.json()



def get_degrees_of_separation(origin, destination, graph): 
    data = graph
    request = requests.put('http://127.0.0.1:5000/degrees-of-separation/{}/{}'.format(origin, destination) , json=data)
    
    return request.json()

