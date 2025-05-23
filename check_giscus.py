import asyncio
from playwright.async_api import async_playwright, ConsoleMessage, Request

async def handle_console_message(msg: ConsoleMessage):
    try:
        print(f"CONSOLE ({msg.type()}): {msg.text()}")
    except Exception as e:
        print(f"Error in handle_console_message: {e}")
        # Fallback to inspect the object if methods fail
        print(f"ConsoleMessage object: type={type(msg)}, dir={dir(msg)}")
        if hasattr(msg, '_initializer'):
             print(f"ConsoleMessage initializer: {msg._initializer}")


async def handle_request_failed(request: Request):
    try:
        failure = request.failure()
        error_text = failure.error_text if failure else "N/A"
        print(f"REQUEST_FAILED: {request.url()} - {error_text}")
    except Exception as e:
        print(f"Error in handle_request_failed: {e}")
        # Fallback to inspect the object
        print(f"Request object: type={type(request)}, dir={dir(request)}")
        if hasattr(request, '_initializer'):
            print(f"Request initializer: {request._initializer}")


async def main():
    print("Starting Playwright script...")
    async with async_playwright() as p:
        browser = None 
        try:
            print("Launching browser...")
            browser = await p.chromium.launch()
            print("Browser launched.")
            page = await browser.new_page()
            print("New page created.")

            # Updated event handling
            page.on("console", lambda msg: asyncio.create_task(handle_console_message(msg)))
            page.on("requestfailed", lambda req: asyncio.create_task(handle_request_failed(req)))

            file_path = "file:///app/site/blog/2024/09/25/i-passed-the-cissp-exam/index.html"
            print(f"Navigating to {file_path}...")

            await page.goto(file_path, wait_until="networkidle", timeout=20000)
            print("Page navigation complete (networkidle).")
            
            print("Waiting for additional 10 seconds for async operations (giscus)...")
            await page.wait_for_timeout(10000) 
            print("Finished waiting.")

        except Exception as e:
            print(f"An error occurred in main: {e}")
        finally:
            if browser:
                print("Closing browser...")
                await browser.close()
                print("Browser closed.")
            else:
                print("Browser was not launched, no need to close.")

if __name__ == "__main__":
    asyncio.run(main())
