answer = ''
goal1 = ["i", "want", "to", "drink", "water"]
goal2 = ["i", "want", "to", "drink", "water"]
cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
cards3 = ["i", "water", "drink"]
cards4 = ["want", "to"]


def solution(cards_a, cards_b, goal):
    ca = 0
    cam = len(cards_a)
    cb = 0
    cbm = len(cards_b)

    for target in goal:

        if (ca < cam) and (target == cards_a[ca]):
            ca += 1

        elif (cb < cbm) and (target == cards_b[cb]):
            cb += 1

        else:
            return 'No'
            break

    return 'Yes'


if __name__ == '__main__':
    print(solution(cards1, cards2, goal1))
