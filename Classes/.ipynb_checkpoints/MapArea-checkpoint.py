from GameElementBase import GameElementBase
class MapArea(GameElementBase):
    def __init__(self,position,row_data):
        self.position = position
        self.visitcount=0
        self.inv=[]
        self.roomid = row_data["RoomID"]
        self.roomname = row_data["Name"]
        self.description = row_data["Description"]
    def getRoomID(self):
        return self.roomid
    def getRoomName(self):
        return self.roomname
    def getDescription(self):
        return self.description
    def getPositionIndex(self):
        return str(self.position[0])+"_"+str(self.position[1])
    def getVisitCount(self):
        return self.visitcount
    def addVisit(self):
        self.visitcount+=1