ITEMS = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}

OFFERS = {"discounted_offers": {"A": (3, 130), "B": (2, 45)},
          "take_free_offers": {"E": (2, "B")}}


def get_items_map(skus):
    items_map = {}
    for item in skus:
        if item in items_map:
            items_map[item] += 1
        else:
            items_map[item] = 1
    return items_map


def is_illegal_basket(skus) -> bool:
    for item in skus:
        if item not in ITEMS:
            return True
    return False


def discounted_offers(items_map, offers):
    checkout_sum = 0
    for k, v in items_map.items():
        if k in offers and v >= offers[k][0]:
            offer_number = v // offers[k][0]
            checkout_sum += (offers[k][1] * offer_number)
            items_map[k] -= offers[k][0] * offer_number

    for k, v in items_map.items():
        if k in ITEMS and v > 0:
            checkout_sum += ITEMS[k] * v
    return checkout_sum


def take_free_offers(skus, offers):
    items_map = get_items_map(skus)
    for k, v in items_map.items():
        if k in offers and v >= offers[k][0] and offers[k][1] in items_map:
            offer_number = v // offers[k][0]
            items_map[OFFERS[k][1]] -= offer_number
    return items_map


def checkout(skus):
    if is_illegal_basket(skus):
        return -1

    items_map = take_free_offers(skus, OFFERS["take_free_offers"])
    checkout_sum = discounted_offers(items_map, OFFERS["discounted_offers"])

    return checkout_sum

