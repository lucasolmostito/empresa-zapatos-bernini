from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from .functions import order_process
from applications.users.mixins import TestPermissionMixin

class SendOrderView(TestPermissionMixin, View):
    """ Process to place the complete order """
    
    def post(self, request, *args, **kwargs):
        order_process(
            self=self,
            user=self.request.user
        )
        
        return HttpResponseRedirect(
            reverse('app_items:add-item')
        )
