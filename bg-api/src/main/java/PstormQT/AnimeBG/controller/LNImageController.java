package PstormQT.AnimeBG.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;

import PstormQT.AnimeBG.controller.LNImageController;
import PstormQT.AnimeBG.model.LNImage;
/**
 * Handles the REST API request for anything related directly at the cupboard
 * {@literal @}RestController Spring annotation identifies this class as a REST API
 * method handler to the Spring framework
 * 
 * @author: all member
 */
import PstormQT.AnimeBG.persistence.lightNovel.LNImageInterfaceDAO;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.PathVariable;




@RestController
@RequestMapping("/image/light-novel")
public class LNImageController  {
    private static final Logger LOG = Logger.getLogger(LNImageController.class.getName());
    private LNImageInterfaceDAO LNLibrary;

    public LNImageController(LNImageInterfaceDAO LNLibrary){
        this.LNLibrary = LNLibrary;
    }

    @PostMapping("")
    public ResponseEntity<LNImage> postLightNovelImage(@RequestBody LNImage LN) {
        LOG.info("POST /image/light-novel" + LN);
        try{
            LNImage image = this.LNLibrary.createLN(LN);
            if (image == null){
                return new ResponseEntity<>(HttpStatus.CONFLICT);
            }
            return new ResponseEntity<LNImage>(image, HttpStatus.CREATED);
        } catch (IOException e){
            LOG.log(Level.SEVERE,e.getLocalizedMessage());
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    
    }

    @GetMapping("/search/all")
    public ResponseEntity<LNImage[]> getAllLN() {
        LOG.info("GET /image/light-novel");
        try{
            LNImage[] LNs = this.LNLibrary.getAllLN();
            return new ResponseEntity<LNImage[]>(LNs, HttpStatus.OK);
        }
        catch (IOException e){
            LOG.log(Level.SEVERE,e.getLocalizedMessage());
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @GetMapping("/search/name")
    public ResponseEntity<LNImage[]> getNameLN(@RequestParam String query) {
        LOG.info("GET /image/light-novel/search/name>query=" + query);
        try{
            LNImage[] LNs = this.LNLibrary.getNameLN(query);
            return new ResponseEntity<LNImage[]>(LNs, HttpStatus.OK);
        }
        catch (IOException e){
            LOG.log(Level.SEVERE,e.getLocalizedMessage());
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @GetMapping("/search/author")
    public ResponseEntity<LNImage[]> getAuthorLN(@RequestParam String query) {
        LOG.info("GET /image/light-novel/search/name>query=" + query);
        try{
            LNImage[] LNs = this.LNLibrary.getAuthorLN(query);
            return new ResponseEntity<LNImage[]>(LNs, HttpStatus.OK);
        }
        catch (IOException e){
            LOG.log(Level.SEVERE,e.getLocalizedMessage());
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @GetMapping("/search/{id}")
    public ResponseEntity<LNImage> getItem(int id){
        LOG.info("GET /image/light-novel/search/" + id);
        try{
            LNImage LN = this.LNLibrary.getLNID(id);
            if(LN != null){
                return new ResponseEntity<LNImage>(LN, HttpStatus.OK);
            }
            else{
                return new ResponseEntity<>(HttpStatus.NOT_FOUND);
            }
        }
        catch(IOException e){
            LOG.log(Level.SEVERE,e.getLocalizedMessage());
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
    
    @PutMapping("/update/all/{id}")
    public ResponseEntity<LNImage> putAll(@PathVariable int id, @RequestBody LNImage LN) {
        LOG.info("PUT /image/light-novel/update/all/" + id);
        try{
            LNImage check = this.LNLibrary.updateAll(LN);
            if (check == null){
                return new ResponseEntity<>(HttpStatus.NOT_FOUND);
            } else{
                return new ResponseEntity<LNImage>(check, HttpStatus.OK);
            }
        }
        catch (IOException e){
            LOG.log(Level.SEVERE,e.getLocalizedMessage());
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @PutMapping("/update/source/{id}")
    public ResponseEntity<LNImage> putSource(@PathVariable int id, @RequestBody String source) {
        LOG.info("PUT /image/light-novel/update/source/" + id);
        try{
            LNImage check = this.LNLibrary.updateSource(source, id);
            if (check == null){
                return new ResponseEntity<>(HttpStatus.NOT_FOUND);
            } else{
                return new ResponseEntity<LNImage>(check, HttpStatus.OK);
            }
        }
        catch (IOException e){
            LOG.log(Level.SEVERE,e.getLocalizedMessage());
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @PutMapping("/update/volume/{id}")
    public ResponseEntity<LNImage> putVolume(@PathVariable int id, @RequestBody Float volume) {
        LOG.info("PUT /image/light-novel/update/volume/" + id);
        try{
            LNImage check = this.LNLibrary.updateVolume(volume, id);
            if (check == null){
                return new ResponseEntity<>(HttpStatus.NOT_FOUND);
            } else{
                return new ResponseEntity<LNImage>(check, HttpStatus.OK);
            }
        }
        catch (IOException e){
            LOG.log(Level.SEVERE,e.getLocalizedMessage());
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @PutMapping("/update/author/{id}")
    public ResponseEntity<LNImage> putAuthor(@PathVariable int id, @RequestBody String author) {
        LOG.info("PUT /image/light-novel/update/author/" + id);
        try{
            LNImage check = this.LNLibrary.updateAuthor(author,id);
            if (check == null){
                return new ResponseEntity<>(HttpStatus.NOT_FOUND);
            } else{
                return new ResponseEntity<LNImage>(check, HttpStatus.OK);
            }
        }
        catch (IOException e){
            LOG.log(Level.SEVERE,e.getLocalizedMessage());
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @PutMapping("/update/author/{id}")
    public ResponseEntity<LNImage> putArtCount(@PathVariable int id, @RequestBody int artCount) {
        LOG.info("PUT /image/light-novel/update/artCount/" + id);
        try{
            LNImage check = this.LNLibrary.updateArtCount(artCount,id);
            if (check == null){
                return new ResponseEntity<>(HttpStatus.NOT_FOUND);
            } else{
                return new ResponseEntity<LNImage>(check, HttpStatus.OK);
            }
        }
        catch (IOException e){
            LOG.log(Level.SEVERE,e.getLocalizedMessage());
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @PutMapping("/update/author/{id}")
    public ResponseEntity<LNImage> putArtCount(@PathVariable int id, @RequestBody boolean color) {
        LOG.info("PUT /image/light-novel/update/color/" + id);
        try{
            LNImage check = this.LNLibrary.updateColor(color,id);
            if (check == null){
                return new ResponseEntity<>(HttpStatus.NOT_FOUND);
            } else{
                return new ResponseEntity<LNImage>(check, HttpStatus.OK);
            }
        }
        catch (IOException e){
            LOG.log(Level.SEVERE,e.getLocalizedMessage());
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }


    @DeleteMapping("/delete/{id}")
    public ResponseEntity<LNImage> deleteItem(@PathVariable int id) {
        LOG.info("DELETE /item/" + id);

        // Replace below with your implementation
        try {
            LNImage LN = this.LNLibrary.getLNID(id);
            if (this.LNLibrary.deleteLN(id))
                return new ResponseEntity<LNImage>(LN,HttpStatus.OK);
            else
                return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
        catch(IOException e) {
            LOG.log(Level.SEVERE,e.getLocalizedMessage());
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
}
