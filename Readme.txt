Little Lemon Restaurant API

API Endpoints for testing:

/api/menu/             → Menu list & create (GET, POST)
/api/menu/<id>/        → Single menu item (GET, PUT, DELETE)

/api/booking/          → Booking list & create (GET, POST)
/api/booking/<id>/     → Single booking (GET, PUT, DELETE)

/api/api-token-auth/   → Generate token for authentication
/auth/users/           → Register a new user (Djoser)
/auth/token/login/     → Login and get token (Djoser)

Database: MySQL
Framework: Django REST Framework
Authentication: Token Authentication