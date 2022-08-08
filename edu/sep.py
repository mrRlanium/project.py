import sys

disk = sys.argv[1]
catalog1 = sys.argv[2]
catalog2 = sys.argv[3]
filename = sys.argv[4]

print(disk + ':\\' + catalog1 + '\\' + catalog2 + '\\' + filename)
print(disk+':', catalog1, catalog2, filename, sep='\\')
