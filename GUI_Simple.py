import PySimpleGUI as sg

# Define the layout
layout = [
    [sg.Text("Welcome to the Calculator")],
    [sg.Text("Select Choice")],
    [sg.Text("1.Add"), sg.Text("2.Subtract"), sg.Text("3.Multiply"), sg.Text("4.Divide")],
    [sg.Input(size=(20, 1), key='-CHOICE-', justification='right', enable_events=True)],
    [sg.Text("Enter first number:"), sg.Input(size=(20, 1), key='-NUM1-', justification='right', enable_events=True)],
    [sg.Text("Enter second number:"), sg.Input(size=(20, 1), key='-NUM2-', justification='right', enable_events=True)],
    [sg.Button('Calculate', bind_return_key=True, enable_events=True), sg.Button('Exit')],
    [sg.Output(size=(40, 10))]
]

# Create the window
window = sg.Window('Calculator', layout, resizable=True)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == 'Calculate':
        choice = values['-CHOICE-']
        num1 = values['-NUM1-']
        num2 = values['-NUM2-']
        
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(num1)
                num2 = float(num2)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '1':
                print(num1, "+", num2, "=", num1 + num2)
            elif choice == '2':
                print(num1, "-", num2, "=", num1 - num2)
            elif choice == '3':
                print(num1, "*", num2, "=", num1 * num2)
            elif choice == '4':
                if num2 == 0:
                    print("Error! Division by zero is not allowed.")
                else:
                    print(num1, "/", num2, "=", num1 / num2)
        else:
            print("Invalid Input")

# Close the window
window.close()
