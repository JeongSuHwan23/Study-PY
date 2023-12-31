class Deque:
  # 덱 초기화
  def __init__(self, size=5):
    self.size = size
    self.deque = [None] * size
    self.front = 0
    self.rear = 0

  # 덱이 비어있는지 확인
  def isEmpty(self):
    return self.front == self.rear

  # 덱이 가득 찼는지 확인
  def isFull(self):
    return self.front == (self.rear + 1) % self.size

  # 덱의 앞쪽에 값 넣기
  def addFront(self, data):
    if self.isFull():
      print("Deque is full")
      return

    self.deque[self.rear] = data
    self.rear += 1

  # 덱의 앞쪽에 있는 값 빼기
  def deleteFront(self):
    if self.isEmpty():
      print("Deque is empty")
      return

    self.rear -= 1
    data = self.deque[self.rear]
    self.deque[self.rear] = None
    print(data)
    return data

  # 덱의 뒤쪽에 값 넣기
  def addRear(self, data):
    if self.isFull():
      print("Deque is full")
      return

    self.front -= 1
    self.deque[self.front] = data

  # 덱의 뒤쪽에 있는 값 빼기
  def deleteRear(self):
    if self.isEmpty():
      print("Deque is empty")
      return

    data = self.deque[self.front]
    self.deque[self.front] = None
    self.front += 1
    print(data)
    return data

  # 덱의 앞쪽에 있는 값 확인
  def getFront(self):
    if self.isEmpty():
      print("Deque is empty")
      return
    return self.deque[(self.rear-1)%self.size]

  # 덱의 뒤쪽에 있는 값 확인
  def getRear(self):
    if self.isEmpty():
      print("Deque is empty")
      return
    return self.deque[self.front]


if __name__ == "__main__":
  d = Deque()

  d.addFront(1)
  d.addFront(2)
  d.addRear(3)
  d.addRear(4)
  d.addRear(5)
  print(d.deque)
  print("Front: ", d.getFront())
  print("Rear: ", d.getRear())
  d.deleteRear()
  print(d.deque)
  d.deleteFront()
  print(d.deque)
