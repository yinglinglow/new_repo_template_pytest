# New Repository Template

This is a starter template for creating new repositories/projects.
Project structure is designed for tests.

- Compatible with Windows - for those who can't use Mac at work (like me)

- Sample code for tests included (assert two dataframes are equal) - using the built-in unittest class. Not pytests, unfortunately, since I also can't install that on my work computer :(

To use:
    git clone https://github.com/yinglinglow/new_repo_template.git

Points to note:
1) __Your main code should be at the main repo level.__ Each project should (ideally) have its own repository. I know, sometimes in a work environment this can be hard to achieve (when a structure is already in place which kind of works... and will take a million years to overhaul). Honestly, just for organisational purposes I keep each project in separate folders in a separate location, and then just move them into whichever folder required at work when necessary. #fornow

2) __Supporting items for tests go into the fixtures folder.__ Put your tests in the tests folder, and the required supporting items for the test to run (e.g. csv files, text files, etc) in the fixtures folders. Ideally your unit tests should be self-contained in the code (i.e. write your expected result into the test code instead of reading a csv file) but if necessary, use the fixtures folder. The sample code includes an example which is meant to help overcome the filepath pains of reading files from the fixtures folder.