from django.http import HttpResponse
from django.shortcuts import render

from gremlin_python import statics
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.process.graph_traversal import __
from gremlin_python.structure.graph import Graph


def test_graph(request):
    connection = DriverRemoteConnection('ws://janusgraph:8182/gremlin', 'g')
    g = traversal().withRemote(connection)
    hercules_age = g.V().has('name', 'hercules').values('age').to_list()
    return HttpResponse(f'Hercules is {hercules_age} years old.')
