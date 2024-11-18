from flask import Flask, render_template, request
import os
import matplotlib.pyplot as plt
from matplotlib.table import Table

app = Flask(__name__)

def calculate_driver(day):
    return sum(int(digit) for digit in str(day)) % 9 or 9

def calculate_conductor(date):
    return sum(int(digit) for digit in date) % 9 or 9

def calculate_kua(year, gender):
    sum_year = sum(int(digit) for digit in str(year)) % 9 or 9
    if gender.lower() == 'male':
        return 11 - sum_year if sum_year != 0 else 2
    elif gender.lower() == 'female':
        return 4 + sum_year if sum_year != 0 else 4

def create_lo_shu_grid(date_str, driver, conductor, kua):
    grid = [[0 for _ in range(3)] for _ in range(3)]
    numbers = [int(digit) for digit in date_str if digit != '-' and digit != '0'] + [driver, conductor, kua]
    positions = {1: (2, 1), 2: (0, 2), 3: (1, 0), 4: (0, 0), 5: (1, 1), 6: (2, 2), 7: (1, 2), 8: (2, 0), 9: (0, 1)}
    for num in numbers:
        if num in positions:
            r, c = positions[num]
            grid[r][c] = str(grid[r][c]) + str(num) if grid[r][c] else str(num)
    return grid

def plot_grid(grid):
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
    # Ensure the static directory exists
    if not os.path.exists('static'):
        os.makedirs('static')
    plt.savefig('static/lo_shu_grid.png')
    plt.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    print("Index route accessed")  # Debug statement
    if request.method == 'POST':
        print("Form submitted")  # Debug statement
        name = request.form['name']
        dob = request.form['dob']
        gender = request.form['gender']
        date_parts = dob.split('-')
        driver = calculate_driver(date_parts[2])
        conductor = calculate_conductor(dob.replace('-', ''))
        kua = calculate_kua(int(date_parts[0]), gender)
        grid = create_lo_shu_grid(dob, driver, conductor, kua)
        plot_grid(grid)
        return render_template('result.html', name=name, grid_image='static/lo_shu_grid.png')
    return render_template('index.html')

if __name__ == '__main__':
    print("Starting Flask app")  # Debug statement
    app.run(debug=True)
