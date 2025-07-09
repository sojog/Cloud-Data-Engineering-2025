#!/usr/bin/env python
import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djproject.settings')
django.setup()

from django.urls import reverse, NoReverseMatch

# Testez diferite nume de URL pentru activare
test_key = 'test123'

url_names = [
    'django_registration_activate',
    'registration_activate', 
    'activation_activate',
    'activate',
]

print("Testing URL names for activation...")
for name in url_names:
    try:
        # Testez cu kwargs
        url = reverse(name, kwargs={'activation_key': test_key})
        print(f"✅ {name} with kwargs: {url}")
    except NoReverseMatch as e:
        try:
            # Testez cu args
            url = reverse(name, args=[test_key])
            print(f"✅ {name} with args: {url}")
        except NoReverseMatch:
            print(f"❌ {name}: not found")

# Listez toate rutele disponibile care conțin 'activ'
from django.urls import get_resolver
resolver = get_resolver()

print("\nAll URLs containing 'activ':")
for pattern in resolver.url_patterns:
    if hasattr(pattern, 'name') and pattern.name and 'activ' in pattern.name:
        print(f"- {pattern.name}: {pattern.pattern}") 