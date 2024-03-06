from lib.space import Space

class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection 

    def all(self):
        rows = self._connection.execute("SELECT * FROM spaces")
        spaces = []
        for row in rows:
            space = Space(
                row["id"], 
                row["name"],
                row["description"],
                row["price"],
                row["date_from"],
                row["date_to"],
                row["user_id"]
                )
            spaces.append(space)
        return spaces
    
    def find(self, id):
        rows = self._connection.execute("SELECT * FROM spaces WHERE id =%s", [id])
        row = rows[0]
        return Space(row["id"], row["name"], row["description"], row["price"], row["date_from"], row["date_to"], row["user_id"])
    
    def create(self, space):
        rows = self._connection.execute(
            'INSERT INTO spaces (name, description, price, date_from, date_to, user_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id',
            [space.name, space.description, round(float(space.price), 2), space.date_from, space.date_to, space.user_id]
            )
        row = rows[0]
        space.id = row["id"]
        return None


