ITEMS = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
OFFERS = {"A": (3, 130), "B": (2, 45), "E": (2, "B")}


def get_items_map(skus):
    items_map = {}
    for item in skus:
        if item in items_map:
            items_map[item] += 1
        else:
            items_map[item] = 1
    return items_map


def checkout(skus):
    items_map = get_items_map(skus)
    checkout_sum = 0

    for k, v in items_map.items():
        if k not in ITEMS:
            return -1

        if k in OFFERS and v >= OFFERS[k][0]:
            offer_number = v // OFFERS[k][0]
            if OFFERS[k][1] in items_map:
                items_map[OFFERS[k][1]] -= offer_number
                continue
            checkout_sum += (OFFERS[k][1] * offer_number)
            items_map[k] -= OFFERS[k][0] * offer_number

    for k, v in items_map.items():
        if k in ITEMS and v > 0:
            checkout_sum += ITEMS[k] * v

    return checkout_sum


