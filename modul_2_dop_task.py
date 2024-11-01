left_number = int(input("Введите число с левой таблички (от 3 до 20)"))
array = []
result_array = []

for i in range(3, left_number+1):
    if left_number % i == 0:
        array.append(i)

result = []
for ar in array:
    for i in range(1, ar+1):
        for j in range(ar, 0, -1):
            if i < j:
                if i + j == ar:
                    result_array.extend([i, j])


print("Введёное число кратно следующим числам:", array)
print("Нужный нам пароль:", *result_array)