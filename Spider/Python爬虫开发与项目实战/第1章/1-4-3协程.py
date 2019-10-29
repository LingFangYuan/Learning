# from gevent import monkey; monkey.patch_all()
# import gevent
# import urllib.request


# def run_task(url):
#     print('Vist --> %s' % url)
#     try:
#         response = urllib.request.urlopen(url)
#         data = response.read()
#         print('%d bytes received from %s.' % (len(data), url))
#     except Exception as e:
#         print(e)


# if __name__ == '__main__':
#     urls = ['https://github.com/', 'https://www.python.org/', 'https://www.cnblogs.com/']
#     greenlets = [gevent.spawn(run_task, url) for url in urls]
#     gevent.joinall(greenlets)


from gevent import monkey; monkey.patch_all()
from gevent.pool import Pool
import urllib.request


def run_task(url):
    print('Vist --> %s' % url)
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        print('%d bytes received from %s.' % (len(data), url))
    except Exception as e:
        print(e)
    return 'url: %s ---> finish' % url


if __name__ == '__main__':
    pool = Pool(2)
    urls = ['https://github.com/', 'https://www.python.org/',
            'https://www.cnblogs.com/']
    results = pool.map(run_task, urls)
    print(results)
