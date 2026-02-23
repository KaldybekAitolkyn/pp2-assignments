import json

def merge_patch(source, patch):
    if not isinstance(patch, dict):
        return patch
    if not isinstance(source, dict):
        source = {}

    result = dict(source)

    for key, patch_value in patch.items():
        if patch_value is None:
            result.pop(key, None)
        else:
            source_value = result.get(key)
            if isinstance(source_value, dict) and isinstance(patch_value, dict):
                result[key] = merge_patch(source_value, patch_value)
            else:
                result[key] = patch_value

    return result

source = json.loads(input().strip())
patch = json.loads(input().strip())

res = merge_patch(source, patch)
print(json.dumps(res, separators=(",", ":"), sort_keys=True, ensure_ascii=False))