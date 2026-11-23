---
name: perchance-image-gen
description: >-
  Generate AI images using the reverse-engineered Perchance b7kc35yv7u backend API.
  Use when the user requests to generate, create, or render images, character portraits,
  anime art, realistic humans, or fantasy concepts using Perchance's free backend without
  API keys or sign-in. Supports 28 art styles, adult/NSFW presets, resolution control
  (512x512, 512x768, 768x512, 768x768), CFG guidance scale, and deterministic seed reproduction.
---

# Perchance Image Generation Skill (b7kc35yv7u)

This skill allows agents to programmatically generate and save AI images using the reverse-engineered Perchance backend API and style templates from `perchance.org/b7kc35yv7u`.

---

<!-- MUSE-ADAPT -->

## Muse adaptation — read first

This skill runs inside Muse's own environment, for Nasser. Where the original instructions below conflict with these points, these points win.

- Host: Linux VM (4 CPU, ~7 GB RAM, x86_64), no GPU. Toolchains live under the home directory only; never rely on system installs. Python deps: `pip install --user` (httpx is the only hard requirement for the CLI path).
- PROXY QUIRK (verified 2026-11-17): this VM's env has bracketed-IPv6 entries in NO_PROXY/no_proxy (`[::1]`, `[fd8b:...]`). httpx crashes parsing them (`InvalidURL: Invalid port: ':1]'`) at Client init. Always run the client with `NO_PROXY=localhost,127.0.0.1 no_proxy=localhost,127.0.0.1` (BOTH cases) prefixed.
- BLOCKED FROM THIS VM (verified 2026-11-17): Perchance/Cloudflare returns HTTP 403 for this VM's egress IP (curl to perchance.org and to image-generation.perchance.org/api/verifyUser both 403; google.com 200). Direct API path fails at user verification (403) and the Playwright browser fallback cannot pass it either from this IP. Cloud-browser test also FAILED the same day (page loads, but Turnstile anti-bot verification fails on both network routes: 'Anti-bot verification failed. VPNs may cause this.'). The skill + client + httpx + playwright + chromium are all installed and the CLI runs, but generation does not work from any of Muse's networks. It should work from a residential IP (e.g. the user's phone via Termux, or the user taking over the live browser from his own connection) - test before promising a generation.
- The user (Nasser) is Persian-speaking and phone-only; he has no computer. Deliverables reach him as files in this chat. Explain everything in simple Persian and translate every English label - his English is effectively zero.
- Register: two-way, comfortable, street-style, blunt and honest. No formalities.
- Never ask design-detail questions. Decide, build, then report shortly.
- The client script lives at `scripts/perchance_client.py` inside this skill folder (with `extracted_styles.json` next to it). The original `C:\ANTI\webgenimg` Windows paths do not exist here; use the skill-local paths. The web app and MCP server from the source repo are NOT installed here - only the CLI client.
- This calls Perchance's free image-generation backend (reverse-engineered, unofficial, no API key). Prompts and generated images go to Perchance's servers. It can break without notice if Perchance changes its backend.
- Adult (+18) styles are for adults only, fictional adults only, no real people, no minors - same rules as the skill's own content rules. Generated images are delivered to Nasser in this chat.
- Apply quality gates silently. Never paste internal gate or lint reports to the user; report outcomes in a few lines.
- Secrets never go into files, memory or chat output. Publishing anything publicly needs his explicit approval first.
- The original skill may name Claude Code tools (Read, Write, Edit, Glob, Grep, Bash) or other agents' commands. Use Muse's own tools instead (file read/write/edit, shell, browser).
## When to Use This Skill

Activate this skill when:
1. The user asks to generate images using Perchance or the `b7kc35yv7u` generator.
2. The user requests text-to-image generation without requiring external paid API keys (OpenAI, Midjourney, Stability AI).
3. The user wants to generate character portraits, artistic illustrations, anime figures, or realistic humans using specific art styles.

---

## Available Execution Methods

Agents can generate images using either the CLI wrapper or by directly executing a Python snippet.

### Method 1: CLI Execution via `run_command` (Recommended)

Run `perchance_client.py` located in `scripts/perchance_client.py`:

```powershell
python scripts/perchance_client.py --prompt "<PROMPT>" --style "<STYLE>" --shape "<RESOLUTION>" --out "<OUTPUT_PATH>"
```

#### Common Examples:

- **Realistic Portrait (512x768)**:
  ```powershell
  python scripts/perchance_client.py --prompt "portrait of a cyberpunk detective standing in neon rain" --style "Realistic humans" --shape "512x768" --out "detective.jpeg"
  ```

- **Fantasy / Cinematic Landscape (768x512)**:
  ```powershell
  python scripts/perchance_client.py --prompt "ancient elven city carved into waterfalls at sunset, volumetric god rays" --style "Realistic images" --shape "768x512" --out "elven_city.jpeg"
  ```

- **Adult / NSFW Style Preset**:
  ```powershell
  python scripts/perchance_client.py --prompt "portrait of a noble sorceress in arcane sanctum" --style "NSFW - Realistic" --adult --shape "512x768" --out "sorceress.jpeg"
  ```

- **Reproduce Exact Seed**:
  ```powershell
  python scripts/perchance_client.py --prompt "majestic phoenix rising from flames" --seed 1068771166 --out "phoenix.jpeg"
  ```

---

### Method 2: Python Script Import

```python
import sys
sys.path.append(r"this skill folder")
from perchance_client import PerchanceClient

client = PerchanceClient()

# Generate image
result = client.generate(
    prompt="portrait of a medieval knight in gothic armor",
    negative_prompt="blurry, distorted, low quality",
    art_style="Realistic images",
    shape="512x768",      # '512x512', '512x768', '768x512', or '768x768'
    guidance_scale=7.0,   # Range: 1.0 to 30.0 (default 7.0)
    seed=-1,              # -1 for random, or specific integer
    adult_mode=False
)

# Download and save
client.download_image(result, "knight.jpeg")
print(f"Image saved. Seed: {result.seed}, ImageID: {result.image_id}")
```

---

## Parameter Specifications

| Parameter | Options / Type | Description |
| :--- | :--- | :--- |
| `prompt` | string (required) | Core text description. Use parentheses `(text)` to add 1.1x weight, `((text))` for 1.2x. |
| `negative_prompt` | string (optional) | Artifacts to suppress (e.g. `bad anatomy, blurry, extra limbs, low quality`). |
| `art_style` | string | One of the 28 pre-built styles (see list below). Default: `"Realistic images"`. |
| `art_style_mix`| string | Secondary style mix. Use `"Not Mix"` or `"NSFW"` to append `, nsfw`. |
| `adult_mode` | boolean | If `true`, injects mature tags and strips anti-NSFW negatives. |
| `shape` | string | `"512x512"` (Square), `"512x768"` (Portrait), `"768x512"` (Landscape), `"768x768"` (Large Square). |
| `guidance_scale` | float | CFG Scale (`1.0` - `30.0`). Default is `7.0`. |
| `seed` | integer | Random seed (`-1` = randomized). Specific number replicates identical image. |

---

## Complete List of 28 Art Styles

### Standard Styles:
- `Realistic images` (High-definition, 4K/8K, sharp focus)
- `Realistic humans` (Detailed human features, skin textures, anatomically accurate)
- `Realistic Human Generator` (Natural raw portrait, film grain, candid)
- `No style` (Raw prompt passed directly to model)
- `Anti-NSFW` (Forces SFW filtering)
- `League of Legends` (Digital concept art, WLOP inspired)
- `MTG Card` (Fantasy trading card illustration)
- `Final Fantasy` (CGI video game 3D style)
- `Dragonball` (Anime style)
- `Star Wars Character` / `Star Wars Battle` (Cinematic space aesthetic)
- `Lego`, `Terraria`, `Webcore`, `Skittles`, `ENA`, `Undertale?`
- `Jester`, `Ninja`, `Neko (Catgirl)`, `American Girl`, `Random Girl 1`, `Random Girl 2`

### Adult (+18) Styles:
- `NSFW - Realistic` (Photorealistic adult aesthetic, volumetric rim lighting)
- `NSFW - Anime` (High-detail anime aesthetic with fluid motion)
- `NSFW - Realistic (Stronger)` (Weighted `(((nsfw)))`)
- `NSFW - Anime (Stronger)` (Weighted `(((nsfw)))`)
- `NSFW Painted Anime` (Painterly anime aesthetic, Pixiv/WLOP inspired)

---

## Web App and MCP Integration

- **Web Application**: Launch `python web_app.py (not installed here)` to start the interactive browser interface on `http://127.0.0.1:8000`.
- **MCP Server**: Launch `python perchance_mcp.py (not installed here)` to expose `generate_perchance_image` tool directly to MCP clients.
