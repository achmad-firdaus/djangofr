print("")

# ----------------------------------
print("Reverse with string: ")
n1 = "italem irad irigayaj =>"
a = "italem"[::-1]
b = "irad"[::-1]
c = "irigayaj"[::-1]
print(n1, a, b, c)

n1 = "iadab itsap ulalreb =>"
a = "iadab"[::-1]
b = "itsap"[::-1]
c = "ulalreb"[::-1]
print(n1, a, b, c)

n1 = "nalub kusutret gnalali =>"
a = "nalub"[::-1]
b = "kusutret"[::-1]
c = "gnalali"[::-1]
print(n1, a, b, c)
# ----------------------------------
print("")

# ----------------------------------
print("Reverse with slicing string: ")
n1 = "italem irad irigayaj =>"
a = n1[0:6][::-1]
b = n1[7:11][::-1]
c = n1[12:20][::-1]
print(n1, a, b, c)

n1 = "iadab itsap ulalreb =>"
a = n1[0:5][::-1]
b = n1[6:11][::-1]
c = n1[12:19][::-1]
print(n1, a, b, c)

n1 = "nalub kusutret gnalali =>"
a = n1[0:5][::-1]
b = n1[6:14][::-1]
c = n1[15:22][::-1]
print(n1, a, b, c)
# ----------------------------------
print("")
