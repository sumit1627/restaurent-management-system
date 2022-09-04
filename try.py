from app import db
from app import Resto

r = Resto(title="abedherug", price = "58")
db.session.add(r)
db.session.commit()
query = Resto.query.all()
print(query)