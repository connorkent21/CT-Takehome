from graphql_relay import from_global_id


def parse_global_relay_id(global_relay_id):
    if not global_relay_id:
        return None

    _, entity_id = from_global_id(global_relay_id)
    return int(entity_id)
