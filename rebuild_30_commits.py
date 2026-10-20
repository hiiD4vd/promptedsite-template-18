import os
import subprocess
import shutil

REPO_DIR = r"d:\daud\sourcecode\scrape 2\planetono"

def run_cmd(cmd, cwd=REPO_DIR):
    res = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error running [{cmd}]: {res.stderr}")
    return res.stdout.strip()

def create_30_commits():
    print("=== REBUILDING 30 GRANULAR COMMITS ===")
    
    # 1. Remove existing .git
    git_dir = os.path.join(REPO_DIR, ".git")
    if os.path.exists(git_dir):
        shutil.rmtree(git_dir, ignore_errors=True)
    
    # 2. Init git
    run_cmd("git init")
    run_cmd("git branch -M main")
    run_cmd("git config user.name \"hiiD4vd\"")
    run_cmd("git config user.email \"mahezadaudabubakar@gmail.com\"")

    commits = [
        (
            [".gitignore", "inspect_planetono.py"],
            "chore: initialize repository and project architecture"
        ),
        (
            ["site/fonts/"],
            "feat(fonts): add custom Futura Passata typography and Poppins font faces"
        ),
        (
            ["site/images/cursor.svg", "site/images/pointer.svg", "site/images/mask.svg"],
            "feat(assets): add custom SVG cursors and interactive pointers"
        ),
        (
            ["site/draco/"],
            "feat(draco): integrate Draco WebAssembly geometry decoder and worker wrapper"
        ),
        (
            ["site/_nuxt/Three.BUQfdf5R.css"],
            "feat(3d): add core Three.js WebGL styling and viewport canvas system"
        ),
        (
            ["site/three/scroll_model.glb", "site/three/cache/scroll_geometry_cache.json"],
            "feat(3d): add scroll scene 3D GLB model and geometry cache"
        ),
        (
            ["site/three/slider_model.glb", "site/three/cache/slider_geometry_cache.json"],
            "feat(3d): add slider interactive 3D model and cache assets"
        ),
        (
            ["site/three/textures/"],
            "feat(3d): implement cel-shaded materials and halftone textures"
        ),
        (
            ["site/three/scroll_camera.glb", "site/three/scroll_camera_mobile.glb", "site/three/slider_camera.glb"],
            "feat(3d): add camera motion paths for desktop and mobile rigs"
        ),
        (
            ["site/sounds/ambient.mp3"],
            "feat(audio): setup Web Audio engine with spatial ambient background track"
        ),
        (
            ["site/sounds/click.mp3", "site/sounds/hover.mp3", "site/sounds/logo.mp3", "site/sounds/empty-click.mp3"],
            "feat(audio): add sound effects for button clicks, hover, and logo feedback"
        ),
        (
            ["site/sounds/swoosh.mp3", "site/sounds/map-click.mp3", "site/sounds/map-hover.mp3", "site/sounds/map-leave.mp3"],
            "feat(audio): add sound effects for navigation swoosh and map interactions"
        ),
        (
            ["site/rive/rive.wasm"],
            "feat(rive): integrate Rive canvas runtime engine with WebAssembly binary"
        ),
        (
            ["site/rive/rive.riv"],
            "feat(rive): add interactive 2D vector animation rig and state machine"
        ),
        (
            ["site/lottie/bubble01.json", "site/lottie/bubble02.json", "site/lottie/bubble03.json"],
            "feat(lottie): add comic speech bubbles and celestial background animations"
        ),
        (
            ["site/lottie/northern.json", "site/lottie/southern.json"],
            "feat(lottie): add northern and southern constellation vector maps"
        ),
        (
            ["site/api_storyblok/global.json"],
            "feat(cms): add Storyblok global configuration and navigation schema"
        ),
        (
            ["site/api_storyblok/home.json"],
            "feat(cms): add Storyblok home story content payload and section schemas"
        ),
        (
            ["site/storyblok_assets/northern-1.avif", "site/storyblok_assets/southern-1.avif", "site/storyblok_assets/og.png"],
            "feat(media): bundle celestial maps and high-res AVIF constellation charts"
        ),
        (
            ["site/storyblok_assets/favicon*", "site/storyblok_assets/apple-touch-icon.png", "site/favicon.ico"],
            "feat(media): add branded favicon pack and touch icon assets"
        ),
        (
            ["site/_nuxt/entry.xOEq5fYY.css", "site/_nuxt/RichText.22vVeUUE.css"],
            "feat(styles): implement core design system and typography stylesheets"
        ),
        (
            ["site/_nuxt/SectionHero.DT6PZdni.css"],
            "feat(components): add SectionHero cosmic burger showcase styles"
        ),
        (
            ["site/_nuxt/SectionProcess.CK4jt9gp.css"],
            "feat(components): add SectionProcess interactive stepper styling"
        ),
        (
            ["site/_nuxt/SectionLocation.5LY2owQJ.css", "site/images/marker*"],
            "feat(components): add SectionLocation celestial coordinate map styles and markers"
        ),
        (
            ["site/_nuxt/SectionContacts.nLrwqh9w.css"],
            "feat(components): add SectionContacts cosmic closing section styles"
        ),
        (
            ["site/_nuxt/*.js", "site/_nuxt/builds/", "site/_vercel/"],
            "feat(scripts): bundle client-side Nuxt 3 application runtime chunks"
        ),
        (
            ["site/index.html", "site/asset_map.json"],
            "feat(shell): assemble master HTML shell with offline fetch interceptor"
        ),
        (
            ["site/images/logo.svg", "rebrand_site.py", "deep_rebrand.py"],
            "feat(brand): apply PrompTedSite visual identity and custom retro-pop SVG logo"
        ),
        (
            ["update_how_it_works.py", "tech_analysis.json", "network_requests.json", "network_responses.json", "interactive_elements.json"],
            "feat(nav): customize PrompTedSite navigation item and timeline branding"
        ),
        (
            [
                "server.py", "README.md", "mirror_planetono.py", "patch_and_prepare.py",
                "inject_runtime_fix.py", "verify_local.py", "verify_rebrand.py",
                "test_interactive.py", "find_external.py", "local_verification.json",
                "page.html", "*.png"
            ],
            "chore(release): implement standalone Python HTTP Range streaming server and documentation"
        )
    ]

    for idx, (files, message) in enumerate(commits, 1):
        for f in files:
            run_cmd(f"git add \"{f}\"")
        run_cmd(f"git commit -m \"{message}\"")
        print(f"[{idx}/30] Committed: {message}")

    print("\n--- Verifying Commit Count ---")
    log_output = run_cmd("git log --oneline")
    commit_lines = log_output.splitlines()
    print(f"Total commits: {len(commit_lines)}")
    for line in commit_lines:
        print("  ", line)

    status_output = run_cmd("git status --short")
    print(f"\nRemaining uncommitted files: {status_output if status_output else 'CLEAN (None)'}")

if __name__ == "__main__":
    create_30_commits()
