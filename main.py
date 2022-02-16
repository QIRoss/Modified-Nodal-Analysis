import sys
import numpy as np

#open netlist text file given as argv[1]
f = open(sys.argv[1])
#split file in a list of strings using 
textFile = f.read().split('\n')
#remove empty lines from list
textFile = list( filter(lambda x:x !='', textFile) )
#remove comments from list
netlist = list( filter(lambda x:x[0] !='*', textFile))

#count total number of nodes
nodeCount = 0
#count total number of currents
currentCount = 0

#map each string from list into an array of netlist parameters as strings
for i in range(len(netlist)):
  netlist[i] = netlist[i].split()

#transform every parameter into integer and floats and count number of nodes
for i in range(len(netlist)):
  if(netlist[i][0][0] == 'R'):
    aux = netlist[i]
    aux[1] = np.uintc(aux[1])
    aux[2] = np.uintc(aux[2])
    aux[3] = np.double(aux[3])
    #swap nodes if a > b
    if(aux[1] > aux[2]):
      aux[1], aux[2] = aux[2], aux[1]
    #count node value
    if(aux[2] > nodeCount):
      nodeCount = aux[2]

  elif(netlist[i][0][0] == 'I'):
    aux = netlist[i]
    aux[1] = np.uintc(aux[1])
    aux[2] = np.uintc(aux[2])
    aux[4] = np.double(aux[4])
    #swap nodes if a > b and multiply value by -1
    if(aux[1] > aux[2]):
      aux[1], aux[2] = aux[2], aux[1]
      aux[4] = np.multiply(-1, aux[4])
    #count node value
    if(aux[2] > nodeCount):
      nodeCount = aux[2]

  elif(netlist[i][0][0] == 'G'):
    aux = netlist[i]
    aux[1] = np.uintc(aux[1])
    aux[2] = np.uintc(aux[2])
    aux[3] = np.uintc(aux[3])
    aux[4] = np.uintc(aux[4])
    aux[5] = np.double(aux[5])
    #swap nodes if a > b and multiply value by -1
    if(aux[1] > aux[2]):
      aux[1], aux[2] = aux[2], aux[1]
      aux[5] = np.multiply(-1, aux[5])
      #swap nodes if c > d and multiply value by -1
    if(aux[3] > aux[4]):
      aux[3], aux[4] = aux[4], aux[3]
      aux[5] = np.multiply(-1, aux[5])
    #count node value
    if(aux[2] > nodeCount):
      nodeCount = aux[2]
    #count node value
    if(aux[4] > nodeCount):
      nodeCount = aux[4]

  elif(netlist[i][0][0] == 'V'):
    aux = netlist[i]
    aux[1] = np.uintc(aux[1])
    aux[2] = np.uintc(aux[2])
    aux[4] = np.double(aux[4])
    #swap nodes if a > b and multiply value by -1
    if(aux[1] > aux[2]):
      aux[1], aux[2] = aux[2], aux[1]
      aux[4] = np.multiply(-1, aux[4])
    #count node value
    if(aux[2] > nodeCount):
      nodeCount = aux[2]
    currentCount += 1
  
  elif(netlist[i][0][0] == 'F'):
    aux = netlist[i]
    aux[1] = np.uintc(aux[1])
    aux[2] = np.uintc(aux[2])
    aux[3] = np.uintc(aux[3])
    aux[4] = np.uintc(aux[4])
    aux[5] = np.double(aux[5])
    #swap nodes if a > b and multiply value by -1
    if(aux[1] > aux[2]):
      aux[1], aux[2] = aux[2], aux[1]
      aux[5] = np.multiply(-1, aux[5])
    #swap nodes if c > d and multiply value by -1
    if(aux[3] > aux[4]):
      aux[3], aux[4] = aux[4], aux[3]
      aux[5] = np.multiply(-1, aux[5])
    #count node value
    if(aux[2] > nodeCount):
      nodeCount = aux[2]
    #count node value
    if(aux[4] > nodeCount):
      nodeCount = aux[4]
    currentCount += 1

  elif(netlist[i][0][0] == 'E'):
    aux = netlist[i]
    aux[1] = np.uintc(aux[1])
    aux[2] = np.uintc(aux[2])
    aux[3] = np.uintc(aux[3])
    aux[4] = np.uintc(aux[4])
    aux[5] = np.double(aux[5])
    #swap nodes if a > b and multiply value by -1
    if(aux[1] > aux[2]):
      aux[1], aux[2] = aux[2], aux[1]
      aux[5] = np.multiply(-1, aux[5])
    #swap nodes if c > d and multiply value by -1
    if(aux[3] > aux[4]):
      aux[3], aux[4] = aux[4], aux[3]
      aux[5] = np.multiply(-1, aux[5])
    #count node value
    if(aux[2] > nodeCount):
      nodeCount = aux[2]
    #count node value
    if(aux[4] > nodeCount):
      nodeCount = aux[4]
    currentCount += 1

  elif(netlist[i][0][0] == 'H'):
    aux = netlist[i]
    aux[1] = np.uintc(aux[1])
    aux[2] = np.uintc(aux[2])
    aux[3] = np.uintc(aux[3])
    aux[4] = np.uintc(aux[4])
    aux[5] = np.double(aux[5])
    #swap nodes if a > b and multiply value by -1
    if(aux[1] > aux[2]):
      aux[1], aux[2] = aux[2], aux[1]
      aux[5] = np.multiply(-1, aux[5])
    #swap nodes if c > d and multiply value by -1
    if(aux[3] > aux[4]):
      aux[3], aux[4] = aux[4], aux[3]
      aux[5] = np.multiply(-1, aux[5])
    #count node value
    if(aux[2] > nodeCount):
      nodeCount = aux[2]
    #count node value
    if(aux[4] > nodeCount):
      nodeCount = aux[4]
    currentCount += 2


