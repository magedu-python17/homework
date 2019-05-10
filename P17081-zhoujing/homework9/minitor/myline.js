import React from 'react'
import echarts from 'echarts'
import ShowService from '../service/show'
import { inject } from '../utils'
import { observer } from 'mobx-react'
import 'echarts/lib/chart/bar'
import 'echarts/lib/component/tooltip'
import 'echarts/lib/component/title'

const service = new ShowService()

@inject({ service })

@observer
export default class Myline extends React.Component {
    constructor(props) {
        super(props)
        const { match: { params } } = props
        props.service.show(params.id)

    }
    values = (m) => {
        let arr=[]
        let i = 0
        for (let x in m) {
            if (x!='date'){
                var ret = { name:x, type:'line', data: m[x],smooth: true }
                arr[i] = ret
                i++
            }
                
        }
        
        return arr
    }
    componentDidUpdate(props) {
        var myChart = echarts.init(document.getElementById('main'));
        myChart.setOption({
            title: {
                text: this.props.service.sta.ip + '  ' + this.props.service.sta.hostname
            },
            tooltip: {
                trigger: 'axis'
            },
            legend: {
                data: Object.keys(this.props.service.sta.states)
            },
            grid: {
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            },
            toolbox: {
                feature: {
                    saveAsImage: {}
                }
            },
            xAxis: {
                type: 'category',
                boundaryGap: false,
                data: this.props.service.sta.states.date.map(x=>new Date(x).toLocaleString())
            },
            yAxis: {
                type: 'value'
            },
            series: this.values(this.props.service.sta.states)
        });
    }



    render() {
        if (this.props.service.state.ip) {
            return <div id='main' style={{ width: 1200, height: 1200 }}></div>
        }
        return <div id='main' style={{ width: 1200, height: 1200 }}></div>
    }

}