GET_ALL_ACTIVE_USERS_QUERY = (
    "SELECT id, name, email, created_at, updated_at,is_active FROM public.user WHERE is_active=true"
)
