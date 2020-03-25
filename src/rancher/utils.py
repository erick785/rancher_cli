class ApiError(Exception):
    def __init__(self, obj):
        self.error = obj
        try:
            msg = '{} : {}\n\t{}'.format(obj.code, obj.message, obj)
            super(ApiError, self).__init__(self, msg)
        except Exception:
            super(ApiError, self).__init__(self, 'API Error')


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

    def dict(self):
        return self.__dict__

    def __str__(self):
        return str(self.__dict__)
