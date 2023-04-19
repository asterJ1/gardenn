class IntBytes {                   
    byte firstByte(int num) {      
        num = (num >> 24) & 0xFF;  
        return (byte) num;         
    }                              
    byte secondByte(int num) {     
        num = (num >> 16) & 0xFF;  
        return (byte) num;         
    }                              
    byte thirdByte(int num) {      
        num = (num >> 8) & 0xFF;   
        return (byte) num;         
    }                              
    byte forthByte(int num) {      
        num = num & 0xFF;          
        return (byte) num;         
    }                              
}                     