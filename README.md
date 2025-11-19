# Django-React Notes App

A full-stack web application for creating and managing notes with user authentication. Built with Django REST Framework backend and React frontend.

## Features

- **User Authentication**: Register and login with JWT tokens
- **Note Management**: Create, read, and delete notes
- **Protected Routes**: Only authenticated users can access notes
- **Token Refresh**: Automatic token refresh for seamless user experience
- **Responsive UI**: Clean and intuitive interface built with React
- **CORS Enabled**: Secure cross-origin communication between frontend and backend

## Tech Stack

### Backend
- **Django 5.2.8** - Web framework
- **Django REST Framework 3.16.1** - RESTful API framework
- **Django CORS Headers 4.9.0** - Cross-origin request handling
- **djangorestframework-simplejwt 5.5.1** - JWT authentication
- **PostgreSQL** (or SQLite for development)
- **Python 3.x**

### Frontend
- **React 19.2.0** - UI library
- **Vite 7.2.2** - Build tool and dev server
- **React Router 7.9.6** - Client-side routing
- **Axios 1.13.2** - HTTP client
- **jwt-decode 4.0.0** - JWT token decoding

## Project Structure

```
Django-React-Project/
├── backend/
│   ├── api/
│   │   ├── migrations/
│   │   ├── models.py          # Note model
│   │   ├── views.py           # API views
│   │   ├── serializers.py     # DRF serializers
│   │   ├── urls.py            # API routes
│   │   └── tests.py
│   ├── backend/
│   │   ├── settings.py        # Django settings
│   │   ├── urls.py            # Main URL config
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── manage.py
│   ├── db.sqlite3
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Form.jsx                # Login/Register form
│   │   │   ├── LoadingIndicator.jsx    # Loading spinner
│   │   │   ├── Note.jsx                # Note display component
│   │   │   └── ProtectedRoute.jsx      # Route protection wrapper
│   │   ├── pages/
│   │   │   ├── Home.jsx                # Notes management page
│   │   │   ├── Login.jsx               # Login page
│   │   │   ├── Register.jsx            # Registration page
│   │   │   └── NotFound.jsx            # 404 page
│   │   ├── styles/
│   │   │   ├── Form.css
│   │   │   ├── Home.css
│   │   │   ├── Note.css
│   │   │   └── loadingIndicator.css
│   │   ├── App.jsx                     # Main app component
│   │   ├── api.js                      # Axios API configuration
│   │   ├── constants.js                # Token constants
│   │   └── main.jsx
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── .env                            # Environment variables
│
├── .gitignore
└── README.md
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- Node.js 16+ and npm
- Git

### Backend Setup

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Create and activate virtual environment**:
   ```bash
   # Windows
   python -m venv env
   env\Scripts\activate
   
   # macOS/Linux
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional)**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Start Django server**:
   ```bash
   python manage.py runserver
   ```
   The backend will run on `http://127.0.0.1:8000`

### Frontend Setup

1. **Navigate to frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Create `.env` file**:
   ```
   VITE_API_URL=http://127.0.0.1:8000
   ```

4. **Start development server**:
   ```bash
   npm run dev
   ```
   The frontend will run on `http://localhost:5173`

## API Endpoints

### Authentication
- `POST /api/user/register/` - Register a new user
  - Body: `{ "username": "string", "password": "string" }`
  
- `POST /api/token/` - Login and get JWT tokens
  - Body: `{ "username": "string", "password": "string" }`
  - Returns: `{ "access": "token", "refresh": "token" }`
  
- `POST /api/token/refresh/` - Refresh access token
  - Body: `{ "refresh": "token" }`

### Notes
- `GET /api/notes/` - Get all notes for authenticated user
- `POST /api/notes/` - Create a new note
  - Body: `{ "title": "string", "content": "string" }`
  
- `DELETE /api/notes/{id}/` - Delete a note

## Usage

1. **Start both servers** (backend on port 8000, frontend on port 5173)

2. **Register**: Navigate to `/register` and create a new account

3. **Login**: Use your credentials to login at `/login`

4. **Create Notes**: On the home page, fill in title and content, then click Submit

5. **View Notes**: All your notes appear on the home page

6. **Delete Notes**: Click the Delete button on any note to remove it

7. **Logout**: Click the logout button to clear your session

## Configuration

### Django Settings (`backend/backend/settings.py`)
- `DEBUG = True` - Set to `False` for production
- `ALLOWED_HOSTS` - Add your domain
- `CORS_ALLOWED_ORIGINS` - Configure allowed frontend URLs
- `SIMPLE_JWT` - Adjust token expiration times

### Frontend Environment (`frontend/.env`)
- `VITE_API_URL` - Backend API URL

## Security Notes

⚠️ **For Development Only:**
- The secret key is exposed in `settings.py` - generate a new one for production
- `DEBUG = True` should be `False` in production
- Use environment variables for sensitive data
- Enable HTTPS in production
- Use strong passwords and proper token expiration

## Build for Production

### Backend
```bash
# Use a production WSGI server like Gunicorn
pip install gunicorn
gunicorn backend.wsgi:application
```

### Frontend
```bash
npm run build
# Output will be in dist/ folder
```

## Troubleshooting

### CORS Errors
- Ensure `CORS_ALLOWED_ORIGINS` in Django settings includes your frontend URL
- Check that the frontend is making requests to the correct backend URL

### 404 Errors
- Verify API endpoints match Django URL configuration
- Check that the baseURL in `api.js` is correct

### Authentication Issues
- Clear browser localStorage if having token issues
- Check token expiration times in `SIMPLE_JWT` settings
- Verify JWT token structure in browser dev tools

### Port Already in Use
- Change port in Django: `python manage.py runserver 8001`
- Change port in Vite: `npm run dev -- --port 5174`

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Author

**Asakhe-S** - [GitHub Profile](https://github.com/Asakhe-S)

## Support

For issues and questions, please open an issue on the [GitHub repository](https://github.com/Asakhe-S/Django-React-Project/issues).

---

**Happy coding!** 🚀
