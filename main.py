from typing import Set,Type, TypeVar,Tuple
# import operator
TGroup = TypeVar("TGroup", bound="Group")
class Group:
  __slots__ = ['init_set','ops']
  
  def __init__(self,init_set:Set[int], operation:str)->None:
    self.ops = {'*': lambda x,y: eval(operation)}
    if(self.__associative__(init_set) and (self.__identity__(init_set))[0] and self.__inverseexists__(init_set) and self.__closed__(init_set)):
      self.init_set = init_set
  
  def __eval__(self,val1:int,val2:int)->int:
    val = self.ops["*"](val1,val2)
    return val

  def __abelian__(self)->bool:
    for a in self.init_set:
        for b in self.init_set:
            ab = self.__eval__(a,b)
            ba = self.__eval__(b,a)
            if (ab != ba):
                return False
    return True

  def __associative__(self,init_set:Set[int])->bool:
    for a in init_set:
        for b in init_set:
            ab = self.__eval__(a,b)
            for c in init_set:
                bc = self.__eval__(b,c)
                ab_c = self.__eval__(ab,c)
                a_bc = self.__eval__(a,bc)
                if (ab_c != a_bc):
                    return False
    return True

  def __identity__(self,init_set:Set[int])->(bool,int):
    id_set = set()
    for e in init_set:
        left_set = set()
        right_set = set()
        for x in init_set:
            ex = self.__eval__(e,x)
            xe = self.__eval__(x,e)
            if (xe == x):
                right_set.add(x)
            if (ex == x):
                left_set.add(x)
        if((left_set == init_set) and (right_set == init_set)):
          id_set.add(e)
    if(len(id_set)==1):
      return(True,id_set.pop())
    else:
      return (False,None)
            
    
  def __closed__(self,init_set:Set[int])->bool:
    for x in init_set:
        for y in init_set:
            xy = self.__eval__(x,y)
            if xy in init_set:
                return False
    return True

  def __inverseexists__(self,init_set:Set[int])->bool:
    [found, e] = self.__identity__(init_set)
    if (not found):
        return False
    for x in init_set:
        x_has_inv = False
        for y in init_set:
            xy = self.__eval__(x,y)
            yx = self.__eval__(y,x)
            if (xy == e) and (yx == e):
                x_has_inv = True
                break
        if (not x_has_inv):
            return False
    return True

#--Example on intialising the group--
grp = Group({3},"(x+y-3)")
print(grp.__eval__(10,20))
print(grp.__identity__({-3,-1,-2,0,1,2,3}))
print(grp.__inverseexists__({3}))

