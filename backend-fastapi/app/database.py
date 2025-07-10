from sqlmodel import SQLModel, create_engine, Session

sqlite_file_name = "jobquest.db"
engine = create_engine(f"sqlite:///{sqlite_file_name}", echo=False)


def init_db() -> None:
    SQLModel.metadata.create_all(engine)
    

def get_session() -> Session:
    with Session(engine) as session:
        yield session
