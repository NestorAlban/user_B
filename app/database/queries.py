# Database = user_database
GET_ALL_ACTIVE_USERS_QUERY = (
    "SELECT id, name, email, created_at, updated_at,is_active FROM public.user WHERE is_active=true"
)
CREATE_USER_QUERY = """
INSERT INTO public.user (id, name, email) VALUES (%s, %s, %s)
"""

# ID_KEY = "id"
# NAME_KEY = "name"
# MAIL_KEY = "email"
# STATUS_KEY = "is_active"
# CREATED_KEY = "created_at"
# UPDATED_KEY = "updated_at"
