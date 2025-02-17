package PstormQT.AnimeBG.persistence.lightNovel;

import java.io.IOException;

import PstormQT.AnimeBG.model.LNImage;

public interface LNImageInterfaceDAO {
    
    LNImage createLN(LNImage ln) throws IOException;

    LNImage[] getAllLN() throws IOException;
    
    LNImage[] getNameLN() throws IOException;
    
    LNImage[] getAuthorLN() throws IOException;

    LNImage getLNID(int id) throws IOException;

    LNImage updateAll(LNImage LN) throws IOException;

    LNImage updateSource(String source) throws IOException;

    LNImage updateVolume(Float vol) throws IOException;

    LNImage updateAuthor(String Author) throws IOException;

    LNImage updateArtCount(int artCount) throws IOException;

    LNImage updateColor(boolean color) throws IOException;
    
    boolean deleteLN(int id) throws IOException;
}
