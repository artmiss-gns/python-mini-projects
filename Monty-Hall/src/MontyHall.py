import random

def get_dors() :
    doors = ["goat", "goat", "car"]
    random.shuffle(doors)
    return doors

def MontyHall(n_iteration:int=100,*, keep:bool) :
    '''
    """Simulates Monty Hall simulation for `n_iteration` times
    args:
        n_iteration: int
        keep: bool
    Returns:
        True if you win the prize, False if you don't
    """    
    '''
    for _ in range(n_iteration) :
        doors = get_dors()
        chosen_door_index = random.choice([0, 1, 2])

        revealed_door_index = [index for index in [0, 1, 2] if doors[index]!="car" and index!=chosen_door_index]
        revealed_door_index = random.choice(revealed_door_index) # revealed_door can have 2 options, if the user chooses
                                                                # the door which contain car behind it
        if not keep :
            chosen_door_index = [index for index in [0, 1, 2] if index!=chosen_door_index and index!=revealed_door_index][0]

        win = True if doors[chosen_door_index] == "car" else False
        yield win
    

if __name__ == "__main__" :
    n_iter = 10000
    keep=True

    win_count = 0
    for s in MontyHall(n_iter, keep=keep) :
        win_count += int(s)
    
    print("Keep:", keep)
    print("win rate:", win_count/n_iter)
    print("loose rate:", (n_iter-win_count)/n_iter)