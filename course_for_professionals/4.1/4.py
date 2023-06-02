import sys

f: list = []

for i in sys.stdin:
    f.append(int(i))

print(f'''Рост самого низкого ученика: {min(f)}
Рост самого высокого ученика: {max(f)}
Средний рост: {sum(f) / len(f)}''' if f else "нет учеников")
