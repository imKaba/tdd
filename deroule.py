# 1. create a project : django-admin startproject example
# 2. create an app    : python manage.py startapp task  | add task to example/settings.py
# 3. migrate          : python manage.py migrate
# 4. run test         : python manage.py test 
# 5. write your first test on task/tests.py (test_model_exist, assert count == 0)
# 6. run test again   : python manage.py test 
# 7. run test differently : python manage.py test task | python manage.py test task.tests | python manage.py test task.tests.TextTaskModel ...
# 8. create an app    : python manage.py startapp reviews | add reviews to example/settings.py
# 9. delete reviews/tests.py
# 10. create a folder reviews/tests
# 11. inside reviews/tests create a file models or whatever name that you want to test
# 12. write your test in the file and run your test : python manage.py test reviews | you will found any tests
# 13. create a __init__.py file in the reviews/tests folder and import the test file you wrote there 
# 14. run your test again et bingoooooooooooooooo
# 15. install coverage : pip install coverage 
#      Coverage.py is a tool for measuring code coverage of Python programs.
#      It monitors your program, noting which parts of the code have been executed,
#      then analyzes the source to identify code that could have been executed but was not.
#      Coverage measurement is typically used to gauge the effectiveness of tests.
#      It can show which parts of your code are being exercised by tests, and which are not.
# 16. run coverage : coverage run manage.py test reviews
# 17. generate a report : coverage report 
# 18. generate html report : coverage html 
# 19. Add a many to many field to the reviews/models.py class Review 
# 20. write and run test for the many-to-many relationship 
# 