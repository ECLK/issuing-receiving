from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated
        return False

class IsOwnerVerify:
    
    def __init__(self, model):
        self.model = model
        
    def verify(self, request, view):
        user = request.user
        if user.is_authenticated:
            try:
                aro = user.aro
            except:
                return False
            id = view.kwargs.get("pk")
            if id is None:
                return True
            try:
                return self.model.objects.get(pk=id).i_r_aro == aro
            except:
                return False
        return False

class IsOwnerCoverVerify:
    def __init__(self, model):
        self.model = model

    def verify(self, request, view):
        user = request.user
        if user.is_authenticated:
            try:
                aro = user.aro
            except:
                return False
            id = view.kwargs.get("pk")
            if id is None:
                return True
            try:
                return self.model.objects.get(pk=id).issued_to_aro_cc.i_r_aro == aro
            except:
                return False
        return False
