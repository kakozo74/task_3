import os
import shutil
import click
import eyed3


@click.command()
@click.option('-s', '--src-dir', default='.', help='Source directory.', show_default=True)
@click.option('-d', '--dst-dir', default='.', help='Destination directory.', show_default=True)
def music_sort(src_dir, dst_dir):
    while True:
        if os.path.isdir(src_dir):
            try:
                it = os.scandir(src_dir)
            except PermissionError as e:
                print(str(e))
                print('Укажите путь к другому исходному каталогу или q для выхода')
                src_dir = input('>>> ')
                if src_dir == 'q':
                    break
            else:
                with it:
                    for entry in it:
                        if not entry.name.startswith('.') and entry.is_file() \
                                and entry.name.lower().endswith('.mp3'):

                            try:
                                audiofile = eyed3.load(entry)
                                if not audiofile.tag.title:
                                    title = entry.name
                                else:
                                    title = audiofile.tag.title.replace('/', ':')
                                if not audiofile.tag.artist or not audiofile.tag.album:
                                    print(f'Недостаточно тегов для сортировки файла: {entry.name}')
                                    continue
                                else:
                                    artist = audiofile.tag.artist.replace('/', ':')
                                    album = audiofile.tag.album.replace('/', ':')

                                audiofile.tag.save()
                            except AttributeError as e:
                                print(f'Что-то не так с файлом: {entry.name}')
                            except PermissionError as e:
                                print(f'Недостаточно прав: {entry.name}')
                                continue
                            else:
                                new_file_name = f'{title} - {artist} - {album}.mp3'
                                if os.path.exists(os.path.join(dst_dir, artist, album)):
                                    shutil.move(os.path.join(src_dir, entry.name),
                                                os.path.join(dst_dir, artist, album, new_file_name))

                                else:
                                    try:
                                        os.makedirs(os.path.join(dst_dir, artist, album))
                                    except PermissionError as e:
                                        print(str(e))
                                        print(
                                            'Укажите путь к другому исходному каталогу или q для выхода')
                                        dst_dir = input('>>> ')
                                        if dst_dir == 'q':
                                            break
                                    else:
                                        shutil.move(os.path.join(src_dir, entry.name),
                                                    os.path.join(dst_dir, artist, album, new_file_name))
                                print(f'{os.path.join(src_dir, entry.name)} '
                                      f'-> {os.path.join(dst_dir, artist, album, new_file_name)}')
                print('Done.')
                break
        else:
            print('Каталог не найден')
            print('Укажите путь к существующему  каталогу или q для выхода')
            src_dir = input('>>> ')
            if src_dir == 'q':
                break


music_sort()