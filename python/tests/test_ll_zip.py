


@pytest.fixture
def after_test():
    linked = Linked_list()
    # linked.append_node()
    linked.insert_node(0)
    linked.insert_node(1)
    linked.insert_node(25)
    linked.insertAfter(1,"khaled")
    return linked
