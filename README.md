**SquadStackParking**
It is a parking space solution. The vehicles could be parked in the parking slots depending on the parking availability.
Parking space takes care of allowing a parker to park the vehicle after registartion number and driving age validation.
Parker is provided the nearest possible parking slot asuuming that the first one is the nearest one.
After parking a vehicle, the parker can anytime choose to leave the parking slot.
Based on the parkers information various queries can be performed on it based on parkers age, registration number.

There are few assumption I took while building this piece - 
1. The parking slot size cannot be less than 1.
2. The drivers age cannot be les than 18 years.
3. The slot on crossing boundry should not be entertained.
4. The user friendly statments i.e PARK, Park, PaRk, park all mean the same thing.
5. The registration number format shoud be valid - AA-01-BB-1111
6. If parking slot is already empty and we try leave on the slot would result in error message.
7. On invalid slot and drivers age, registration number would show the error message.

***Requirement to run :***
```
Python >= 3.7
pip install -r requirements.txt  (for running the test cases)
```

***How to run - ***
Note - (use python or python3, pip or pip3 depending on your machine configuration)**
```
python app.py input.txt  (There is a input.txt file already created for your ease)
python -m pytest -m parking_space (for running all the test cases)
```

Overview of design - 
1. For creating the user friendly enviorment, we need to process the input. This processing of the input does not limit us to case sensitivity.
2. We can use any command line interface library for easing the process but I have created and used my own interface.
3. All the top level functionalities are visible to the users but the real functioning behind them is all encapsulated.
4. For easing the development process I have maintained not to use any hard coded values rather I have used constant file to have a single source of truth.
5. For the error messages I have maintained a object with error message and code so that it becomes super easy to trace the error of a huge system.
6. All the test are marker with the pytest marker so that on specifying one single marker we can run all relevant tests at one shot.
