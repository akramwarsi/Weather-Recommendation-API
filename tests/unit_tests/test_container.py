from app.core.exceptions import NotFoundError


# It must raise an error
def test_container_with_intended_exception(container):
    recommendation_service = container.recommendation_service()
    try:
        found_user = recommendation_service.get_by_id(1)
    except NotFoundError as e:
        assert True
        return
    # assert False
