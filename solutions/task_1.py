def pull(n: int):
    epic_hero, legendary_hero = 0, 0
    f = 0
    legendary_hero = n//90
    if n >= 90:
        n -= 1
    epic_hero = n//10
    return ((epic_hero, legendary_hero))