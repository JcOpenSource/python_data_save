import pickle

with open('temp.pkl', 'rb') as file:
    result = pickle.load(file)

print(result)
