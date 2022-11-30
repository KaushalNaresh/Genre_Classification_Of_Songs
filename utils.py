import os.path
# Number of samples per 30s audio clip.
# TODO: fix dataset to be constant.
NB_AUDIO_SAMPLES = 1321967
SAMPLING_RATE = 44100


def get_audio_path(audio_dir, track_id, genre = None):
    """
    Return the path to the mp3 given the directory where the audio is stored
    and the track ID.
    """
    if genre:
        """
        Examples
        --------
        >>> import utils
        >>> AUDIO_DIR = os.environ.get('AUDIO_DIR')
        >>> utils.get_audio_path(AUDIO_DIR, 2)
        'GTZAN_DIR/genres_original/genre/00002.mp3'
        """
        tid_str = '{:05d}'.format(track_id)
        return os.path.join(audio_dir+"genres_original/", genre, genre+"."+tid_str+".wav")
    else:
        """
        Examples
        --------
        >>> import utils
        >>> AUDIO_DIR = os.environ.get('AUDIO_DIR')
        >>> utils.get_audio_path(AUDIO_DIR, 2)
        '../data/fma_small/000/000002.mp3'
        """
        tid_str = '{:06d}'.format(track_id)
        return os.path.join(audio_dir, tid_str[:3], tid_str + '.mp3')