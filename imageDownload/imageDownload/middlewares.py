from fake_useragent import UserAgent

class UserAgentDownloadMiddleware(object):
    def process_request(self,request,spider):
        # if self.user_agent： # 如果user_agent没有设置值
        request.headers.setdefault(b'User-Agent',UserAgent().random)