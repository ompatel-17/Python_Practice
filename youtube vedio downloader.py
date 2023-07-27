from pytube import YouTube

link = "https://www.youtube.com/watch?v=8S1Kt7AjtHY"
yt_1 = YouTube(link)

print(yt_1.title)
print(yt_1.thumbnail_url)

# videos = yt_1.streams.all()
# vid = list(enumerate(videos))

# for i in vid:
#     print(i)
# print()

# strm = int(input("Enter: "))

# videos[strm].download()
# print("Doenload Complete.....")