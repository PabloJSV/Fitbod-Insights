# Test to add simple interface

import PySimpleGUI as sg
# let's load WorkoutExport.csv as a Pandas dataframe
import pandas as pd
df = pd.read_csv('WorkoutExport.csv')
df.head()
# split date between date and time
df['Date', 'Time'] = df['Date'].str.split(' ', expand=True)[1]
df['YYYY/MM/DD'] = df['Date'].str.split(' ', expand=True)[0]
df['Time'] = df['Date'].str.split(' ', expand=True)[1]
df.head()

#TODO: group Time by early morning, morning, afternoon, evening, night
# Group by Time if time is between 12am and 5am, then it's early morning
df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.hour
df['TimeOfDay'] = df['Hour'].apply(lambda x: 'Early Morning' if x >= 0 and x < 6 else 'Morning' if x >= 6 and x < 12 else 'Afternoon' if x >= 12 and x < 17 else 
'Evening' if x >= 17 and x < 21 else 'Night' if x >= 21 and x < 24 else None)
df.head()
#TODO: Offer insights about times of day that are most effective for each exercise

# Count different values in TimeOfDay column
df['TimeOfDay'].value_counts(1)
# get maximum value in TimeOfDay first column
df['TimeOfDay'].value_counts(1).idxmax()
df['TimeOfDay'].value_counts(1).max()
Test_interface = ('You have been most active in the',df['TimeOfDay'].value_counts(1).idxmax(), ', doing',round((df['TimeOfDay'].value_counts(1).max() * 100), 2), '% of your workouts')
print('You have been most active in the',df['TimeOfDay'].value_counts(1).idxmax(), ', doing',round((df['TimeOfDay'].value_counts(1).max() * 100), 2), '% of your workouts')

1 + 1

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text(*"Test_interface"), sg.InputText()],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ],

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()