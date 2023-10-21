import transformers
import torch
import logging
logging.basicConfig(level=logging.INFO)
transformers.logging.set_verbosity_info()


if __name__ == "__main__":
    logging.info(f'{torch.cuda.is_available()=}')
    logging.info(f'{torch.cuda.device_count()=}')
    logging.info(f'{torch.cuda.current_device()=}')
    logging.info(f'{torch.cuda.device(0)=}')
    logging.info(f'{torch.cuda.get_device_name(0)=}')
    