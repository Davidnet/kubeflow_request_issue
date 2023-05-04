# %%
from kfp import dsl


@dsl.component
def print_component(str_exmpl: str) -> None:
    print(str_exmpl)


@dsl.pipeline
def pipeline():
    print_task = print_component(str_exmpl="Hello World!")


if __name__ == "__main__":
    import kfp

    print(kfp.__version__)
    kfp.compiler.Compiler().compile(pipeline, "pipeline.yaml")

# %%
