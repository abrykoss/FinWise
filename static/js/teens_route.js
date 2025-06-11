// Визначення етапів гри (переміщено на початок)
const steps = [
    {
        title: "Етап 1: Ти отримав зарплату!",
        description: "Ти отримав 1000 грн зарплати. Як розпорядитися цими коштами?",
        choices: [
            { text: "Заощадити 500 грн", action: () => { gameState.balance += 500; gameState.points += 10; gameState.progress += 20; return "Ти заощадив 500 грн! +10 балів"; }},
            { text: "Витратити 700 грн на новий одяг", action: () => { if (gameState.balance >= 700) { gameState.balance -= 700; gameState.points += 5; gameState.progress += 10; return "Ти витратив 700 грн. +5 балів"; } else return "Недостатньо коштів!"; }},
            { text: "Інвестувати 600 грн", action: () => { if (gameState.balance >= 600) { gameState.balance -= 600; gameState.points += 15; gameState.progress += 15; return "Ти інвестував 600 грн! +15 балів"; } else return "Недостатньо коштів!"; }}
        ]
    },
    {
        title: "Етап 2: Несподівані витрати",
        description: "Тобі потрібно оплатити ремонт телефону за 400 грн. Що зробиш?",
        choices: [
            { text: "Оплатити ремонт", action: () => { if (gameState.balance >= 400) { gameState.balance -= 400; gameState.points += 5; gameState.progress += 20; return "Ти оплатив ремонт. +5 балів"; } else return "Недостатньо коштів!"; }},
            { text: "Відкласти ремонт", action: () => { gameState.points -= 5; gameState.progress += 10; return "Ти відкладаєш ремонт, але це може викликати проблеми. -5 балів"; }}
        ]
    },
    {
        title: "Етап 3: Додатковий заробіток",
        description: "Тобі пропонують підробіток за 800 грн. Що зробиш?",
        choices: [
            { text: "Взяти підробіток", action: () => { gameState.balance += 800; gameState.points += 10; gameState.progress += 20; return "Ти заробив 800 грн! +10 балів"; }},
            { text: "Відмовитися", action: () => { gameState.progress += 5; return "Ти відмовився від підробітку."; }}
        ]
    },
    {
        title: "Етап 4: Можливість заощадити",
        description: "Ти можеш відкрити депозит із 700 грн на 6 місяців. Що обереш?",
        choices: [
            { text: "Відкрити депозит", action: () => { if (gameState.balance >= 700) { gameState.balance -= 700; gameState.points += 15; gameState.progress += 20; return "Ти відкрив депозит! +15 балів"; } else return "Недостатньо коштів!"; }},
            { text: "Залишити кошти", action: () => { gameState.progress += 10; return "Ти залишив кошти на рахунку."; }}
        ]
    },
    {
        title: "Етап 5: Велика покупка",
        description: "Ти хочеш купити новий гаджет за 1200 грн. Що зробиш?",
        choices: [
            { text: "Купити гаджет", action: () => { if (gameState.balance >= 1200) { gameState.balance -= 1200; gameState.points += 10; gameState.progress += 20; return "Ти купив гаджет! +10 балів"; } else return "Недостатньо коштів!"; }},
            { text: "Заощадити", action: () => { gameState.points += 5; gameState.progress += 15; return "Ти вирішив заощадити. +5 балів"; }}
        ]
    }
];

// Ініціалізація або завантаження стану гри з localStorage
let gameState = JSON.parse(localStorage.getItem('finwiseGameState'));

// Логування для діагностики
console.log('Завантажений стан з localStorage:', gameState);

// Явне скидання до першого етапу при завантаженні, якщо стан є
if (gameState) {
    console.log('Перевіряємо стан для скидання до step: 1');
    if (gameState.step !== 1 ) {
        console.log('Скидаємо до першого етапу');
        gameState = {
            balance: 1000,
            step: 1,
            points: 0,
            progress: 0
        };
    }
} else {
    console.log('Стан відсутній, ініціалізуємо заново');
    gameState = {
        balance: 1000,
        step: 1,
        points: 0,
        progress: 0
    };
}
saveGameState(); // Зберігаємо початковий стан

// Збереження стану в localStorage при зміні
function saveGameState() {
    localStorage.setItem('finwiseGameState', JSON.stringify(gameState));
    console.log('Збережено стан у localStorage:', gameState);
}

// Функція для відображення поточного етапу
function renderStep() {
    console.log('Рендеринг етапу:', gameState.step); // Логування для перевірки
    const step = gameState.step <= steps.length ? steps[gameState.step - 1] : {
        title: "Гру завершено!",
        description: `Твій кінцевий баланс: ${gameState.balance} грн. Бали: ${gameState.points}.`,
        choices: [{
            text: "Грати ще раз",
            action: () => {
                console.log('Скидаємо гру до першого етапу');
                gameState = {
                    balance: 1000,
                    step: 1,
                    points: 0,
                    progress: 0
                };
                saveGameState();
                document.getElementById('result').textContent = ""; // Очищаємо попередній результат
                location.reload(); // Перезавантажуємо сторінку для гарантованого скидання
                return "";
            }
        }]
    };
    document.getElementById('step-title').textContent = step.title;
    document.getElementById('step-description').textContent = step.description;

    const choicesDiv = document.getElementById('choices');
    choicesDiv.innerHTML = ''; // Очищаємо попередні кнопки
    if (step.choices && step.choices.length > 0) {
        console.log('Додаємо кнопки вибору:', step.choices.map(c => c.text)); // Логування тексту кнопок
        step.choices.forEach((choice, index) => {
            const button = document.createElement('button');
            button.className = 'choice-btn';
            button.textContent = choice.text;
            button.onclick = () => {
                const result = choice.action();
                document.getElementById('result').textContent = result;
                if (gameState.step === steps.length) {
                    gameState.step += 1; // Перехід до стану завершення після 5-го етапу
                    console.log('Перехід до завершення гри, step стало:', gameState.step);
                } else if (gameState.step < steps.length) {
                    gameState.step += 1; // Перехід до наступного етапу
                }
                gameState.progress = Math.min(gameState.progress, 100);

                // Оновлення UI
                document.getElementById('balance').textContent = `${gameState.balance} грн`;
                document.getElementById('step-number').textContent = gameState.step > steps.length ? 'Завершено' : gameState.step;
                document.getElementById('points').textContent = gameState.points;
                document.getElementById('progress-bar').style.width = `${gameState.progress}%`;

                // Збереження стану
                saveGameState();

                renderStep();
            };
            choicesDiv.appendChild(button);
        });
    } else {
        console.log('Немає доступних виборів для цього етапу');
    }
}

// Ініціалізація гри
document.addEventListener('DOMContentLoaded', () => {
    console.log('Сторінка завантажена, викликаємо renderStep');
    // Оновлення UI з поточного стану
    document.getElementById('balance').textContent = `${gameState.balance} грн`;
    document.getElementById('step-number').textContent = gameState.step > steps.length ? 'Завершено' : gameState.step;
    document.getElementById('points').textContent = gameState.points;
    document.getElementById('progress-bar').style.width = `${gameState.progress}%`;
    renderStep();
});