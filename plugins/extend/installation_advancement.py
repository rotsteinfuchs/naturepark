from beet import Context, ItemModel, Model, Texture
from PIL import Image


def pack_logo(ctx: Context):
    if "installation_advancement" not in ctx.meta:
        ctx.meta["installation_advancement"] = {}

    ctx.meta["installation_advancement"]["icon"] = {
        "id": "minecraft:paper",
        "components": {"item_model": ctx.meta["generate_namespace"] + ":logo"},
    }

    ctx.assets[ctx.meta["generate_namespace"] + ":logo"] = ItemModel(
        {
            "model": {
                "type": "minecraft:model",
                "model": ctx.meta["generate_namespace"] + ":item/logo",
            }
        }
    )

    ctx.assets[ctx.meta["generate_namespace"] + ":item/logo"] = Model(
        {"parent": "item/generated", "textures": {"layer0": ctx.meta["generate_namespace"] + ":item/logo"}}
    )

    ctx.assets[ctx.meta["generate_namespace"] + ":item/logo"] = Texture(source_path="src/pack.png")
