def pue_calculator(it_val, predicted_energy_value):
  try:
    return  (((predicted_energy_value * 24) + it_val) / it_val)
  except Exception as e:
    return e
  