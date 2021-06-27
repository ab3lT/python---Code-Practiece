from TerminalBlog.database import Database
from TerminalBlog.menu import Menu


Database.initialize()
menu = Menu()
menu.run_menu()

"""
uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['fullstack']
collection = database['students']

students = [student for student in collection.find({})]

print(students)


blog1 = Blog(author="Daniel Kibret",
             title="The tale of two monuments",
             description="Description of the blog about the tale of the two monuments")

blog1.new_post()
blog1.save_to_mongo()
from_database = Blog.from_mongo(blog1.id)
print(blog1.get_posts())

"""
