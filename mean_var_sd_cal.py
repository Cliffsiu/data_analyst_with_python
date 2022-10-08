def calculate(lst):
  """
  This calculator return the mean, varience, SD, max, min, and the sum of a list with nine elements. 
  
  """
  if len(lst) != 9:
    raise ValueError("List must contain nine numbers.")
  x = np.array(lst).reshape(3,3)
  return {'mean': [x.mean(axis=0).tolist(), x.mean(axis=1).tolist(), x.mean()],\
    'variance': [x.var(axis=0).tolist(), x.var(axis=1).tolist(), x.var()], \
    'standard deviation': [x.std(axis=0).tolist(), x.std(axis=1).tolist(), x.std()], \
    'max': [x.max(axis=0).tolist(), x.max(axis=1).tolist(), x.max()], \
    'min': [x.min(axis=0).tolist(), x.min(axis=1).tolist(), x.min()], \
    'sum': [x.sum(axis=0).tolist(), x.sum(axis=1).tolist(), x.sum()]}
