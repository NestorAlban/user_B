# Database = user_database
GET_ALL_ACTIVE_USERS_QUERY = (
    "SELECT id, name, email, created_at, updated_at,is_active FROM public.user_database WHERE is_active=true"
)

CREATE_A_NEW_USER_QUERY = "INSERT INTO public.user_status(name, email, is_active) VALUES (%s, %s, %s)"

GET_ONE_USER_QUERY = "SELECT * FROM public.user_status WHERE idper="


ID_KEY = "id"
NAME_KEY = "name"
MAIL_KEY = "email"
STATUS_KEY = "is_active"
CREATED_KEY = "created_at"
UPDATED_KEY = "updated_at"
