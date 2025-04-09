import sqlite3

def get_unique_participants_count(cursor):
    cursor.execute("SELECT COUNT(DISTINCT userEmail) FROM User")
    return cursor.fetchone()[0]

def increment_image_point(cursor, image_id):
    cursor.execute("UPDATE Images SET points = points + 1 WHERE image_id = ?", (image_id,))

def get_image_percentage(cursor, image_id, total_participants):
    cursor.execute("SELECT points FROM Images WHERE image_id = ?", (image_id,))
    points = cursor.fetchone()[0]
    return (points / total_participants) * 100

def main():
    conn = sqlite3.connect('imageDB.db')
    cursor = conn.cursor()

    total_participants = get_unique_participants_count(cursor)
    print(f"Total unique participants: {total_participants}")

    image_id = 1  # Example image ID
    increment_image_point(cursor, image_id)
    conn.commit()

    percentage = get_image_percentage(cursor, image_id, total_participants)
    print(f"Image {image_id} chosen percentage: {percentage:.2f}%")

    conn.close()

if __name__ == "__main__":
    main()