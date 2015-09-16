# -*- coding: utf-8 -*-
# 第 0003 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
# fail to install redis, skip it
import redis
import uuid

redis_server = redis.StrictRedis(host='localhost', port=6379, db=0)


def create_code(number=200):
    result = []
    while True is True:
        temp = str(uuid.uuid1()).replace('-', '')
        if not temp in result:
            result.append(temp)
        if len(result) is number:
            break
    return result


def cleanUp(prefix='showmethecode'):
    keys = redis_server.keys('%s_*' % prefix)
    for key in keys:
        redis_server.delete(key)


def insertCode(code, prefix='showmethecode'):
    redis_server.set('%s_%s' % (prefix, code), code)


def selectCodes(prefix='showmethecode'):
    keys = redis_server.keys('%s_*' % prefix)
    result = []
    for key in keys:
        result.append(redis_server.get(key))
    return result


def Process():
    cleanUp()
    code = create_code()
    for c in code:
        insertCode(c)
    result = selectCodes()
    return result

Process()
