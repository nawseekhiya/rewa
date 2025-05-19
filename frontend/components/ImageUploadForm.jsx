import React, { useState } from 'react';
import { TouchableOpacity, Text, Alert, ActivityIndicator, StyleSheet, Platform } from 'react-native';
import * as ImagePicker from 'expo-image-picker';
import { API_URL } from '../constants/config';

export default function ImageUploadForm({ onPrediction }) {
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState('');

    const handleUpload = async () => {
        try {
            // Request permissions (mobile only)
            if (Platform.OS !== 'web') {
                const { status } = await ImagePicker.requestMediaLibraryPermissionsAsync();
                if (status !== 'granted') return;
            }

            // Launch image picker
            const result = await ImagePicker.launchImageLibraryAsync({
                mediaTypes: ImagePicker.MediaTypeOptions.Images,
                quality: 0.8,
                allowsEditing: true,
                aspect: [4, 3],
            });

            if (result.canceled) return;

            setIsLoading(true);
            setError('');
            const image = result.assets[0];

            // Web-specific handling
            if (Platform.OS === 'web') {
                const response = await fetch(image.uri);
                const blob = await response.blob();
                const file = new File([blob], `water_${Date.now()}.jpg`, { type: blob.type });

                const formData = new FormData();
                formData.append('image', file);
                
                const uploadResponse = await fetch(API_URL, {
                    method: 'POST',
                    body: formData,
                });
                
                const data = await uploadResponse.json();
                onPrediction(data);
                return;
            }

            // Mobile handling
            const ext = image.uri.split('.').pop();
            const file = {
                uri: image.uri,
                name: `water_${Date.now()}.${ext}`,
                type: `image/${ext}`,
            };

            const formData = new FormData();
            formData.append('image', file);

            const response = await fetch(API_URL, {
                method: 'POST',
                body: formData,
                headers: { 'Accept': 'application/json' },
            });

            if (!response.ok) throw new Error('Upload failed');
            
            const data = await response.json();
            onPrediction(data);

        } catch (error) {
            setError(error.message);
            Alert.alert('Error', error.message);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <>
            <TouchableOpacity
                style={[styles.button, isLoading && styles.disabled]}
                onPress={handleUpload}
                disabled={isLoading}
            >
                {isLoading ? (
                    <ActivityIndicator color="#fff" />
                ) : (
                    <Text style={styles.buttonText}>Analyze Water Quality</Text>
                )}
            </TouchableOpacity>
            
            {error && <Text style={styles.errorText}>{error}</Text>}
        </>
    );
}

const styles = StyleSheet.create({
    button: {
        backgroundColor: '#2196F3',
        padding: 15,
        borderRadius: 8,
        alignItems: 'center',
        marginVertical: 20,
        minWidth: 240,
    },
    buttonText: {
        color: 'white',
        fontSize: 16,
        fontWeight: '600',
    },
    disabled: {
        opacity: 0.6,
    },
    errorText: {
        color: '#ff4444',
        marginTop: 10,
        fontSize: 14,
        textAlign: 'center',
        maxWidth: 300,
    },
});