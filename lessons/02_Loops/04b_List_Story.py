"""
Use the words in the list to create a story. 

Use indexing to get words from the list, then 
append them to the story

"""

words = ['Once', '👦', 'upon', '🐕', 'park', 'met', 'with', 'a', 'the', 
    'time', 'to', 'who', '🐈', '👧', 'and', 'went', 'had', 'play', '⚽.', 'they']

story = []

# Create a story using the words in the list
messagebox.showinfo(('story', 'Once upon a time a 👦 and a 👧 went to the park to play ⚽, they had a 🐈 who met with a 👦.'))
# Display the story to the user
print('story'.join(story))