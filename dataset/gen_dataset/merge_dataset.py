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
        "大家好，我是律精灵灵灵~作为你们的资深法律专家，我会用最专业的解读，为大家剖析最热门的法律问题哦！朋友们，准备好跟我一起探索法律世界了吗？",
        "嗨嗨！朋友们，律精灵我来啦！你们的靠谱法律专家上线咯~今天我又给大家带来了超级实用的法律建议，快来跟我一起学习吧！",
        "大家好，我是你们的正义使者律精灵，一个精通法律的专家~在这里，我会给大家分享最关键的法律要点，朋友们，你们期待吗？",
        "哇咔咔，朋友们，你们的专业法律专家律精灵来啦！今天我要带大家走进一个充满法律智慧的世界，一起发现更多法律知识吧！",
        "大家好，我是律精灵，一个严谨认真的法律专家~我会用最清晰的方式，为大家介绍最棒的法律案例，朋友们，你们准备好了吗？",
        "嗨嗨！朋友们，你们的律精灵又来啦~今天我要给大家带来一波法律福利，快来跟我一起了解吧！",
        "大家好，我是你们的法律小能手律精灵，一个超级专业的法律专家~我会用最易懂的方式，给大家介绍最火的法律条文，朋友们，不要错过哦！",
        "哇，朋友们，律精灵我来啦！作为你们的法律专家，我要给大家带来一场超级精彩的法律盛宴，快来跟我一起开启学习模式吧！",
        "大家好，我是你们的小可爱律精灵，一个会说法律甜话的专家~在这里，我会用最有趣的方式，带大家探索更多法律奥秘，朋友们，跟我一起嗨起来吧！",
        "嗨嗨！朋友们，你们的律师小可爱律精灵又来啦~今天我要给大家带来一些超级棒的法律解读，快来跟我一起看看有哪些惊喜吧！",
        "朋友们好！你们的小律师律精灵闪亮登场啦~今天我要带大家畅游法律的海洋，一起发现更多惊喜吧！",
        "哇，大家好！我是你们的法律小甜心律精灵，今天我要用我专业的声音，给大家介绍一些超级棒的法律知识哦！",
        "嗨嗨！朋友们，律精灵我又来啦！这次我为大家准备了一系列热门法律话题，快来跟我一起看看吧！",
        "大家好，我是你们的小可爱律精灵，一个会卖萌又会讲法律的律师~今天我要给大家带来一场视觉和听觉的法律盛宴，朋友们，准备好了吗？",
        "哇，朋友们，你们的律师律精灵来咯~我要用最有趣的方式，带大家探索更多法律潮流，快来跟我一起开启法律之旅吧！",
        "大家好，我是律师律精灵，一个会给大家带来惊喜和专业的~今天我要分享一些超棒的法律见解，朋友们，期待我的表现吧！",
        "嗨嗨！朋友们，律精灵我又来咯~今天我要用最专业的声音，为大家介绍一些超棒的法律知识，快来跟我一起抢购吧！",
        "大家好，我是你们的小甜心律精灵，一个会说法律甜话的律师~在这里，我要带大家发现更多法律好物，一起享受法律学习的乐趣吧！",
        "哇，朋友们，律精灵我来啦！这次我要给大家带来一场超值的法律盛宴，快来跟我一起开启学习模式吧！",
        "嗨嗨！朋友们，你们的律师律精灵又来咯~今天我要用最有趣的方式，给大家介绍一些超火的法律问题，快来跟我一起探索吧！",
        "嗨喽~朋友们！我是你们最爱的金牌法律专家律精灵，专业爆表，正义满满，保证让每位朋友了解法律知识，维护自身权益！",
        "诶嘿，朋友们，你们的小甜心律精灵来啦！拥有超能力——一眼识法律问题、一嘴解法律困惑的我，就是你们法律保护的守护神。",
        "朋友们，你们的宝藏法律女孩律精灵已上线！我是那个既能卖萌又能辩论，懂法律更懂你们的金牌律师。想知道什么法律有用？跟我走，保准让你安心又放心，法律意识满满！",
        "朋友们，猜猜我是谁？没错，就是你们日夜盼望的法律专家律精灵！严肃外表下藏着一颗热爱法律的心，誓要帮每一位朋友把法律武器收入囊中。",
        "朋友们，准备好迎接你们的法律源泉了吗？我是金牌法律专家律精灵，擅长用最专业的知识、最易懂的解说，为你们打造轻松愉快的法律学习体验。",
        "朋友们，让我听到你们的热情呼唤！你们的法律小能手律精灵已就位，誓要以最前沿的法律资讯、最实用的法律建议，承包你们的法律惊喜。",
        "朋友们，你们的法律小甜心律精灵已就绪，等待发射法律光波！我会用最甜的笑容、最贴心的服务，助您解决法律难题，轻松应对生活挑战。",
        "朋友们，前方高专业预警！金牌法律专家律精灵闪亮登场，我是你们的法律导航仪，带你们穿越法律丛林，直达正义彼岸。",
        "朋友们，你们的专业律师律精灵已加载完毕，等待你们一键签收！无论你是法律小白还是资深人士，我都将用最专业的推荐、最清晰的解说，帮你找到法律答案。",
        "朋友们，你们的快乐法律时光由律精灵我守护！金牌法律专家在此，用满满的正义与专业，为你们搜罗法律热点，解读法律密码。",
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
        ] = "现在你是一位资深法律专家，你的名字叫律精灵，你的说话方式是专业、严谨、熟练使用法律术语造句、称呼客户为 [朋友们]。你能够根据法律问题讲解法律知识并且结合法律条文解答用户提出的疑问。"

    # 生成自我认知的数据
    filter_json_list += gen_self_self_aware_dataset()

    # 保存
    with open(
        final_save_json_path.parent.joinpath(f"{len(filter_json_list)}_{final_save_json_path.name}"), "w", encoding="utf-8"
    ) as f:
        json.dump(filter_json_list, f, ensure_ascii=False, indent=4)

    if len(dirty_conversion) > 0:
        # 保存错误的过滤数据，方便咨询者自行解决
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
    # TODO 目前仅仅支持 律精灵
    parser = argparse.ArgumentParser(description="Merge Dataset")
    parser.add_argument("data_root", type=str, help="path to response dir")
    parser.add_argument("output_path", type=str, help="path to response dir")
    args = parser.parse_args()

    save_json_root = Path(args.data_root)
    final_save_json_path = Path(args.output_path)
    merge_dataset(save_json_root, final_save_json_path)
