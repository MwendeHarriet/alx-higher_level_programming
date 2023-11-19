#!/usr/bin/python3
"""This script script that adds the State object “Louisiana” to the
    database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    name = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    host = "localhost"
    port = 3306
    query = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(name, pwd, host, port, db)
    engine = create_engine(query, pool_pre_ping=True)
    session = Session(engine)
    newS = State(name="Louisiana")
    session.add(newS)
    session.commit()
    state = session.query(State) \
        .order_by(State.id).filter(State.name == "Louisiana").first()
    print(state.id)
