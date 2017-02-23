var React = require('react');
var {AppRegistry, Text, StyleSheet, View} = require('react-native');
var json_data = require('./data.json');
var Swiper = require('react-native-swiper');

const styles = StyleSheet.create({
    wrapper: {
    },
    slide1: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#9DD6EB',
    },
    slide2: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#97CAE5',
    },
    slide3: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#92BBD9',
    },
    text: {
        color: '#fff',
        fontSize: 30,
        fontWeight: 'bold',
        maxWidth: 600,
    }
})

var Test = React.createClass({
    getInitialState: () => {
        return {
            index: 0
        }
    },

    getDefaultProps: () => {
        return {
            datas: [],
            amt: 0
        }
    },

    shuffle: function(array) {
        var currentIndex = array.length, temporaryValue, randomIndex;
        while (0 !== currentIndex) {
            randomIndex = Math.floor(Math.random() * currentIndex);
            currentIndex -= 1;
            temporaryValue = array[currentIndex];
            array[currentIndex] = array[randomIndex];
            array[randomIndex] = temporaryValue;
        }
        return array;
    },

    comp: function (data) {
        this.props.amt = 5;
        if(this.props.datas.length != 0) {
            this.props.datas = [];
        }
        for(var i = 0; i < data.datas.length; i++) {
            this.props.datas.push(data.datas[i]);
        }
    },

    componentWillMount: function () {
        var data = json_data;
        this.comp(data);
        this.props.datas = this.shuffle(this.props.datas);
    },

    render: function () {
        var rows = [];
        var astyles = [styles.slide1, styles.slide2, styles.slide3];

        function randomIntFromInterval(min,max) {
            return Math.floor(Math.random()*(max-min+1)+min);
        }

        for(var i = 0; i < this.props.datas.length; i++) {
            var k = (
                <View style = {astyles[randomIntFromInterval(0, astyles.length - 1)]} key = {i}>
                    <Text style = {styles.text}>{this.props.datas[i]}</Text>
                </View>
            );
            rows.push(k);
        }

        return (
            <Swiper style = {styles.wrapper} showsButtons = {true} showsPagination = {false}>
                {rows}
            </Swiper>
        )
    }
})

AppRegistry.registerComponent("iniTest", () => Test);
