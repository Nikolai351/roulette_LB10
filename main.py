import random

from essence import Essence


def main():
    essences = []
    sum_essences = 0
    for _ in range(10):
        e = Essence()
        e.count_health()
        sum_essences += e.health
        essences.append(e)

    for _, e in enumerate(essences):
        e.health /= sum_essences

    cumulative_amount = 0
    roulette_list = []
    for _, e in enumerate(essences):
        cumulative_amount += e.health
        roulette_list.append(cumulative_amount)

    # d = {}
    # for _ in range(1_000_000):
    ball = random.random()
    for i, e in enumerate(essences):
        if ball < roulette_list[i]:
            print(ball, roulette_list[i])
            print(f'№ {i} Value {e.health}')
            # if i not in d:
            #     d[i] = 1
            # else:
            #     d[i] += 1
            break

    # for key, value in sorted(d.items(), key=lambda x: x[0]):
    #     print(key, value)


if __name__ == '__main__':
    main()
