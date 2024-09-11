lockdown = False
grana = 130

status = 'Em casa' if lockdown and grana <= 100 else 'uhuuuuuuuu'

print(f'o status é {status}')