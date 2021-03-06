#! /usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import logging
import logging.handlers
import sys

try:
  import config.fixbrokendumpsconfig as configModule
except ImportError:
    import fixbrokendumpsconfig as configModule

import socorro.lib.ConfigurationManager as configurationManager
import socorro.cron.fixBrokenDumps as fixBrokenDumps
import socorro.lib.util as sutil

try:
  config = configurationManager.newConfiguration(configurationModule=configModule, applicationName="Fix Broken Dumps")
except configurationManager.NotAnOptionError, x:
  print >>sys.stderr, x
  print >>sys.stderr, "for usage, try --help"
  sys.exit(1)

logger = logging.getLogger("fix_broken_dumps")
logger.setLevel(logging.DEBUG)

sutil.setupLoggingHandlers(logger, config)
sutil.echoConfig(logger, config)

try:
  #last_date_processed = fixBrokenDumps.fix(config, logger, config.brokenFirefoxLinuxQuery, config.brokenFirefoxLinuxFixer)
  #last_date_processed = fixBrokenDumps.fix(config, logger, config.brokenFennecQuery, config.brokenFennecFixer)
  last_date_processed = fixBrokenDumps.fix(config, logger, config.brokenBoot2GeckoQuery, config.brokenBoot2GeckoFixer)

  fixBrokenDumps.save_last_run_date(config, last_date_processed)
  logger.debug('stored last_date_processed: %s' % last_date_processed)
finally:
  logger.info("done.")
