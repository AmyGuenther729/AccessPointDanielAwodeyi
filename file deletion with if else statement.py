import os
if os.path.exists("demofile.txt"):
  os.remove ("demofile.text")
else:
  print("The file does not exist")