from index import RetailPrices,Session

with Session.begin() as db:
    result=db.query(RetailPrices).all()
    for row in result:
        print(row.total_price)