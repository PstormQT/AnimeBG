package PstormQT.AnimeBG.controller;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;

import PstormQT.AnimeBG.controller.LightNovelImageController;
import PstormQT.AnimeBG.model.Image;
/**
 * Handles the REST API request for anything related directly at the cupboard
 * {@literal @}RestController Spring annotation identifies this class as a REST API
 * method handler to the Spring framework
 * 
 * @author: all member
 */

@RestController
@RequestMapping("/image/light-novel")
public class LightNovelImageController  {
    private static final Logger LOG = Logger.getLogger(LightNovelImageController.class.getName());
    

}
