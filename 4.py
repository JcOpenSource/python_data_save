import pickle

result = [1.0, 2, 3, 4, 5]
with open('temp.pkl', 'wb') as file:
    pickle.dump(result, file)
