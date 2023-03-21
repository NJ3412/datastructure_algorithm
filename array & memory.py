from queue import LifoQueue

s = LifoQueue()

s.put('cat')
s.put('dog')
s.put('rat')

s.get('cat')
print(s.queue)
s.get('dog')
print(s.queue)
s.get('rat')
print(s.queue)
s.get_nowait('rat,'blabla')
