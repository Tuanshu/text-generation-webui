   not OK:
   
   request = {
        "prompt": context,
        "max_new_tokens": 512,
        "do_sample": True,
        "temperature": 1.3,
        "top_p": 0.1,  # 0.1        # 如果 1
        "typical_p": 1,
        "repetition_penalty": 1,
        "top_k": 40,  # 40               2  
        "min_length": 0,
        "no_repeat_ngram_size": 0,
        "num_beams": 1,
        "penalty_alpha": 0,
        "length_penalty": 1,  # 1
        "early_stopping": False,
        "seed": -1,
        "add_bos_token": True,
        "truncation_length": 2048,
        "ban_eos_token": False,
        "skip_special_tokens": True,
        "stopping_strings": [],
    }


OK:
    request = {
        "prompt": context,
        "max_new_tokens": 512,
        "do_sample": True,
        "temperature": 1.3,
        "top_p": 1,  # 0.1        # 如果 1
        "typical_p": 1,
        "repetition_penalty": 1,
        "top_k": 40,  # 40               2
        "min_length": 0,
        "no_repeat_ngram_size": 0,
        "num_beams": 1,
        "penalty_alpha": 0,
        "length_penalty": 1,  # 1
        "early_stopping": False,
        "seed": -1,
        "add_bos_token": True,
        "truncation_length": 2048,
        "ban_eos_token": False,
        "skip_special_tokens": True,
        "stopping_strings": [],
    }


Not OK:

    request = {
        "prompt": context,
        "max_new_tokens": 512,
        "do_sample": True,
        "temperature": 1.3,
        "top_p": 1,  # 0.1        # 如果 1
        "typical_p": 1,
        "repetition_penalty": 1,
        "top_k": 1,  # 40               2
        "min_length": 0,
        "no_repeat_ngram_size": 0,
        "num_beams": 1,
        "penalty_alpha": 0,
        "length_penalty": 1,  # 1
        "early_stopping": False,
        "seed": -1,
        "add_bos_token": True,
        "truncation_length": 2048,
        "ban_eos_token": False,
        "skip_special_tokens": True,
        "stopping_strings": [],
    }

    usually OK (sometime not ok):
     request = {
        "prompt": context,
        "max_new_tokens": 512,
        "do_sample": True,
        "temperature": 1.3,
        "top_p": 1,  # 0.1        # 如果 1
        "typical_p": 1,
        "repetition_penalty": 1,
        "top_k": 2,  # 40               2
        "min_length": 0,
        "no_repeat_ngram_size": 0,
        "num_beams": 1,
        "penalty_alpha": 0,
        "length_penalty": 1,  # 1
        "early_stopping": False,
        "seed": -1,
        "add_bos_token": True,
        "truncation_length": 2048,
        "ban_eos_token": False,
        "skip_special_tokens": True,
        "stopping_strings": [],
    }


    Not OK:
        request = {
        "prompt": context,
        "max_new_tokens": 512,
        "do_sample": True,
        "temperature": 0,# 1.3
        "top_p": 1,  # 0.1        # 如果 1
        "typical_p": 1,
        "repetition_penalty": 1,
        "top_k": 1,  # 40               2
        "min_length": 0,
        "no_repeat_ngram_size": 0,
        "num_beams": 1,
        "penalty_alpha": 0,
        "length_penalty": 1,  # 1
        "early_stopping": False,
        "seed": -1,
        "add_bos_token": True,
        "truncation_length": 2048,
        "ban_eos_token": False,
        "skip_special_tokens": True,
        "stopping_strings": [],
    }


    not OK:

       request = {
        "prompt": context,
        "max_new_tokens": 2048, #512
        "do_sample": True,
        "temperature": 0,# 1.3
        "top_p": 1,  # 0.1        # 如果 1
        "typical_p": 1,
        "repetition_penalty": 1,
        "top_k": 1,  # 40               2
        "min_length": 0,
        "no_repeat_ngram_size": 0,
        "num_beams": 1,
        "penalty_alpha": 0,
        "length_penalty": 1,  # 1
        "early_stopping": False,
        "seed": -1,
        "add_bos_token": True,
        "truncation_length": 2048,
        "ban_eos_token": False,
        "skip_special_tokens": True,
        "stopping_strings": [],
    }


