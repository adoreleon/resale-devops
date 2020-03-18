from django.contrib import admin


class BaseModelAdmin(admin.ModelAdmin):
    def __init__(self, *args, **kwargs):
        if self.readonly_fields is not None and isinstance(self.readonly_fields, (list, set, tuple)):
            self.readonly_fields += ("updated_by", )
        super(BaseModelAdmin, self).__init__(*args, **kwargs)
