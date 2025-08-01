#!/usr/bin/env python3
#
# Copyright (c) 2016-2018, Neil Booth
#
# All rights reserved.
#
# See the file "LICENCE" for information about the copyright
# and warranty status of this software.

'''Script to kick off the server.'''

import asyncio
import logging
import sys

import electrumx
from electrumx import Controller, Env
from electrumx.lib.util import CompactFormatter, make_logger


def main():
    '''Set up logging and run the server.'''
    log_fmt = Env.default('LOG_FORMAT', '%(levelname)s:%(name)s:%(message)s')
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(CompactFormatter(log_fmt))
    logger = make_logger('electrumx', handler=handler, level='INFO')

    logger.info(
        f'ElectrumX server starting. '
        f'({electrumx.BRANDING}. version={electrumx.__version__})')
    try:
        if sys.version_info < (3, 10):
            raise RuntimeError('ElectrumX requires Python 3.10 or greater')
        env = Env()
        logger.info(f'logging level: {env.log_level}')
        logger.setLevel(env.log_level)
        controller = Controller(env)
        asyncio.run(controller.run())
    except Exception:
        logger.exception('ElectrumX server terminated abnormally')
    else:
        logger.info('ElectrumX server terminated normally')


if __name__ == '__main__':
    main()
