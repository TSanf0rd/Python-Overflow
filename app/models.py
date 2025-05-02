from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, Table
from sqlalchemy.orm import relationship


# Association Tables
dependency_table = Table(
    'dependency',
    Model.metadata,
    Column('lib_id', Integer, ForeignKey('library.id'), primary_key=True),
    Column('depend_id', Integer, ForeignKey('library.id'), primary_key=True)
)

lib_tag_table = Table(
    'lib_tag',
    Model.metadata,
    Column('lib_id', Integer, ForeignKey('library.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tag.id'), primary_key=True)
)

supported_versions_table = Table(
    'supported_versions',
    Model.metadata,
    Column('sup_vers_id', Integer, primary_key=True),
    Column('version_id', Integer, ForeignKey('version.id'), primary_key=True)
)

# Main Models
class Library(Model):
    id = Column(Integer, primary_key=True)
    category = Column(String(50))
    name = Column(String(50), nullable=False)
    lib_description = Column(Text, nullable=False)
    author = Column(String(50), nullable=False)
    doc_url = Column(String(100))

    functions = relationship("Function", back_populates="library")
    types = relationship("Type", back_populates="library")
    modules = relationship("Module", back_populates="library")
    versions = relationship("Version", back_populates="library")
    dependencies = relationship("Library",
                                secondary=dependency_table,
                                primaryjoin=id==dependency_table.c.lib_id,
                                secondaryjoin=id==dependency_table.c.depend_id,
                                backref="dependents")
    tags = relationship("Tag", secondary=lib_tag_table, back_populates="libraries")

    def __repr__(self):
        return self.name

class Function(Model):
    func_name = Column(String(50), primary_key=True)
    source_code = Column(Text)
    func_description = Column(Text, nullable=False)
    lib_id = Column(Integer, ForeignKey('library.id'), nullable=False)

    library = relationship("Library", back_populates="functions")

class Type(Model):
    type_name = Column(Integer, primary_key=True)
    type_code = Column(Text)
    type_description = Column(Text, nullable=False)
    lib_id = Column(Integer, ForeignKey('library.id'), nullable=False)

    library = relationship("Library", back_populates="types")

class Module(Model):
    mod_id = Column(Integer, primary_key=True)
    mod_name = Column(String(50), nullable=False)
    mod_code = Column(Text)
    mod_description = Column(Text, nullable=False)
    lib_id = Column(Integer, ForeignKey('library.id'), nullable=False)

    library = relationship("Library", back_populates="modules")

class Version(Model):
    id = Column(Integer, primary_key=True)
    release_date = Column(Date, nullable=False)
    change_log = Column(Text, nullable=False)
    lib_id = Column(Integer, ForeignKey('library.id'), nullable=False)

    library = relationship("Library", back_populates="versions")
    contributors = relationship("Contributor", back_populates="version")

class Contributor(Model):
    con_id = Column(Integer, primary_key=True)
    ver_id = Column(Integer, ForeignKey('version.id'), primary_key=True)
    con = Column(String(50), nullable=False)

    version = relationship("Version", back_populates="contributors")

class Tag(Model):
    id = Column(Integer, primary_key=True)
    tag_name = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)

    libraries = relationship("Library", secondary=lib_tag_table, back_populates="tags")

print("✅ Library is:", Library)
