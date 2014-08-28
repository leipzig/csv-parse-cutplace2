from cutplace import checks
from cutplace import ranges

class SevenEightNineTen(checks.AbstractCheck):
    """Check that entries of have other fields if seven is active"""
    def __init__(self, description, rule, availableFieldNames, location=None):
        self.as_super = super(SevenEightNineTen, self)
        self.as_super.__init__(description, rule, availableFieldNames, location)
        self.reset()

    def checkRow(self, rowMap, location):
        if(rowMap["FIELD7"]!=''):
            if(any([rowMap["FIELD8"]=='',rowMap["FIELD9"]=='',rowMap["FIELD10"]==''):
                raise checks.CheckError(location)