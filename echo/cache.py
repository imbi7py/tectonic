
# TODO: allow batching with *_many() ops

from tectonic.client import WorkerClient

worker_client = WorkerClient()


def main():
    server = CacheServer(CacheBackend())
    server.serve()


class CacheServer(object):
    def __init__(self, backend):
        self.backend = backend

    def serve(self, bound_socket):
        pass


class CacheBackend(object):
    def __init__(self, initial_data=None):
        self._data = initial_data or {}

    def create(self, key, value, ttl=None, autoupdate=True):
        pass

    def update(self, key, value, ttl=None, autocreate=True):
        pass

    def get(self, key):
        # name: read()?
        pass

    def delete(self, key, silent=True):
        pass

    @classmethod
    def from_file(self, in_file):
        pass

    def to_file(self, out_file):
        pass
