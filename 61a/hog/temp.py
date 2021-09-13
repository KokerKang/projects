from hog import piggy_points, roll_dice
from dice import make_fair_dice, six_sided, four_sided, make_test_dice
from ucb import main, trace, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.

def roll_dice(num_rolls, dice=six_sided):
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'

    sum = 0 
    sow_sad = False
    while num_rolls > 0:
        value = dice()
        if value == 1:
            sow_sad = True
        sum += value
        num_rolls -= 1
    if sow_sad:
        return 1
    return sum

def piggy_points(score):
    k = score ** 2
    return int(min(str(k))) + 3

def take_turn(num_rolls, opponent_score, dice=six_sided, goal=GOAL_SCORE):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 in the case
    of a player using Piggy Points.
    Return the points scored for the turn by the current player.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function that simulates a single dice roll outcome.
    goal:            The goal score of the game.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < goal, 'The game should be over.'
    # BEGIN PROBLEM 3
    if num_rolls == 0:
        return piggy_points(opponent_score)
    else:
        return roll_dice(num_rolls, dice)
    # END PROBLEM 3

def more_boar(player_score, opponent_score):
    
    temp_player = str(player_score)
    temp_oppnent = str(opponent_score)

    temp_player = temp_player.zfill(2)
    temp_oppnent = temp_oppnent.zfill(2)
    if int(temp_player[0]) >= int(temp_oppnent[0]):
        return False
    if int(temp_player[1:]) >= int(temp_oppnent[1:]):
        return False
    return True
def next_player(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> next_player(0)
    1
    >>> next_player(1)
    0
    """
    return 1 - who

def silence(score0, score1):
    return silence
    
def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,
         goal=GOAL_SCORE, say=silence):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    score0:     Starting score for Player 0
    score1:     Starting score for Player 1
    dice:       A function of zero arguments that simulates a dice roll.
    goal:       The game ends and someone wins when this score is reached.
    say:        The commentary function to call at the end of the first turn.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"

    while (score0 < goal) and (score1 < goal):
        if who == 0:
            score0 += take_turn(strategy0(score0, score1), score1, dice, goal)
            if not more_boar(score0, score1):
                who = next_player(who)
        else:
            score1 += take_turn(strategy1(score1, score0), score0, dice, goal)
            if not more_boar(score1, score0):
                who = next_player(who)


    # END PROBLEM 5
    # (note that the indentation for the problem 6 prompt (***YOUR CODE HERE***) might be misleading)
    # BEGIN PROBLEM 6
    "*** YOUR CODE HERE ***"
    # END PROBLEM 6
    return score0, score1



    