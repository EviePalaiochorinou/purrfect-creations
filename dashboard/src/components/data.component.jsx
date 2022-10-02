
const Data = ({name, metric}) => (
    <div className='item-info'>
        <h3 className='item-title'>{name}</h3>
        <p className='item-metrics'>{metric}</p>
    </div>
);

export default Data;