from waitress import serve
    
from yourdjangoproject.wsgi import application
    
if __name__ == '__main__':
    serve(application)