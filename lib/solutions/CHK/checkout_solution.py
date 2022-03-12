ITEMS = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10}

OFFERS = {"discounted_offers": {"A": [(5, 200), (3, 130)], "B": [(2, 45)]},
          "take_free_offers": {"E": [(2, "B")], "F": [(2, "F")]}}


def has_offer(offers, k, v):
    if k in offers:
        for offer in offers[k]:
            if v >= offer[0]:
                return True, offer
    return False, None


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
    for k, _ in items_map.items():
        item_has_offer, offer = has_offer(offers, k, items_map[k])
        while item_has_offer:
            offer_number = items_map[k] // offer[0]
            checkout_sum += (offer[1] * offer_number)
            items_map[k] -= offer[0] * offer_number
            item_has_offer, offer = has_offer(offers, k, items_map[k])

    for k, v in items_map.items():
        if k in ITEMS and v > 0:
            checkout_sum += ITEMS[k] * v
    return checkout_sum


def take_same_item_free(items_map, item, offer_number, free_item):
    if free_item in items_map and item == free_item and offer_number >= items_map[free_item]:
        return True
    return False


def take_free_offers(skus, offers):
    items_map = get_items_map(skus)
    for k, _ in items_map.items():
        item_has_offer, offer = has_offer(offers, k, items_map[k])
        if item_has_offer:
            free_item = offer[1]
            offer_number = items_map[k] // offer[0]
            # Check if offer item the same as free item, then items must be more than offer by 1
            if k == free_item and offer[0] + 1 <= items_map[k]:
                items_map[free_item] -= offer_number
            else:  # free item is different from offer item
                while item_has_offer and free_item in items_map:
                    items_map[free_item] -= offer_number
                    item_has_offer, offer = has_offer(offers, k, items_map[k])
    return items_map


def checkout(skus):
    if is_illegal_basket(skus):
        return -1

    items_map = take_free_offers(skus, OFFERS["take_free_offers"])
    checkout_sum = discounted_offers(items_map, OFFERS["discounted_offers"])

    return checkout_sum



