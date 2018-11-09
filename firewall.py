
class Firewall:

	def __init__(self, rulesFileName):
		self.rulesFileName = rulesFileName
		self.inboundProtocolDict = {}
		self.inboundProtocolDict = {}

	def processRulesFile(self):
		return

	def accept_packet(self, directionString, protocolNameString, portNumber, IPAddressString):

		return False

	def addProtocol(self, directionDict, protocolName):
		return

	def addToProtocolRules(self, protocol,  portIntervalString, IPIntervalString):
		return

	def getProtocolRules(self, direction, protocolName):
		return


class ProtocolRules:

	def __init__(self, protocolName):
		self.protocolName = protocolName
		self.rules = {}

	def addRule(self, portIntervalString, IPIntervalString):
		return

	def isValidPacket(self, portString, IPString):
		return


class PortInterval:

	def __init__(self, portString):
		(lowerLimit, upperLimit) = self.portStringToInterval(portString)
		self.lowerLimit = lowerLimit
		self.upperLimit = upperLimit

	def contains(self, portString):
		return

	def portStringToInterval(self, portString):
		return


class IPInterval:

	def __init__(self, IPString):
		(lowerLimit, upperLimit) = self.IPStringToInterval(IPString)
		self.lowerLimit = lowerLimit
		self.upperLimit = upperLimit

	def contains(self, IPString):
		return

	def IPStringToInterval(self, IPString):
		return

	def parseIPString(self, IPString):
		return
