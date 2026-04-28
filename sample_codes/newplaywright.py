# test_files.py - Handling file uploads and downloads

from playwright.sync_api import sync_playwright, expect
from pathlib import Path

def file_handling():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        print("\n=== FILE UPLOADS & DOWNLOADS ===\n")
        
        
        print("--- FILE UPLOADS ---\n")
        
        page.goto("https://the-internet.herokuapp.com/upload")
        
        
        # Create a test file first
        test_file = Path("test_upload.txt")
        test_file.write_text("This is a test file for upload")
        
        # Upload the file
        file_input = page.locator("#file-upload")
        file_input.set_input_files(str(test_file))
        print(f"   Uploaded: {test_file}")
        
        # Submit the upload
        page.click("#file-submit")
        
        # Verify upload success
        success_message = page.locator("#uploaded-files")
        expect(success_message).to_contain_text("test_upload.txt")
        print("   ✅ File uploaded successfully")
        
        # 2. Upload multiple files
        print("\n2. Uploading multiple files:")
        
        # Create multiple test files
        files_to_upload = []
        for i in range(3):
            test_file = Path(f"test_file_{i}.txt")
            test_file.write_text(f"This is test file {i}")
            files_to_upload.append(str(test_file))
        
        # Upload all files
        page.goto("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_input_multiple")
        page.frame_locator("iframe[name='iframeResult']").locator("input[type='file']").set_input_files(files_to_upload)
        print(f"   Uploaded {len(files_to_upload)} files")
        
        # 3. Upload from memory (without saving to disk)
        print("\n3. Uploading from memory:")
        
        file_content = b"File content from memory"
        file_input.set_input_files(
            files=[
                {"name": "memory_file.txt", "mimeType": "text/plain", "buffer": file_content}
            ]
        )
        print("   ✅ Uploaded file from memory")
        
        # 4. Clear file selection
        print("\n4. Clearing file selection:")
        file_input.set_input_files([])
        print("   ✅ File selection cleared")
        
        # ========== FILE DOWNLOADS ==========
        print("\n--- FILE DOWNLOADS ---\n")
        
        page.goto("https://the-internet.herokuapp.com/download")
        
        # 5. Download single file
        print("5. Downloading file:")
        
        # Start listening for download
        with page.expect_download() as download_info:
            page.click(".example a")  # Click download link
        
        download = download_info.value
        
        # Get download information
        print(f"   File name: {download.suggested_filename}")
        print(f"   Page URL: {download.page.url}")
        
        # Save to specific location
        download.save_as(f"downloaded_{download.suggested_filename}")
        print("   ✅ File downloaded and saved")
        
        # 6. Download and read in memory
        print("\n6. Downloading and reading in memory:")
        
        with page.expect_download() as dl_info:
            page.click(".example a")
        
        download_obj = dl_info.value
        
        # Read content without saving
        content = download_obj.read()
        print(f"   Downloaded {len(content)} bytes")
        
        # 7. Cancel download
        print("\n7. Canceling download:")
        
        # Create a download listener that cancels
        def cancel_download(download):
            print(f"   Cancelling: {download.suggested_filename}")
            download.cancel()
        
        page.on("download", cancel_download)
        
        page.click(".example a")
        page.wait_for_timeout(1000)
        print("   ✅ Download cancelled")
        
        # 8. Wait for download to complete
        print("\n8. Waiting for download completion:")
        
        with page.expect_download() as download_info:
            page.click(".example a")
        
        download_complete = download_info.value
        path = download_complete.save_as("complete_download.pdf")
        
        # Check file exists
        if Path(path).exists():
            print(f"   ✅ Download complete: {path}")
        
        # ========== BEST PRACTICES ==========
        print("\n--- BEST PRACTICES ---\n")
        
        print("✅ 1. Use set_input_files() for file uploads")
        print("✅ 2. Always use expect_download() for downloads")
        print("✅ 3. Clean up test files after tests")
        print("✅ 4. Test file size limits and formats")
        print("✅ 5. Handle download dialogs with page.on('download')")
        
        # Clean up test files
        print("\n🧹 Cleaning up test files...")
        for file in Path(".").glob("test_file_*.txt"):
            file.unlink()
        for file in Path(".").glob("downloaded_*"):
            file.unlink()
        print("   ✅ Cleanup complete")
        
        browser.close()

if __name__ == "__main__":
    file_handling()