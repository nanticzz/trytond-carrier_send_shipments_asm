# This file is part of the carrier_send_shipments_asm module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

import logging

try:
    from asm.picking import *
except ImportError:
    message = 'Install ASM from Pypi: pip install asm'
    logging.getLogger('asm').error(message)
    raise Exception(message)

__all__ = ['CarrierApi']
__metaclass__ = PoolMeta


class CarrierApi:
    __name__ = 'carrier.api'

    @classmethod
    def get_carrier_app(cls):
        '''
        Add Carrier ASM APP
        '''
        res = super(CarrierApi, cls).get_carrier_app()
        res.append(('asm', 'ASM'))
        return res

    def test_asm(self, api):
        '''
        Test ASM connection
        :param api: obj
        '''
        message = 'Connection unknown result'
        
        with API(api.username, api.debug) as asm_api:
            message = asm_api.test_connection()
        self.raise_user_error(message)
