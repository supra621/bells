from django.http import HttpResponse

from pyArango.connection import *


def test_graph(request):
    conn = Connection(arangoURL='http://arangodb:8529')
    # conn.createDatabase(name='test_db')
    db = conn['test_db']
    # collection = db.createCollection(name='users')
    collection = db['users']
    for i in range(20):
        doc = collection.createDocument()
        doc['name'] = f'Tesla {i}'
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
    results = [x for x in query]
    return HttpResponse(results)