Not OK:

    request = {
        "prompt": context,
        "max_new_tokens": 2048,  # 512
        "do_sample": False,  # True
        "temperature": 0,  # 1.3
        "top_p": 1,  # 0.1        # 如果 1
        "typical_p": 1,
        "repetition_penalty": 1,
        "top_k": 1,  # 40               2
        "min_length": 0,
        "no_repeat_ngram_size": 0,
        "num_beams": 1,
        "penalty_alpha": 0,
        "length_penalty": 1,  # 1
        "early_stopping": False,
        "seed": -1,
        "add_bos_token": True,
        "truncation_length": 2048,
        "ban_eos_token": False,
        "skip_special_tokens": True,
        "stopping_strings": [],
    }


    Not OK:
       request = {
        "prompt": context,
        "max_new_tokens": 2048,  # 512
        "do_sample": False,  # True
        "temperature": 0,  # 1.3
        "top_p": 1,  # 0.1        # 如果 1
        "typical_p": 1,
        "repetition_penalty": 1,
        "top_k": 2,  # 40               2
        "min_length": 0,
        "no_repeat_ngram_size": 0,
        "num_beams": 1,
        "penalty_alpha": 0,
        "length_penalty": 1,  # 1
        "early_stopping": False,
        "seed": -1,
        "add_bos_token": True,
        "truncation_length": 2048,
        "ban_eos_token": False,
        "skip_special_tokens": True,
        "stopping_strings": [],
    }

    Not OK:
       request = {
        "prompt": context,
        "max_new_tokens": 2048,  # 512
        "do_sample": True,  # True
        "temperature": 0,  # 1.3
        "top_p": 1,  # 0.1        # 如果 1
        "typical_p": 1,
        "repetition_penalty": 1,
        "top_k": 2,  # 40               2
        "min_length": 0,
        "no_repeat_ngram_size": 0,
        "num_beams": 1,
        "penalty_alpha": 0,
        "length_penalty": 1,  # 1
        "early_stopping": False,
        "seed": -1,
        "add_bos_token": True,
        "truncation_length": 2048,
        "ban_eos_token": False,
        "skip_special_tokens": True,
        "stopping_strings": [],
    }


    Not OK:
      request = {
        "prompt": context,
        "max_new_tokens": 512,  # 512
        "do_sample": True,  # True
        "temperature": 0,  # 1.3
        "top_p": 1,  # 0.1        # 如果 1
        "typical_p": 1,
        "repetition_penalty": 1,
        "top_k": 2,  # 40               2
        "min_length": 0,
        "no_repeat_ngram_size": 0,
        "num_beams": 1,
        "penalty_alpha": 0,
        "length_penalty": 1,  # 1
        "early_stopping": False,
        "seed": -1,
        "add_bos_token": True,
        "truncation_length": 2048,
        "ban_eos_token": False,
        "skip_special_tokens": True,
        "stopping_strings": [],
    }

    Usually OK:
        request = {
        "prompt": context,
        "max_new_tokens": 512,  # 512
        "do_sample": True,  # True
        "temperature": 1,  # 1.3
        "top_p": 1,  # 0.1        # 如果 1
        "typical_p": 1,
        "repetition_penalty": 1,
        "top_k": 2,  # 40               2
        "min_length": 0,
        "no_repeat_ngram_size": 0,
        "num_beams": 1,
        "penalty_alpha": 0,
        "length_penalty": 1,  # 1
        "early_stopping": False,
        "seed": -1,
        "add_bos_token": True,
        "truncation_length": 2048,
        "ban_eos_token": False,
        "skip_special_tokens": True,
        "stopping_strings": [],
    }


    Usually OK:
      request = {
        "prompt": context,
        "max_new_tokens": 1024,  # 512
        "do_sample": True,  # True
        "temperature": 1,  # 1.3
        "top_p": 1,  # 0.1        # 如果 1
        "typical_p": 1,
        "repetition_penalty": 1,
        "top_k": 2,  # 40               2
        "min_length": 0,
        "no_repeat_ngram_size": 0,
        "num_beams": 1,
        "penalty_alpha": 0,
        "length_penalty": 1,  # 1
        "early_stopping": False,
        "seed": -1,
        "add_bos_token": True,
        "truncation_length": 2048,
        "ban_eos_token": False,
        "skip_special_tokens": True,
        "stopping_strings": [],
    }

    not OK:
        request = {
        "prompt": context,
        "max_new_tokens": 1024,  # 512
        "do_sample": True,  # True
        "temperature": 1,  # 1.3
        "top_p": 1,  # 0.1        # 如果 1
        "typical_p": 1,
        "repetition_penalty": 1,
        "top_k": 2,  # 40               2
        "min_length": 0,
        "no_repeat_ngram_size": 0,
        "num_beams": 1,
        "penalty_alpha": 0,
        "length_penalty": 1,  # 1
        "early_stopping": False,
        "seed": 17,  # -1
        "add_bos_token": True,
        "truncation_length": 2048,
        "ban_eos_token": False,
        "skip_special_tokens": True,
        "stopping_strings": [],
    }


