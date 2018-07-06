#!/usr/bin/env python
from cvm.dom import Selector
from cvm.view import Field, View, Page, Group


class LoginPage(Page):
    def __init__(self):
        self.username = Field(Selector.ID, "auth")
        self.password = Field(Selector.ID, "password")
        self.submit = Field(Selector.CSS, "button[type=submit]")


class IndexPage(Page):
    def __init__(self):
        self.forums = Group(ForumItem(Selector.CSS, ".cForumList .ipsDataItem"))


class ForumItem(View):
    def __init__(self, selector: Selector, value: str):
        super().__init__(selector, value)
        self.title = Field(Selector.CSS, ".ipsDataItem_title > a")
        self.date = Field(Selector.CSS, ".ipsDataItem_lastPoster time")


class ForumPage(Page):
    def __init__(self):
        self.topics = Group(TopicItem(Selector.CSS, ".cTopicList:not(.cForumQuestions) .ipsDataItem"))
        self.nav = NavView(Selector.CSS, ".ipsButtonBar .ipsPagination")


class TopicItem(View):
    def __init__(self, selector: Selector, value: str):
        super().__init__(selector, value)
        self.title = Field(Selector.CSS, ".ipsDataItem_title .ipsContained > a")
        self.date = Field(Selector.CSS, ".ipsDataItem_lastPoster time")


class TopicPage(Page):
    def __init__(self):
        self.comments = Group(CommentItem(Selector.CSS, ".ipsComment"))
        self.nav = NavView(Selector.CSS, ".ipsSpacer_bottom .ipsPagination")


class CommentItem(View):
    def __init__(self, selector: Selector, value: str):
        super().__init__(selector, value)
        self.date = Field(Selector.CSS, ".ipsComment_meta time")
        self.body = Field(Selector.CSS, ".ipsComment_content")
        self.attachments = Group(Field(Selector.CSS, "a.ipsAttachLink:not([data-fileid])"))


class NavView(View):
    def __init__(self, selector: Selector, value: str):
        super().__init__(selector, value)
        self.first = Field(Selector.CSS, ".ipsPagination_first > a")
        self.prev = Field(Selector.CSS, ".ipsPagination_prev > a")
        self.next = Field(Selector.CSS, ".ipsPagination_next > a")
        self.last = Field(Selector.CSS, ".ipsPagination_last > a")

