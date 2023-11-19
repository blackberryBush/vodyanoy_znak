from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from dvv import *
from acf import *
from Dv2 import *
from attendance import *
from attendance2 import *
from cr import *
from pr import *

from Dv22 import *
from acf2 import *
from attendance21 import *
from attendance21 import *
from attendance22 import *
import PIL
from PIL import ImageTk, Image


class Window:
	def __init__(self, master):
		self.master = master

		self.frame = tk.Frame(self.master)
		self.frame.pack(expand=True, fill=tk.BOTH)

		self.label = tk.Label(self.frame, text="My NotePad")
		self.label.pack()
		self.text = tk.Text(self.frame, undo=True, height=20, width=70)
		self.text.pack(expand=True, fill=tk.BOTH)
		self.text.insert("1.0","Частные выводы по оттоку клиентов.\nПричина 0. Количество клиентов -	2106.	Часть компаний терпят убытки (916 компаний). Наиболее популярные ОКВЭД: Строительство жилых и нежилых зданий, Производство прочих строительно-монтажных работ, Деятельность автомобильного грузового транспорта. 2023 г.: согласно информации, полученной из открытых источников (BDD Group), строительство подорожало на 30% из-за подорожания материалов и логистики. Кластер (причина) \n1. Количество клиентов -	1.	Ликвидация фирмы и огромный убыток Кластер (причина) 2. Количество клиентов -	1.	Близкий к '0' доход и ОКВЭД, связанный с строительством\nКластер (причина) 3. Количество клиентов -	1.	Высокий доход, но доп. ОКВЭД связан с строительными работами, у клиента есть страхование ответственности. Вероятно, отказ от услуг эквайринга связан с уменьшением издержек / закрытием неликвида.\nКластер (причина) 4. Количество клиентов -	1.	Клиент связан со строительными проектами, доход выше нуля. Вероятно, отказ от услуг эквайринга связан с уменьшением издержек / закрытием неликвида.\nКластер (причина) 5. Количество клиентов -	1.	Клиент терпит убытки, бизнес связан с арендой и управлением собственным или арендованным торговым объектом недвижимого имущества. Возможно, клиент ориентирован на туризм, убытки связаны с сокращением туризма с 2022 года.\nКластер (причина) 6. Количество клиентов -	1.	У клиента есть аккредитив, нет инвестиционных продуктов, есть банковские продукты (7 шт). Клиент терпит убытки, бизнес связан с арендой и управлением собственным или арендованным торговым объектом недвижимого имущества. Возможно, клиент ориентирован на туризм, убытки связаны с сокращением туризма с 2022 года.\nКластер (причина) 7. Количество клиентов -	1.	Клиент терпит убытки, бизнес связан с деятельность заказчика-застройщика, генерального подрядчика.\nКластер (причина) 8. Количество клиентов -	1.	Строительство жилых и нежилых зданий, уменьшение убытков\nКластер (причина) 9. Количество клиентов -	1.	Клиент связан с предоставлением образования (среднее, общее); клиент терпит убытки.\nКластер (причина) 10. Количество клиентов -	1.	Клиент связан с разработкой строительных проектов и терпит серьезные убытки.\nКластер (причина) 11. Количество клиентов -	1.	Предоставление консультационных услуг при купле-продаже недвижимого имущества за вознаграждение или на договорной основе, убытки\nКластер (причина) 12. Количество клиентов -	7.	Клиенты связаны либо со строительным бизнесом, либо с розничной торговлей. У клиентов нет валютных рассчетных счетов. 5 клиентов терпят убытки.\nКластер (причина) 13. Количество клиентов -	256.	Клиенты связаны с неджвижимостью, грузоперевозками и инженераными работами. 121 клиент терпит убытки, в основном из указанных областей. Проектное финансирование есть только у одного человека.\nКластер (причина) 14. Количество клиентов -	1.	Клиент терпит убытки, у клиента есть продукты экосистемы (сбербанк???). Клиент сокращает убыток средств.\nКластер (причина) 15. Количество клиентов -	18.	Аномалия, слишком разные клиенты\nКластер (причина) 16. Количество клиентов -	48.	Аномалия, слишком разные клиенты\nКластер (причина) 17. Количество клиентов -	1.	Уменьшение убытков\nКластер (причина) 18. Количество клиентов -	7.	Клиент терпит убытки, бизнес связан с деятельностью в строительном деле\nКластер (причина) 19. Количество клиентов -	40529	У клиентов нет проектного финансирования (имеют - 3 чел). Подаваляющее большинство клиентов не застраховано имущественно (27 чел. ). Часть компаний терпят убытки. Компания в ликвидации\nКластер (причина) 20. Количество клиентов -	3.	Уменьшение убытков\nОбобщение частных выводов СБЕР БАНК \n1. Большая часть клиентов, отказавшихся от услуги «эквайринг», или близких к этому, связаны с рынком недвижимости или строительства через ОКВЭД. На втором месте – грузоперевозки. \n2. Подавляющее количество клиентов в «опасной зоне» не пользуются инвестиционными инструментами, банковскими продуктами, проектным финансированием и иными инструментами кредитования. \n3. Фирмы, проходящие через процедуру ликвидации, отказываются от дополнительных услуг, в том числе - эквайринг. \n4.Ряд клиентов, находящихся в «опасной зоне», склонны в дальнейшем сократить пользование услугами, в том числе и эквайрингом.\n\nВыводы \nДля сокращения оттока клиентов рекомендуется провести маркетинговую кампанию, направленную на предоставление инструментов инвестирования или кредитования клиентам, находящимся в «опасной зоне».")


