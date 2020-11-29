from ie_api import IECore
from ie_api import ExecutableNetwork
from ie_api import InferRequest
from ie_api import IENetwork


def rebuild_IECore(xml_config_file):
    return IECore(xml_config_file)

def rebuild_ExecutableNetwork():
    return ExecutableNetwork()

def rebuild_InferRequest():
    return InferRequest()

def rebuild_IENetwork(model, weights, init_from_buffer):
    return IENetwork(model, weights, init_from_buffer)
