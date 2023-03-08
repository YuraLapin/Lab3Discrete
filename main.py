def check_matrix(matrix):
	outerLength = len(matrix)
	for arr in matrix:
		if outerLength != len(arr):
			return False
	return True

def print_matrix_element(num, matrix_size):
	spaces = len(str(matrix_size)) - len(str(num)) + 1
	print(num, end = spaces * " ")

def print_matrix(matrix):
	if check_matrix(matrix):
		size = len(matrix)
		for i in range(size + 1):
			print_matrix_element(i, size)
		print()
		for i in range(size):
			print_matrix_element(i + 1, size)
			for j in range(size):
				print_matrix_element(matrix[i][j], size)
			print()

def check_int(str):
	if str == None or str == "":
		return False
	for char in str:
		if char not in "-0123456789":
			return False
	return True

def get_int(message):
	print(message)
	ans = input()
	while not check_int(ans):
		print("Число должно состоять только из цифр и быть целым")
		print(message)
		ans = input()
	return int(ans)

def get_positive_int(message):
	ans = get_int(message)
	while ans <= 0:		
		print("Число должно быть положительным ")
		ans = get_int(message)		
	return ans	

def get_positive_int_lower_than(message, max):
	ans = get_positive_int(message)
	while ans > max:		
		print("Число не может быть больше ", max)
		ans = get_positive_int(message)		
	return ans	

def fill_matrix_with_zero(size):
	ans = [[0 for i in range(size)] for j in range(size)]
	return ans

def multiply_matrix(matrix_1, matrix_2):
	size = len(matrix_1)
	ans = fill_matrix_with_zero(size)
	if check_matrix(matrix_1) and check_matrix(matrix_2) and len(matrix_1) == len(matrix_2):
			size = len(matrix_1)
			for i in range(size):
				for j in range(size):
					for k in range(size):
						ans[i][j] += matrix_1[k][j] * matrix_2[i][k]
					ans[i][j] = min(1, ans[i][j])
	return ans

def rise_matrix_to_power(matrix, power):
	size = len(matrix)
	ans = fill_matrix_with_zero(size)
	if check_matrix(matrix):
		if power == 0:
			for i in range(size):
				ans[i][i] = 1
		elif power == 1:
			ans = matrix	
		elif power > 1:
			ans = matrix
			for i in range(power - 1):
				ans = multiply_matrix(ans, matrix)
	return ans

def sum_matrix(matrix_1, matrix_2):
	size = len(matrix_1)
	ans = fill_matrix_with_zero(size)
	if check_matrix(matrix_1) and check_matrix(matrix_2) and len(matrix_1) == len(matrix_2):
		for i in range(size):
			for j in range(size):
				ans[i][j] = matrix_1[i][j] + matrix_2[i][j]
				ans[i][j] = min(1, ans[i][j])
	return ans

def sum_of_line_of_matrix(matrix, count):
	size = len(matrix)
	ans = fill_matrix_with_zero(size)
	for i in range(count + 1):
		ans = sum_matrix(ans, rise_matrix_to_power(matrix, i))
	return ans

def transpose(matrix):
	size = len(matrix)
	ans = fill_matrix_with_zero(size)
	if check_matrix(matrix):
		for i in range(size):
			for j in range(size):
				ans[i][j] = matrix[j][i]
	return ans

def logical_and(matrix_1, matrix_2):
	size = len(matrix)
	ans = fill_matrix_with_zero(size)
	if check_matrix(matrix_1) and check_matrix(matrix_2) and len(matrix_1) == len(matrix_2):
		for i in range(size):
			for j in range(size):
				if matrix_1[i][j] == matrix_2[i][j] == 1:
					ans[i][j] = 1
				else:
					ans[i][j] = 0
	return ans

def count(list):
	ans = 0
	for arr in list:
		for elem in arr:
			ans += 1
	return ans

def extract_answer(matrix, list):
	if check_matrix(matrix):
		size = len(matrix)
		current_component = []
		to_delete = []
		for i in range(size):
			if matrix[0][i] == 1:
				current_component.append(i + 1 + count(list))
				to_delete.append(i)
		to_delete.reverse()
		for i in to_delete:
			matrix.pop(i)
			for arr in matrix:
				arr.pop(i)
		list.append(current_component)		
		if len(matrix) > 0:
			return extract_answer(matrix, list)
		else:
			return list
		
def find_components(matrix):
	if check_matrix(matrix):
		print(LINE, "\nR:")
		r = sum_of_line_of_matrix(matrix, size)
		print_matrix(r)

		print(LINE, "\nR^T:")
		r_t = transpose(r)
		print_matrix(r_t)

		print(LINE, "\nR&R^T")
		answer = logical_and(r, r_t)
		print_matrix(answer)

		print(LINE, "\nANSWER:")
		print(extract_answer(answer, []))


def main():
	LINE = "-------------------------------------------" 

	size = get_positive_int("Введите размер матрицы: ")
	matrix = fill_matrix_with_zero(size)

	go_on = True
	while go_on:
		print(LINE)
		print_matrix(matrix)
		print(LINE)
		print("1 - Добавить связь")
		print("2 - Найти компоненты связности")
		print("3 - Выход")
		ans = get_int("Выберите действие [1-3]: ")
		if ans == 1:
			n_1 = get_positive_int_lower_than("Введите номер вершины отправления: ", size)
			n_2 = get_positive_int_lower_than("Введите номер вершины прибытия: ", size)
			matrix[n_1 - 1][n_2 - 1] = 1			
		elif ans == 2:
			find_components(matrix)
			go_on = False
		elif ans == 3:
			go_on = False
		else:
			print("Введено неверное число")
		
if __name__ == "__main__":
	main()	