from flask import g
from flask.ext.babel import ngettext

from .location import Location


class RoomGroup(Location):
    priority = 10

    def __init__(self, graph, name, titles={}, any_titles={}):
        super().__init__(name, titles)
        self.graph = graph
        self.any_titles = any_titles
        self.rooms = []

    @property
    def subtitle(self):
        return ngettext('%(num)d room', '%(num)d rooms', num=len(self.rooms))

    @property
    def title(self):
        return self.any_titles.get(g.locale, self.name)

    @property
    def collection_title(self):
        return super().title

    @property
    def nodes(self):
        return sum((r.nodes for r in self.rooms), [])

    def __repr__(self):
        return 'RoomGroup(%s)' % repr(self.name)
