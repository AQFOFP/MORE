import logging

from django.utils.deprecation import MiddlewareMixin

error_log = logging.getLogger()


class ErrorMiddleware(MiddlewareMixin):

    def process_exception(self, request, exceptions):
        print("============ErrorMiddleware=========")
        error_log.error(exceptions)