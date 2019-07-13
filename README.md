# New Repository Template

This is a starter template for creating new repositories/projects.

Project structure is designed for:
- pytest
- pytest coverage
- @pytest.fixtures
- fixtures folders
- importing from other .py files in the same packagename/ folder.

I also tried to include some good-to-haves:
- type hinting
- documentation (as per numpy standards)

---

__Setup:__

1. Install pipenv if you haven't already

2. `mkdir new_repo_template; cd new_repo_template` - Create your root folder and go into it, this is where you will be running your commands from.

3. `mkdir packagename; mkdir tests; mkdir fixtures` - Create folders to store your actual module, your tests, and your test fixtures (e.g. csv files)

4. `pipenv --python 3.7` - Create a new environment

5. `pipenv install pytest` - Install all your required packages. Remember to also do `pipenv install pytest-cov`

6. Write your tests and modules

7. `pipenv run pytest --cov=packagename tests/` - Runs your tests and gives a coverage report

8. To exit pipenv shell, type `exit`


---

__Questions:__

__1) Where do I store my CSV files that I need for my tests?__

Ideally your unit tests should be self-contained in the code (i.e. write your expected result into the test code instead of reading a csv file) but if necessary, use the fixtures folder.

__2) Where do I need to put my \_\_init\_\_.py files?__

So far, it seems like it is only critical in the tests/ folder. I may be wrong! Some people put it in packagename/ folder as well (I not quite sure how it works still...)