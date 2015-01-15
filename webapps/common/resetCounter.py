#!/usr/bin/env python

from lib import dummy
from redis import Redis

print dummy.dummy()

with open('/code/key_name.txt') as f:
    config = f.read().strip()
    redis = Redis(host='redis_1', port=6379)
    redis.set(config, 0)
    print 'Reset %s counter' % config
