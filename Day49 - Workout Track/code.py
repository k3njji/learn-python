from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_PASSWORD = os.getenv("ACCOUNT_PASSWORD")
EMAIL_ACCOUNT = os.getenv("ACCOUNT_EMAIL")

URL = 'https://appbrewery.github.io/gym/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = "C:\\selenium_profiles\\gym_profile"
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)


def login():
    login_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
    )
    login_link.click()

    email_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "email-input"))
    )

    password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "password-input"))
    )

    email_input.send_keys(EMAIL_ACCOUNT)
    password_input.send_keys(EMAIL_PASSWORD)

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit-button"))
    )
    submit_button.click()

def chech_booked():
    booked_classes = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "Schedule_dayGroup__y79__"))
    )

    bookings = []

    for booked in booked_classes:
        # ✓ Already on waitlist: HIIT Class on Tue, Aug 12
        class_name = booked.find_elements(By.CLASS_NAME, "ClassCard_className__q0kVz")
        class_date = booked.find_element(By.CLASS_NAME, "Schedule_dayTitle__YBybs").text

        status = booked.find_elements(By.CLASS_NAME, "ClassCard_bookButton__DMM1I")

        for i in range(len(status)):
            if(status[i].text == "Booked" or status[i].text == "Waitlisted"):
                print(f"Already {status[i].text}: {class_name[i].text} on {class_date}")
                bookings.append([status[i].text, class_name[i].text, class_date])
            elif status[i].text == "Join Waitlist":
                status[i].click()
                print(f"Joined waitlist for: {class_name[i].text} on {class_date}")
                bookings.append([status[i].text, class_name[i].text, class_date])

        return bookings

            # print(f"{status[i].text} {class_name[i].text} on {class_date}")

        # print(type(status))
        # print(len(class_name))
        # print(len(class_date), " 2")

        # print(len(status))

        # print(class_date[:].text)

        # for class_status in status:
        #     print(class_status.text)

        # for i in range(len(class_name)):
            # print(i)
            # print(f"{status[i].text} {class_name[i].text} on {class_date[i].text}")

        
        
    # booked = []


    # for booked in booked_classes:

def book_class():
    booked_classes = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "Schedule_dayGroup__y79__"))
    )

    bookings = []

    for booked in booked_classes:
        class_name = booked.find_elements(By.CLASS_NAME, "ClassCard_className__q0kVz")
        class_date = booked.find_element(By.CLASS_NAME, "Schedule_dayTitle__YBybs").text
        # class_time = booked.find_elements(By.CLASS_NAME, "ClassCard_classDetail__Z8Z8f")

        status = booked.find_elements(By.CLASS_NAME, "ClassCard_bookButton__DMM1I")

        if(('Thu' in class_date) or ('Tue' in class_date)):
            class_time = booked.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
            for i in range(len(status)):
                # if(class_date):
                print(class_time[i])
                    # if(class_time[i].text.replace("Time:", "").strip() == "6:00 PM"):
                    #     print("enter")
                    #     status[i].click()
                    #     bookings.append([status[i].text, class_name[i].text, class_date])
            # if(status[i].text == "Booked" or status[i].text == "Waitlisted"):
            #     print(f"Already {status[i].text}: {class_name[i].text} on {class_date}")
            #     bookings.append([status[i].text, class_name[i].text, class_date])
            # elif status[i].text == "Join Waitlist":
            #     status[i].click()
            #     print(f"Joined waitlist for: {class_name[i].text} on {class_date}")
            #     bookings.append([status[i].text, class_name[i].text, class_date])

        # return bookings



def statistics(bookings):
    booked_count = 0
    waitlisted_count = 0
    joined_waitlist_count = 0

    for booking in bookings:
        if booking[0] == "Booked":
            booked_count += 1
        elif booking[0] == "Waitlisted":
            waitlisted_count += 1
        elif booking[0] == "Join Waitlist":
            joined_waitlist_count += 1

    print("\nStatistics:")
    print(f"Total Booked: {booked_count}")
    print(f"Total Waitlisted: {waitlisted_count}")
    print(f"Total Joined Waitlist: {joined_waitlist_count}")


login()
book = chech_booked()
statistics(book)
book2 = book_class()
# updates(book2)
input("Press Enter to exit...")