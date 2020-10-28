class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = 'http://ip:port'
        request.meta['proxy'] = 'http://user:password@ip:port'