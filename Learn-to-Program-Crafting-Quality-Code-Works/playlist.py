'''
Created on Apr 17, 2013

@author: Majid Hameed
'''
import song


class Playlist:
    '''
    A song Playlist.
    '''
    
    
    def __init__(self, title):
        ''' (Playlist, str) -> NoneType
        
        >>> playlist = Playlist('Canadian Artists')
        >>> playlist.title
        Canadian Artists
        '''
        self.title = title
        self.songs = []
        
    
    def add(self, song):
        ''' (Playlist, song) -> NoneType
        
        >>> stompa = song.Song("Serena Ryder", "Stompa", 3, 15)
        >>> playlist = Playlist('Canadian Artists')
        >>> playlist.add_song(stompa)
        >>> playlist.songs
        [stompa]
        '''
        self.songs.append(song)
        
    def get_duration(self):
        ''' (Playlist) -> (int, int)

        Return the duration of this playlist as tuple of minutes and
        seconds.

        >>> playlist = Playlist('Canadian Artists')
        >>> playlist.add(song.Song('Neil Young', 'Harvest Moon', 5, 3))
        >>> playlist.add(song.Song('Serena Ryder', 'Stompa', 3, 15)
        >>> playlist.duration()
        (8, 18)
        '''
        
        minutes = 0
        seconds = 0
        for song in self.songs:
            minutes += song.minutes
            seconds += song.seconds
        return (minutes + seconds // 60, seconds % 60)
    
    def __str__(self):
        ''' (Playlist) -> str
        
        Return a string representation of this playlist.

        >>> playlist = Playlist('Canadian Artists')
        >>> playlist.add(song.Song('Neil Young', 'Harvest Moon', 5, 3))
        >>> playlist.add(song.Song('Serena Ryder', 'Stompa', 3, 15)
        """Canadian Artists (10:35)
        1. Neil Young, Harvest Moon (5:03)
        2. Serena Ryder, Stompa (3:15)
        3. Stompin' Tom Connors (2:17)"""
        '''
        duration = self.get_duration()
        playlist_str = self.title + ' ({0}:{1})'.format(duration[0], str(duration[1]).rjust(2, '0'))
        song_count = 1
        for song in self.songs:
            playlist_str += '\n{0}. '.format(song_count) + str(song)
            song_count += 1
        return playlist_str     

if __name__ == '__main__':
    
    playlist = Playlist('Canadian Artists')
    playlist.add(song.Song('Neil Young', 'Harvest Moon', 5, 3))
    playlist.add(song.Song('Serena Ryder', 'Stompa', 3, 15))
    playlist.add(song.Song("Stompin' Tom Connors", "The Hockey Song", 2, 17))
    
    print(playlist)
