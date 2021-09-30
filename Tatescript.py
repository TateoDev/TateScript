import time

variables = {}
commands = []


def establish(option, isRead):
  split = option.split()
  IntName = split[1]
  
  
  IntValue = split[2]
  

  variables[IntName] = IntValue
  commands.append('establish '+ str(IntName) + " " + str(IntValue))

def wordify(list):
  comp = ""
  for word in list:
    comp = str(comp + word + " ")
  comp = comp.replace('"', "")
  return comp

def printer(option):
  split = option.split()
  if split[1][0] == '"':
    if split[-1][-1] == '"':
        var = wordify(split[1:])
        print(var)
        commands.append('print "' + str(var) + '"')
  elif option[len("print "):len("print ")+1] != '"':
      varToPrint = variables[split[1]]
      print(varToPrint)
      commands.append('print '+ split[1])
  
def saveAs(filename):
  newFile = open("Programs/"+filename + ".tate", "w")
  for command in commands:
    newFile.write(command + "\n")
  newFile.close()

def determine(line, fileLines):
  split = line.split()
  if split:
      if split[0] == "establish":
        establish(line, 1)
      elif split[0] == "print":
        printer(line)
      elif split[0] == "sleep":
        time.sleep(int(split[1]))
      elif split[0] == "repeat":
        for x in range(int(split[1])):
          start = int(split[2])
          end = int(split[3])
          for line in fileLines[start:end]:
            determine(line, fileLines)

def read(filename):
  readFile = open("Programs/"+filename + ".tate", "r")
  fileLines = readFile.readlines()
  for line in fileLines:
    determine(line, fileLines)

    

while True:
 option = input()
 split = option.split()
 if split[0] == "establish":
    establish(option, 0)
 if option[0:len("print ")] == "print ":
    printer(option)
 if option[0:len("save ")] == "save ":
    saveAs(option[len("save "):len(option)])
 if option[0:len("open ")] == "open ":
    read(split[1])
 if split[0] == "sleep":
   time.sleep(int(split[1]))
