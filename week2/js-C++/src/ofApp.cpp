#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){
    segments = 400;
    mouseX =20;
    mouseY =20;
    osc1 = maxiOsc();
    osc2 = maxiOsc();
    osc3 = maxiOsc();
    osc4 = maxiOsc();
    osc5 = maxiOsc();
    
    
    ofSoundStreamSettings settings;
    settings.numOutputChannels = 2;
    settings.sampleRate = 44100;
    settings.bufferSize = 512;
    settings.numBuffers = 4;
    settings.setOutListener(this);
    soundStream.setup(settings);
}

//--------------------------------------------------------------
void ofApp::update(){

}

//--------------------------------------------------------------
void ofApp::draw(){
    double spacing = TWO_PI / segments;
    int radius = 180;
    ofBackground(ofColor::black);
    waveform.clear();
    for (int i = 0; i < 1*segments; i++)
    {
        double x;
         double y;

        x = radius*cos(spacing*i/2*(mouseX*2))*3;
        y = radius*sin(spacing*i/2*(mouseY*2))*3;
     
        ofSetColor(0x7f, 0, 0xff);
        waveform.addVertex(x+radius+60, y+radius+60);
    }
    waveform.draw();
}

//--------------------------------------------------------------
void ofApp::audioOut(ofSoundBuffer &outBuffer) {
    double averageOutput = 0;
    
    for (int i=0; i<512; i++) {
        double sig1 = osc1.sinewave(440);
        double sig2 = osc2.coswave(263.6);
        double sig3 = osc3.sinewave(298);
        double sig4 = osc4.coswave(352);
        double sig5 = osc5.sinewave(256);
        int CurrentCount;
        int CurrentCount2;
          
        int freq = 10;
              
                 
        double out =  sig1 + sig2;
        double out2 = sig3 + sig4;
        double out3 = sig5;
        
        outBuffer.getSample(i, 0) = out;
        outBuffer.getSample(i, 1) = out2;
    }
}
//--------------------------------------------------------------
void ofApp::keyPressed(int key){

}

//--------------------------------------------------------------
void ofApp::keyReleased(int key){

}

//--------------------------------------------------------------
void ofApp::mouseMoved(int x, int y ){
    mouseY = y;
    mouseX = x;
}

//--------------------------------------------------------------
void ofApp::mouseDragged(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mousePressed(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mouseReleased(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mouseEntered(int x, int y){

}

//--------------------------------------------------------------
void ofApp::mouseExited(int x, int y){

}

//--------------------------------------------------------------
void ofApp::windowResized(int w, int h){

}

//--------------------------------------------------------------
void ofApp::gotMessage(ofMessage msg){

}

//--------------------------------------------------------------
void ofApp::dragEvent(ofDragInfo dragInfo){

}
