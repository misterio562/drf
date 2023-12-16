from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()
# register maneja todo el CRUD, no es necesario hacer create, read, update y delete
router.register('api/projects', ProjectViewSet, 'projects') # ruta, viewset, nombrecualquier de esa ruta

urlpatterns = router.urls