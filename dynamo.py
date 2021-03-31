def get_update_item_params(update):
    update_expression = 'set '
    expression_attribute_values = {}
    expression_attribute_names = {}
    # TODO if object then do nested
    keys_to_update = update.items()
    keys_to_update = filter(lambda key_value_pair : (key_value_pair[0] != 'student_id'), keys_to_update) # cannot update primary key
    keys_to_update = list(keys_to_update)
    for idx, (k, v) in enumerate(keys_to_update):
        update_expression += f'#{k}=:_{k}'
        if idx + 1 != len(keys_to_update):
            update_expression += ', '
        if type(v) == float:
            v = str(v)
        expression_attribute_values[f':_{k}'] = v
        expression_attribute_names[f"#{k}"] = k
    return {
        'UpdateExpression': update_expression,
        'ExpressionAttributeValues': expression_attribute_values,
        'ExpressionAttributeNames': expression_attribute_names,
        'ReturnValues': "UPDATED_NEW"
    }

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return (str(o) for o in [o])
        return super(DecimalEncoder, self).default(o)