from case import Case
from random import choice

class Field ():
  def __init__(self  , minesCnt , dimensions  ):
    self.width = dimensions[0] # larg
    self.height = dimensions[1] # long
    self.minesCnt = minesCnt
    self.field =  [[ Case ((x,y) , 'safe') for x in range(self.width)] for y in range(self.height)]
    self.mines = []

  def initField(self):
    """ Place les bombes dans la grille """
    for _ in range (self.minesCnt):
      placed = False
      while  not placed:
        row = choice(self.field)
        case = choice(row)
        # setType return false si la case contient deja une bombe
        if case.setType('mine') != False:
          placed =True
          self.mines.append(case)

  def countBombs(self):
    directions = [-1,0,1]
    for mine in self.mines:
      for neighbor in self.getNeighbors(mine):
        if neighbor.type != 'mine':
          neighbor.bombcount+=1

  def countFlags(self, case):
    count = 0
    directions= [-1,0,1]
    for neighbor in self.getNeighbors(case):
      if neighbor.state == 'flagged':
        count += 1
    return count

  def getCase (self , pos):
    return self.field [ pos [1]][ pos[0]]

  def clear(self , pos):
    current_case = self.getCase(pos)
    current_case.state = 'cleared'

    if current_case.type == 'safe' and current_case.bombcount == 0:
      self.clearAllFrom(current_case.pos)

    if current_case.type == 'mine':

      current_case.type = 'mine_expl'
      current_case.state = 'cleared'
      self.lost()


  def showAll(self):
    for row in self.field:
      for case in row:
        case.state = 'cleared'

  def lost(self):
    for m in self.mines:
      if m.state  != 'flagged' and m.type != 'mine_expl':
        m.type = 'perdu'
        m.state = 'cleared'

  def win (self):
    pass

  def getNeighbors(self, case):
    directions= [-1,0,1]
    for y in directions:
      for x in directions:
        if not x == y == 0 :
          pos_x = case.x + x
          pos_y = case.y + y
          if  0 <= pos_x < self.width and 0 <= pos_y < self.height:
            neighbor = self.getCase( (pos_x , pos_y))
            yield neighbor


  def clearAllFromRecursive(self, pos):
    """ 
     -Utiliser une fonction recursive cause des bug lier au limites
    de recursion quand les dimension de la taille de la liste "field"
    est trop grande

    """
    case = self.getCase(pos)
    if case.state == 'hidden':
      return False

    if case.type == 'mine':
      case.setType('mine_expl')
      self.lost()

    elif case.type == 'safe':
      case.state = 'cleared'
      if self.countFlags(case) != case.bombcount:
        pass
      else :
        for neighbor in self.getNeighbors(case):
          if neighbor.state != 'cleared' and neighbor.state != 'flagged':
            neighbor.state = 'cleared'
            if (neighbor.bombcount == 0 ):
              self.clearAllFrom(neighbor.pos)


  def clearAllFrom(self, pos):
    origincase = self.getCase(pos)

    if origincase.state == 'hidden' or origincase.bombcount != self.countFlags(origincase) or origincase.state == 'flagged':
      return False


    caseQueue = [origincase]
    x = 0

    for case in caseQueue:
      for neighbor in self.getNeighbors(case):
        if neighbor.state == 'hidden' :
          neighbor.state = 'cleared'
          if neighbor.type == 'mine':
            neighbor.setType('mine_expl')
            self.lost()
            return False

          elif neighbor.type == 'safe' and neighbor.bombcount == 0:
            if neighbor not in caseQueue:
              caseQueue.append(neighbor)




  def has_exploded(self):
    for mine in self.mines:
      if mine.type == 'mine_expl':
        return True
    return False

  def completed(self):
    for row in self.field:
      for case in row :
        if case.type == 'mine' and case.state != 'flagged':
          return False
        elif case.type == 'safe' and case.state != 'cleared':
          return False

    return True
