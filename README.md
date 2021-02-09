# splitwise

```python manage.py runserver 0.0.0.0:8000  

http://0.0.0.0:8000/admin/


setting.py change MYsql settings
Assumpsion:
	--User is Already login in system
	--User will add friend via email_id(that exists in db) or user_id
	-- Using Default User(Django User)
	--Group admin would be one - who create the group

work to do 
1) /create_group 
2) /add_to_group
3) /balance 
4) /add_expense
5) /list of all transaction


Model Design: models.py

User:
userid, name , email

Group:
Id , name, created_by


Group_User:
Id,  Group_id, user_id,


Expenses_In_group:
Group_id, user_id, expenses, meta -> text

```