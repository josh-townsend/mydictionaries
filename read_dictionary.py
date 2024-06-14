import pickle

infile = open("datastore.dat", "rb")

datastore = pickle.load(infile)

print(datastore)

datastore["retail"] = [{'room-number': 105, 'use': 'office', 'sq-ft': 150, 'price': 100}]

print(datastore)

outifle = open("datastore.dat" , "wb")
pickle.dump(datastore,outfile)