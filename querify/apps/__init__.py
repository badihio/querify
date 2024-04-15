from . import k8s
from . import process
from . import storage
from .base_app import BaseSource


all_apps = {
    'k8s': k8s.App(),
    'process': process.App(),
    'storage': storage.App(),
}
