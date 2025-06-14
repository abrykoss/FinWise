from flask import Flask, render_template, session, redirect, url_for, request, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Додайте реальний секретний ключ

# Головна сторінка з вибором режиму
@app.route('/')
def index():
    return render_template('index.html')

# Словник із правильними відповідями для кожного тесту
CORRECT_ANSWERS = {
    'budget': {'q1': 'b', 'q2': 'b', 'q3': 'b', 'q4': 'b', 'q5': 'b'},
    'taxes': {'q1': 'b', 'q2': 'b', 'q3': 'b', 'q4': 'b', 'q5': 'b'},
    'deposit': {'q1': 'c', 'q2': 'b', 'q3': 'b', 'q4': 'c', 'q5': 'c'},
    'credit': {'q1': 'b', 'q2': 'c', 'q3': 'b', 'q4': 'b', 'q5': 'c'},
    'banking': {'q1': 'b', 'q2': 'b', 'q3': 'c', 'q4': 'c', 'q5': 'c'},
    'marketing': {'q1': 'b', 'q2': 'b', 'q3': 'c', 'q4': 'b', 'q5': 'c'},
    'pricing': {'q1': 'b', 'q2': 'b', 'q3': 'c', 'q4': 'b', 'q5': 'b'},
    'saving': {'q1': 'b', 'q2': 'b', 'q3': 'b', 'q4': 'c', 'q5': 'a'},
    'investing': {'q1': 'c', 'q2': 'b', 'q3': 'b', 'q4': 'b', 'q5': 'a'},
    'pyramid': {'q1': 'b', 'q2': 'b', 'q3': 'b', 'q4': 'b', 'q5': 'b'},
}

# Режим для підлітків
@app.route('/teens')
def teens():
    # Ініціалізація прогресу в сесії
    if 'progress' not in session:
        session['progress'] = {
            'completed_topics': 0,
            'total_score': 0,
            'topics': {
                'budget': {'completed': False, 'score': 0},
                'taxes': {'completed': False, 'score': 0},
                'deposit': {'completed': False, 'score': 0},
                'credit': {'completed': False, 'score': 0},
                'banking': {'completed': False, 'score': 0},
                'marketing': {'completed': False, 'score': 0},
                'pricing': {'completed': False, 'score': 0},
                'saving': {'completed': False, 'score': 0},
                'investing': {'completed': False, 'score': 0},
                'pyramid': {'completed': False, 'score': 0},
            }
        }

    # Розрахунок прогресу
    completed = session['progress']['completed_topics']
    total_topics = len(session['progress']['topics'])
    progress_percentage = round((completed / total_topics) * 100) if total_topics > 0 else 0
    total_score = session['progress']['total_score']

    return render_template(
        'teens.html',
        progress_percentage=progress_percentage,
        total_score=total_score,
        topics=session['progress']['topics']
    )


# Обробка результатів тесту
@app.route('/submit-test/<topic>', methods=['POST'])
def submit_test(topic):
    if topic not in CORRECT_ANSWERS:
        return jsonify({'error': 'Невірна тема'}), 400

    data = request.json
    score = 0
    correct_answers = CORRECT_ANSWERS[topic]

    # Перевірка відповідей
    for q, answer in data.items():
        if answer == correct_answers.get(q):
            score += 2

    # Якщо тест уже був пройдений, віднімаємо попередню оцінку з total_score
    if session['progress']['topics'][topic]['completed']:
        previous_score = session['progress']['topics'][topic]['score']
        session['progress']['total_score'] -= previous_score
    else:
        # Якщо тест проходиться вперше, збільшуємо кількість завершених тем
        session['progress']['completed_topics'] += 1

    session['progress']['topics'][topic]['completed'] = True
    session['progress']['topics'][topic]['score'] = score
    session['progress']['total_score'] += score

    if session['progress']['total_score'] < 0:
        session['progress']['total_score'] = 0

    session.modified = True

    return jsonify({
        'score': score,
        'total_score': session['progress']['total_score'],
        'completed_topics': session['progress']['completed_topics']
    })




# Режим для дітей
@app.route('/kids')
def kids():
    return render_template('kids.html')

# Режим для підлітків


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

@app.route('/teens/calculators')
def teens_calculators():
    return render_template('teens_calculators.html')

@app.route('/teens/courses/budget')
def teens_course_budget():
    return render_template('teens_budget.html')

@app.route('/teens/courses/taxes')
def teens_course_taxes():
    return render_template('teens_taxes.html')

@app.route('/teens/courses/deposit')
def teens_course_deposit():
    return render_template('teens_deposit.html')

@app.route('/teens/courses/credit')
def teens_course_credit():
    return render_template('teens_credit.html')

@app.route('/teens/courses/banking')
def teens_course_banking():
    return render_template('teens_banking.html')

@app.route('/teens/courses/marketing')
def teens_course_marketing():
    return render_template('teens_marketing.html')

@app.route('/teens/courses/pricing')
def teens_course_pricing():
    return render_template('teens_pricing.html')

@app.route('/teens/courses/saving')
def teens_course_saving():
    return render_template('teens_saving.html')

@app.route('/teens/courses/investing')
def teens_course_investing():
    return render_template('teens_investing.html')

@app.route('/teens/courses/pyramid')
def teens_course_pyramid():
    return render_template('teens_pyramid.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/teens/courses/budget/test')
def teens_budget_test():
    return render_template('teens_budget_test.html')

@app.route('/teens/courses/taxes/test')
def teens_taxes_test():
    return render_template('teens_taxes_test.html')

@app.route('/teens/courses/deposit/test')
def teens_deposit_test():
    return render_template('teens_deposit_test.html')

@app.route('/teens/courses/credit/test')
def teens_credit_test():
    return render_template('teens_credit_test.html')

@app.route('/teens/courses/banking/test')
def teens_banking_test():
    return render_template('teens_banking_test.html')

@app.route('/teens/courses/marketing/test')
def teens_marketing_test():
    return render_template('teens_marketing_test.html')

@app.route('/teens/courses/pricing/test')
def teens_pricing_test():
    return render_template('teens_pricing_test.html')

@app.route('/teens/courses/saving/test')
def teens_saving_test():
    return render_template('teens_saving_test.html')

@app.route('/teens/courses/investing/test')
def teens_investing_test():
    return render_template('teens_investing_test.html')

@app.route('/teens/courses/pyramid/test')
def teens_pyramid_test():
    return render_template('teens_pyramid_test.html')
@app.route('/terms')
def terms():
    return render_template('terms.html')



if __name__ == '__main__':
    app.run(debug=True)