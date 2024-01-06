import random 

temperature_data = [random.randint(50,100) for _ in range(7)]
avg_temperature = sum(temperature_data) / len(temperature_data)

if avg_temperature >= 80:
    weather_summary = 'It was a hot week'
elif avg_temperature >= 60:
    weather_summary = 'The weather was pleasant'
else:
    weather_summary = 'It was a cold week'
    
print('Daily temperatures: ')

for day,temperature in enumerate(temperature_data,start=1):
    print(f'Day {day}: {temperature}F')

print(f'\naverage temperature for the week: {avg_temperature: .2F}')
print(weather_summary)