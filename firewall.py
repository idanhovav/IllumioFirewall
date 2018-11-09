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
		protocolRules = self.getProtocolRules(direction, protocolName)

		return protocolRules.isValidPacket(portNumber, IPAddressString)

	def addProtocol(self, protocolRulesByName, protocolName):

		protocolRulesByName[protocolName] = ProtocolRules(protocolName)

	def getProtocolRules(self, direction, protocolName):
		protocolRulesByName = self.protocolRulesByDirection[direction]

		return protocolRulesByName[protocolName]


class ProtocolRules:

	def __init__(self, protocolName):
		self.protocolName = protocolName
		self.rules = {} # portNumber -> IPInterval

	def addRule(self, portIntervalString, IPIntervalString):
		portInterval = PortInterval(portIntervalString)
		newIPInterval = IPInterval(IPIntervalString)

		for port in portInterval.getIterable():
			self.addIPIntervalToPort(port, newIPInterval)

		return

	def isValidPacket(self, portNumber, IPString):
		if portNumber not in self.rules:
			return False

		allowedIPIntervals = self.rules[portNumber]

		return any([IPInterval.contains(IPString) for IPInterval in allowedIPIntervals])

	def addIPIntervalToPort(self, port, IPInterval):
		if port not in self.rules:
			self.rules[port] = [IPInterval]
		else:
			self.rules[port].append(IPInterval)

		return


class PortInterval:

	def __init__(self, portString):
		(lowerLimit, upperLimit) = self.portStringToInterval(portString)
		self.lowerLimit = lowerLimit
		self.upperLimit = upperLimit

	def contains(self, portString):
		return

	def portStringToInterval(self, portString):
		return (0, 0)

	def getIterable(self):
		return range(self.lowerLimit, self.upperLimit + 1) # + 1 to make inclusive


class IPInterval:

	def __init__(self, IPString):
		(lowerLimit, upperLimit) = self.IPStringToInterval(IPString)
		self.lowerLimit = lowerLimit
		self.upperLimit = upperLimit

	def contains(self, IPString):
		return

	def IPStringToInterval(self, IPString):
		return (0, 0)

	def parseIPString(self, IPString):
		return
