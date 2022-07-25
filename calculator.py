a = int(input('введите первое число: '))
operator = input ('''Доступные функции калькулятора: 
                   + для сложения,
                   - для вычитания,
                   * для умножения,
                   / для деления ,
                   // для целочисленного деления,
                    для возведения в степень,
                   % для деления с остатком 
                   Ввести оператор: ''')
b = int(input('введите второе число: '))
if operator == '+':
    print ('{} + {}'.format(a,b),'=',a+b)
elif operator == '-':
    print ('{} - {}'.format(a,b),'=',a-b)
elif operator == '/':
    print('{} / {}'.format(a, b), '=', int(a / b))
elif operator == '*':
    print ('{} * {}'.format(a,b),'=',a*b)
elif operator == '//':
    print('{} // {}'.format(a, b), '=', a // b)
elif operator == '':
    print('{}  {}'.format(a, b), '=', a  b)
elif operator == '%':
    print ('{} % {}'.format(a,b),'=','{} // {}'.format(a-(a % b),b),'=' ,a // b, 'остаток',a % b)
else :
    print ('error,данная функция недоступна!')
