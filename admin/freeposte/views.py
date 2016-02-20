import flask_admin as admin
from flask_admin.contrib import sqla

from freeposte import app, db, models


# Flask admin
admin = admin.Admin(app, name='Freeposte.io', template_mode='bootstrap3')


class BaseModelView(sqla.ModelView):

    def after_model_change(self, form, model, is_created):
        db.session.commit()

    def after_model_delete(self, model):
        db.session.commit()


class DomainModelView(BaseModelView):
    pass


class UserModelView(BaseModelView):
    pass


class AliasModelView(BaseModelView):
    pass


# Add views
admin.add_view(DomainModelView(models.Domain, db.session))
admin.add_view(UserModelView(models.User, db.session))
admin.add_view(AliasModelView(models.Alias, db.session))