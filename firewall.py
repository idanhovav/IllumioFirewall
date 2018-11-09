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
		ruleString = ruleString.rsplit()[0]
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

	def contains(self, portNumber):
		return (self.lowerLimit <= portNumber and portNumber <= self.upperLimit)

	def portStringToInterval(self, portString):
		(lowerLimitString, upperLimitString) = ("", "")

		if self.isPortRange(portString):
			(lowerLimitString, upperLimitString) = portString.split("-")
		else:
			(lowerLimitString, upperLimitString) = (portString, portString)

		return (int(lowerLimitString), int(upperLimitString))

	def getIterable(self):
		return range(self.lowerLimit, self.upperLimit + 1) # + 1 to make inclusive

	def isPortRange(self, portString):

		return "-" in portString


class IPInterval:

	def __init__(self, IPString):
		(lowerLimit, upperLimit) = self.IPStringToInterval(IPString)
		self.lowerLimit = lowerLimit
		self.upperLimit = upperLimit

	def contains(self, IPString):
		# Since these are strings, comparison should be lexicographically.
		# TODO: check this is true
		return (self.lowerLimit <= IPString and IPString <= self.upperLimit)
		return

	def IPStringToInterval(self, IPString):

		return IPString.split("-") if self.isIPRange(IPString) else (IPString, IPString)

	def isIPRange(self, IPString):

		return "-" in IPString
