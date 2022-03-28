# Database = user_database
GET_ALL_ACTIVE_USERS_QUERY = (
    "SELECT id, name, email, created_at, updated_at,is_active FROM public.user_database WHERE is_active=true"
)

CREATE_USER_QUERY = """
INSERT INTO public.user_database (name, email, is_active, created_at, updated_at) VALUES (%s, %s, %s, %s, %s)
"""

GET_ONE_USER_QUERY = """
SELECT * FROM public.user_database WHERE id=
"""

UPDATE_USER_DATA_QUERY = """
UPDATE public.user_database SET name=%s, email=%s, updated_at=%s   WHERE id=%s
"""

UPDATE_USER_STATUS_QUERY = """
UPDATE public.user_database SET is_active=%s, updated_at=%s   WHERE id=%s
"""


# ID_KEY = "id"
# NAME_KEY = "name"
# MAIL_KEY = "email"
# STATUS_KEY = "is_active"
# CREATED_KEY = "created_at"
# UPDATED_KEY = "updated_at"
