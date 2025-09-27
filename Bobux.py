import webbrowser
print("Choose option 1 or 2")
print("\n 1) Redirect to free robux site")
print("\n 2) Exit")
option=int(input())
if option==1:
    url = "https://docs.google.com/forms/d/e/1FAIpQLSdLLYPpbN5DDXy4icn1UrT2MnDeWbAtIplE9hAzFDDpRv6cFQ/viewform?usp=dialog"
    webbrowser.open(url)
else:
    exit()

