import os
from datetime import datetime


class Screenshot:

    @staticmethod
    def capture(driver, test_name):

        folder = "screenshots"

        if not os.path.exists(folder):
            os.makedirs(folder)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = os.path.join(
            folder,
            f"{test_name}_{timestamp}.png"
        )

        driver.save_screenshot(filename)

        print(f"Screenshot saved: {filename}")