from yummy_cereal.annotated_fields import cls_is_annotated, get_cls_annotations


class AnnotatedClass:
    name: str


class BlankClass:
    pass


def test_cls_is_annotated() -> None:
    assert cls_is_annotated(AnnotatedClass)
    assert not cls_is_annotated(BlankClass)


def test_get_cls_annotations() -> None:
    assert get_cls_annotations(AnnotatedClass) == {"name": str}
    assert get_cls_annotations(BlankClass) == {}
