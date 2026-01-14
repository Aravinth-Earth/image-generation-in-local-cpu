# Local Media Generation (CPU-based Stable Diffusion)

> **License**: GNU Affero General Public License v3.0  
> **Author**: Aravinth-Earth

Generate AI images locally on your CPU without needing a GPU. Perfect for testing and running on any machine.

---

## ⚠️ Before You Start - What You Need

This guide assumes you're on **Windows**. Don't worry if you're not technical - we'll explain everything!

### System Requirements (Check Your Computer)

- **Python 3.10 or newer** - [Check if you have it](#check-python)
- **8GB+ RAM** (16GB recommended for best performance)
- **~5GB free disk space** (for AI models, downloaded once)
- **Any CPU** (no GPU needed - works on laptop, desktop, etc.)

### What is "Python" and Why Do We Need It?

Python is a programming language. Think of it like a translator that understands instructions. We'll use Python to run the AI image generator.

### What is "pip"?

`pip` is like an app store for Python. It downloads and installs code libraries that our program needs to work.

### What is a "Virtual Environment"?

A virtual environment is an isolated folder on your computer where we install Python packages just for this project. This keeps everything organized and prevents conflicts with other programs. Think of it like a separate workspace.

---

## Step 0: Check Python is Installed ✓

### Check Python

1. **Open Windows Terminal or Command Prompt**
   - Press `Windows key + R`
   - Type `cmd` and press Enter
   - A black window will open

2. **Check Python version:**
   ```bash
   python --version
   ```

3. **What you should see:**
   ```
   Python 3.10.x (or newer like 3.11, 3.12)
   ```

   ✅ **If you see Python 3.10+:** Great! Go to Step 1.
   
   ❌ **If you see "Python is not recognized":** Python isn't installed. [Download Python here](https://www.python.org/downloads/) → Run installer → **CHECK "Add Python to PATH"** → Install

---

## Step 1: Download This Project

**Choose Option A or B below:**

### Option A: Download as ZIP (Easiest - No Git Needed)

1. Go to: [Aravinth-Earth/image-generation-in-local-cpu](https://github.com/Aravinth-Earth/image-generation-in-local-cpu)
2. Click the green **Code** button
3. Click **Download ZIP**
4. **Unzip** the file somewhere easy to find (like `C:\Users\YourName\Documents\local-media-gen`)
5. Go to **Step 2**

### Option B: Clone with Git (For Advanced Users)

If you have Git installed:
```bash
git clone https://github.com/Aravinth-Earth/image-generation-in-local-cpu.git
cd local-media-gen
```

---

## Step 2: Create a Virtual Environment

**This is important!** A virtual environment keeps everything organized.

### On Windows (Using Command Prompt/PowerShell):

1. **Open Command Prompt** (press `Windows key + R`, type `cmd`, press Enter)

2. **Navigate to the project folder:**
   ```bash
   cd C:\path\to\your\local-media-gen
   ```
   *(Replace `C:\path\to\your\` with where you saved the project)*

3. **Create the virtual environment:**
   ```bash
   python -m venv venv
   ```
   This creates a folder called `venv` - this is your isolated workspace.

4. **Activate the virtual environment:**
   ```bash
   venv\Scripts\activate
   ```
   
   **You should see `(venv)` appear at the start of your command line** - this means it's working!

### Using an IDE? (Optional - Easier Way)

If you have **Visual Studio Code** installed:

1. Open VS Code
2. Open the project folder: File → Open Folder → Select `local-media-gen`
3. Open Terminal: Terminal → New Terminal
4. The terminal automatically shows your project path
5. Run the activate command above
6. Continue to Step 3

---

## Step 3: Install Dependencies

Now that your virtual environment is activated (you should see `(venv)` in the terminal), run:

```bash
pip install -r requirements.txt
```

**What's happening:**
- `pip` downloads Python packages your program needs
- `requirements.txt` is a list of everything to install
- **First time only:** Downloads ~4GB of AI model weights (one-time, be patient!)

**Expected output:**
```
Successfully installed torch, diffusers, pillow, ...
```

✅ **All packages installed!** Move to Step 4.

---

## Step 4: Customize Your Image Settings (Optional)

Before running, you can customize what the AI generates.

1. **Open `cpu_sd.py` in a text editor** (Notepad works, or use VS Code)

2. **Look for these lines in `cpu_sd.py` (around line 88-137):**

```python
# ============================================================================
# GENERATION PARAMETERS
# ============================================================================
prompt = "A tiny robot reading a book under a streetlamp, rainy night, cinematic lighting"
# What to generate. Be descriptive! More details = more varied results.

negative_prompt = "blurry, low quality, distorted"
# What to AVOID in the image. Helps prevent unwanted artifacts.

width = 384
# Image width in pixels. Range: 256-768 (multiples of 64 recommended)
# Smaller = faster. 384 is good balance for CPU.

height = 384
# Image height in pixels. Range: 256-768

steps = 10
# Denoising iterations. Range: 5-50 (more steps = better quality but MUCH slower)
# 5-10 = fast draft (CPU ideal), 20-30 = good quality, 40+ = very slow

guidance_scale = 5.0
# How strictly to follow the prompt. Range: 1.0-20.0
# 1.0-3.0 = creative/random, 5.0-7.0 = balanced (recommended), 10.0+ = very strict

seed = random.randint(0, 4294967295)
# Leave as random for different images, or use: seed = 1234 for reproducible results

save_intermediate_steps = True
# True = save all 10 steps to see progression
# False = save only final image (faster)
```

**💡 First Time Tips:**
- Don't change anything yet - just run it as-is!
- **First generation takes longer** (downloading ~4GB of AI model weights)
- Keep settings as-is on first run: 384x384, 10 steps
- Subsequent runs will be **much faster** (2-3 minutes)

---

## Step 5: Run the Image Generator

1. **Make sure your virtual environment is active** - you should see `(venv)` in the terminal

2. **Run the program:**
   ```bash
   python cpu_sd.py
   ```

3. **First run - what you'll ACTUALLY see:**
   ```
   Loading pipeline (first run will download weights)...
   
   Loading pipeline components...: 100%|##########| 6/6 [00:00<00:00, 10.10it/s]
   Loaded in 3.7s
   Generating...
   
     0%|          | 0/10 [00:00<?, ?it/s]
     Step 01 saved at 170746: outputs\20260114_170730\steps\step_01_170746.png
    10%|#         | 1/10 [00:15<02:15, 15.08s/it]
     Step 02 saved at 170759: outputs\20260114_170730\steps\step_02_170759.png
    20%|##        | 2/10 [00:28<01:52, 14.06s/it]
     Step 03 saved at 170811: outputs\20260114_170730\steps\step_03_170811.png
    30%|###       | 3/10 [00:40<01:32, 13.24s/it]
     Step 04 saved at 170823: outputs\20260114_170730\steps\step_04_170823.png
    40%|####      | 4/10 [00:52<01:17, 12.84s/it]
     Step 05 saved at 170836: outputs\20260114_170730\steps\step_05_170836.png
    50%|#####     | 5/10 [01:05<01:03, 12.78s/it]
     Step 06 saved at 170849: outputs\20260114_170730\steps\step_06_170849.png
    60%|######    | 6/10 [01:18<00:50, 12.73s/it]
     Step 07 saved at 170901: outputs\20260114_170730\steps\step_07_170901.png
    70%|#######   | 7/10 [01:30<00:38, 12.67s/it]
     Step 08 saved at 170914: outputs\20260114_170730\steps\step_08_170914.png
    80%|########  | 8/10 [01:43<00:25, 12.76s/it]
     Step 09 saved at 170927: outputs\20260114_170730\steps\step_09_170927.png
    90%|######### | 9/10 [01:56<00:12, 12.74s/it]
     Step 10 saved at 170940: outputs\20260114_170730\steps\step_10_170940.png
   100%|##########| 10/10 [02:09<00:00, 12.86s/it]
   100%|##########| 10/10 [02:17<00:00, 13.70s/it]
   
   Final image: outputs\20260114_170730\20260114_170730_384x384_s10_g5.0_seed1053752477.png
   Metadata: outputs\20260114_170730\20260114_170730_384x384_s10_g5.0_seed1053752477.json
   Generation time: 145.4s
   ```

4. **What you're seeing:**
   - `Loading pipeline components...` = Initializing the AI model (3.7 seconds)
   - `0% | 0/10` = Progress bar showing 10 steps running
   - `Step 01 saved at 170746: ...` = Each step being saved with timestamp
   - Progress bar with `|` fills up as it progresses (0% → 100%)
   - Warnings about deprecated features are normal (ignore them)
   - `Final image: outputs\20260114_170730\...png` = Location of your generated image
   - `Generation time: 145.4s` = Total time (~2 minutes 25 seconds)

✅ **Success!** Your image is generated and saved.

---

## Step 6: Find Your Generated Images

Your images are in: **`outputs/YYYYMMDD_HHMMSS/`** (a timestamped folder)

### Real Example (From Actual Run):

```
outputs/
└── 20260114_170730/                    # Timestamp: Jan 14, 2026 at 17:07:30
    ├── steps/                           # All 10 denoising steps (progression)
    │   ├── step_01_170746.png
    │   ├── step_02_170759.png
    │   ├── step_03_170811.png
    │   ├── step_04_170823.png
    │   ├── step_05_170836.png
    │   ├── step_06_170849.png
    │   ├── step_07_170901.png
    │   ├── step_08_170914.png
    │   ├── step_09_170927.png
    │   └── step_10_170940.png
    │
    ├── 20260114_170730_384x384_s10_g5.0_seed1053752477.png
    │   ↑ THE FINAL IMAGE (open this!) 🎨
    │
    └── 20260114_170730_384x384_s10_g5.0_seed1053752477.json
        ↑ Metadata with all settings
```

### What Each File Is:

| File | What It Is |
|------|-----------|
| `step_01.png` - `step_10.png` | 10 progression images (AI "painting" steps) |
| Final `.png` file | **Your complete AI-generated image** ✨ |
| `.json` file | Settings & statistics (prompt, seed, generation time) |

### Open Your Image:

1. Open Windows File Explorer
2. Go to: `local-media-gen\outputs\`
3. Open the **latest timestamped folder** (highest number)
4. Open the `.png` file (NOT the step images)
5. **That's your AI image!** 🎨

### What the Metadata Contains:

```json
{
  "timestamp": "2026-01-14T17:09:55.546229",
  "generation_folder": "20260114_170730",
  "prompt": "A tiny robot reading a book under a streetlamp, rainy night, cinematic lighting",
  "negative_prompt": "blurry, low quality, distorted",
  "width": 384,
  "height": 384,
  "steps": 10,
  "guidance_scale": 5.0,
  "seed": 1053752477,
  "generation_time_seconds": 145.4,
  "model_id": "runwayml/stable-diffusion-v1-5",
  "intermediate_steps_saved": true
}
```

### Reading the Filename:

```
20260114_170730_384x384_s10_g5.0_seed1053752477.png
│               │      │    │    │
│               │      │    │    └─ Seed (for reproducibility)
│               │      │    └─ Guidance scale (5.0)
│               │      └─ Steps (10 steps)
│               └─ Dimensions (384×384 pixels)
└─ Timestamp (2026-01-14 at 17:07:30)
```

### Step Filenames:

Step files include timestamps too:
```
step_01_170746.png  = Step 1, saved at 17:07:46
step_02_170759.png  = Step 2, saved at 17:07:59
...
step_10_170940.png  = Step 10, saved at 17:09:40
```

**💡 The timestamps in step filenames show when each step was saved!**

---

## ⚡ Speed Tips (For Impatient People!)

| Setting | Speedup | Impact |
|---------|---------|--------|
| 384×384 → 256×256 | 30% faster | Image is smaller |
| 10 steps → 5 steps | 50% faster | Lower quality |
| Disable step images | 10% faster | Don't see progress |
| guidance 5.0 → 3.0 | Sometimes faster | Less accurate to prompt |

**Example:** 256×256 + 5 steps = ~1 minute on modern CPU

---

## ❓ Troubleshooting

### Problem: "Python is not recognized"
**Solution:** Python isn't installed or not added to PATH
- Download from [python.org](https://www.python.org/downloads/)
- Run installer
- **IMPORTANT:** Check "Add Python to PATH"
- Restart command prompt

### Problem: "No module named 'X'" (after pip install)
**Solution:** Virtual environment not activated
- Make sure you see `(venv)` in your terminal
- Run: `venv\Scripts\activate`

### Problem: It's taking forever!
**This is normal.** First run downloads models (~5GB). Just wait.
- Subsequent runs will be much faster
- To speed up future runs, use smaller images or fewer steps

### Problem: Out of memory / "Killed"
**Solution:** Your computer doesn't have enough RAM
- Reduce resolution: 384→256
- Reduce steps: 10→5
- Close other programs

### Problem: "CUDA not available"
**This is fine!** That's for GPU. You're using CPU, which is expected.

---

## 🎨 I Want Different Images!

### Same Prompt, Different Images?
Change the **seed** number:
```python
seed = 1235  # Try 1236, 1237, 1238... for variations
```

### Same Seed, Same Prompt = Always the Same Image
This is intentional! It's how you ensure reproducibility. Want something different? Change the seed!

### Try Random Seeds:
```python
import random
seed = random.randint(0, 4294967295)  # Always different
```

---

## 🔬 Advanced: Change AI Models

You can use different AI models. Edit the `model_id` in `cpu_sd.py` (around line 57):

```python
# Current (recommended for CPU):
model_id = "runwayml/stable-diffusion-v1-5"
```

### Top 10 Best Models for CPU:

```python
1. "runwayml/stable-diffusion-v1-5"          # ← RECOMMENDED (best balance)
2. "CompVis/stable-diffusion-v1-4"            # Slightly faster
3. "prompthero/openjourney"                   # Artistic style
4. "Linaqruf/anything-v3.0"                   # Fast, good for anime
5. "DGSpitzer/Cyberpunk-Anime-Diffusion"     # Anime focused
6. "Deltaadams/DreamShaper"                  # Good quality/speed balance
7. "stabilityai/stable-diffusion-2-1-base"   # Higher quality (slower)
8. "emilianJR/chilloutmix_NiPRunwayML"       # Photorealistic
9. "majicMixRealm_betterFidelityFp16"        # Better details
10. "eimiss/EimMix_Final-Model"               # Excellent (very slow on CPU)
```

### Top 10 Best Models for GPU (Much Faster!):

```python
1. "runwayml/stable-diffusion-v1-5"                    # Still good
2. "stabilityai/stable-diffusion-xl-base-1.0"         # 4x better quality
3. "stabilityai/stable-diffusion-3-medium-diffusers"  # Latest (best)
4. "Lykon/dreamshaper-8"                              # Excellent photorealism
5. "civitai/Chilloutmix_NiPRunwayML"                  # Photorealistic
6. "OFA-Sys/model-card"                               # Multimodal (advanced)
7. "stablediffusionapi/sdxl-lightning"                # Super fast on GPU
8. "stabilityai/sdxl-turbo"                           # Real-time generation
9. "alsomitra/protovision-xl-anime-engine"            # Anime (amazing)
10. "dreamlike-art/dreamlike-photoreal-2.0"           # Photo quality
```

### How to Change Models:

1. Open `cpu_sd.py` in a text editor
2. Find line 57: `model_id = "runwayml/stable-diffusion-v1-5"`
3. Replace with any model above, e.g.: `model_id = "prompthero/openjourney"`
4. Save the file
5. Run: `python cpu_sd.py`
6. First run with new model will download it (~4GB again)

**💡 Tip:** Different models work best with different prompts. Experiment to find your favorite!

### Find More Models:
- **Hugging Face Hub:** [https://huggingface.co/models?pipeline_tag=text-to-image](https://huggingface.co/models?pipeline_tag=text-to-image)
- **Civitai:** [https://civitai.com](https://civitai.com) - Community models, sorted by quality/ratings
- **Model Comparison:** [https://stable-diffusion-art.com/models/](https://stable-diffusion-art.com/models/)

