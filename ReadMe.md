# Local Media Generation (CPU-based Stable Diffusion)

> **License**: GNU Affero General Public License v3.0  
> **Author**: Aravinth-Earth

Generate AI images locally on your CPU without needing a GPU. Perfect for testing and running on any machine.

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

That's it! Standard `pip install` works fine for CPU. PyTorch includes CPU support by default.

**Note:** First run downloads ~4GB model weights (one-time only).

### 2. Run Image Generation

```bash
python cpu_sd.py
```

### 3. Find Your Images

Check: `outputs/yyyymmddhhmmss/`

**Folder structure:**
```
outputs/
└── 20250114_143022/              # Timestamp folder for this generation
    ├── steps/                     # All denoising steps (if enabled)
    │   ├── 20250114_143022_step_00.png
    │   ├── 20250114_143022_step_01.png
    │   └── ...
    ├── 20250114_143022_384x384_s10_g5.0_seed1234_prompt_text.png  # Final image
    └── 20250114_143022_384x384_s10_g5.0_seed1234_prompt_text.json   # Metadata
```

## Customize Settings

Edit these in `cpu_sd.py`:

```python
# What to generate - be descriptive!
prompt = "A tiny robot reading a book under a streetlamp, rainy night, cinematic lighting"

# Image dimensions. Range: 256-768 (multiples of 64 work best)
# 256x256 = fastest, 384x384 = good balance, 512x512 = slower, 768x768 = very slow
width = 384
height = 384

# Denoising steps. Range: 5-50
# 5-10 = fast draft (CPU good)
# 20-30 = good quality (GPU ideal)
# 40+ = excellent but very slow
steps = 10

# Prompt adherence. Range: 1.0-20.0
# 1-3 = creative/random, 5-7 = balanced (recommended), 10+ = very strict
# Higher values sometimes faster but may look "overcooked"
guidance_scale = 5.0

# Random seed for reproducible results. Range: 0-4294967295
# IMPORTANT: Same seed + same prompt = IDENTICAL image every time
# To get variations, change seed: 1234, 1235, 1236, etc.
seed = 1234

# Save all denoising progression steps
save_intermediate_steps = True  # True = 11 images, False = 1 image
```

## Why Are My Images Almost Identical?

**You're using the same seed!** 

The `seed` parameter controls randomness. When you use the same seed (e.g., 1234), you get:
- **Identical** images with the same prompt & parameters
- This is actually USEFUL for testing and reproducibility

To get **different** images:
```python
seed = 1234  # Try 1235, 1236, 1237, etc.
```

Or use random seeds:
```python
import random
seed = random.randint(0, 4294967295)
```

The same seed + same prompt always produces the same image - it's not a bug, it's a feature!

## Model Selection

Edit `model_id` in `cpu_sd.py` to use different models.

### Best Models for CPU (10 Top Choices)

```python
# Speed/Quality Balanced (RECOMMENDED)
model_id = "runwayml/stable-diffusion-v1-5"

# Also good for CPU:
"CompVis/stable-diffusion-v1-4"                    # Slightly faster
"prompthero/openjourney"                           # Artistic style
"Linaqruf/anything-v3.0"                           # Anime/fast
"DGSpitzer/Cyberpunk-Anime-Diffusion"             # Anime focused
"Deltaadams/DreamShaper"                          # Good quality/speed
"stabilityai/stable-diffusion-2-1-base"           # Higher quality (slower)
"emilianJR/chilloutmix_NiPRunwayML"              # Photorealistic
"majicMixRealm_betterFidelityFp16"                # Better details
"eimiss/EimMix_Final-Model"                       # Excellent (slowest)
```

### Top Models for GPU (Much Faster!)

```python
# Latest and best quality:
"stabilityai/stable-diffusion-xl-base-1.0"        # 4x better quality (larger)
"stabilityai/stable-diffusion-3-medium-diffusers" # Latest version
"Lykon/dreamshaper-8"                             # Excellent photorealism
"civitai/Chilloutmix_NiPRunwayML"                # Photorealistic
"stablediffusionapi/sdxl-lightning"               # Super fast on GPU
"stabilityai/sdxl-turbo"                          # Real-time generation
"alsomitra/protovision-xl-anime-engine"           # Anime (amazing)
"dreamlike-art/dreamlike-photoreal-2.0"           # Photo quality
"OFA-Sys/model-card"                              # Multimodal (advanced)
```

### Find More Models

- **Hugging Face Hub:** https://huggingface.co/models?pipeline_tag=text-to-image&sort=trending
- **Civitai:** https://civitai.com (community models, ratings)
- **Model Index:** https://stable-diffusion-art.com/models/


- **Reduce resolution**: 512→384 (30% faster)
- **Reduce steps**: 20→10 (50% faster)
- **Reduce guidance**: 7→5 (sometimes faster)
- **Turn off steps**: Set `save_intermediate_steps = False`

**Speed example:** 384x384, 10 steps = ~2 minutes on modern CPU

## Live Updates

As generation runs, each step is saved immediately to `steps/` folder. Watch the image evolve step-by-step!

## System Requirements

- Python 3.8+
- 8GB RAM (16GB recommended)
- Any CPU (GPU not needed)
- ~5GB disk space (models download once)

## FAQ


**Q: Why is it slow?**
A: CPU inference takes time. Use the speed tips above or reduce `steps` more.

**Q: Can I use a different model?**
A: Yes! Change `model_id` in `cpu_sd.py` to any Stable Diffusion 1.5 model from Hugging Face.

**Q: What are the step images?**
A: Each step shows the denoising process. Step 0 = noise, Step 10 = final image. Like watching an artist gradually reveal a painting!

