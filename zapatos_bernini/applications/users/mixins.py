from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy, reverse

from .models import User


def check_ocupation_user(ocupation, user_ocupation):
    
    if (ocupation == User.ADMINISTRADOR or ocupation == user_ocupation):
        return True
    else:
        return False
    
    
class TestPermissionMixin(LoginRequiredMixin):
    login_url = reverse_lazy('app_users:user-login')
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        
        if not check_ocupation_user(request.user.ocupation, User.CLIENTE):
            return HttpResponseRedirect(
                reverse(
                    'app_users:user-login'
                )
            )
        
        return super().dispatch(request, *args, **kwargs)
    
    
class AdminPermissionMixin(LoginRequiredMixin):
    login_url = reverse_lazy('app_users:user-login')
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        
        if not check_ocupation_user(request.user.ocupation, User.ADMINISTRADOR):
            return HttpResponseRedirect(
                reverse(
                    'app_users:user-login'
                )
            )
        
        return super().dispatch(request, *args, **kwargs)