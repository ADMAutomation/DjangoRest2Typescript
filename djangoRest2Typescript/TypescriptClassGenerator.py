from __future__ import unicode_literals
from rest_framework.metadata import SimpleMetadata
import os

class TypescriptClassGenerator:
    PYTHON2JSON_TYPE = {
        'string': 'string',
        'boolean': 'boolean',
        'number': 'number',
        'integer': 'number',
        'float': 'number',
        'decimal': 'number',
        'field': 'any',
        'email': 'string',
        'datetime': 'string',
        'date': 'string',
        'choice': 'string',
        'image upload': 'string',
        'file upload': 'string',
    }
    @staticmethod
    def getStaticOptionsCode(fieldName, fieldOptions):
        result = u'    public static get %s_options():{ [key: string] : any; } {' % fieldName
        result += os.linesep
        result += u'        return {'
        result += os.linesep

        keys = fieldOptions.keys()
        for k in ['required', 'read_only', 'max_length']:
            if k in keys:
                result += u'            "%s": %s, ' % (k, str(fieldOptions[k]).lower())
                result += os.linesep

        for k in ['label', 'help_text', 'type']:
            if k in keys:
                result += u'            "%s": "%s", ' % (k, str(fieldOptions[k]).lower())
                result += os.linesep
        result += u'        };'
        result += os.linesep
        result += u'    }'
        result += os.linesep
        return result
    @staticmethod
    def getSerializerName(serializer):
        return serializer.__class__.__name__

    @staticmethod
    def getClassName(apiViewInstance, serializer = None):
        if serializer is None:
            serializer = apiViewInstance.serializer_class()
        return serializer.__class__.__name__

    @staticmethod
    def getVersionCode(version = None):
        result = u''
        if version is not None:
            result = u'/*\n * Version %s\n*/\n\n' % version
        return result
    @staticmethod
    def getChoicesCode(fieldName, values):
        result = u'    public static get %s_choices():{ [key: string] : string; } {' % fieldName
        result += os.linesep
        result += u'        return {'
        result += os.linesep
        for v in values:
            result += u'            "%s": "%s", ' % ( v['value'], v['display_name'] )
            result += os.linesep
        result += u'        };'
        result += os.linesep
        result += u'    }'
        result += os.linesep
        return result

    @staticmethod
    def getFieldsCode(data):
        result = ''
        for key in data.keys():
            if data[key]['type'] in TypescriptClassGenerator.PYTHON2JSON_TYPE.keys():
                result += os.linesep
                result += u'    public %s:%s;' % (
                    key,
                    TypescriptClassGenerator.PYTHON2JSON_TYPE[data[key]['type']]
                )
                result += os.linesep
                result += TypescriptClassGenerator.getStaticOptionsCode(key, data[key])
                if data[key]['type'] == 'choice':
                    result += TypescriptClassGenerator.getChoicesCode(key, data[key]['choices'])
            else:
                raise Exception('Not supported type %s for field %s' % (data[key]['type'], key))

        return result


    @staticmethod
    def getCodeFromSerializer(serializer, version = None):
        result = TypescriptClassGenerator.getVersionCode(version)
        data = SimpleMetadata().get_serializer_info(serializer)
        name = TypescriptClassGenerator.getSerializerName(serializer)
        result += 'export class %s {' % name
        result += os.linesep
        result += TypescriptClassGenerator.getFieldsCode(data)
        result += '}'
        return result

    @staticmethod
    def getCode(apiViewInstance, version = None):
        result = TypescriptClassGenerator.getVersionCode(version)

        metadata = apiViewInstance.metadata_class()
        serializer = apiViewInstance.serializer_class()
        data = metadata.get_serializer_info(serializer)
        name = '%sView' % TypescriptClassGenerator.getClassName(apiViewInstance, serializer)
        result += 'export class %s {' % name
        result += os.linesep
        result += TypescriptClassGenerator.getFieldsCode(data)
        result += '}'
        return result
