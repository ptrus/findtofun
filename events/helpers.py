

def get_modified_stuff(dict1, dict2):
    ''' Helper function for determing changed fields in model instance '''
    modified = {}
    for key, value in dict2.items():
        if (key in dict1 and
                value is not dict1.get(key)):
            modified[key] = dict2[key]

    return modified


def process_modified_stuff(model_instance, attrs, data):
    ''' Helper function for processing changed fields in model instance '''
    dict1 = {}
    for key in attrs:
        value = getattr(model_instance, key)
        dict1[key] = value

    modified = get_modified_stuff(dict1, data)
    for key, value in modified.items():
        setattr(model_instance, key, value)

    return modified.keys()


def change(obj, data, attrs, instance):
    modified_attrs = []
    for attr in attrs:
        tmp = data.get(attr)
        if (isinstance(tmp, instance) and
                tmp is not getattr(obj, attr)):
            setattr(obj, attr, tmp)
            modified_attrs.append(attr)

    return modified_attrs


def change_numfields(obj, data, attrs):
    return change(obj, data, attrs, (int, long))


def change_urlfields(obj, data, attrs):
    return change(obj, data, attrs, basestring)


def change_textfields(obj, data, attrs):
    return change(obj, data, attrs, basestring)
