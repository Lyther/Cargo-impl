ALTOGETHER = False

def d2sec(value):
    return value * 24 * 3600
def h2sec(value):
    return value * 3600
def min2sec(value):
    return value * 60

weekNumDict = {
    '周一': 1,    
    '周二': 2,    
    '周三': 3,    
    '周四': 4,    
    '周五': 5,    
    '周六': 6,    
    '周日': 7    
}

timestampDict = {
    0: {'start': 0, 'end': h2sec(7)},
    1: {'start': h2sec(8), 'end': h2sec(8) + min2sec(50)},
    2: {'start': h2sec(9), 'end': h2sec(9) + min2sec(50)},
    3: {'start': h2sec(10) + min2sec(20), 'end': h2sec(11) + min2sec(10)},
    4: {'start': h2sec(11) + min2sec(20), 'end': h2sec(12) + min2sec(10)},
    5: {'start': h2sec(14) + min2sec(00), 'end': h2sec(14) + min2sec(50)},
    6: {'start': h2sec(15) + min2sec(00), 'end': h2sec(15) + min2sec(50)},
    7: {'start': h2sec(16) + min2sec(20), 'end': h2sec(17) + min2sec(10)},
    8: {'start': h2sec(17) + min2sec(20), 'end': h2sec(18) + min2sec(10)},
    9: {'start': h2sec(19) + min2sec(00), 'end': h2sec(19) + min2sec(50)},
    10: {'start': h2sec(20) + min2sec(00), 'end': h2sec(20) + min2sec(50)},
    11: {'start': h2sec(21) + min2sec(00), 'end': h2sec(21) + min2sec(50)},
    12: {'start': h2sec(23) + min2sec(00), 'end': h2sec(23) + min2sec(59)},
}

def timestamp(week=1, day=1, session=0, point='start'):
    endurance = 0
    if ALTOGETHER:
        endurance += d2sec((week-1) * 7)
        endurance += d2sec(day-1)
    endurance += timestampDict[session][point]
    return endurance