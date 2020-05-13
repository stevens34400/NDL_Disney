# NDL Disney

## Image Processing
Image processing team primarily focused on the detection of characters in movies and their removal from their respective frames. Colors present in background of each frame in tandem with other features of tool was used to provide insight to movie scene. Algorithm utilized k-means clustering to identify a set of colors from a scene. As colors of characters rarely change throughout a movie, palette of colors for character was used to detect and place a contour around characters. Bounding box was formed from contour and a crop feature was used to remove character from scene.

### Original Frame
<p align="center">
  <img width="800" height="400" src="https://github.com/stevens34400/NDL_Disney/blob/master/images/original_frame.PNG">
</p>

### Character Detection and Contour
<p align="center">
  <img width="800" height="400" src="https://github.com/stevens34400/NDL_Disney/blob/master/images/contour_frame.PNG">
</p>
Placed contour lines around objects that had similar palette of colors to character.

### Bounding Box and Character Deletion
<p align="center">
  <img width="800" height="400" src="https://github.com/stevens34400/NDL_Disney/blob/master/images/char_deletion.PNG">
</p>
Created bounding box from contour lines and cropped are in bounding box from scene. 
