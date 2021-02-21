import pygame
import random
 
pygame.init()
 
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 400
 
BLACK = (0,0,0)
WHITE = (255,255,255)
 
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
pygame.display.set_caption('My Cool Graphics')
clock = pygame.time.Clock()
 
families = []

class Dude:
  animationFinished = False
  
  
  def __init__(self, position, size):
    self.position = position
    self.size = size
    self.leftHanded = random.randrange(100) < 20
    # default the time to a random time so that all animations don't start at exactly
    # the same time
    self.time = pygame.time.get_ticks() + random.randrange(3000)
    self.animation = self.animateStanding

  def getExtentsRect(self):
    return pygame.Rect([0, 0, 16*self.size, 16*self.size])

  def drawStanding(self, gameDisplay):
    scale = self.size
    posAdjusted = (self.position[0], self.position[1] - (16*scale))

    # body
    pygame.draw.line(gameDisplay, (0,0,0), (posAdjusted[0]+(8 * scale),posAdjusted[1]+(4 * scale)), (posAdjusted[0]+(8 * scale),posAdjusted[1]+(12 * scale)))

    # left arm
    pygame.draw.line(gameDisplay, (0,0,0), (posAdjusted[0]+(2 * scale),posAdjusted[1]+(2 * scale)), (posAdjusted[0]+(8 * scale),posAdjusted[1]+(6 * scale)))

    # right arm
    pygame.draw.line(gameDisplay, (0,0,0), (posAdjusted[0]+(14 * scale),posAdjusted[1]+(2*scale)), (posAdjusted[0]+(8*scale),posAdjusted[1]+(6*scale)))

    # left leg
    pygame.draw.line(gameDisplay, (0,0,0), (posAdjusted[0]+(8*scale),posAdjusted[1]+(12*scale)), (posAdjusted[0]+(4*scale),posAdjusted[1]+(16*scale)))

    # right leg
    pygame.draw.line(gameDisplay, (0,0,0), (posAdjusted[0]+(8*scale),posAdjusted[1]+(12*scale)), (posAdjusted[0]+(12*scale),posAdjusted[1]+(16*scale)))

    # head
    pygame.draw.circle(gameDisplay, (0, 0, 0), [posAdjusted[0] + (8*scale),posAdjusted[1] + (2*scale)], 2*scale, 1)

  def drawWaving(self, gameDisplay):
    scale = self.size
    posAdjusted = (self.position[0], self.position[1] - (16*scale))

    # body
    pygame.draw.line(gameDisplay, (0,0,0), (posAdjusted[0]+(8 * scale),posAdjusted[1]+(4 * scale)), (posAdjusted[0]+(8 * scale),posAdjusted[1]+(12 * scale)))

    if self.leftHanded:
      # left arm normal
      pygame.draw.line(gameDisplay, (0,0,0), (posAdjusted[0]+(2 * scale),posAdjusted[1]+(2 * scale)), (posAdjusted[0]+(8 * scale),posAdjusted[1]+(6* scale)))
      # right arm waving
      pygame.draw.line(gameDisplay, (0,0,0), (posAdjusted[0]+(14 * scale),posAdjusted[1]+(6 *scale)), (posAdjusted[0]+(8 *scale),posAdjusted[1]+(6*scale)))

    else:
      # left arm waving
      pygame.draw.line(gameDisplay, (0,0,0), (posAdjusted[0]+(2 * scale),posAdjusted[1]+(6 * scale)), (posAdjusted[0]+(8 * scale),posAdjusted[1]+(6* scale)))
      # right arm normal
      pygame.draw.line(gameDisplay, (0,0,0), (posAdjusted[0]+(14 * scale),posAdjusted[1]+(2*scale)), (posAdjusted[0]+(8*scale),posAdjusted[1]+(6*scale)))


    # left leg
    pygame.draw.line(gameDisplay, (0,0,0), (posAdjusted[0]+(8*scale),posAdjusted[1]+(12*scale)), (posAdjusted[0]+(4*scale),posAdjusted[1]+(16*scale)))

    # right leg
    pygame.draw.line(gameDisplay, (0,0,0), (posAdjusted[0]+(8*scale),posAdjusted[1]+(12*scale)), (posAdjusted[0]+(12*scale),posAdjusted[1]+(16*scale)))

    # head
    pygame.draw.circle(gameDisplay, (0, 0, 0), [posAdjusted[0] + (8*scale),posAdjusted[1] + (2*scale)], 2*scale, 1)


  def drawSplits(self, gameDisplay):
    scale = self.size
    posAdjusted = (self.position[0], self.position[1] - (16*scale))

    # body
    pygame.draw.line(gameDisplay, (0,0,0), (posAdjusted[0]+(8 * scale),posAdjusted[1]+(4 * scale)), (posAdjusted[0]+(8 * scale),posAdjusted[1]+(12 * scale)))

    # left arm normal
    pygame.draw.line(gameDisplay, (0,0,0), (posAdjusted[0]+(2 * scale),posAdjusted[1]+(2 * scale)), (posAdjusted[0]+(8 * scale),posAdjusted[1]+(6 * scale)))
    # right arm normal
    pygame.draw.line(gameDisplay, (0,0,0), (posAdjusted[0]+(14 * scale),posAdjusted[1]+(2*scale)), (posAdjusted[0]+(8*scale),posAdjusted[1]+(6*scale)))


    # left leg
    pygame.draw.line(gameDisplay, (0,0,0), (posAdjusted[0]+(8*scale),posAdjusted[1]+(12*scale)), (posAdjusted[0]+(4*scale),posAdjusted[1]+(12*scale)))

    # right leg
    pygame.draw.line(gameDisplay, (0,0,0), (posAdjusted[0]+(8*scale),posAdjusted[1]+(12*scale)), (posAdjusted[0]+(12*scale),posAdjusted[1]+(12*scale)))

    # head
    pygame.draw.circle(gameDisplay, (0, 0, 0), [posAdjusted[0] + (8*scale),posAdjusted[1] + (2*scale)], 2*scale, 1)


  def animateWave(self, gameDisplay):
    timeElapsed = pygame.time.get_ticks() - self.time
    if timeElapsed % 1000 < 500:
      self.drawStanding(gameDisplay)
    else:
      self.drawWaving(gameDisplay)

    if timeElapsed > 5000:
      return True
    
    return False

  def animateJumpSplits(self, gameDisplay):
    timeElapsed = pygame.time.get_ticks() - self.time
    if timeElapsed < 300:
      self.drawStanding(gameDisplay)
    else:
      self.drawSplits(gameDisplay)

    if timeElapsed > 600:
      return True
    
    return False

  def animateStanding(self, gameDisplay):
    self.drawStanding(gameDisplay)

    timeElapsed = pygame.time.get_ticks() - self.time
    
    if timeElapsed > 2000:
      return True

    return False

  def draw(self,gameDisplay):
    if self.animationFinished:
      self.time = pygame.time.get_ticks()
      whichOne = random.randrange(3)
      if whichOne == 0:
        self.animation = self.animateWave
      elif whichOne == 1:
        self.animation = self.animateJumpSplits
      elif whichOne == 2:
        self.animation = self.animateStanding

    if self.animation:
      self.animationFinished = self.animation(gameDisplay)

    


