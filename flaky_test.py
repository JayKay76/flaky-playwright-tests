import random
import time
import json
from playwright.sync_api import sync_playwright

def run_test() -> dict:
    """Runs a Playwright test that randomly fails to simulate flaky behavior."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            page.goto("https://www.elverys.ie/")  # Replace with your URL
            time.sleep(random.uniform(0.5, 10))  # Simulate variable network latency
            
            # Simulating a flaky test condition (10% chance of failure)
            if random.random() < 0.10:
                raise Exception("Simulated Flaky Test Failure")

            result = {"success": True, "timestamp": time.time()}
        except Exception as e:
            result = {"success": False, "error": str(e), "timestamp": time.time()}
        finally:
            browser.close()

        return result

if __name__ == "__main__":
    results = []
    for i in range(100):  # Run test 100 times
        print(f"Running test iteration {i + 1}/100...")
        results.append(run_test())

    # Save results to JSON file
    with open("test_results.json", "w") as f:
        json.dump(results, f, indent=4)

    print("Test execution completed. Results saved to test_results.json.")