Not OK:
  request = {
        "prompt": context,
        "max_new_tokens": 512,  # 512
        "do_sample": True,  # True
        "temperature": 1,  # 1.3
        "top_p": 1,  # 0.1        # 如果 1
        "typical_p": 1,
        "repetition_penalty": 1,
        "top_k": 2,  # 40               2
        "min_length": 0,
        "no_repeat_ngram_size": 0,
        "num_beams": 1,
        "penalty_alpha": 0,
        "length_penalty": 1,  # 1
        "early_stopping": False,
        "seed": 17,  # -1
        "add_bos_token": True,
        "truncation_length": 2048,
        "ban_eos_token": False,
        "skip_special_tokens": True,
        "stopping_strings": [],
    }

    OK:
     request = {
        "prompt": context,
        "max_new_tokens": 512,  # 512
        "do_sample": True,  # True
        "temperature": 1,  # 1.3
        "top_p": 1,  # 0.1        # 如果 1
        "typical_p": 1,
        "repetition_penalty": 1,
        "top_k": 10,  # 40               2
        "min_length": 0,
        "no_repeat_ngram_size": 0,
        "num_beams": 1,
        "penalty_alpha": 0,
        "length_penalty": 1,  # 1
        "early_stopping": False,
        "seed": 17,  # -1
        "add_bos_token": True,
        "truncation_length": 2048,
        "ban_eos_token": False,
        "skip_special_tokens": True,
        "stopping_strings": [],
    }

    Not OK:
       request = {
        "prompt": context,
        "max_new_tokens": 512,  # 512
        "do_sample": True,  # True
        "temperature": 1,  # 1.3
        "top_p": 1,  # 0.1        # 如果 1
        "typical_p": 1,
        "repetition_penalty": 1,
        "top_k": 4,  # 40               2
        "min_length": 0,
        "no_repeat_ngram_size": 0,
        "num_beams": 1,
        "penalty_alpha": 0,
        "length_penalty": 1,  # 1
        "early_stopping": False,
        "seed": 17,  # -1
        "add_bos_token": True,
        "truncation_length": 2048,
        "ban_eos_token": False,
        "skip_special_tokens": True,
        "stopping_strings": [],
    }


Not OK:
 request = {
        "prompt": context,
        "max_new_tokens": 512,  # 512
        "do_sample": True,  # True
        "temperature": 1,  # 1.3
        "top_p": 1,  # 0.1        # 如果 1
        "typical_p": 1,
        "repetition_penalty": 1,
        "top_k": 8,  # 40               2
        "min_length": 0,
        "no_repeat_ngram_size": 0,
        "num_beams": 1,
        "penalty_alpha": 0,
        "length_penalty": 1,  # 1
        "early_stopping": False,
        "seed": 17,  # -1
        "add_bos_token": True,
        "truncation_length": 2048,
        "ban_eos_token": False,
        "skip_special_tokens": True,
        "stopping_strings": [],
    }

    Not OK:
    request = {
        "prompt": context,
        "max_new_tokens": 1024,  # 512
        "do_sample": False,  # True
        "temperature": 1,  # 1.3
        "top_p": 1,  # 0.1        # 如果 1
        "typical_p": 1,
        "repetition_penalty": 1,
        "top_k": 10,  # 40               2
        "min_length": 0,
        "no_repeat_ngram_size": 0,
        "num_beams": 1,
        "penalty_alpha": 0,
        "length_penalty": 1,  # 1
        "early_stopping": False,
        "seed": 17,  # -1
        "add_bos_token": True,
        "truncation_length": 2048,
        "ban_eos_token": False,
        "skip_special_tokens": True,
        "stopping_strings": [],
    }