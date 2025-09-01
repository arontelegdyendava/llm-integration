# Book summaries dictionary (add more as needed)
book_summaries_dict = {
    "The Hobbit": (
        "Bilbo Baggins, a comfortable and unadventurous hobbit, is taken by surprise when he is invited on a mission to recover the dwarves' treasure guarded by the dragon Smaug. "
        "On the journey, he discovers courage and inner resources he didn't know he had. The story is full of fantastic creatures, unexpected friendships, and tense moments."
    ),
    "1984": (
        "George Orwell's novel describes a dystopian society under total state control. People are constantly watched by 'Big Brother,' and free thought is considered a crime. "
        "Winston Smith, the main character, tries to resist this oppressive regime. It is a story about freedom, truth, and ideological manipulation."
    ),
    "To Kill a Mockingbird": (
        "A story set in the racially charged American South, focusing on themes of justice, empathy, and moral growth. Scout Finch and her brother Jem learn about prejudice and compassion as their father, Atticus, defends a black man wrongly accused of a crime."
    ),
    "Brave New World": (
        "In a futuristic society driven by technology and pleasure, individuality is suppressed for the sake of stability. Bernard Marx and Lenina Crowne begin to question the cost of conformity and the loss of personal freedom."
    ),
    "Harry Potter and the Sorcerer's Stone": (
        "Harry discovers he is a wizard and attends Hogwarts, where he makes friends, faces magical challenges, and uncovers the truth about his parents. Themes include friendship, bravery, and the battle between good and evil."
    ),
    "The Catcher in the Rye": (
        "Holden Caulfield, a disenchanted teenager, wanders New York City searching for meaning and authenticity. The novel explores alienation, innocence, and the struggle to find one's place in the world."
    ),
    "The Great Gatsby": (
        "Set in the Roaring Twenties, Jay Gatsby pursues wealth and love in a world of glamour and illusion. The story examines themes of ambition, love, and the American Dream."
    ),
    "Moby-Dick": (
        "Captain Ahab obsessively hunts the white whale, Moby-Dick, risking his crew and sanity. The novel explores obsession, revenge, and humanity's relationship with nature."
    ),
    "War and Peace": (
        "A sweeping epic of Russian society during the Napoleonic Wars, focusing on the lives of Pierre, Natasha, and Andrei. Themes include war, peace, love, and personal transformation."
    ),
    "The Lord of the Rings: The Fellowship of the Ring": (
        "Frodo Baggins embarks on a quest to destroy a powerful ring that threatens Middle-earth. The journey is filled with danger, friendship, and the struggle between good and evil."
    ),
}

def get_summary_by_title(title: str) -> str:
    """Look up the title and return the full summary."""
    summary = book_summaries_dict.get(title)
    if summary:
        return summary
    else:
        return f"Sorry, no summary found for '{title}'."