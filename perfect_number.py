def perfect_number(number):
    _sum = 0
    for _ in range(1, number):
        if number % _ == 0:
            _sum += _
        
    return number == _sum
