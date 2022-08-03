#!/usr/bin/python3

import log
import view



logger = log.Log('foo.log')


view.init(logger)

logger.get_event('Hello world!')