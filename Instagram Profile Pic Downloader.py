import instaloader

ig = instaloader.Instaloader()
username = input("Enter username :\n")

ig.download_profile(username, profile_pic_only=True)
