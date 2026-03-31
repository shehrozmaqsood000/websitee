#!/usr/bin/env python3
"""
HOPE Preparations – Single File Website Builder
Run this to regenerate index.html with all images embedded.
"""
import base64, json, os

def b64img(path, mime='image/jpeg'):
    try:
        with open(path,'rb') as f:
            return f'data:{mime};base64,' + base64.b64encode(f.read()).decode()
    except Exception as e:
        print(f"Warning: could not load {path}: {e}")
        return ''

base = '/home/claude/hope-preparations/assets/images'
imgs = {
    'logo':   b64img(f'{base}/logo.png','image/png'),
    'dir':    b64img(f'{base}/director2.jpg'),
    'tielts': b64img(f'{base}/teacher-ielts.jpg'),
    'tsci':   b64img(f'{base}/teacher-science.jpg'),
    'tcomp':  b64img(f'{base}/teacher-computer.jpg'),
    'tgk':    b64img(f'{base}/teacher-gk.jpg'),
    'tmath':  b64img(f'{base}/teacher-math.jpg'),
    'tcs':    b64img(f'{base}/teacher-cs-skills.jpg'),
    'bielts': b64img(f'{base}/banner-ielts.jpg'),
    'blaw':   b64img(f'{base}/banner-law.jpg'),
    'bmain':  b64img(f'{base}/banner-main.jpg'),
}

print("Images loaded:")
for k,v in imgs.items():
    print(f"  {k}: {len(v)//1024} KB")

print("\nBuilding HTML...")
print("Done – see build output")
