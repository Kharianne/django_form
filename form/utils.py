def replace_key_to_label(label_mapping: dict, cleaned_data: dict):
    """
    Get labels instead of field name
    
    :param label_mapping: original label mapping from form Meta class
    :param cleaned_data: cleaned data from form after POST request
    :return: dictionary of replaced keys
    """""
    replaced = dict()
    print(label_mapping)
    for key, value in cleaned_data.items():
        try:
            replaced[label_mapping[key]] = value
        except KeyError:
            # In case we cannot get label, we use original name
            replaced[key] = value
    return replaced
