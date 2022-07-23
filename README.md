# Library-Management-System

Library Management System
Features List

Student features:

Can register on the platform and then login using the auth token.
After authentication:-
Can reserve a book.
Can view his own profile.
Can edit/update his/her profile.
Can view list of Books

Admin/Librarian features:

Can create/update users, books, roles, categories, book categories.
Can assign an admin role to a registered user.
Can issue a book or reserve a book for a student.
Can return a book when a student returns the book. (Calculated fine stored in Issued Books table)
Can view lists of Users, Books, Roles, Categories, Book Categories, Issued Books, Reserved Books and User Roles.
Admin has permission to list/create/update/delete/retrieve for all tables and fields.
Can return a book.

Extra features and constraints:

Auto-assign new user role as Student.
If a book is currently issued or reserved, the user cannot issue or reserve it.
If a particular user has reserved it, only he/she can issue it.
The reserved book gets unreserved if the book is not issued within 2 days.
Only an authenticated user can access his own profile (retrieve or update).
Auto Fine calculation (Rs. 5 for each day).
Created_by, updated_by, deleted_by, date_created, date_updated and date_deleted should auto populate.

Relationships:

Book & Category - One to Many (BookCategory)
User & Role - One to Many (UserRole)
Book & User - One to Many (IssuedBook & ReservedBook)
