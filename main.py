import itertools

def isunique(string):
  count=0
  for i in string:
    if string.count(i) > 1:
      count+=1
    else:
      pass
  if count > 0:
    return False
  else:
    return True

def rowprobe(row):
  row=str(row)
  permlist,probe=[],[]
  for perm in itertools.permutations('1234'):
    permlist.append("".join(list(perm)))
  for perm in permlist:
        if all(perm[row.find(i)] == i for i in row if i != '0'):
          probe.append(perm)
  return probe

def solve4x4(A,B,C,D):
  Aprobe=rowprobe(A)
  Bprobe=rowprobe(B)
  Cprobe=rowprobe(C)
  Dprobe=rowprobe(D)
  for a in Aprobe:
    for b in Bprobe:
      for c in Cprobe:
        for d in Dprobe:
            if all(isunique(a[n]+b[n]+c[n]+d[n]) is True for n in range(4)):
              if all(isunique(a[n]+a[n+1]+b[n]+b[n+1])is True for n in [0,2]):
                if all(isunique(c[n]+c[n+1]+d[n]+d[n+1])is True for n in [0,2]):
                  print(a+"\n"+b+"\n"+c+"\n"+d+"\n")
                  return [a,b,c,d]



A='0010'
B='1000'
C='2040'
D='0103'

solve4x4(A,B,C,D)