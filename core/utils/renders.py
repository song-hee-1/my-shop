from rest_framework.renderers import JSONRenderer


class CustomRender(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context.get('response').status_code

        response = {
            'meta': {
                'code': status_code,
                'message': data.get('detail') if status_code >= 400 else renderer_context.get('response').status_text,
            },
            'data': None if status_code >= 400 else data
        }

        return super().render(response, accepted_media_type, renderer_context)
