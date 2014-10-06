
# TODO: naming

import socket
from contextlib import closing

from passage.way import Passageway
from passage.connections import connect

import messages as M

DEFAULT_BUREAUCRAT_PATH = 'bureaucrat.sock'


class WorkerClient(object):

    def __init__(self, bc_path=None):
        self.bc_path = bc_path or DEFAULT_BUREAUCRAT_PATH

    def request_socket(self, family, type, proto, host, port):
        with closing(connect(self.bc_path)) as uds:
            passage_way = Passageway()

            M._sendall(uds, M.WantSocket(family, type, proto, host, port))

            response, _ = M._recvall(uds)

            assert isinstance(response, M.HaveSocket)
            assert response == (family, type, proto, host, port)

            return passage_way.obtain(uds, socket.socket)

    def request_channel(self, identity, partner):
        with closing(connect(self.bc_path)) as uds:
            passage_way = Passageway()

            M._sendall(uds, M.WantChannel(identity, partner))

            response, _ = M._recvall(uds)

            assert isinstance(response, M.HaveChannel)
            assert response == (identity, partner)
            return passage_way.obtain(uds, socket.socket)
