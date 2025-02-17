package PstormQT.AnimeBG.persistence.lightNovel;

import java.io.IOException;

import PstormQT.AnimeBG.model.LNImage;

public interface LNImageInterfaceDAO {
    
    LNImage createLN(LNImage LN) throws IOException;

    LNImage[] getAllLN() throws IOException;
    
    LNImage[] getNameLN(String name) throws IOException;
    
    LNImage[] getAuthorLN(String Author) throws IOException;

    LNImage getLNID(int id) throws IOException;

    LNImage updateAll(LNImage LN) throws IOException;

    LNImage updateSource(String source, int ID) throws IOException;

    LNImage updateVolume(Float vol, int ID) throws IOException;

    LNImage updateAuthor(String Author, int ID) throws IOException;

    LNImage updateArtCount(int artCount, int ID) throws IOException;

    LNImage updateColor(boolean color, int ID) throws IOException;
    
    boolean deleteLN(int id) throws IOException;
}
