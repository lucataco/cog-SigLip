# google/siglip-base-patch16-224 Cog model

This is an implementation of the [google/siglip-base-patch16-224](https://huggingface.co/google/siglip-base-patch16-224) as a Cog model. [Cog packages machine learning models as standard containers.](https://github.com/replicate/cog)

## Basic usage

Run a prediction

    cog predict -i image=@cats.jpg

## Example:

Output: [{'score': 0.1979, 'label': '2 cats'}, {'score': 0.0, 'label': ' a remote'}, {'score': 0.0, 'label': ' a plane'}]

![input image](cats.jpg)

## License

The code in this repository is licensed under the [Apache License 2.0](LICENSE).

The model weights are not covered by this license. [google/siglip-base-patch16-224](https://huggingface.co/google/siglip-base-patch16-224) is released under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license.
