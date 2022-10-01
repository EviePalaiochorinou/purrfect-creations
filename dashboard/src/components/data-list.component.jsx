import Data from './data.component';

const DataList = ({orderData}) => {
    let list = []
    for (const [name, metric] of Object.entries(orderData)){
        list.push(<Data name={name} metric={metric}></Data>)
    }
    <div className='data-list'>
        {list}
    </div>
}

export default DataList;