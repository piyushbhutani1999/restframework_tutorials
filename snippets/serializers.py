from rest_framework import serializers
from snippets.models import Snippets, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(required = False, allow_blank = True, max_length = 100)
    code = serializers.CharField(style = {'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required = True)
    language = serializers.ChoiceField(choices= LANGUAGE_CHOICES, default = 'python')
    style = serializers.ChoiceField(choices = STYLE_CHOICES, default = 'friendly')

    def create(self, validated_data):
        return Snippets.objects.create(**validated_data)

    def update(self, instance, valideated_data):
        instance.title = valideated_data.get('title', instance.title)
        instance.code = valideated_data.get('code', instance.code)
        instance.linenos = valideated_data.get('linenons', instance.linenos)
        instance.language = valideated_data.get('language', instance.language)
        instance.style = valideated_data.get('style', instance.style)
        instance.save()
        return instance