import sys
input = sys.stdin.readline

channel_n = 100

channel = map(int, input().split())

m = map(int, input().split())

break_buttons = list(map(int, input().split()))

# + 또는 - 버튼만을 눌러서 센 것
max_count = abs(channel_n - channel) 



