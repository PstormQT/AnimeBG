package PstormQT.AnimeBG.model;

import java.util.logging.Logger;

import com.fasterxml.jackson.annotation.JsonProperty;

public abstract class Image {
    private static final Logger LOG = Logger.getLogger(Image.class.getName());

    @JsonProperty("id") private int id;
    @JsonProperty("source") private String source;
    @JsonProperty("author") private String author;
    @JsonProperty("path") private String path;

    public Image(@JsonProperty("id") int id,
                @JsonProperty("source") String source,
                @JsonProperty("author") String author,
                @JsonProperty("path") String path){

        this.id = id;
        this.source = source;
        this.author = author;
        this.path = path;
    }

    public int getID(){
        return this.id;
    }

    public String getSource(){
        return this.source;
    }

    public void setSource(String source){
        this.source = source;
    }

    public String getAuthor(){
        return this.author;
    }

    public void setAuthor(String author){
        this.author = author;
    }

    public String getPath(){
        return this.path;
    }

    public void setPath(String path){
        this.path = path;
    }

}