def button1_click():
	test()
	test2()
	test3()
	test4()
	test5()

def button2_click():
	test6()
	test7()
	test8()

def test6():
	path = '1.xlsx'
	df1 = load_data(path)
	client_data1 = df1.loc[combobox2.get()].values

	statistics = calculate_statistics(client_data1)
	adf_test_result = perform_adf_test(client_data1)
	print(statistics)
	s = statistics.split()
	print(s)
	label10['text'] = 'Мат ожидание ' + s[0]
	label11['text'] = 'Дисперсия ' + s[1]
	label12['text'] = 'Ср квадратичное отклон ' + s[2]
	print(adf_test_result)

	a = adf_test_result.split()
	print(a)
	label13['text'] = 'ADF statistic' + a[0]
	label14['text'] = 'p-value ' + a[1]

	label16['text'] = 	a[3]
	label17['text'] = a[5]
	label18['text'] = a[7]

	write_results_to_file('results.txt', statistics + '\n' + adf_test_result)


def test7():
	arg1 = combobox2.get()

	path1 = '3.xlsx'
	process_file(arg1, path1)

	path2 = '4.xlsx'
	process_file(arg1, path2)

	images4 = PhotoImage(file="2.2.png.png")
	images4 = images4.subsample(2, 2)
	image_lab4 = Label(frame2)
	image_lab4.image = images4
	image_lab4['image'] = image_lab4.image
	image_lab4.place(x=20, y=210)


def test8():
	arg1 = combobox2.get()
	run_attendance(arg1)

	images5 = PhotoImage(file="attendance21.png")
	images5 = images5.subsample(2, 2)
	image_lab5 = Label(frame2)
	image_lab5.image = images5
	image_lab5['image'] = image_lab5.image
	image_lab5.place(x=500, y=210)

	run_attendance(arg1)
	images6 = PhotoImage(file="attendance2.png")
	images6 = images6.subsample(2, 2)
	image_lab6 = Label(frame2)
	image_lab6.image = images6
	image_lab6['image'] = image_lab6.image
	image_lab6.place(x=500, y=600)

def test9():
	arg1 = combobox2.get()

	process_file('3.xlsx', arg1)
	process_file('4.xlsx', arg1)


def test():
	path = '1.xlsx'
	df = load_data(path)
	client_data = df.loc[combobox1.get()].values

	statistics = calculate_statistics(client_data)
	adf_test_result = perform_adf_test(client_data)
	print(statistics)
	s = statistics.split()
	label1['text'] = 'Мат ожидание ' + s[0]
	label2['text'] = 'Дисперсия ' + s[1]
	label3['text'] = 'Ср квадратичное отклон ' + s[2]
	print(adf_test_result)

	a = adf_test_result.split()
	print(1)
	print(a)
	label4['text'] = 'ADF statistic' + a[0]
	label5['text'] = 'p-value ' + a[1]

	label7['text'] = a[2] +' '+a[3]
	label8['text'] = a[4] +' '+a[5]
	label9['text'] = a[6] +' '+a[7]

	write_results_to_file('results.txt', statistics + '\n' + adf_test_result)





def test2():
	arg1 = combobox1.get()

	path1 = '1.xlsx'
	process_file(arg1, path1)

	path2 = '2.xlsx'
	process_file(arg1, path2)

	images = PhotoImage(file = "1.png.png")
	images = images.subsample(3,3)
	image_lab = Label(frame1)
	image_lab.image = images
	image_lab['image'] = image_lab.image
	image_lab.place(x=20, y=400)

