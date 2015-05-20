from mapzen.cache import Notifier
from mapzen.cache import S3
from redis import StrictRedis
from tilequeue.cache import RedisCacheIndex
from tilequeue.tile import serialize_coord
import sys
import traceback


class OnCacheSave(object):

    def __init__(self, redis_cache_index):
        self.redis_cache_index = redis_cache_index

    def __call__(self, data):
        # cache_data has keys: body, layer, coord, format
        # in case more are needed later
        coord = data.get('coord')
        assert coord is not None, 'Missing coord in on save cache notification'
        coord_str = serialize_coord(coord)
        try:
            self.redis_cache_index.index_coord(coord)
            print 'Added to tiles of interest: %s' % coord_str
        except:
            print >> sys.stderr, \
                'Error adding to tiles of interest: %s' % coord_str
            traceback.print_exc(file=sys.stderr)


def make_redis_client(host, port, db):
    assert host, 'Missing redis host'
    assert port, 'Missing redis port'
    redis_client = StrictRedis(host, port, db)
    return redis_client


def make_tilestache_s3_cache(
        bucket=None, access=None, secret=None, use_locks=False, path='',
        reduced_redundancy=True, gzip_formats=None,
        redis_host=None, redis_port=6379, redis_db=0,
        redis_cache_set_key='tilestache.cache'):

    s3_cache = S3(bucket, access, secret, use_locks, path, reduced_redundancy,
                  gzip_formats)

    redis_client = make_redis_client(redis_host, redis_port, redis_db)

    redis_cache_index = RedisCacheIndex(redis_client, redis_cache_set_key)
    on_save = OnCacheSave(redis_cache_index)
    notifying_cache = Notifier(s3_cache, on_save)

    return notifying_cache
