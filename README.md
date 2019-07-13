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

__Questions:__

__1) Where do I store my CSV files that I need for my tests?__

Ideally your unit tests should be self-contained in the code (i.e. write your expected result into the test code instead of reading a csv file) but if necessary, use the fixtures folder.

__2) Where do I need to put my \_\_init\_\_.py files?__

So far, it seems like it is only critical in the tests/ folder. I may be wrong! Some people put it in packagename/ folder as well (I not quite sure how it works still...)