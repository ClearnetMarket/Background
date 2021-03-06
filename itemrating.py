from app import db
from sqlalchemy import func

from app.classes.item import Item_MarketItem
from app.classes.userdata import UserData_Feedback

# this script once a day


def marketitemrating():
    """
    Gets all feedbacks
    finds how many
    finds average for an item
    :return:
    """
    item = db.session.query(Item_MarketItem).all()
    for f in item:
        if f:
            # count of how many
            getratings = db.session.query(UserData_Feedback)
            getratings = getratings.filter(UserData_Feedback.type == 1)
            getratings = getratings.filter(UserData_Feedback.item_id == f.id)
            rate = getratings.count()

            # gets average of item score
            getratingsitem = db.session.query(func.avg(UserData_Feedback.itemrating))
            getratingsitem = getratingsitem.filter(UserData_Feedback.item_id == f.id)
            avgrateitem = getratingsitem.all()
            try:
                itemscore = (avgrateitem[0][0])

                if itemscore is None:
                    itemscore = 0
            except:
                itemscore = 0

            # how many
            f.reviewcount = rate
            # avg for item
            f.itemrating = itemscore

            db.session.add(f)

    db.session.commit()


marketitemrating()


