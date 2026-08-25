print('Practcing the questions from the chat gpt !')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared = [x ** 2 for x in numbers]
print(f"The squared nums is {squared}")

numbers = [12, 7, 5, 18, 21, 30, 9, 44, 17, 60]
evens = [x for x in numbers if x % 2 == 0]
print(evens)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
q3 = [x ** 2 for x in numbers if x % 2 == 0]
print(f"The even squares is {q3}")

words = ["python", "java", "javascript", "go", "rust", "html", "css"]
q4 = [len(w) for w in words if len(w) > 3]
print(f"The words more than 3 chars is {q4}")

numbers = [1, 2, 3, 4, 5]
q5 = {n : n**2 for n in numbers}
print(f"the dict is {q5}")

numbers = [1, 12, 15, 20, 25, 30, 33, 40, 50, 55]
q6 = [x for x in numbers if x % 5 ==0 and x > 20]
print(q6)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
q7 = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print(q7)

words = [
    "python",
    "java",
    "javascript",
    "go",
    "rust",
    "programming",
    "AI",
    "backend"
]
q8 = [w.upper() for w in words if len(w) > 5 ]
print(f"Thw words greater than 5 in caps {q8}")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
empty_list = []
q9 = [x for row in matrix for x in row]
# q9 = [[x*2 for x in row] for row in matrix]
print(q9)

students = {
    "Rahul": 85,
    "Sujith": 92,
    "Arun": 67,
    "Priya": 78,
    "Kiran": 95,
    "Manoj": 54
}
q10 = {k : "Pass" for k , v in students.items() if v >= 80 }
print(q10)

numbers = [3, 8, 11, 14, 17, 20, 23, 26, 29, 32]
q11 = [x ** 3 for x in numbers if x % 2 ==0 and x > 10]
print(q11)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
q12 = [[x * 10 for x in row] for row in matrix]
print(q12)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
q13 = [x  for row in matrix for x in row if x % 2 ==0 and x > 5]
print(q13)

prices = {
    "apple": 50,
    "banana": 30,
    "mango": 80,
    "orange": 40,
    "grapes": 120
}
q14 = [fruit for fruit, price in prices.items() if price > 50 ]
print(q14)

students = {
    "Rahul": 85,
    "Sujith": 92,
    "Arun": 67,
    "Priya": 78,
    "Kiran": 95,
    "Manoj": 54
}
q15 = {name :("excellent" if score >= 90 else "good" if score >= 75 else "Average")for name, score in students.items() }
print(q15)