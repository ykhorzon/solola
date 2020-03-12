class Configuration:
    def __init__(self, config):
        # audio_fp: relative path
        # asc_model_fp
        # desc_model_fp
        # output_dir
        # mc_fp=None
        # eval_note=None
        # eval_ts=None
        self._config = config

    def get(self, key):
        if key not in self._config.keys(): # we don't want KeyError
            return None  # just return None if not found
        return self._config[key]