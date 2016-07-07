# The MIT License (MIT)
# 
# Copyright (c) 2016 Reinaldo Astudillo
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation 
# files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, 
# modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom 
# the Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE 
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR 
# IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

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
