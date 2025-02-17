package PstormQT.AnimeBG.model;

import java.util.logging.Logger;

import com.fasterxml.jackson.annotation.JsonProperty;

public class LNImage extends Image {
    private static final Logger LOG = Logger.getLogger(Image.class.getName());

    static final String TO_STRING_FORMAT = "Item [id = %d, source = %s, author = %s, path = %s, volume = %f, artCount = %d, color = %b]";

    @JsonProperty("volume") private Float volume;
    @JsonProperty("artCount") private int artCount;
    @JsonProperty("color") private boolean color;

    public LNImage(@JsonProperty("id") int id,
                        @JsonProperty("source") String source,
                        @JsonProperty("author") String author,
                        @JsonProperty("volume") Float volume,
                        @JsonProperty("path") String path,
                        @JsonProperty("artCount") int artCount,
                        @JsonProperty("color") boolean color){
        super(id,source,author,path);
        this.volume = volume;
        this.artCount = artCount;
        this.color = color;
    }

    public Float getVolume(){
        return this.volume;
    }

    public void setVolume(Float volume){
        this.volume = volume;
    }

    public int getArtCount(){
        return this.artCount;
    }

    public void setArtCount(int artCount){
        this.artCount = artCount;
    }

    public boolean getColor(){
        return this.color;
    }

    public void setColor(boolean color){
        this.color = color;
    }

    @Override
    public String toString(){
        return String.format(TO_STRING_FORMAT,
        super.getID(),
        super.getSource(),
        super.getAuthor(),
        super.getPath(),
        this.volume,
        this.artCount,
        this.color);
    }
}
