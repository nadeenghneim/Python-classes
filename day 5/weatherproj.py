weather= int(input("What is today's weather in Celcius: "))
if weather < 5:
    print("it's going to be very cold. bring a very warm jacket.")
elif 5 <= weather < 15:
    print("make sure to bring a jacket it might get cold!")
elif 20 >= weather > 15:
    print("it's pretty warm, no need for a jacket!")
else:
    print("it's very hot, wear light!")
