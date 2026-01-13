#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Local CPU Stable Diffusion Image Generation
Copyright (C) 2026 Aravinth-Earth

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import os
import time
import json
from datetime import datetime
import torch
import random
from diffusers import StableDiffusionPipeline

def ensure_output_dir():
    """Create outputs directory if it doesn't exist."""
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def create_generation_folder(timestamp):
    """Create a timestamped generation folder with steps subfolder."""
    output_dir = ensure_output_dir()
    gen_folder = os.path.join(output_dir, timestamp)
    steps_folder = os.path.join(gen_folder, "steps")
    os.makedirs(steps_folder, exist_ok=True)
    return gen_folder, steps_folder

def generate_filename(width, height, steps, guidance_scale, seed):
    """Generate dynamic filename with parameters (without timestamp)."""
    filename = f"{width}x{height}_s{steps}_g{guidance_scale}_seed{seed}"
    return filename

def main():
    # ============================================================================
    # MODEL SELECTION
    # ============================================================================
    # Stable Diffusion 1.5 (RECOMMENDED FOR CPU)
    model_id = "runwayml/stable-diffusion-v1-5"
    
    # Other CPU-Friendly Models (Top 10):
    # 1. "runwayml/stable-diffusion-v1-5" - Best quality/speed balance
    # 2. "CompVis/stable-diffusion-v1-4" - Slightly faster
    # 3. "prompthero/openjourney" - Good artistic style
    # 4. "Linaqruf/anything-v3.0" - Fast anime/illustration style
    # 5. "DGSpitzer/Cyberpunk-Anime-Diffusion" - Anime focused
    # 6. "Deltaadams/DreamShaper" - Good quality/speed
    # 7. "stabilityai/stable-diffusion-2-1-base" - Higher quality (slower)
    # 8. "emilianJR/chilloutmix_NiPRunwayML" - Photorealistic
    # 9. "majicMixRealm_betterFidelityFp16" - Better details
    # 10. "eimiss/EimMix_Final-Model" - Excellent quality but slower
    
    # GPU-Optimized Models (Top 10 - much faster on GPU):
    # 1. "runwayml/stable-diffusion-v1-5" - Best all-around
    # 2. "stabilityai/stable-diffusion-xl-base-1.0" - Higher quality (4x larger)
    # 3. "stabilityai/stable-diffusion-3-medium-diffusers" - Latest, best quality
    # 4. "Lykon/dreamshaper-8" - Excellent photorealism
    # 5. "civitai/Chilloutmix_NiPRunwayML" - Photorealistic
    # 6. "OFA-Sys/model-card" - Multimodal (very advanced)
    # 7. "stablediffusionapi/sdxl-lightning" - Super fast on GPU
    # 8. "stabilityai/sdxl-turbo" - Real-time generation
    # 9. "alsomitra/protovision-xl-anime-engine" - Anime (amazing quality)
    # 10. "dreamlike-art/dreamlike-photoreal-2.0" - Photo quality

    
    # CPU-only
    device = "cpu"
    torch.set_num_threads(max(1, os.cpu_count() or 1))

    print("Loading pipeline (first run will download weights)...")
    t0 = time.time()

    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float32,   # CPU: float32 is safest
        safety_checker=None,         # optional: speeds up a bit
        requires_safety_checker=False
    )
    pipe = pipe.to(device)

    print(f"Loaded in {time.time() - t0:.1f}s")

    # ============================================================================
    # GENERATION PARAMETERS
    # ============================================================================
    prompt = "A tiny robot reading a book under a streetlamp, rainy night, cinematic lighting"
    # What to generate. Be descriptive! More details = more varied results.
    # Examples: landscape, portrait, still life, product photo, illustration, etc.
    
    negative_prompt = "blurry, low quality, distorted"
    # What to AVOID in the image. Helps prevent unwanted artifacts.
    # Common: "blurry, low quality, distorted, bad anatomy, ugly, deformed"
    
    width = 384
    # Image width in pixels. Range: 256-768 (multiples of 64 recommended)
    # Smaller = faster but lower quality. 384 is good balance for CPU.
    
    height = 384
    # Image height in pixels. Range: 256-768 (multiples of 64 recommended)
    # Smaller = faster but lower quality. Square (384x384) is good for CPU.
    
    steps = 10
    # Denoising iterations. Range: 5-50 (more steps = better quality but MUCH slower)
    # 5-10 = fast draft, 20-30 = good quality, 40-50 = excellent but very slow
    # CPU: 10 is recommended, GPU: 20-30
    
    guidance_scale = 5.0
    # How strictly to follow the prompt. Range: 1.0-20.0
    # 1.0 = ignore prompt (creative but random)
    # 5.0-7.0 = good balance (recommended)
    # 10.0-15.0 = very strict to prompt (less creative)
    # 20.0+ = extremely strict (may look overly "cooked"/oversaturated)
    # NOTE: Lower values are often faster!
    
    # seed = 1234
    seed = random.randint(0, 4294967295)
    # Random seed for reproducibility. Range: any integer (0-4294967295)
    # SAME seed + SAME prompt + SAME params = IDENTICAL image every time
    # Change seed to get different variations: 1234, 1235, 1236, etc.
    # If seed varies, images will differ even with same prompt!
    
    save_intermediate_steps = True
    # Save all 10 denoising steps to see generation progression
    # True = see progression (11 images total: 10 steps + 1 final)
    # False = only save final image (faster, 1 image total)

    generator = torch.Generator(device=device).manual_seed(seed)
    
    # Create timestamped generation folder early for live saving
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    gen_folder, steps_folder = create_generation_folder(timestamp)
    base_filename = generate_filename(width, height, steps, guidance_scale, seed)

    print("Generating...")
    t1 = time.time()
    
    # Create callback to save intermediate steps live with dynamic timestamps
    def callback(step, _timestep, latents):
        """Callback to save intermediate images as they're generated (live streaming)."""
        if save_intermediate_steps:
            try:
                from PIL import Image
                import numpy as np
                
                # Get current time for this specific step
                step_time = datetime.now().strftime("%H%M%S")
                
                # Decode latents to image
                with torch.no_grad():
                    image = pipe.vae.decode(
                        latents / pipe.vae.config.scaling_factor, 
                        return_dict=False
                    )[0]
                
                # Convert to PIL Image
                image_np = image.cpu().permute(0, 2, 3, 1).numpy()
                image_np = (image_np / 2 + 0.5).clip(0, 1)
                image_np = (image_np * 255).astype(np.uint8)[0]
                pil_image = Image.fromarray(image_np)
                
                # Save immediately with dynamic timestamp for each step
                step_img_path = os.path.join(steps_folder, f"step_{step:02d}_{step_time}.png")
                pil_image.save(step_img_path)
                print(f"  Step {step:02d} saved at {step_time}: {step_img_path}")
            except Exception:
                print(f"  Warning: Could not save step {step}")
    
    out = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        width=width,
        height=height,
        num_inference_steps=steps,
        guidance_scale=guidance_scale,
        generator=generator,
        callback=callback,
        callback_steps=1
    )
    img = out.images[0]
    dt = time.time() - t1

    # Save final image in main generation folder with full detailed name
    final_img_path = os.path.join(gen_folder, f"{timestamp}_{base_filename}.png")
    img.save(final_img_path)
    print(f"\nFinal image: {final_img_path}")
    
    # Save metadata in main generation folder
    metadata = {
        "timestamp": datetime.now().isoformat(),
        "generation_folder": timestamp,
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "width": width,
        "height": height,
        "steps": steps,
        "guidance_scale": guidance_scale,
        "seed": seed,
        "generation_time_seconds": dt,
        "model_id": model_id,
        "intermediate_steps_saved": save_intermediate_steps
    }
    metadata_path = os.path.join(gen_folder, f"{timestamp}_{base_filename}.json")
    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)
    
    print(f"Metadata: {metadata_path}")
    print(f"Generation time: {dt:.1f}s")

if __name__ == "__main__":
    main()
