from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, 
    QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup)

from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2 
        self.wrong3 = wrong3



app = QApplication([])

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Вопрос')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('1')
rbtn_2 = QRadioButton('2')
rbtn_3 = QRadioButton('3')
rbtn_4 = QRadioButton('4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

#панель результата
AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('прав или не прав')
lb_Correct = QLabel('ответ тут')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment = Qt.AlignHCenter, stretch = 2)
AnsGroupBox.setLayout(layout_res)
#размещаем виджеты в окне
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch = 2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

anwsers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(anwsers)
    anwsers[0].setText(q.right_answer)
    anwsers[1].setText(q.wrong1)
    anwsers[2].setText(q.wrong2)
    anwsers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if anwsers[0].isChecked():
        show_correct('Правильно!')
    else:
        if anwsers[1].isChecked() or anwsers[2].isChecked() or anwsers[3].isChecked():
            show_correct('НЕверно!')

def next_question():
    window.cur_question += 1
    if window.cur_question >= len(question_list):
       window.cur_question = 0
    q = question_list[window.cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить'
        check_answer()
    else:
        next_question()



window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')

window.cur_question = -1

question_list = []

question_list.append(Question('Государстыеный язык Бразилии', 'Бразильский', 'Португальский', 'Итальянский', 'Испанский'))
question_list.append(Question('Какой самый лучший фильм', 'Титаник', 'Марвел', 'Человек-паук', 'Война бесконечности'))
question_list.append(Question('Лучший человек в мире после родствиников', 'кумир', 'певец', 'актёр', 'писатель'))
question_list.append(Question('Самый богатый человек в мире', 'адвокат', 'Генерал', 'призедент', 'Илон Маск'))
question_list.append(Question('Самый смешной человек', 'Байден призедент США', 'клоун', 'А4', 'сестра'))
question_list.append(Question('что круче', 'машины', 'вила', 'бизнес', 'спорт кары'))
question_list.append(Question('Что хочешь' 'телевизор', 'компютер', 'кольцо', 'секрет', 'всего', 'мира'))
question_list.append(Question('Какой самый сложный язык' 'Англиский', 'Русский', 'Украинский', 'Бритальский'))
question_list.append(Question('Какой лучший телефон', 'Айфон', 'Андройд', 'Самсунг', 'Нокия'))
question_list.append(Question('Лучшая еда', 'КФС', 'Бургеркинг', 'Макдольнакс', 'Домашняя'))
question_list.append(Question('Самое дорогое', 'кольцо', 'золото', 'алмаз', 'аметист'))
question_list.append(Question('Машина мечты' 'ламборгини', 'тесла', 'бугати', 'лимузин'))
question_list.append(Question('Что надо ребёнку', 'телефон', 'деньги', 'еда', 'семья'))
question_list.append(Question('Что надо в зомби апокалепсис', 'вода', 'еда', 'оружие', 'топор'))
question_list.append(Question('Что надо тебе', 'машина', 'дом', 'деньги', 'бизнес'))
            
btn_OK.clicked.connect(click_OK)
window.resize(400, 300)
next_question()

window.show()

app.exec()
