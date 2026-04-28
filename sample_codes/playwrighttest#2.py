# test_screenshots_videos.py - Screenshots, videos, and visual testing

from playwright.sync_api import sync_playwright, expect
from pathlib import Path

def media_capture():
    with sync_playwright() as p:
        # Create context with video recording
        context = p.chromium.launch_persistent_context(
            user_data_dir="./temp_profile",
            headless=False,
            viewport={"width": 1280, "height": 720},
            record_video_dir="videos/",  # Record video
            record_video_size={"width": 1280, "height": 720}
        )
        
        page = context.new_page()
        
        print("\n=== SCREENSHOTS & VIDEOS ===\n")
        
        # ========== SCREENSHOTS ==========
        print("--- SCREENSHOTS ---\n")
        
        page.goto("https://example.com")
        
        # 1. Full page screenshot
        print("1. Full page screenshot:")
        page.screenshot(path="screenshots/full_page.png", full_page=True)
        print("   ✅ Full page screenshot saved")
        
        # 2. Element screenshot
        print("\n2. Element screenshot:")
        heading = page.locator("h1")
        heading.screenshot(path="screenshots/heading.png")
        print("   ✅ Element screenshot saved")
        
        # 3. Screenshot with clip (specific area)
        print("\n3. Screenshot of specific area:")
        page.screenshot(
            path="screenshots/clip.png",
            clip={"x": 50, "y": 50, "width": 200, "height": 100}
        )
        print("   ✅ Clipped screenshot saved")
        
        # 4. Screenshot as bytes (in memory)
        print("\n4. Screenshot as bytes:")
        screenshot_bytes = page.screenshot()
        print(f"   Screenshot size: {len(screenshot_bytes)} bytes")
        
        # 5. Quality settings for JPEG
        print("\n5. JPEG with quality settings:")
        page.screenshot(
            path="screenshots/quality.jpg",
            type="jpeg",
            quality=80  # 0-100
        )
        print("   ✅ JPEG screenshot saved with 80% quality")
        
        # 6. Screenshot without animations
        print("\n6. Disable animations before screenshot:")
        page.add_style_tag(content="* { transition: none !important; animation: none !important; }")
        page.screenshot(path="screenshots/no_animations.png")
        print("   ✅ Screenshot with animations disabled")
        
        # ========== VISUAL COMPARISON ==========
        print("\n--- VISUAL COMPARISON ---\n")
        
        # 7. Visual regression testing
        print("7. Visual regression testing:")
        
        # First run: Create baseline
        if not Path("screenshots/baseline.png").exists():
            page.screenshot(path="screenshots/baseline.png")
            print("   ✅ Baseline screenshot created")
        
        # Then compare
        try:
            expect(page).to_have_screenshot(path="screenshots/baseline.png")
            print("   ✅ Screenshot matches baseline")
        except AssertionError:
            print("   ⚠️ Screenshot differs from baseline")
        
        # ========== ELEMENT STATES ==========
        print("\n--- ELEMENT STATES ---\n")
        
        # 8. Screenshot of element in different states
        print("8. Element state screenshots:")
        
        # Hover state
        hover_element = page.locator("a")
        hover_element.hover()
        hover_element.screenshot(path="screenshots/hover_state.png")
        print("   ✅ Hover state screenshot")
        
        # Focus state
        search_box = page.get_by_role("textbox")
        if search_box.count() > 0:
            search_box.focus()
            search_box.screenshot(path="screenshots/focus_state.png")
            print("   ✅ Focus state screenshot")
        
        # ========== DOM SNAPSHOTS ==========
        print("\n--- DOM SNAPSHOTS ---\n")
        
        # 9. Save HTML content
        print("9. Saving DOM snapshot:")
        html_content = page.content()
        
        with open("screenshots/page_snapshot.html", "w") as f:
            f.write(html_content)
        print("   ✅ HTML snapshot saved")
        
        # ========== VIDEO RECORDING ==========
        print("\n--- VIDEO RECORDING ---\n")
        
        # 10. Stop recording and save video
        print("10. Video recording:")
        
        # Perform some actions to record
        page.goto("https://example.com")
        page.click("a")
        page.go_back()
        
        # Close context to save video
        context.close()
        
        # Find the video file
        video_files = list(Path("videos/").glob("*.webm"))
        if video_files:
            print(f"   ✅ Video saved: {video_files[0]}")
            print(f"   Video size: {video_files[0].stat().st_size} bytes")
        
        # ========== BEST PRACTICES ==========
        print("\n--- BEST PRACTICES ---\n")
        
        print("✅ 1. Use unique names for screenshots (include timestamp)")
        print("✅ 2. Take screenshots on test failures automatically")
        print("✅ 3. Use visual regression tests for critical UI")
        print("✅ 4. Disable animations when taking screenshots")
        print("✅ 5. Store videos for failed tests only (to save space)")
        
        # 11. Screenshot with timestamp
        print("\n11. Timestamped screenshot:")
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Create screenshots directory for test run
        test_run_dir = Path(f"screenshots/run_{timestamp}")
        test_run_dir.mkdir(parents=True, exist_ok=True)
        
        page.screenshot(path=str(test_run_dir / "page.png"))
        print(f"   ✅ Screenshot saved in {test_run_dir}")
        
        # Clean up
        print("\n🧹 Cleaning up...")
        import shutil
        shutil.rmtree("./temp_profile", ignore_errors=True)
        print("   ✅ Cleanup complete")

if __name__ == "__main__":
    media_capture()