Gn = np.zeros((nodeCount+1+currentCount, nodeCount+1+currentCount))
I = np.zeros(nodeCount+1+currentCount)

actualCurrent = 1

print(Gn)
print(I)

print(netlist)

for i in range(len(netlist)):
  aux = netlist[i]
  #insert resistor stamp
  if(aux[0][0] == 'R'):
    a = aux[1]
    b = aux[2]
    conductance = np.double(1/aux[3])
    Gn[a][a] = Gn[a][a] + conductance
    Gn[a][b] = Gn[a][b] - conductance
    Gn[b][a] = Gn[b][a] - conductance
    Gn[b][b] = Gn[b][b] + conductance
  #insert currentSource stamp
  elif(aux[0][0] == 'I'):
    a = aux[1]
    b = aux[2]
    # i represents current value from source, not an index variable
    i = aux[4]
    I[a] = I[a] - i
    I[b] = I[b] + i
  #insert controledCurrentSource stamp
  elif(aux[0][0] == 'G'):
    a = aux[1]
    b = aux[2]
    c = aux[3]
    d = aux[4]
    value = aux[5]
    Gn[a][c] = Gn[a][c] + value
    Gn[a][d] = Gn[a][d] - value
    Gn[b][c] = Gn[b][c] - value
    Gn[b][d] = Gn[b][d] + value
  #insert V stamp
  elif(aux[0][0] == 'V'):
    a = aux[1]
    b = aux[2]
    value = aux[4]
    I[nodeCount + actualCurrent] -= value
    Gn[nodeCount + actualCurrent ][a] -= 1
    Gn[nodeCount + actualCurrent ][b] += 1
    Gn[a][nodeCount + actualCurrent]  += 1
    Gn[b][nodeCount + actualCurrent]  -= 1
    actualCurrent += 1
  #insert F stamp
  elif(aux[0][0] == 'F'):
    a = aux[1]
    b = aux[2]
    c = aux[3]
    d = aux[4]
    value = aux[5]
    Gn[nodeCount + actualCurrent][c] -= 1
    Gn[nodeCount + actualCurrent][d] += 1
    Gn[a][nodeCount + actualCurrent] += value
    Gn[b][nodeCount + actualCurrent] -= value
    Gn[c][nodeCount + actualCurrent] += 1
    Gn[d][nodeCount + actualCurrent] -= 1
    actualCurrent += 1
  elif(aux[0][0] == 'E'):
    a = aux[1]
    b = aux[2]
    c = aux[3]
    d = aux[4]
    value = aux[5]
    Gn[nodeCount + actualCurrent][a] -= 1
    Gn[nodeCount + actualCurrent][b] += 1
    Gn[nodeCount + actualCurrent][c] += value
    Gn[nodeCount + actualCurrent][d] -= value
    Gn[a][nodeCount + actualCurrent] += 1
    Gn[b][nodeCount + actualCurrent] -= 1
    actualCurrent += 1
  elif(aux[0][0] == 'H'):
    a = aux[1]
    b = aux[2]
    c = aux[3]
    d = aux[4]
    value = aux[5]
    Gn[nodeCount + actualCurrent + 1][a] -= 1
    Gn[nodeCount + actualCurrent + 1][b] += 1
    Gn[nodeCount + actualCurrent][c] -= 1
    Gn[nodeCount + actualCurrent][d] += 1
    Gn[nodeCount + actualCurrent + 1][nodeCount + actualCurrent] += value
    Gn[a][nodeCount + actualCurrent + 1] += 1
    Gn[b][nodeCount + actualCurrent + 1] -= 1
    Gn[c][nodeCount + actualCurrent] += 1
    Gn[d][nodeCount + actualCurrent] -= 1
    actualCurrent += 2



#remove ground line/column
Gn = Gn[1:,1:]
I = I[1:]

print(Gn,'gN\n',I,'I','\n')

def solve(Gn, I ):
  e2 = np.linalg.solve(Gn,I)
  return e2

e = solve(Gn,I)
print(np.ndarray.round(e,3))