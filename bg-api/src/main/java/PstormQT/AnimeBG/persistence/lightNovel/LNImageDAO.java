package PstormQT.AnimeBG.persistence.lightNovel;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Map;
import java.util.TreeMap;
import java.util.logging.Logger;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import com.fasterxml.jackson.databind.ObjectMapper;

import PstormQT.AnimeBG.model.LNImage;

@Component
public class LNImageDAO implements LNImageInterfaceDAO {
    private static final Logger LOG = Logger.getLogger(LNImage.class.getName());
    Map<Integer, LNImage> lns; // Local cache to prevent unnecessary file loading
    private ObjectMapper objectMapper;
    private static int nextId = 0;
    private String filename;

    public LNImageDAO(@Value("${image.file}") String filename, ObjectMapper objectMapper) throws IOException{
        this.filename = filename;
        this.objectMapper = objectMapper;
        load();
    }

    /**
     * Create a synchronized zone for ID of the game
     * @return
     */
    private synchronized static int nextId() {
        int id = nextId;
        ++nextId;
        return id;
    }

    /**
     * Load the JSON file
     */
    private boolean load() throws IOException {
        lns = new TreeMap<>();
        nextId = 0;

        // Deserialize JSON objects from the file into an array of Items
        LNImage[] imageData = objectMapper.readValue(new File(filename), LNImage[].class);

        // Add each item to the tree map and track the highest ID
        for (LNImage ln : imageData) {
            lns.put(ln.getID(), ln);
            if (ln.getID() > nextId) {
                nextId = ln.getID();
            }
        }
        // Ensure the next ID is one greater than the max ID
        nextId++;
        return true;
    }

    /**
     * Save into the JSON file
     * @return
     * @throws IOException
     */
    private boolean save() throws IOException {
        LNImage[] imageLN = getLNArray();

        // Serialize Java objects into JSON and save to file
        objectMapper.writeValue(new File(filename), imageLN);
        return true;
    }


    /**
     * Get every item in the cupboard
     * @return
     */
    private LNImage[] getLNArray() {
        return getLNArray(null);
    }

    /**
     * Get item containing name in the cupboard - null to get everythin
     * @param containText : Text to check against
     * @return: the item list which match the name
     */
    private LNImage[] getLNArray(String containText) {
        ArrayList<LNImage> imageList = new ArrayList<>();

        for (LNImage image : this.lns.values()) {
            if (containText == null || image.getSource().contains(containText)) {
                imageList.add(image);
            }
        }
        return imageList.toArray(new LNImage[0]);
    }

    private LNImage[] getLNArrayAuthor(String containAuthor) {
        ArrayList<LNImage> imageList = new ArrayList<>();

        for (LNImage image : this.lns.values()) {
            if (containAuthor == null || image.getAuthor().contains(containAuthor)) {
                imageList.add(image);
            }
        }
        return imageList.toArray(new LNImage[0]);
    }

    @Override
    public LNImage createLN(LNImage LN) throws IOException {
        synchronized(this.lns){
            LNImage image = new LNImage(nextId(),LN.getSource(), LN.getAuthor(),
                    LN.getVolume(), LN.getPath(), LN.getArtCount(), LN.getColor());
            this.lns.put(image.getID(), image);
            save();
            return image;
        }
    }

    @Override
    public LNImage[] getAllLN() throws IOException {
        synchronized(this.lns){
            return getLNArray(null);
        }
    }

    @Override
    public LNImage[] getNameLN(String name) throws IOException {
        synchronized(this.lns){
            return getLNArray(name);
        }
    }

    @Override
    public LNImage[] getAuthorLN(String author) throws IOException {
        synchronized(this.lns){
            return getAuthorLN(author);
        }
    }

    @Override
    public LNImage getLNID(int id) throws IOException {
        synchronized(this.lns) {
            if (this.lns.containsKey(id))
                return this.lns.get(id);
            else
                return null;
        }
    }

    @Override
    public LNImage updateAll(LNImage LN) throws IOException {
        synchronized(this.lns) {
            if (this.lns.containsKey(LN.getID()) == false)
                return null;  // hero does not exist

            this.lns.put(LN.getID(),LN);
            save(); // may throw an IOException
            return LN;
        }
    }

    @Override
    public LNImage updateSource(String source, int ID) throws IOException {
        synchronized(this.lns){
            if(this.lns.containsKey(ID) == false)
                return null;
            this.lns.get(ID).setSource(source);
            save();
            return this.lns.get(ID);
        }
    }

    @Override
    public LNImage updateVolume(Float vol, int ID) throws IOException {
        synchronized(this.lns){
            if(this.lns.containsKey(ID) == false)
                return null;
            this.lns.get(ID).setVolume(vol);
            save();
            return this.lns.get(ID);
        }
    }

    @Override
    public LNImage updateAuthor(String Author, int ID) throws IOException {
        synchronized(this.lns){
            if(this.lns.containsKey(ID) == false)
                return null;
            this.lns.get(ID).setAuthor(Author);;
            save();
            return this.lns.get(ID);
        }
    }

    @Override
    public LNImage updateArtCount(int artCount, int ID) throws IOException {
        synchronized(this.lns){
            if(this.lns.containsKey(ID) == false)
                return null;
            this.lns.get(ID).setArtCount(artCount);;
            save();
            return this.lns.get(ID);
        }
    }

    @Override
    public LNImage updateColor(boolean color, int ID) throws IOException {
        synchronized(this.lns){
            if(this.lns.containsKey(ID) == false)
                return null;
            this.lns.get(ID).setColor(color);
            save();
            return this.lns.get(ID);
        }
    }

    @Override
    public boolean deleteLN(int id) throws IOException {
        synchronized(this.lns) {
            if (this.lns.containsKey(id)) {
                this.lns.remove(id);
                return save();
            }
            else
                return false;
        }
    }
    
}
