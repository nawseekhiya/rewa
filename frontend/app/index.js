// app/App.js
import { View, Text, ScrollView } from 'react-native';
import { useState } from 'react';
import ImageUploadForm from '../components/ImageUploadForm';
import PollutionResult from '../components/PollutionResult';
import { SEVERITY_COLORS } from '../constants/config';

export default function App() {
    const [prediction, setPrediction] = useState(null);
    const [error, setError] = useState('');

    return (
        <ScrollView contentContainerStyle={{ flexGrow: 1, padding: 20 }}>
            <Text style={{ fontSize: 24, marginBottom: 20, textAlign: 'center' }}>
                AI Water Pollution Detector
            </Text>
            
            <ImageUploadForm 
                onPrediction={(data) => {
                    setPrediction(data);
                    setError('');
                }}
            />
            
            {error && (
                <Text style={{ color: 'red', marginTop: 20, textAlign: 'center' }}>
                    {error}
                </Text>
            )}
            
            {prediction && (
                <PollutionResult data={prediction} />
            )}
        </ScrollView>
    );
}