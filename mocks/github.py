# -*- coding: utf-8 -*-

"""
Mocks for the Github API library tests.

"""


from httmock import response, urlmatch


NETLOC = r'(.*\.)?api\.github\.com$'
HEADERS = {'content-type': 'application/json'}
GET = 'get'


class Resource:
    """ A GitHub resource.

    :param path: The file path to the resource.

    """

    def __init__(self, path):
        self.path = path

    def get(self):
        """ Perform a GET request on the resource.

        :rtype: str

        """
        with open(self.path, 'r') as f:
            content = f.read()
        return content


@urlmatch(netloc=NETLOC, method=GET)
def resource_get(url, request):
    file_path = url.netloc + url.path
    try:
        content = Resource(file_path).get()
    except EnvironmentError:
        # catch any environment errors (i.e. file does not exist) and return a
        # 404.
        return response(404, {}, HEADERS, None, 5, request)
    return response(200, content, HEADERS, None, 5, request)