def test3():
	try:
		arg1 = combobox1.get()

		# Чтение данных из Excel
		df = read_excel_data('1.xlsx')
		x = df.loc[combobox1.get()].values
		df = read_excel_data('2.xlsx')
		y = df.loc[combobox1.get()].values
		if np.all(x == 0) or np.all(x == 1) or np.all(y == 0) or np.all(y == 1):
			print("All values are 0 or 1.")
			exit(0)

		min_length = min(len(x), len(y))
		x = x[:min_length]
		y = y[:min_length]
		print(x)
		print(y)

		# Вычисление корреляций
		correlations = compute_correlations(x, y)

		# Отрисовка
		correlation_methods = ['Pearson', 'Spearman', 'Kendall', 'covariance', 'R^2']
		plot_correlations(correlation_methods, correlations)
	except:
		print(123)

def test4():
	arg1 = combobox1.get()
	run_attendance(arg1)

	images1 = PhotoImage(file="attendance.png")
	images1 = images1.subsample(3, 3)
	image_lab1 = Label(frame1)
	image_lab1.image = images1
	image_lab1['image'] = image_lab1.image
	image_lab1.place(x=500, y=400)

	run_attendance(arg1)

	images2 = PhotoImage(file="attendance2.png")
	images2 = images2.subsample(3, 3)
	image_lab2 = Label(frame1)
	image_lab2.image = images2
	image_lab2['image'] = image_lab2.image
	image_lab2.place(x=500, y=100)

def test5():
	run_cr(1)
	run_cr(2)

	images3 = PhotoImage(file="cr1.png")
	images3 = images3.subsample(3, 3)
	image_lab3 = Label(frame1)
	image_lab3.image = images3
	image_lab3['image'] = image_lab3.image
	image_lab3.place(x=1000, y=400)

	run_pr(1)
	images4 = PhotoImage(file="pr1.png")
	images4 = images4.subsample(3, 3)
	image_lab4 = Label(frame1)
	image_lab4.image = images4
	image_lab4['image'] = image_lab4.image
	image_lab4.place(x=1000, y=100)


window = Tk()
window.geometry("1920x1080")
window.title('лучшая прога')


notebook = ttk.Notebook(window)
notebook.pack(expand=True, fill=BOTH)
 
# создаем пару фреймвов
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)
 
frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)
frame3.pack(fill=BOTH, expand=True)
 
# добавляем фреймы в качестве вкладок
notebook.add(frame1, text="Приближение 1")
notebook.add(frame2, text="Приближение 2")
notebook.add(frame3, text="Приближение 3")



button1 = ttk.Button(frame1, text = 'Запустить', state='enabled', command=button1_click)
button1.place(x=165, y=15, width = 250, height = 25)

with open('USER.txt', 'r', encoding='utf8') as f:
	a = list(map(lambda x: x.strip(),f.readlines()))
	
combobox1 = ttk.Combobox(frame1, values=a)
combobox1.place(x=20, y=15)

label1 = ttk.Label(frame1, text = 'Математическое ожидание')
label1.place(x=20, y=45)

label2 = ttk.Label(frame1, text = 'Дисперсия')
label2.place(x=20, y=65)

label3 = ttk.Label(frame1, text = 'Средне квадатичное отклонение')
label3.place(x=20, y=85)

label4 = ttk.Label(frame1, text = 'ADF statistic')
label4.place(x=20, y=115)

label5 = ttk.Label(frame1, text = 'p-value')
label5.place(x=20, y=135)

label6 = ttk.Label(frame1, text = 'critical values:')
label6.place(x=20, y=155)

label7 = ttk.Label(frame1, text = '		 ')
label7.place(x=20, y=175)

label8 = ttk.Label(frame1, text = '		 ')
label8.place(x=20, y=195)

label9 = ttk.Label(frame1, text = '		 ')
label9.place(x=20, y=215)




button2 = ttk.Button(frame2, text='Запустить', state='enabled', command=button2_click)
button2.place(x=165, y=15, width=250, height=25)


combobox2 = ttk.Combobox(frame2, values=a)
combobox2.place(x=20, y=15)


label10 = ttk.Label(frame2, text='Мат ожидание')
label10.place(x=20, y=45)

label11 = ttk.Label(frame2, text='Дисперсия')
label11.place(x=20, y=65)

label12 = ttk.Label(frame2, text='Ср квадатичное отклон')
label12.place(x=20, y=85)

label13 = ttk.Label(frame2, text='ADF statistic')
label13.place(x=20, y=115)

label14 = ttk.Label(frame2, text='p-value')
label14.place(x=20, y=135)

label15 = ttk.Label(frame2, text='critical values:')
label15.place(x=20, y=155)

label16 = ttk.Label(frame2, text='		 ')
label16.place(x=20, y=175)

label17 = ttk.Label(frame2, text='		 ')
label17.place(x=20, y=195)

label18 = ttk.Label(frame2, text='		 ')
label18.place(x=20, y=215)

windowos = Window(frame3)


window.mainloop()