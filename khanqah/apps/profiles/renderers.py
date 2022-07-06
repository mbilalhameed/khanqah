import json

from psycopg2.extensions import JSON
from rest_framework.renderers import JSONRenderer


class ProfileJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accept_media_types=None, renderer_context=None):
        errors =data.get('errors', None)

        if errors is not None:
            return super(ProfileJSONRenderer, self).render(data)

        return json.dumps({'profile': data})
