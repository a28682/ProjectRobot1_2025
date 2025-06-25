import hashlib
from k210_models import initialization, face_reg
import music
import basic

k210_models.initialization()
music.set_built_in_speaker_enabled(True)
face = -2
basic.clear_screen()


def hash_face_id(face_id):
    return hashlib.sha256(str(face_id).encode()).hexdigest()


def on_forever():
    if face == 0:
        music._play_default_background(music.built_in_playable_melody(Melodies.POWER_UP),
                                       music.PlaybackMode.UNTIL_DONE)
        basic.clear_screen()
    if face == 1:
        music._play_default_background(music.built_in_playable_melody(Melodies.JUMP_UP),
                                       music.PlaybackMode.UNTIL_DONE)
        basic.clear_screen()
    if face == 2:
        music._play_default_background(music.built_in_playable_melody(Melodies.POWER_DOWN),
                                       music.PlaybackMode.UNTIL_DONE)
        basic.clear_screen()


basic.forever(on_forever)


def on_forever2():
    global face
    raw_face = k210_models.face_reg()

    if raw_face >= 0:
        hashed_value = hash_face_id(raw_face)

        face = raw_face
        basic.show_number(face)


basic.forever(on_forever2)