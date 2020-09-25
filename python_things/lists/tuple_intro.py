"""Introduction to Tuples."""
# t = 'a', 'b', 'c'
#
# print(t)
albums = [
    ('Welcome to my Nightmare', 'Alice Cooper', 1975),
    ('Bad Company', 'Bad Company', 1974),
    ('Nightflight', 'Budgie', 1981),
    ('More Mayhem', 'Emilda May', 2011),
    ('Ride the Lightning', 'Metallica', 1984),
]

for album in albums:
    title, artist, year = album
    print(f"Album: {title}, Artist: {artist}, Year: {year}")
