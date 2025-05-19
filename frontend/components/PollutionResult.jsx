// components/PollutionResult.jsx
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { SEVERITY_COLORS } from '../constants/config';

const PollutionResult = ({ data }) => {
    const color = SEVERITY_COLORS[data.pollution_level] || 'gray';

    return (
        <View style={[styles.card, { borderColor: color }]}>
            <Text style={styles.title}>Analysis Result:</Text>
            <Text style={[styles.severity, { color }]}>
                {data.pollution_level}
            </Text>
            <Text style={styles.confidence}>
                Confidence: {(data.confidence * 100).toFixed(1)}%
            </Text>
            {data.received_image && (
                <Text style={styles.note}>Image processed successfully</Text>
            )}
        </View>
    );
};

const styles = StyleSheet.create({
    card: {
        marginTop: 20,
        padding: 15,
        borderRadius: 8,
        borderWidth: 2,
        backgroundColor: 'white',
    },
    title: {
        fontSize: 18,
        marginBottom: 10,
        fontWeight: 'bold',
    },
    severity: {
        fontSize: 24,
        fontWeight: 'bold',
        marginBottom: 8,
    },
    confidence: {
        fontSize: 16,
        color: '#666',
    },
    note: {
        marginTop: 10,
        fontSize: 12,
        color: '#999',
    },
});

export default PollutionResult;