from flask import Flask, render_template

app = Flask(__name__)

# Головна сторінка з вибором режиму
@app.route('/')
def index():
    return render_template('index.html')

# Режим для дітей
@app.route('/kids')
def kids():
    return render_template('kids.html')

# Режим для підлітків
@app.route('/teens')
def teens():
    return render_template('teens.html')

# Додаткові маршрути для підлітків
@app.route('/teens/courses')
def teens_courses():
    return render_template('teens_courses.html')

@app.route('/teens/quizzes')
def teens_quizzes():
    return render_template('teens_quizzes.html')

@app.route('/teens/budget')
def teens_budget():
    return render_template('teens_budget.html')

@app.route('/teens/ratings')
def teens_ratings():
    return render_template('teens_ratings.html')

@app.route('/teens/decision')
def teens_decision():
    return render_template('teens_decision.html')

@app.route('/teens/route')
def teens_route():
    return render_template('teens_route.html')

@app.route('/teens/credit')
def teens_credit():
    return render_template('teens_credit.html')

if __name__ == '__main__':
    app.run(debug=True)