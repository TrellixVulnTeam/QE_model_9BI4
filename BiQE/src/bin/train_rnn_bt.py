import argparse
from src.main_1 import train_rnn_bt
from . import auto_mkdir

parser = argparse.ArgumentParser()

parser.add_argument('--transformer_model_name', type=str,
                    help="The name of the model. Will alse be the prefix of saving archives.")

parser.add_argument('--transformer_model_bt_name', type=str,
                    help="The name of the model. Will alse be the prefix of saving archives.")

parser.add_argument('--qe_model_name', type=str,
                    help="The name of the model. Will alse be the prefix of saving archives.")

parser.add_argument('--reload', action="store_true",
                    help="Whether to restore from the latest archives.")

parser.add_argument('--config_path', type=str,
                    help="The path to config file.")

parser.add_argument('--log_path', type=str, default="./log",
                    help="The path for saving tensorboard logs. Default is ./log")

parser.add_argument('--saveto_transformer_model', type=str, default="./save",
                    help="The path for saving models. Default is ./save.")
parser.add_argument('--saveto_transformer_model_bt', type=str, default="./save",
                    help="The path for saving models. Default is ./save.")
parser.add_argument('--saveto_qe_model', type=str, default="./save",
                    help="The path for saving models. Default is ./save.")


parser.add_argument('--debug', action="store_true",
                    help="Use debug mode.")

parser.add_argument("--model_path", type=str,
                    help="""Path to transformer model files.""")

parser.add_argument("--model_bt_path", type=str,
                    help="""Path to transformer bt model files.""")
parser.add_argument("--qe_model_path", type=str,default="",
                    help="""Path to transformer model files.""")

parser.add_argument('--use_gpu', action="store_true",
                    help="Whether to use GPU.")

parser.add_argument('--pretrain_path', type=str, default="", help="The path for pretrained model.")


def run(**kwargs):
    args = parser.parse_args()

    # Modify some options.
    for k, v in kwargs.items():
        setattr(args, k, v)

    auto_mkdir(args.log_path)
    auto_mkdir(args.saveto_transformer_model)
    auto_mkdir(args.saveto_transformer_model_bt)
    auto_mkdir(args.saveto_qe_model)

    train_rnn_bt(args)


if __name__ == '__main__':
    run()
