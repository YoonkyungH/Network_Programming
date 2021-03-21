import sys

days = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31}

# 해당 월의 일수 출력
month = input('Input month: ')
print(days[month])


# 알파벳 순서대로 월 출력
print(sorted(days))


# 일수가 31인 월 출력
for key, value in days.items():
    if value == 31:
        print(key)


# 월의 일수를 기준으로 오름차순으로 쌍(key-value) 출력
for key, value in sorted(days.items(), key=lambda x: x[1]):
    print(key, value)


# 사용자가 월의 3자리만 입력하면 월의 일수 출력(ex. Jan, Feb)
# strip(): 주어진 문자열 양끝 공백과 \n 삭제
month = sys.stdin.readline().strip()
for key, value in days.items():
    if month in key:
        print(value)