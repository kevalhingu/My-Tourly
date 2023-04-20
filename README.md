# Project Title
 
My-Tourly - A responsive tour and travel website built in Django and Python. 

## Description
   
My-Tourly is a tour and travel website that allows users to discover and book travel packages, hotels, and transportation services with ease. The website features a functional login module and payment gateway for hassle-free booking.
   
## Getting Started 
 
### Dependencies      

* Python 3.6 or higher
* Django 3.1.7 or higher
* PostgreSQL 9.5 or higher (optional)
 
### Installation

1. Clone the repository: `git clone https://github.com/your-username/my-tourly.git`
2. Install the dependencies: `pip install -r requirements.txt`
3. Set up the database:
   * If you're using PostgreSQL, create a new database and update the settings in `mytourly/settings.py` accordingly.
   * If you're using SQLite (the default), no further configuration is required.
4. Run the migrations: `python manage.py migrate`
5. Create a superuser: `python manage.py createsuperuser`
6. Start the development server: `python manage.py runserver`

### Usage
 
1. Navigate to the homepage and browse through the available travel packages, hotels, and transportation services.
2. Login or create an account to make a booking and proceed to checkout.
3. Payment can be made through the integrated payment gateway for a hassle-free experience.

<!-- ### Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b new-feature`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin new-feature`. -->
