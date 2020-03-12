from os import path
import numpy as np        
from melody.melody_extraction import extract_melody

class Solola:
    def __init__(self, config):
        # original main() in main.py
        # main(audio_fp,      asc_model_fp,      desc_model_fp,      output_dir,      mc_fp=None,   eval_note=None, eval_ts=None)
        # main(args.audio_fp, args.asc_model_fp, args.desc_model_fp, args.output_dir, args.melody_contour, args.evaluate)
        self._audio_fp = config.get('audio_fp')
        self._output_dir = config.get('output_dir')
        self._mc_fp = config.get('mc_fp')
        self._audio_fn = path.splitext(path.basename(self._audio_fp))[0]
        self._save_dir = path.join(self._output_dir, self._audio_fn)
        
        # extract melody
        # self.extract_melody()
         
        # # Prepare transcribed input
        # audio, sr = rosa.load(audio_fp, sr=None, mono=True)
        # melody = Contour(0, mc_midi)

        # notes = transcribe(audio, melody, asc_model_fp, desc_model_fp, save_dir, audio_fn)
        
        pass
    
    def extract_melody(self):
        mc = None
        mc_midi = None
        if self._mc_fp is None:
            mc, mc_midi = extract_melody(self._audio_fp, self._save_dir)
        else:
            mc_midi = np.loadtxt(mc_fp)
        self._mc = mc
        self._mc_midi = mc_midi
    
    def transcribe(self, audio_file = 'undefined'):
        # audio_fp, asc_model_fp, desc_model_fp, output_dir, mc_fp=None, eval_note=None, eval_ts=None
        # transcribe
         
        
    def synthesizeMZXML(self):
        # generate mzxml
        return 'mzxml'