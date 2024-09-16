def match_case_experiment(number):
    match number:
        case number if number % 2 == 0:
            return "even"
        case number if number % 2 == 1:
            return "odd"
        case _:
            return "unknown"
