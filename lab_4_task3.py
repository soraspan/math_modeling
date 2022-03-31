import physconst as pc

def mech_energ(arg1, arg2, arg3):
  E = arg1 * pc.g * arg2 + (arg1 * arg3**2) / 2
  return E

print(mech_energ(1, 2, 3))