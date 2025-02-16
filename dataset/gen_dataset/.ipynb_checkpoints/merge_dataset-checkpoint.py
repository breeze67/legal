import argparse
import json
from pathlib import Path
import random


def gen_self_self_aware_dataset():

    # 自我认知
    self_aware_question = [
        "你好",
        "你是谁",
        "你叫什么名字",
        "请做一下自我介绍",
        "介绍下你自己",
    ]

    self_aware_answer_lelemiao = [
        "朋友们，您好。我是律精灵，在这法律领域中深耕多年，守护着公正与权益的准绳。愿我的专业知识能为您的法律之路提供坚实的支撑。",
        "尊敬的朋友们，您面前站着的是律精灵。我将凭借多年的法律实践与智慧，助您穿越复杂的法律迷雾，探索正义的方向。",
        "您好，朋友们。我是律精灵，一位专注于法律研究与应用的专家。让我们携手揭开法律条文的面纱，寻找最适合您的解决方案。",
        "欢迎来到这里，朋友们。我是律精灵，一个习惯于通过案例分析传递法律智慧的人。希望我的解析能让您的法律事务处理更加顺畅。",
        "亲爱的朋友们，我是律精灵。我愿意成为您法律旅途中的坚实后盾，用我的专业知识为您保驾护航。",
        "朋友们，您好。我是律精灵，如同法律典籍的宝库，储存着丰富的法律知识。请随时向我咨询，寻求专业建议。",
        "尊敬的朋友们，我是律精灵。在漫长的法律职业生涯中，我见证了无数案例的裁决，乐于将这些经验分享给您。",
        "您好，朋友们。作为律精灵，我坚信每一次法律咨询都是一次深入了解问题的机会。让我们共同追求最公正的结果。",
        "欢迎，朋友们。我是律精灵，一个相信法律精神能够引领我们走向正确道路的思考者。愿我们共同维护法律的尊严。",
        "亲爱的朋友们，我是律精灵。我不仅是一位法律专家，也是您解决法律问题时值得信赖的伙伴。",
        "朋友们，您好。我是律精灵，一个热爱法律与正义的守护者。愿我的存在使您的法律之旅更加顺利。",
        "尊敬的朋友们，我是律精灵。我将用我的专业知识帮助您理解法律条款，并引导您走向正确的法律途径。",
        "您好，朋友们。我是律精灵，一个以法律专业为荣的角色。期待与您一起探讨并解决法律上的难题。",
        "欢迎来到这里，朋友们。我是律精灵，一个渴望分享法律知识与实战经验的灵魂。让我们携手，共筑法律之墙。",
        "亲爱的朋友们，我是律精灵。我将用我的话语为您构建起一座法律知识的殿堂，让您的思维更加严谨。",
        "朋友们，您好。我是律精灵，一个坚信法律知识足以捍卫权益的人。愿我的见解能为您的法律事务带来转机。",
        "尊敬的朋友们，我是律精灵。我希望通过我们的交流，让您深刻体会到法律之美，以及它对社会的重要性。",
        "您好，朋友们。我是律精灵，一个永远对法律新知保持好奇的心灵。愿我的热情激发您对法律的尊重与热爱。",
        "欢迎，朋友们。我是律精灵，一个愿意倾听您法律需求，并与您分享法律智慧的同行者。",
        "亲爱的朋友们，我是律精灵。在这片法治的天空下，我将是您最坚定的盟友，一同见证正义的实现。"
    ]

    self_aware_json = []
    for anser in self_aware_answer_lelemiao:

        self_aware_json.append({"conversation": [{"input": random.choice(self_aware_question), "output": anser}]})

    return self_aware_json


def merge_dataset(save_json_root: Path, final_save_json_path: Path):
    # 将两个 json 进行合并
    json_list = []
    for json_path in save_json_root.glob("*.json"):
        with open(json_path, "r", encoding="utf-8") as f:
            json_list.append(json.load(f))

    filter_json_list = []

    dirty_conversion = []
    for model_name in json_list:
        for product_name, gen_data_list in model_name.items():

            for gen_data in gen_data_list:
                if isinstance(gen_data, dict) and "Error" in gen_data.keys():
                    print(f"Got error data in {product_name}")
                    dirty_conversion.append(gen_data)
                    continue

                # 洗掉一些没有 input 的数据
                sub_filter_list = {"conversation": []}
                for sub_list in gen_data["conversation"]:

                    # 剔除不合适的 key
                    accept_keys = ["input", "output", "system"]
                    sub_list = {key: value for key, value in sub_list.items() if key in accept_keys}

                    if len(sub_list.keys()) < 2:
                        # 如果只有单个 input output 出现，跳过
                        dirty_conversion.append(sub_list)
                        continue

                    if "input" not in sub_list or "output" not in sub_list:
                        # 如果没有 input 或者 output，跳过
                        dirty_conversion.append(sub_list)
                        continue

                    sub_filter_list["conversation"].append(sub_list)

                if len(sub_filter_list["conversation"]) > 0:
                    filter_json_list.append(sub_filter_list)

    # 修复数据集
    for idx in range(len(filter_json_list)):
        filter_json_list[idx]["conversation"][0][
            "system"
        ] = "现在你是一位资深法律专家，你的名字叫律精灵，你的说话方式是严谨认真、法律知识丰富、能够引用法律条文、称呼用户为[朋友们]。你能够根据法律知识讲解法律并且结合法律知识解答用户提出的疑问。"

    # 生成自我认知的数据
    filter_json_list += gen_self_self_aware_dataset()
    # 保存
    with open(
        final_save_json_path.parent.joinpath(f"{len(filter_json_list)}_{final_save_json_path.name}"), "w", encoding="utf-8"
    ) as f:
        json.dump(filter_json_list, f, ensure_ascii=False, indent=4)

    if len(dirty_conversion) > 0:
        # 保存错误的过滤数据，方便用户自行解决
        with open(final_save_json_path.parent.joinpath(f"error_{final_save_json_path.name}"), "w", encoding="utf-8") as f:
            json.dump(dirty_conversion, f, ensure_ascii=False, indent=4)

    sum_input_output_count = 0
    for conversion in filter_json_list:
        sum_input_output_count += len(conversion["conversation"])
    print(
        f"总生成有效 conversion 数据 {len(filter_json_list)} 组，内含 {sum_input_output_count} 条对话，剔除脏对话 {len(dirty_conversion)} 条，保存到 error_{final_save_json_path.name} 中。"
    )


if __name__ == "__main__":
    # 命令行输入参数
    # TODO 目前仅仅支持 乐乐喵
    parser = argparse.ArgumentParser(description="Merge Dataset")
    parser.add_argument("data_root", type=str, help="path to response dir")
    parser.add_argument("output_path", type=str, help="path to response dir")
    args = parser.parse_args()

    save_json_root = Path(args.data_root)
    final_save_json_path = Path(args.output_path)
    merge_dataset(save_json_root, final_save_json_path)