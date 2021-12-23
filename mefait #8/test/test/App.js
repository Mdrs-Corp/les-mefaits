import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

export default function App() {
    return ( 
    <View style = { styles.container }>
    <Text> Alexis Derail je le gnock </Text></View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex:1,
        backgroundColor:'#6174ee',
        alignItems:'center',
        justifyContent: 'center',
        fontFamily: 'Consolas'
    },
});