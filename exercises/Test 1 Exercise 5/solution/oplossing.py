def ToetsPunt(punten, max_punten, max_score):
  score = punten * max_score / max_punten
  # of: score = (punten / max_punten) * max_score
  # De tests worden enkel gedaan met die getallen waarbij deze twee uitdrukkingen gelijk zijn.
  return score