from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from app import appbuilder
from .models import Library, Function, Type, Module, Version, Contributor, Tag

class LibraryModelView(ModelView):
    datamodel = SQLAInterface(Library)
    list_columns = ['name', 'author', 'category']
    search_columns = ['name', 'author', 'category', 'lib_description']
    base_order = ('name', 'asc')
    label_columns = {'lib_description': 'Description'}

appbuilder.add_view(
    LibraryModelView,
    "Search Libraries",
    icon="fa-book",
    category="Library Management"
)

class FunctionModelView(ModelView):
    datamodel = SQLAInterface(Function)
    list_columns = ['func_name', 'func_description', 'library']
    search_columns = ['func_name', 'func_description']
    base_order = ('func_name', 'asc')

appbuilder.add_view(
    FunctionModelView,
    "Manage Functions",
    icon="fa-code",
    category="Library Management"
)

class TypeModelView(ModelView):
    datamodel = SQLAInterface(Type)
    list_columns = ['type_name', 'type_description', 'library']
    search_columns = ['type_name', 'type_description']
    base_order = ('type_name', 'asc')

appbuilder.add_view(
    TypeModelView,
    "Manage Types",
    icon="fa-cogs",
    category="Library Management"
)

class ModuleModelView(ModelView):
    datamodel = SQLAInterface(Module)
    list_columns = ['mod_name', 'mod_description', 'library']
    search_columns = ['mod_name', 'mod_description']
    base_order = ('mod_name', 'asc')

appbuilder.add_view(
    ModuleModelView,
    "Manage Modules",
    icon="fa-cogs",
    category="Library Management"
)

class VersionModelView(ModelView):
    datamodel = SQLAInterface(Version)
    list_columns = ['release_date', 'change_log', 'library']
    search_columns = ['change_log', 'library']
    base_order = ('release_date', 'desc')

appbuilder.add_view(
    VersionModelView,
    "Manage Versions",
    icon="fa-cogs",
    category="Library Management"
)

class ContributorModelView(ModelView):
    datamodel = SQLAInterface(Contributor)
    list_columns = ['con', 'ver_id', 'version.library']
    search_columns = ['con']
    base_order = ('con', 'asc')

appbuilder.add_view(
    ContributorModelView,
    "Manage Contributors",
    icon="fa-user",
    category="Library Management"
)

class TagModelView(ModelView):
    datamodel = SQLAInterface(Tag)
    list_columns = ['tag_name', 'description']
    search_columns = ['tag_name', 'description']
    base_order = ('tag_name', 'asc')

appbuilder.add_view(
    TagModelView,
    "Manage Tags",
    icon="fa-tag",
    category="Library Management"
)
