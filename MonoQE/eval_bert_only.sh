#!/usr/bin/env bash

export CUDA_VISIBLE_DEVICES=3

echo "Using GPU $CUDA_VISIBLE_DEVICES..."
#--output_dir_src ./qe_src_en2de2017_src2mt_finetuning_no_common_multilingual_output/ \
#--output_dir_mt ./qe_mt_en2de2017_src2mt_finetuning_no_common_multilingual_output/ \

export QE_DIR=/home/houq/pytorch_bert/pytorch-pretrained-BERT-master/QE_en2de2017
export BERT_PRE_TRAINED_MODEL_DIR_SRC=/home/user_data/houq/bert_model/bert-base-cased
export BERT_PRE_TRAINED_MODEL_DIR_MT=/home/user_data/houq/bert_model/bert-base-multilingual-cased

python -m examples.bert_only_eval \
  --task_name QE \
  --do_train \
  --do_eval \
  --data_dir $QE_DIR/ \
  --bert_model_src $BERT_PRE_TRAINED_MODEL_DIR_SRC/ \
  --bert_model_mt $BERT_PRE_TRAINED_MODEL_DIR_MT/ \
  --max_seq_length=50 \
  --train_batch_size=24 \
  --eval_batch_size=24 \
  --learning_rate 2e-5 \
  --num_train_epochs 10.0 \
  --output_dir_src ./qe_src_en2de2017_train_src2mt_finetuning_no_common_multilingual_output_3_bs_32/ \
  --output_dir_mt ./qe_mt_en2de2017_train_src2mt_finetuning_no_common_multilingual_output_3_bs_32/ \
  --output_dir_fc ./qe_fc_en2de2017_train_src2mt_finetuning_no_common_multilingual_output_3_bs_32/fnn.best.1100\
  --saveto "./result_en2de2017_train_src2mt_finetuning_no_common_multilingual_3_bs_32/QE_en2de2017_train_predict.hter" \