class Family:
  def __init__(self, position, size):
    self.position = position
    self.size = size

    self.members = []

    x = position[0]
    # 80% chance that we have a mom
    if random.randrange(100) < 80:
      mom = Dude((x, position[1]), 5 * size)
      self.members.append(mom)
      x = x + mom.getExtentsRect().width
    # 80% chance that we have a dad
    if random.randrange(100) < 80:
      dad = Dude((x, position[1]), 4 * size)
      self.members.append(dad)
      x = x + dad.getExtentsRect().width

    for i in range(random.randrange(4)):
      kid = Dude((x, position[1]), (random.randrange(3) + 1) * size)
      self.members.append(kid)
      x = x + kid.getExtentsRect().width

  def getExtentsRect(self):
    width = 0
    height = 0
    for i in self.members:
      memberRect = i.getExtentsRect()
      width = width + memberRect.width
      if memberRect.height > height:
        height = memberRect.height
    
    return pygame.Rect([0, 0, width, height])

  def draw(self, gameDisplay):
    for i in self.members:
      i.draw(gameDisplay)  



def setup():
  gameDisplay.fill(WHITE)
  pygame.display.update()

  global families

  rows = 5
  for y in range(rows):
    columns = 7 * (y+1)
    xPos = 0
    for x in range(columns):
      family = Family((xPos,DISPLAY_HEIGHT - 200 * (y/rows)), 1 - y/rows)
      xPos = xPos + family.getExtentsRect().width
      families.append(family)



def graphicsLoop(): 
    gameExit = False
 
    while not gameExit:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                print("Goodbye.")
                quit()
 
 
        # erase the screen on each loop by filling the screen white
        gameDisplay.fill(WHITE)

        for i in families:
          i.draw(gameDisplay)

        pygame.display.update()
        
        
        # limit the refresh rate to 60 fps
        clock.tick(60)


setup()
graphicsLoop()