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
Python >= 3.7
pip install -r requirements.txt  (for running the test cases)

***How to run - ***
**Note - (use python or python3, pip or pip3 depending on your machine configuration)**
python app.py input.txt  (There is a input.txt file already created for your ease)
python -m pytest -m parking_space (for running all the test cases)

