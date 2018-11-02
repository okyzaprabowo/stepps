from SWChecker.BakuChecker import BakuChecker

class SWChecker:
	def __init__(self, dictFile):
		self.checkerList = []
		self.checkerList.append(BakuChecker(dictFile))
	def check(self, text):
		errList = []

		for checker in self.checkerList:
			errList += checker.check(text)

		for err in errList:
			text = text.replace(err.original, err.output)

		return text