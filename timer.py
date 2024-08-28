import time

# Get the input time in seconds from the user
seconds = int(input("Enter the time in seconds: "))

# Simple countdown loop
for i in range(seconds, -1, -1):
    print(i, end=' \r')
    time.sleep(1)

print("Time's up!")
time.sleep(1)
