class Firewall:

	allowedDirections = ["inbound", "outbound"]

	def __init__(self, rulesFileName):
		self.rulesFileName = rulesFileName
		self.protocolRulesByDirection = {} # direction -> protocol names -> ProtocolRules

		for direction in Firewall.allowedDirections:
			self.protocolRulesByDirection[direction] = {}

		self.processRulesFile()
		# Future optimization: merge IP Address intervals per port per protocol


	def processRulesFile(self):
		with open(self.rulesFileName) as rulesFile:
			for line in rulesFile:
				(directionString, protocolName, portString, IPAddressString) = self.parseRuleString(line)
				protocolRulesByName = self.protocolRulesByDirection[directionString]
				if protocolName not in protocolRulesByName:
					self.addProtocol(protocolRulesByName, protocolName)
				protocolRules = protocolRulesByName[protocolName]
				protocolRules.addRule(portString, IPAddressString)

		return

	def parseRuleString(self, ruleString):

		return ruleString.split(",")

	def accept_packet(self, direction, protocolName, portNumber, IPAddressString):
		protocolRules = getProtocolRules(direction, protocolName)

		return protocolRules.isValidPacket(portNumber, IPAddressString)

	def addProtocol(self, protocolRulesByName, protocolName):

		protocolRulesByName[protocolName] = ProtocolRules(protocolName)

	def getProtocolRules(self, direction, protocolName):
		protocolRulesByName = self.protocolRulesByDirection[direction]

		return protocolRulesByName[protocolName]


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
