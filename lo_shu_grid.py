import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.table import Table

def calculate_driver(day):
    return sum(int(digit) for digit in str(day)) % 9 or 9

def calculate_conductor(date):
    return sum(int(digit) for digit in date) % 9 or 9

def calculate_kua(year, gender):
    sum_year = sum(int(digit) for digit in str(year)) % 9 or 9
    if gender.lower() == 'male':
        return 11 - sum_year if sum_year != 0 else 2  # Handle case when sum_year is 0
    elif gender.lower() == 'female':
        return 4 + sum_year if sum_year != 0 else 4  # Handle case when sum_year is 0

def create_lo_shu_grid(date_str, driver, conductor, kua):
    grid = [[0 for _ in range(3)] for _ in range(3)]
    numbers = [int(digit) for digit in date_str if digit != '-' and digit != '0'] + [driver, conductor, kua]
    positions = {1: (2, 1), 2: (0, 2), 3: (1, 0), 4: (0, 0), 5: (1, 1), 6: (2, 2), 7: (1, 2), 8: (2, 0), 9: (0, 1)}
    for num in numbers:
        if num in positions:
            r, c = positions[num]
            grid[r][c] = str(grid[r][c]) + str(num) if grid[r][c] else str(num)
    return grid

def plot_grid(name, grid):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_frame_on(False)
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    tb = Table(ax, bbox=[0, 0, 1, 1])
    tb.auto_set_font_size(False)
    tb.set_fontsize(14)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            tb.add_cell(i, j, 1/3, 1/3, text=grid[i][j], loc='center', facecolor='lightblue', edgecolor='black')
    ax.add_table(tb)
    ax.set_title(name, fontsize=16, fontweight='bold')
    plt.show()

def process_birthdate(name, birthdate, gender):
    date_parts = birthdate.split('-')
    driver = calculate_driver(date_parts[0])
    conductor = calculate_conductor(birthdate.replace('-', ''))
    kua = calculate_kua(int(date_parts[2]), gender)
    grid = create_lo_shu_grid(birthdate, driver, conductor, kua)
    plot_grid(name, grid)

# Input Data
data = [
    {"name": "John", "birthdate": "13-01-2005", "gender": "male"},
    {"name": "Jane", "birthdate": "15-02-1998", "gender": "female"},
    # Add more entries here
]

for entry in data:
    process_birthdate(entry['name'], entry['birthdate'], entry['gender'])
