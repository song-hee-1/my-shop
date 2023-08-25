from rest_framework.renderers import JSONRenderer


class CustomRender(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_data = renderer_context.get('response')
        status_code = response_data.status_code

        response = {
            'meta': {
                'code': status_code,

                'message': response_data.status_text,
            },
            'data': data
        }

        if status_code >= 400:
            response['data'] = None

        return super(CustomRender, self).render(response, accepted_media_type, renderer_context)