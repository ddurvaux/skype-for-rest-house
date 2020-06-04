//  IR remote sender 
//
//	v 1.0 - 01/06/2020 - initial release (Marc Durvaux)
//
//  
//
//

// design control
test_fit   = 0 ;	// set to one for test fit
top_bottom = 1 ;	// 0 = bottom only, 1 = top only
ear_mouse  = 0 ;    // set to one to add ear mouse to avoid warping during 3D printing

// parameters
$fn = 100 ;
tol        = 0.50 ;	    // 
wall_th    = 2.00 ;     // side wall thickness

mouse_ear_h =  0.80 ;   // mouse ears to avoid warping
mouse_ear_r = 10.00 ;    

// bottom part
in_x = 72.00 ;
in_y = 55.00 ;
in_z = 33.00 ;

// USB connector
usb_w = 12.00 + 4 * tol ;
usb_h = 11.00 + 4 * tol ;
usb_y = usb_w - 9.40 + 2 * tol ;
usb_z =  4.00 - 2 * tol ;

// window
win_w = 35.00 ;
win_h = 14.00 ;

// cover
top_h = 10.00 ;

// fixation screw
out_d =  2.20 ;
in_d  =  1.10 ;


// calculated dimensions
out_x = in_x + 2 * wall_th;
out_y = in_y + 2 * wall_th;
out_z = in_z + 1 * wall_th;


// create device
if (test_fit == 1) {
	// test fit
	bottom_case();
    translate([0, 0 , out_z + wall_th])
        rotate([ 0, 180, 0])
            cover();
} else {
	if (top_bottom < 1) {
		bottom_case(); 
	} else {
        cover();
	}
}



module cover() {
    difference() {
        union() {
            translate([-out_x/2, -out_y/2, 0]) 
                cube( size=[out_x, out_y, wall_th] ) ;      
            translate([-in_x/2 + tol, -in_y/2 + win_h + tol, 0])
                cube( size=[wall_th, in_y - 2 * win_h, top_h] ) ; 
            translate([in_x/2 - wall_th - tol, -in_y/2 + tol, 0])
                cube( size=[wall_th, in_y - 2 * tol, top_h] ) ; 
        }
        
        union() {
        translate([-out_x, 0 , top_h /2]) 
            rotate([ 0, 90, 0])
                cylinder( h = 2 * out_x, d = in_d) ;
        
        x_cut = win_w + 2 * wall_th ;    
        translate([-out_x/2 - wall_th, out_y/2 - win_h + tol, -wall_th]) 
            cube( size=[x_cut, win_h, 3 * wall_th] ) ;     
        translate([-out_x/2 - wall_th, -out_y/2 -tol , -wall_th]) 
            cube( size=[x_cut, win_h, 3 * wall_th] ) ;     
        } 
    }
}


module bottom_case() {
    difference() {
        translate([-out_x/2, -out_y/2, 0]) 
            cube( size=[out_x, out_y, out_z] ) ;        
        
        union() {
            translate([-in_x/2, -in_y/2, wall_th]) 
                cube( size=[in_x, in_y, out_z] ) ; 
            
            translate([-out_x/2 - wall_th, usb_y , usb_z + wall_th]) 
                cube( size=[4 * wall_th , usb_w, usb_h] ) ; 
            
            translate([in_x/2 - win_w, -out_y , out_z - win_h]) 
                cube( size=[win_w , 2 * out_y, win_h + tol] ) ; 
            
            translate([-out_x, 0 , out_z + wall_th - top_h /2]) 
                rotate([ 0, 90, 0])
                    cylinder( h = 2 * out_x, d = out_d) ;
             
        }   
    }
}


module add_ear_mouse( x, y) {
    if (ear_mouse == 1) {   // add mouse ears to avoid warping
        translate([-x, -y, 0])
            cylinder(h=mouse_ear_h, r=mouse_ear_r) ;   
        translate([-x, y, 0])
            cylinder(h=mouse_ear_h, r=mouse_ear_r) ;
        translate([x, -y, 0])
            cylinder(h=mouse_ear_h, r=mouse_ear_r) ;
        translate([x, y, 0])
            cylinder(h=mouse_ear_h, r=mouse_ear_r) ;  
    }  
}

