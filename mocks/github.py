# -*- coding: utf-8 -*-

"""
Mocks for the Github API library tests.

"""


from httmock import response, urlmatch


NETLOC = r'(.*\.)?api\.github\.com$'
HEADERS = {'content-type': 'application/json'}
GET = 'get'


@urlmatch(netloc=NETLOC, path='/repos', method=GET)
def repository(url, request):
    name = url.path.split('/')[-1]
    content = {'name': name}
    return response(200, content, HEADERS, None, 5, request)
