def GetMiddleStr(content,startStr,endStr):#extract string between 2 keywords
  startIndex = content.index(startStr)
  if startIndex>=0:
    startIndex += len(startStr)
  endIndex = content.index(endStr)
  return content[startIndex:endIndex]

class Robot(object):
  def __init__(self,originalX,originalY,originalFacing):
    self.originalX = originalX
    self.originalY = originalY
    self.originalFacing = originalFacing
  def calFacing(self,filterCommand):
    if filterCommand == 'LEFT':
      if self.originalFacing == 'NORTH':
        self.originalFacing = 'WEST'
      elif self.originalFacing == 'EAST':
        self.originalFacing = 'NORTH'
      elif self.originalFacing == 'SOUTH':
        self.originalFacing = 'EAST'
      elif self.originalFacing == 'WEST':
        self.originalFacing = 'SOUTH'
    elif filterCommand == 'RIGHT':
      if self.originalFacing == 'NORTH':
        self.originalFacing = 'EAST'
      elif self.originalFacing == 'EAST':
        self.originalFacing = 'SOUTH'
      elif self.originalFacing == 'SOUTH':
        self.originalFacing = 'WEST'
      elif self.originalFacing == 'WEST':
        self.originalFacing = 'NORTH'
  def calDestination(self):
    if self.originalFacing == 'NORTH':
      self.originalY += 1
    elif self.originalFacing == 'EAST':
      self.originalX += 1
    elif self.originalFacing == 'SOUTH':
      self.originalY -= 1
    elif self.originalFacing == 'WEST':
      self.originalX -= 1
  def restore(self,originalX,originalY,originalFacing):#prevent robot fall
    self.originalX = originalX
    self.originalY = originalY
    self.originalFacing = originalFacing

if __name__ == "__main__":
  inputCommand = input("please input command: ").upper()#prevent uppercase and lowercase
  filterContent = GetMiddleStr(inputCommand,'PLACE','REPORT').split()#extract['0,0,NORTH', 'MOVE']
  #find the original position
  originalStatus = filterContent[0].split(',')
  originalX = int(originalStatus[0])
  originalY = int(originalStatus[1])
  originalFacing = originalStatus[2]
  robot = Robot(originalX,originalY,originalFacing)
  for x in filterContent:
    if x == 0:#skip '0,0,NORTH'
      continue
    if x == 'LEFT' or x == 'RIGHT':
      robot.calFacing(x)
    elif x == 'MOVE':
      robot.calDestination()
  print('-----------------------------------------------------------------------------------------------------')
  if robot.originalX > 5 or robot.originalX < 0 or robot.originalY > 5 or robot.originalY < 0:
    robot.restore(originalX,originalY,originalFacing)
    print('Cancel command. It will let robut fall. Restore previous position')
    print('Previous position: '+str(robot.originalX)+','+str(robot.originalY)+','+robot.originalFacing)
  else:
    print('Output: '+str(robot.originalX)+','+str(robot.originalY)+','+robot.originalFacing)
