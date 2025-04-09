import sqlite3


class EditDatabase:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    #update images
    def update_image(self, image_id, new_path=None, new_height=None, new_width=None):
        # Build the UPDATE statement dynamically based on provided values
        update_fields = []
        update_values = []

        if new_path is not None:
            update_fields.append("image_path = ?")
            update_values.append(new_path)
        if new_height is not None:
            update_fields.append("height = ?")
            update_values.append(new_height)
        if new_width is not None:
            update_fields.append("width = ?")
            update_values.append(new_width)

        if update_fields:
            update_statement = f"UPDATE Images SET {', '.join(update_fields)} WHERE image_id = ?"
            update_values.append(image_id)  # Add image_id to the values
            self.cursor.execute(update_statement, update_values)
            self.conn.commit()
    
    #update user
    def update_user(self, userEmail, new_age=None, new_gender=None, new_visualArtsCourse=None):
        update_fields = []
        update_values = []

        if new_age is not None:
            update_fields.append("userAge = ?")
            update_values.append(new_age)
        if new_gender is not None:
            update_fields.append("userGender = ?")
            update_values.append(new_gender)
        if new_visualArtsCourse is not None:
            update_fields.append("visualArtsCourse = ?")
            update_values.append(new_visualArtsCourse)

        if update_fields:
            update_statement = f"UPDATE User SET {', '.join(update_fields)} WHERE userEmail = ?"
            update_values.append(userEmail)
            self.cursor.execute(update_statement, update_values)
            self.conn.commit()

    #update questions
    def update_question(self, qid, new_text=None, new_image_id=None):
        update_fields = []
        update_values = []

        if new_text is not None:
            update_fields.append("question_text = ?")
            update_values.append(new_text)
        if new_image_id is not None:
            update_fields.append("image_id = ?")
            update_values.append(new_image_id)

        if update_fields:
            update_statement = f"UPDATE Question SET {', '.join(update_fields)} WHERE qid = ?"
            update_values.append(qid)
            self.cursor.execute(update_statement, update_values)
            self.conn.commit()

    #update ratings
    def update_rating(self, rating_id, new_userEmail=None, new_image_id=None, new_rating=None):
        update_fields = []
        update_values = []

        if new_userEmail is not None:
            update_fields.append("userEmail = ?")
            update_values.append(new_userEmail)
        if new_image_id is not None:
            update_fields.append("image_id = ?")
            update_values.append(new_image_id)
        if new_rating is not None:
            update_fields.append("rating = ?")
            update_values.append(new_rating)

        if update_fields:
            update_statement = f"UPDATE Rating SET {', '.join(update_fields)} WHERE rating_id = ?"
            update_values.append(rating_id)
            self.cursor.execute(update_statement, update_values)
            self.conn.commit()

    #update admin info
    def update_admin(self, adminEmail, new_username=None, new_password=None):
        update_fields = []
        update_values = []

        if new_username is not None:
            update_fields.append("adminUsername = ?")
            update_values.append(new_username)
        if new_password is not None:
            update_fields.append("adminPassword = ?")
            update_values.append(new_password)

        if update_fields:
            update_statement = f"UPDATE Admin SET {', '.join(update_fields)} WHERE adminEmail = ?"
            update_values.append(adminEmail)
            self.cursor.execute(update_statement, update_values)
            self.conn.commit()

    def close(self):
        self.conn.close()