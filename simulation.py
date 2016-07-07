import random
car = 'Car '
goat = 'Goat'
def print_scenario(contest):
    'Print the contest, the partipant does not see this'
    print '|',
    for obj in contest:
        print obj,'|',
def strategy1(contest, picked):
    'Strategy 1 Keep your first selection this do not change your inital guess'
    print "Selected", picked,
    return picked

def strategy2(contest, picked):
    'Strategy 2 change your inital guess'
    # All possible options
    options = range(0,len(contest))
    # Change your initial pick
    options.remove(picked)
    # Discover a goat
    for i in range(0,len(options)):
        if contest[options[i]] == goat:
            break
    options.remove(options[i])
    # Pick the next one
    result = options[random.randint(0,len(options)-1)]
    print "Selected", result,
    return result 

def has_won(contest,picked):
    'Return if you have won the car'
    return contest[picked] == car

def run_contest(contest,strategy):
    'contest is the inital scenario strategy to use (change or not your inital guess) return True if you the partipant has won or false if not'
    print 'Contest:',
    print_scenario(contest)
    picked = random.randint(0,len(contest)-1)
    print ', picked (blindly)',picked,
    picked = strategy(contest,picked)
    if has_won(contest,picked):
        print "Win",
        return True
    print "Lost",
    return False

if __name__ == '__main__':
    #Number of experiments
    ncontests = 100000
    contest = [car,goat,goat]
    wins1 = 0
    wins2 = 0
    for i in range(0,ncontests):
        random.shuffle(contest)
        if run_contest(contest,strategy1):
            wins1 = wins1 + 1
        print ""
        if run_contest(contest,strategy2):
            wins2 = wins2 + 1
        print ""

    print "Strategy 1: Number of contest =", ncontests, "Wins =", wins1, "Probability =",float(wins1)/float(ncontests)
    print "Strategy 2: Number of contest =", ncontests, "Wins =", wins2, "Probability =",float(wins2)/float(ncontests)
