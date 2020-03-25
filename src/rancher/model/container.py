class VolumeMount(object):
    def __init__(self):
        self.mountPath = None
        self.mountPropagation = None
        self.name = None
        self.readOnly = None
        self.subPath = None
        self.subPathExpr = None


class VolumeDevice(object):
    def __init__(self):
        self.devicePath = None
        self.name = None


class ResourceRequirements(object):
    def __init__(self):
        self.limits = {}
        self.requests = {}


class ContainerPort(object):
    def __init__(self):
        self.containerPort = None
        self.dnsName = None
        self.hostIp = None
        self.hostPort = None
        self.kind = None
        self.name = None
        self.protocol = None
        self.sourcePort = None


class EnvironmentFrom(object):
    def __init(self):
        self.optional = False
        self.prefix = None
        self.source = None
        self.sourceKey = None
        self.sourceName = None
        self.targetKey = None


class Container(object):
    def __init__(self):
        self.allowPrivilegeEscalation = False
        self.capAdd = []
        self.capDrop = []
        self.command = []
        self.entrypoint = []
        self.environment = {}
        self.environmentFrom = list()
        self.exitCode = None
        self.image = None
        self.imagePullPolicy = None
        self.initContainer = False
        self.livenessProbe = None
        self.name = None
        self.ports = None
        self.postStart = None
        self.preStop = None
        self.privileged = False
        self.procMount = None
        self.readOnly = False
        self.readinessProbe = None
        self.resources = None
        self.restartCount = None
        self.runAsGroup = None
        self.runAsNonRoot = False
        self.startupProbe = None
        self.state = None
        self.stdin = False
        self.stdinOnce = False
        self.tty = False
        self.terminationMessagePath = None
        self.terminationMessagePolicy = None
        self.transitioning = None
        self.transitioningMessage = None
        self.uid = None
        self.volumeDevices = None
        self.volumeMounts = None
        self.windowsOptions = None
        self.workingDir = None
