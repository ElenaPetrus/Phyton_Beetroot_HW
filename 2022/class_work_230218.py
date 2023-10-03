class MyObject:
    """Context manager class"""

    def __enter__(self):
        print("We are entering the context manager")
        return "some object that we will work with"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("We are cleaning up, we will do it regardless of what happens in the context manager block")
        print("We are doing it even if there was an error")
        print(
            f"We might have caught an exception, type is {type}, value is {exc_val}")


with MyObject() as object_inside_a_context_manager:
    # 'with' tells us we are entering the context manager block
    print(object_inside_a_context_manager)
    raise AttributeError("some error message")
    # the end of the context manager block
