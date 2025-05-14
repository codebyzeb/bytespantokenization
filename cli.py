import os

import typer

from commands import analysis, data, extract, ngram, tokenizers, upload, eval

# Set this here in order to have effect
# See: https://github.com/huggingface/transformers/issues/25305#issuecomment-1852931139
# os.environ["TRANSFORMERS_CACHE"] = "./.huggingface_cache"
CACHE_PATH = "./.huggingface_cache"
os.environ["HF_HOME"] = CACHE_PATH
os.environ["HF_DATASETS_CACHE"] = CACHE_PATH
os.environ["TORCH_HOME"] = CACHE_PATH
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"

app = typer.Typer()
app.add_typer(analysis.app, name="analysis")
app.add_typer(data.app, name="data")
app.add_typer(ngram.app, name="ngram")
app.add_typer(extract.app, name="extract")
app.add_typer(tokenizers.app, name="tokenizers")
app.add_typer(upload.app, name="upload")
app.add_typer(eval.app, name="eval")


if __name__ == "__main__":
    app()
