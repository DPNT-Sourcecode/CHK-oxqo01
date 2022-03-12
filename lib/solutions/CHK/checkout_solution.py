ITEMS = {"A": 50,
         "B": 30,
         "C": 20,
         "D": 15,
         "E": 40,
         "F": 10,
         "G": 20,
         "H": 10,
         "I": 35,
         "J": 60,
         "K": 80,
         "L": 90,
         "M": 15,
         "N": 40,
         "O": 10,
         "P": 50,
         "Q": 30,
         "R": 50,
         "S": 30,
         "T": 20,
         "U": 40,
         "V": 50,
         "W": 20,
         "X": 90,
         "Y": 10,
         "Z": 50
         }

OFFERS = {
    "discounted_offers": {
        "A": [(5, 200), (3, 130)],
        "B": [(2, 45)],
        "H": [(10, 80), (5, 45)],
        "K": [(2, 150)],
        "P": [(5, 200)],
        "Q": [(3, 80)],
        "V": [(3, 130), (2, 90)]
    },
    "take_free_offers": {
        "E": [(2, "B")],
        "F": [(2, "F")],
        "N": [(3, "M")],
        "R": [(3, "Q")],
        "U": [(3, "U")]
    },
    "group_offers": {
        "STXYZ": [(3, 45)]
    }
}


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
            # Check if offer item the same as free item, then items must be more than offer by 1
            if k == free_item and offer[0] + 1 <= items_map[k]:
                items_map[free_item] -= (items_map[k] - 1) // offer[0]
            elif k == free_item:
                continue
            elif free_item in items_map:  # free item is different from offer item
                offer_number = items_map[k] // offer[0]
                items_map[free_item] -= offer_number
    return items_map


def group_offers(items_map, offers, checkout_sum):

    return checkout_sum


def checkout(skus):
    if is_illegal_basket(skus):
        return -1

    items_map = take_free_offers(skus, OFFERS["take_free_offers"])
    checkout_sum = discounted_offers(items_map, OFFERS["discounted_offers"])
    checkout_sum = group_offers(items_map, OFFERS["group_offers"])

    return checkout_sum
