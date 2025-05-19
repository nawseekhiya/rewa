import React from 'react';
import { TouchableOpacity, Text, Alert } from 'react-native';
import * as ImagePicker from 'expo-image-picker';

export default function ImageUploadForm() {
  const handleUpload = async () => {
    const permission = await ImagePicker.requestMediaLibraryPermissionsAsync();
    
    if (!permission.granted) {
      Alert.alert('Permission required!');
      return;
    }

    const result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.Images,
      quality: 0.8,
    });

    if (!result.canceled) {
      // Handle image upload to Flask API here
      const image = result.assets[0];
      console.log('Selected image:', image.uri);
    }
  };

  return (
    <TouchableOpacity
      onPress={handleUpload}
      style={{ 
        backgroundColor: '#2196F3',
        padding: 15,
        borderRadius: 8,
        alignItems: 'center'
      }}
    >
      <Text style={{ color: 'white', fontSize: 18 }}>
        Upload Water Photo
      </Text>
    </TouchableOpacity>
  );
}