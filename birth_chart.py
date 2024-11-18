import pandas as pd
import matplotlib.pyplot as plt

def calculate_driver(date):
    return sum(int(d) for d in str(date.day)) % 9

def calculate_conductor(date):
    return sum(int(d) for d in date.strftime('%d%m%Y')) % 9

def calculate_kua(year, gender):
    sum_year = sum(int(d) for d in str(year)) % 9
    return 11 - sum_year if gender == 'male' else 4 + sum_year

def lo_shu_grid(date, driver, conductor, kua):
    grid = [[0]*3 for _ in range(3)]
    numbers = [int(d) for d in date.strftime('%d%m%Y')] + [driver, conductor, kua]
    positions = {(4,0,0), (9,0,1), (2,0,2), (3,1,0), (5,1,1), (7,1,2), (8,2,0), (1,2,1), (6,2,2)}
    for num in numbers:
        for pos in positions:
            if num == pos[0]:
                grid[pos[1]][pos[2]] += 1
    return grid

def plot_grid(grid):
    fig, ax = plt.subplots()
    table = plt.table(cellText=grid, loc='center')
    table.set_fontsize(14)
    table.scale(1, 4)
    ax.axis('off')
    plt.show()

birthdate = pd.to_datetime('2005-01-13')
driver_num = calculate_driver(birthdate)
conductor_num = calculate_conductor(birthdate)
kua_num = calculate_kua(birthdate.year, 'male')

grid = lo_shu_grid(birthdate, driver_num, conductor_num, kua_num)
plot_grid(grid)
