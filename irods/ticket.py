from __future__ import absolute_import
from irods.api_number import api_number
from irods.message import (
    iRODSMessage, TicketAdminRequest)

import logging

logger = logging.getLogger(__name__)


class Ticket(object):
    def __init__(self, ticket_str=None):
        self._ticket = ticket_str

    @property
    def ticket(self):
        return self._ticket

    def set_for_session(self, session):
        message_body = TicketAdminRequest("session", self.ticket)
        message = iRODSMessage("RODS_API_REQ", msg=message_body, int_info=api_number['TICKET_ADMIN_AN'])

        with session.pool.get_connection() as conn:
            conn.send(message)
            response = conn.recv()
