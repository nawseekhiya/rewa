import { View, Text } from 'react-native';
import ImageUploadForm from '../components/ImageUploadForm';

export default function App() {
  return (
    <View style={{ flex: 1, padding: 20 }}>
      <Text style={{ fontSize: 24, marginBottom: 20 }}>
        Water Pollution Detector
      </Text>
      <ImageUploadForm />
    </View>
  );
}