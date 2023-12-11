from itertools import cycle

from django.http import HttpResponse

from pyArango.connection import *
from pyArango.theExceptions import CreationError

names = cycle(['simba', 'mufasa', 'rafiki', 'nala', 'surabi', 'pumba', 'timon'])


def test_graph(request):
    conn = Connection(arangoURL='http://arangodb:8529')
    try:
        db = conn.createDatabase(name='test_db')
    except CreationError:
        db = conn['test_db']
    try:
        collection = db.createCollection(name='users')
    except CreationError:
        collection = db['users']
    for i in range(20):
        name = next(names)
        doc = collection.createDocument()
        doc['name'] = f'{name} {i}'
        doc['number'] = i
        doc['species'] = 'human'
        doc.save()
    doc = collection.createDocument()
    doc['name'] = 'Tesla-101'
    doc['number'] = 101
    doc['species'] = 'human'
    doc['name'] = 'Simba'
    # doc.patch()
    # doc.delete()
    example = {'species': 'human'}
    query = collection.fetchByExample(example, batchSize=20, count=True)
    results = [x['name'] for x in query]
    return HttpResponse(results)
