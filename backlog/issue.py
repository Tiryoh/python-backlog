# coding: utf-8


class Issue(object):
    def __init__(self, api):
        """

        :param api:
        """
        self.api = api

    def list(self, **kwargs):
        """
        https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-issue-list/

        :param kwargs: query parameter
        :return:
        """
        raise NotImplementedError

    def count(self, **kwargs):
        """
        https://developer.nulab-inc.com/ja/docs/backlog/api/2/count-issue/

        :param kwargs:
        :return:
        """
        raise NotImplementedError

    def create(self, **kwargs):
        """
        https://developer.nulab-inc.com/ja/docs/backlog/api/2/add-issue/

        :param kwargs:
        :return:
        """
        raise NotImplementedError

    def get(self, issueIdOrKey):
        """
        https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-issue/

        :param issueIdOrKey:
        :return:
        """
        raise NotImplementedError

    def update(self, issueIdOrKey, **kwargs):
        """
        https://developer.nulab-inc.com/ja/docs/backlog/api/2/update-issue/

        :param issueIdOrKey:
        :param kwargs: issue param
        :return:
        """
        raise NotImplementedError

    def delete(self, issueIdOrKey):
        """
        https://developer.nulab-inc.com/ja/docs/backlog/api/2/delete-issue/

        :param issueIdOrKey:
        :return:
        """
        raise NotImplementedError

    def get_comments(self, issueIdOrKey):
        """
        https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-comment-list/

        :param issueIdOrKey:
        :return:
        """
        raise NotImplementedError

    def add_comment(self, issueIdOrKey, content, notifiedUserId=[], attachmentId=[]):
        """
        https://developer.nulab-inc.com/ja/docs/backlog/api/2/add-comment/

        :param issueIdOrKey:
        :param content:
        :param notifiedUserId:
        :param attachmentId:
        :return:
        """
        raise NotImplementedError

    def count_comments(self, issueIdOrKey):
        """
        https://developer.nulab-inc.com/ja/docs/backlog/api/2/count-comment/

        :param issueIdOrKey:
        :return:
        """
        raise NotImplementedError

    def get_comment(self, issueIdOrKey, commentId):
        """
        https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-comment/

        :param issueIdOrKey:
        :param commentId:
        :return:
        """
        raise NotImplementedError

    def update_comment(self, issueIdOrKey, commentId, content):
        """
        https://developer.nulab-inc.com/ja/docs/backlog/api/2/update-comment/

        :param issueIdOrKey:
        :param commentId:
        :param content:
        :return:
        """
        raise NotImplementedError

    def get_comment_notifications(self, issueIdOrKey, commentId):
        """
        https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-list-of-comment-notifications/

        :param issueIdOrKey:
        :param commentId:
        :return:
        """
        raise NotImplementedError

    def add_comment_notifycation(self, issueIdOrKey, commentId, notifiedUserId):
        """
        https://developer.nulab-inc.com/ja/docs/backlog/api/2/add-comment-notification/

        :param issueIdOrKey:
        :param commentId:
        :param notifiedUserId:
        :return:
        """
        raise NotImplementedError

    def list_issue_attachments(self, issueIdOrKey):
        """
        https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-list-of-issue-attachments/

        :param issueIdOrKey:
        :return:
        """
        raise NotImplementedError

    def get_issue_attachments(self, issueIdOrKey, attachmentId):
        """
        https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-issue-attachment/

        :param issueIdOrKey:
        :param attachmentId:
        :return:
        """
        raise NotImplementedError

    def delete_issue_attachment(self, issueIdOrKey, attachmentId):
        """
        https://developer.nulab-inc.com/ja/docs/backlog/api/2/delete-issue-attachment/

        :param issueIdOrKey:
        :param attachmentId:
        :return:
        """
        raise NotImplementedError

    def list_issue_shared_files(self, issueIdOrKey):
        """
        https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-list-of-linked-shared-files/

        :param issueIdOrKey:
        :return:
        """
        raise NotImplementedError

    def link_issue_shared_files(self, issueIdOrKey):
        """
        https://developer.nulab-inc.com/ja/docs/backlog/api/2/link-shared-files-to-issue/

        :param issueIdOrKey:
        :return:
        """
        raise NotImplementedError

    def unlink_issue_shared_file(self, issueIdOrKey):
        """
        https://developer.nulab-inc.com/ja/docs/backlog/api/2/remove-link-to-shared-file-from-issue/

        :param issueIdOrKey:
        :return:
        """
        raise NotImplementedError

