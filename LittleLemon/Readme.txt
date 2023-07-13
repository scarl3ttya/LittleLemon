/*  URLs  */

about/
menu/               <--- List everything on the menu
menu/<int:pk>
reservations/       <--- User interface to view ALL reservations
book/               <--- User interface to BOOK a reservations
bookings?date=2023-07-12  <--specific dates
api/booking/        <--- API interface for reservations
api/menu/
api/menu/<int:pk>
api-token-auth/
auth/
auth/


/*  NOTES  */

/* setup database before migrate 
*  python manage.py makemigrations
*  python manage.py migrate
*/

install mysqlclient 
mysql -u root -p
show databases;
create database LittleLemon;
// use LittleLemon;
// show tables; 


/* don't forget to create user and grant permissions 
*  Sometimes you have to clear and flush cache so you can create the user 
*/

DROP user admindjango@localhost;
FLUSH privileges;

CREATE USER 'admindjango'@'localhost' IDENTIFIED BY 'employee@123!';
GRANT ALL PRIVILEGES ON *.* TO 'admindjango'@'localhost';

/*  settings.py */
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'LittleLemon',
        'USER': 'admindjango',
        'PASSWORD': 'employee@123!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}