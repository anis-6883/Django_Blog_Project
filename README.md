# Django Blog Project
___
## Project Features 
1. User Authentication System
1. Add Forgot & Reset Password System
1. Full *CRUD* operation on Blog
1. Dynamic url routing
1. User's Profile with Signal
1. Like on Blog Post
1. Comment on Blog Post
1. Pagination
1. Use Third-Party Package
___

## Settings Configuration

In *settings file* in the Django project folder...
```
EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST          = 'smtp.gmail.com'
EMAIL_PORT          = 587
EMAIL_USE_TLS       = True
EMAIL_HOST_USER     = '#Your gmail'
EMAIL_HOST_PASSWORD = '#Your Password'
---
> In EMAIL_HOST_USER, you use your own 'yourmail@gmail.com' in a single quotation or double quotation. 

> In EMAIL_HOST_PASSWORD, you use your own 'password' in a single quotation or double quotation. 
---
## Password Configuration 
1. If you are not using ***2-steps verification***, you have to ***allow a less secure app*** for your Gmail account.
1. If you use ***2-steps verification***, you have to use the ***app password*** for your application. They will give you a plain text password for your particular app. You can use that password in ***EMAIL_HOST_PASSWORD*** without using your main Gmail password. 
