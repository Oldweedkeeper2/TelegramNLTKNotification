from core.alert.texts.keywords_list import SIMPLE_ALERT_TEXTS, TEST_GROUP_TEXTS


def is_alert_text(text):
    return any(alert_text in text.lower() for alert_text in SIMPLE_ALERT_TEXTS)


def is_test_group_text(text):
    return any(test_text in text.lower() for test_text in TEST_GROUP_TEXTS)
