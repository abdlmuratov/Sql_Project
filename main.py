from database import SessionLocal, engine, Base
from models import Author, Category, Post, Tag

Base.metadata.create_all(bind=engine)

db = SessionLocal()

try:
    new_author = Author(full_name="Vali Aliev", email="aliev@google.com")
    db.add(new_author)
    db.commit()
    db.refresh(new_author)

    tech_cat = Category(name="Texnologiya")
    python_tag = Tag(name="Python")
    sql_tag = Tag(name="SQL")
    
    db.add_all([tech_cat, python_tag, sql_tag])
    db.commit()

    new_post = Post(
        title="SQLAlchemy haqida",
        content="ORM modellari bilan ishlash juda qiziq.",
        author_id=new_author.id,
        category_id=tech_cat.id
    )
    new_post.tags.append(python_tag)
    new_post.tags.append(sql_tag)
    
    db.add(new_post)
    db.commit()


except Exception as e:
    print(f"Error: {e}")
    db.rollback()
finally:
    db.close()