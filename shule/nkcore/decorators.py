from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test 


# Admin checking login....

def admin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_admin,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )

    if function:
        return actual_decorator(function)
    return actual_decorator


#  Cachier checking login.....

def cachier_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    actual_decorator = user_passes_test( 
        lambda u: u.is_active and u.is_cachier,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )

    if function:
        return actual_decorator(function)
    return actual_decorator

# Secretary checking login.....

def secretary_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_secretary, 
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )

    if function:
        return actual_decorator(function)
    return actual_decorator
