import Data from './data.component';

const DataList = ({orderData}) => {
    let list = []
    for (const [name, metric] of Object.entries(orderData)){
        // Ideally, we would have another component created conditionally to display tables of orders instead of a whole array or object.
        list.push(<Data key={name} name={name} metric={JSON.stringify(metric)}></Data>)
    }
    console.log(list)
    return <div className='data-list' key="id-list">
        {list}
    </div>
}

export default DataList;