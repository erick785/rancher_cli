class PodDNSConfig(object):
    def __init__(self):
        self.nameservers = None
        self.options = None
        self.searches = None


class PodDNSConfigOption(object):
    def __init__(self):
        self.name = None
        self.value = None


class DaemonSetCondition(object):
    def __init__(self):
        self.lastTransitionTime = None
        self.message = None
        self.reason = None
        self.status = None
        self.type = None


class DaemonSetConfig(object):
    def __init__(self):
        self.maxUnavailable = None
        self.minReadySeconds = None
        self.revisionHistoryLimit = None
        self.strategy = None


class DaemonSetStatus(object):
    def __init__(self):
        self.collisionCount = None
        self.conditions = None
        self.currentNumberScheduled = None
        self.desiredNumberScheduled = None
        self.numberAvailable = None
        self.numberMisscheduled = None
        self.numberReady = None
        self.numberUnavailable = None
        self.observedGeneration = None
        self.updatedNumberScheduled = None


class OwnerReference(object):
    def __init__(self):
        self.apiVersion = None
        self.blockOwnerDeletion = None
        self.controller = None
        self.kind = None
        self.name = None
        self.uid = None


class PublicEndpoint(object):
    def __init__(self):
        self.addresses = None
        self.allNodes = None
        self.hostname = None
        self.ingressId = None
        self.nodeId = None
        self.path = None
        self.podId = None
        self.port = None
        self.protocol = None
        self.serviceId = None


class PodReadinessGate(object):
    def __init__(self):
        self.conditionType = None


class Scheduling(object):
    def __init__(self):
        self.node = None
        self.priority = None
        self.priorityClassName = None
        self.scheduler = None
        self.tolerate = None


class LabelSelector(object):
    def __init__(self):
        self.matchExpressions = None
        self.matchLabels = None


class LabelSelectorRequirement(object):
    def __init__(self):
        self.key = None
        self.operator = None
        self.values = None


class TopologySpreadConstraint(object):
    def __init__(self):
        self.labelSelector = None
        self.maxSkew = None
        self.topologyKey = None
        self.whenUnsatisfiable = None

class LocalObjectReference(object):
    def __init__(self):
        self.name = None

class DaemonSet(object):
    def __init__(self):
        self.id = None
        self.type = None
        self.links = None
        self.actions = None
        self.activeDeadlineSeconds = None
        self.annotations = None
        self.automountServiceAccountToken = None
        self.containers = None
        self.created = None
        self.creatorId = None
        self.dnsConfig = None
        self.dnsPolicy = None
        self.daemonSetConfig = None
        self.daemonSetStatus = None
        self.enableServiceLinks = None
        self.ephemeralContainers = None
        self.fsgid = None
        self.gids = None
        self.hostAliases = None
        self.hostIPC = None
        self.hostNetwork = None
        self.hostPID = None
        self.hostname = None
        self.imagePullSecrets = None
        self.labels = None
        self.name = None
        self.namespaceId = None
        self.nodeId = None
        self.overhead = None
        self.ownerReferences = None
        self.preemptionPolicy = None
        self.projectId = None
        self.publicEndpoints = None
        self.readinessGates = None
        self.removed = None
        self.restartPolicy = None
        self.runAsGroup = None
        self.runAsNonRoot = None
        self.runtimeClassName = None
        self.scheduling = None
        self.selector = None
        self.serviceAccountName = None
        self.shareProcessNamespace = None
        self.state = None
        self.subdomain = None
        self.sysctls = None
        self.terminationGracePeriodSeconds = None
        self.topologySpreadConstraints = None
        self.transitioning = None
        self.transitioningMessage = None
        self.uuid = None
        self.uid = None
        self.volumes = None
        self.windowsOptions = None
        self.workloadAnnotations = None
        self.workloadLabels = None
        self.workloadMetrics = None
