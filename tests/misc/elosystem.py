def expected_score(rating_a, rating_b):
  """
  Calculates the expected score of player A against player B.

  Args:
      rating_a: The Elo rating of player A.
      rating_b: The Elo rating of player B.

  Returns:
      The expected score of player A (between 0 and 1).
  """
  k = 32  # Tuning constant (usually between 20 and 32)
  return 1 / (1 + 10 ** ((rating_b - rating_a) / k))

def update_elo(player_a_rating, player_b_rating, player_a_score, player_b_score):
  """
  Updates the Elo ratings of two players based on the game outcome.

  Args:
      player_a_rating: The Elo rating of player A before the game.
      player_b_rating: The Elo rating of player B before the game.
      player_a_score: The score of player A (1 for win, 0 for loss).
      player_b_score: The score of player B (1 for win, 0 for loss).

  Returns:
      A tuple containing the updated Elo ratings for player A and player B.
  """
  k = 32  # Tuning constant (usually between 20 and 32)
  expected_a_score = expected_score(player_a_rating, player_b_rating)
  expected_b_score = expected_score(player_b_rating, player_a_rating)

  new_rating_a = player_a_rating + k * (player_a_score - expected_a_score)
  new_rating_b = player_b_rating + k * (player_b_score - expected_b_score)

  return new_rating_a, new_rating_b

# Example usage
player_a_rating = 1500
player_b_rating = 1500

# Player A wins
player_a_score = 1
player_b_score = 0

new_rating_a, new_rating_b = update_elo(player_a_rating, player_b_rating, player_a_score, player_b_score)

print("Player A new rating:", new_rating_a)
print("Player B new rating:", new_rating_b)
