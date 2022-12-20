import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
a = np.array([])
b = np.array([])
c = np.append(a,[3,4])
d = np.append(b,[2,7])
print(cosine_similarity([c],[d])[0][0])