from django.shortcuts import render
from django.conf import settings

from django import http

class BlockedIpMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.META['REMOTE_ADDR'] in settings.BLOCKED_IPS:
            return render(request, "auctions/blocked.html")
        response = self.get_response(request)
        return response