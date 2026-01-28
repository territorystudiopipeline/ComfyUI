# -*- coding: utf-8 -*-

name = 'ComfyUI'

version = '9.9.9'

description = \
    """ ComfyUI
    """

variants = [['python-_3.12']]

requires = [
    'comfyui_frontend_package', 
    'comfyui_workflow_templates', 
    'comfyui_embedded_docs', 
    'torch', 
    'torchsde', 
    'torchvision', 
    'torchaudio', 
    'numpy', 
    'einops', 
    'transformers', 
    'tokenizers', 
    'sentencepiece', 
    'safetensors', 
    'aiohttp', 
    'yarl', 
    'PyYAML', 
    'pillow', 
    'scipy', 
    'tqdm', 
    'psutil', 
    'alembic', 
    'SQLAlchemy', 
    'av', 
    'comfy_kitchen', 
    'kornia', 
    'spandrel', 
    'pydantic', 
    'pydantic_settings'
]

def commands():
    env.COMFYUI_MODEL_LOCATION = "X:/__pipeline/software/ai_models/"

    env.COMFY_ROOT = expandvars("{root}")

    env.PATH.append(expandvars("{root}"))
