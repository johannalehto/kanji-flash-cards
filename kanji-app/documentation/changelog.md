## Week 6
- Application is broken again and it doesn't include new functionalities, neither tests
- I started building the GUI and rather many views at the same time, ran into problems which are not yet solved

## Week 5
- Application works now with the basic functions
- Created a method for creating word list from any .csv-file, but in the current demo it is ran directly with default file
- UI still in command line
- Added some tests
### Coming up:
- GUI
- Right answers will be removed from the main review pile and moved to another
- User can choose which one of these pile they want to review
- Statistics of correct answers

## Week 4

- Trying to make the current structure work when user uploads a word list of their own, so far it is not working manually
- Refactured the code to cleaner package structure
- Added more separate class objects and trying to plan application logic between them
- UI still in command line, but separated further from the rest of the program
- Replaced print and input -methods with the new io class
- Tests need to be written for everything and unfortunately there are none at the moment
- The previous tests are not valid anymore

## Week 3

- Added main structure for the program
- UI currently in command line, executed by UI Class
- Added Learn Class for handling the learning the cards
- Added Review Class for handling the review of the cards
- Added first tests to Review Class
    - Check answer - returns correct values, tested
