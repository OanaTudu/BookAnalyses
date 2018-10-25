def ecdf(data):
  """Compute the empirical cumulative distribution function for a one dim array of measurements"""
  #Number of data points:
  n = len(data)
  #x-data:
  x = np.sort(data)
  #y-data:
  y=np.arange(1,n+1)/n
  
  return x,y
