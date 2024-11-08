from pathlib import Path
import os
import environ
from corsheaders.defaults import default_headers

# Inicializa o django-environ
env = environ.Env(
    DEBUG=(bool, False)  # Define o valor padrão de DEBUG como False
)

# Carrega o arquivo .env se ele existir
environ.Env.read_env(os.path.join(Path(__file__).resolve().parent.parent, '.env'))

# Diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Chave secreta
SECRET_KEY = env('SECRET_KEY')

# Debug - deve ser False em produção
DEBUG = env.bool('DEBUG', default=False)

# Hosts permitidos
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['127.0.0.1', 'localhost'])

# Definindo o ID do site
SITE_ID = 1

# Aplicações instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',         # Necessário para alguns pacotes de autenticação
    'egressos',                     # Seu aplicativo Django
    'corsheaders',                  # Para lidar com CORS
    'rest_framework',               # Django REST Framework
    'rest_framework.authtoken',     # Autenticação baseada em token
    'django_extensions',            # Ferramentas de desenvolvimento adicionais, como o shell_plus
    'debug_toolbar',                # Ferramenta para debug no Django (desenvolvimento local)
]

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Middleware para CORS
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Condicional para adicionar o 'debug_toolbar' apenas no modo DEBUG
if DEBUG:
    MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

# Configuração do CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

CORS_ALLOW_CREDENTIALS = True  # Permite o envio de cookies com requisições CORS
CORS_ALLOW_HEADERS = list(default_headers) + [
    'X-Custom-Header',
]

# Para desenvolvimento, você pode usar CORS_ALLOW_ALL_ORIGINS
if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True

# Configuração do Debug Toolbar
INTERNAL_IPS = [
    '127.0.0.1',  # Necessário para o funcionamento do debug toolbar em desenvolvimento
]

# URL de configuração das rotas
ROOT_URLCONF = 'setup.urls'

# Configurações de templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'setup/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Aplicação WSGI
WSGI_APPLICATION = 'setup.wsgi.application'

# Configuração do banco de dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validação de senha
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internacionalização e Fuso Horário
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Fortaleza'
USE_I18N = True
USE_TZ = True

# Configurações de arquivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'setup/statics')  # Pasta onde os arquivos estáticos estão no projeto
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # Diretório onde os arquivos estáticos serão coletados (em produção)

# Configurações de arquivos de mídia
MEDIA_URL = '/media/'  # URL base para arquivos de mídia
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Diretório onde os arquivos de mídia serão armazenados

# Configuração do Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_CONTENT_NEGOTIATION_CLASS': 'rest_framework.negotiation.DefaultContentNegotiation',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}


# Reinicie o servidor após atualizar este arquivo
