def bootstrap_replicate_1d(data, func):
  """Generaste bootstrap replicate of 1D data."""
  return func(np.random.choice(data, len(data))

def draw_bs_reps(data, func, size=1):
    """Draw bootstrap replicates."""

    # Initialize array of replicates: bs_replicates
    bs_replicates = np.empty(size)

    # Generate replicates
    for i in range(size):
        bs_replicates[i] = bootstrap_replicate_1d(data, func)

    return bs_replicates
