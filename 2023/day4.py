import sys

def parse_card(card:str):
    '''
    Format input into two lists of integers.
    '''
    card = card.replace(":", "|")
    card_elements = card.split("|")
    #print(f'card elements {card_elements}')
    w = [int(i) for i in card_elements[1].split(' ') if i != '']
    H = [int(i) for i in card_elements[2].split(' ') if i != '']

    w.sort() # O(|w|)
    #print(f'w {w}')
    #print(f'H {H}')
    return (w, H)

def search_winners(w:list, H:list):
    '''
    Count elements of H that are in w. w MUST be sorted from lowest to highest.
    '''
    orig_w = w
    p = 0
    q = len(w)
    c = 0
    r = 0 # TODO: remove
    for i, h in enumerate(H):
        w = orig_w
        p = 0 
        q = len(orig_w)
        while True: # could make recursive
            #if h == 90:
            #    print(f'ROUND {r}: p = {p}; q = {q}; w = {w}')
            idx = len(w) // 2
            comparison = w[idx]
            if h == comparison:
                #print(f'h {h} = comparison {comparison}!')
                c += 1
                r = 0
                break
            elif h < comparison:
                # if h == 90:
                #     print(f'h {h} < comparison {comparison}')
                q = idx 
                w = w[p:q]
                #if h == 90:
                #    print(f'new w: {w}')
                r += 1
            else:
                #if h == 90:
                #    print(f'h {h} > comparison {comparison}')
                p = idx + 1
                w = w[p:q+1]
                # if h == 90:
                #     print(f'new w: {w}')
                r += 1
            if len(w) == 0:
                r = 0
                break
            p = 0
            q = len(w) - 1
    return c

def count_cards(cards:list)->tuple:
    '''
    Iterate through cards and get total points
    '''
    card_points = []
    card_counts = [1] * len(cards)
    parent_cards = [ [] for _ in range(len(cards)) ]
    total_card_count = 0
    for i, card in enumerate(cards):
        w, H = parse_card(card)
        c = search_winners(w, H)
        if c > 0:
            card_points.append(2 ** (c - 1))
        else:
            card_points.append(0)
        for k in range(0, c):
            parent_cards[i + k + 1].append(i)
            card_counts[i + k + 1] += 1
        card_count = 1
        for parent in parent_cards[i]:
            card_count += card_counts[parent]
        card_counts[i] = card_count
        total_card_count += card_count
    return (sum(card_points), total_card_count)


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        mode = args[1]
    else:
        mode = 'normal'
    if mode == 'test':
        FILEPATH = 'day4_test.txt'
    else:
        FILEPATH = 'day4.txt'
    with open(FILEPATH) as f:
        raw = f.readlines()
        lines = [i.strip('\n') for i in raw]
        total_points, total_card_count = count_cards(lines)
        print(f'TOTAL POINTS: {total_points}')
        print(f'TOTAL CARDS: {total_card_count}')

