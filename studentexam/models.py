"""
The `Question` model previously defined here has been superseded by
`companylogin.models.Question`.  The studentexam app just imports the
companylogin version so we keep this file for backwards compatibility but
don't register a new model.

If migrations still include this model, you should delete the corresponding
table or create a migration that removes it.  For now the class is renamed
to `LegacyQuestion` and not referenced elsewhere.
"""

from django.db import models


class LegacyQuestion(models.Model):
    # kept for migration history only - do not use in new code
    question_text = models.CharField(max_length=200)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=100)

    def __str__(self):
        return self.question_text

