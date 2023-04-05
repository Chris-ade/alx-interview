#!/usr/bin/python3
""" Prime Game module """


def isWinner(x, nums):
    """ Returns the name of the player that won the most rounds """
    def is_prime(num):
        """ Check if number is prime """
        if num < 2:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    
    winners = {"Maria": 0, "Ben": 0}
    
    for n in nums:
        primes = [i for i in range(2, n+1) if is_prime(i)]
        turn = 0  # Maria goes first, so turn = 0 for Maria, turn = 1 for Ben
        while primes:
            valid_moves = []
            for p in primes:
                if n % p == 0:
                    valid_moves.append(p)
            if not valid_moves:
                break  # no valid moves left
            if turn == 0:
                # Maria's turn
                chosen_move = max(valid_moves)
                winners["Maria"] += 1
            else:
                # Ben's turn
                chosen_move = min(valid_moves)
                winners["Ben"] += 1
            turn = (turn + 1) % 2  # switch turns
            primes = [p for p in primes if p not in range(chosen_move, n+1, chosen_move)]
    
    if winners["Maria"] > winners["Ben"]:
        return "Maria"
    elif winners["Ben"] > winners["Maria"]:
        return "Ben"
    else:
        return None
