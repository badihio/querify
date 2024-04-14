from . import k8s
from . import storage
from .base_app import BaseSource


all_apps = {
    'storage': storage.App(),
    'k8s': k8s.App(),
}
