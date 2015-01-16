#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace cv;
using namespace std;

int main( int argc, char** argv )
{
    Mat src, src_gray;
    Rect roi;
    int thresh = 105;
    int max_thresh = 255;
    RNG rng(12345);


    /// Load source image and convert it to gray
    src = imread(argv[1]);

    // Crop top and bottom parts
    int o1 = src.rows / 12;
    int o2 = src.rows - (src.rows / 9);
    roi = Rect(0, o1, src.cols, o2-o1);

    /// Convert image to gray and blur it
    cvtColor( src, src_gray, CV_BGR2GRAY );
    blur( src_gray, src_gray, Size(3,3) );

    Mat threshold_output;
    vector<vector<Point> > contours;
    vector<Vec4i> hierarchy;

    /// Detect edges using Threshold
    threshold( src_gray, threshold_output, thresh, 255, THRESH_BINARY );
    /// Find contours
    findContours( threshold_output(roi).clone(), contours, hierarchy, CV_RETR_LIST, CV_CHAIN_APPROX_SIMPLE, Point(0, 0) );

    /// Approximate contours to polygons + get bounding rects and circles
    vector<vector<Point> > contours_poly( contours.size() );
    vector<Rect> boundRect( contours.size() );
    vector<Point2f>center( contours.size() );
    vector<float>radius( contours.size() );

    for( int i = 0; i < contours.size(); i++ ) {
        approxPolyDP( Mat(contours[i]), contours_poly[i], 3, true );
        boundRect[i] = boundingRect( Mat(contours_poly[i]) );
        minEnclosingCircle( (Mat)contours_poly[i], center[i], radius[i] );
        // add back crop offset
        center[i].y += o1;
    }

    // Draw polygonal contour + bonding rects + circles
    // Output them in a Pythonic list way
    // TODO: Port this code to Python :)
    Mat drawing = Mat::zeros( threshold_output.size(), CV_8UC3 );
    std::cout << "[\n";
    for( int i = 0; i< contours.size(); i++ )
    {
        Vec3b color = src.at<Vec3b>((int)center[i].y, (int)center[i].x);
        Scalar col = Scalar(color[0], color[1], color[2]);
        circle(drawing, center[i], 1, col, 2, 8, 0 );
        std::cout << "\t[" << col << "," << (int)center[i].x << ", " << (int)center[i].y << "],\n";
    }
    std::cout << "\n]" << "\n";

    // Just for seeing
    imwrite("contours.png", drawing);

    return(0);
}
