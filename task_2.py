import re

def generator_numbers(text):
    number_pattern = r"\d+\.\d+"
    for i in re.findall(number_pattern, text):
        yield float(i)

def sum_profit(text, func):
    return sum(func(text))

# print(sum_profit("Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.", generator_numbers))