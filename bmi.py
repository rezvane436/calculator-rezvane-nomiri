print('****** Body Mass Index ******')

weight = float(input("please enter your weight (kg): "))
heigh = float(input("please enter your heigh (m): "))

bmi = weight / (heigh*heigh)

if(bmi < 18.5):
    print('your bmi is', bmi, 'and you have underwight')
elif(bmi < 24.9):
    print('your bmi is', bmi, 'and you are normal !!')
elif(bmi < 29.9):
    print('your bmi is', bmi, 'and you have owerweight')
elif(bmi < 34.9):
    print('your bmi is', bmi, 'and you are obese')
else:
    print('your bmi is', bmi, 'and you are extremeli obese')
