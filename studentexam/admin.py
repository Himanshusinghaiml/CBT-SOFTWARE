"""The studentexam app no longer defines its own Question model.

For backwards compatibility we register the central Question model from
`companylogin`.  The legacy class lives in models.py for migration history
only and should not be used.
"""

from django.contrib import admin

# import the primary Question definition so it appears in the admin site
try:
    from companylogin.models import Question  # noqa: E402
except ImportError:
    Question = None  # if companylogin isn't installed for some reason

# The shared `Question` model is defined in `companylogin.models`. We
# import it here only if we need references, but we **do not** register
# it again with the admin site since it's already registered by the
# companylogin app. Attempting to register it twice leads to a
# ``AlreadyRegistered`` exception during startup (see tracebacks in the
# project history).

# If for some reason you want to provide a different ModelAdmin when the
# studentexam app is active, you can unregister and re-register it with
# a custom admin class. For now, we take the safe route and leave the
# registration solely in companylogin.

# Do not register `Question` here; it is registered in companylogin.admin
