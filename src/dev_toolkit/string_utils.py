"""
Developer text transformation, casing, and normalization utilities.
"""

import re

def slugify(text: str) -> str:
    """Converts input string into URL-safe slug format."""
    text = re.sub(r'[^\w\s-]', '', text.lower())
    return re.sub(r'[-\s]+', '-', text).strip('-')

def camel_to_snake(text: str) -> str:
    """Converts camelCase or PascalCase strings to snake_case."""
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    return pattern.sub('_', text).lower()

def snake_to_camel(text: str) -> str:
    """Converts snake_case strings to camelCase."""
    components = text.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])
