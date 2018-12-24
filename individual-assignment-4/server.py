# -*- coding: utf-8 -*-

 #%% Excersise 1&2

from flask import Flask, jsonify, request
server = Flask("Server Running on port 5000")

@server.route('/upload-graph', methods=['POST'])
def upload_graph():
    body = request.get_json()
    return jsonify(body)


@server.route('/degrees-of-separation/<origin>/<destination>', methods=['PUT'])
def find_path(origin, destination, graph='', path=[]):


    graph = request.get_json()

    graph = jsonify(graph)


    path = path + [origin]


    
    if origin == destination:
        return jsonify(path)

    
    if origin not in graph:
        return jsonify(None)

    
    for node in graph[origin]:
        
        if node not in path:
            
            newpath = find_path(node, destination, graph, path)

            
            if newpath is not None:

server.run()