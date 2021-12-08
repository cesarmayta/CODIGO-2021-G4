import { CulqiProvider, Culqi } from 'react-culqi';

const App = () => {
  return (
    <CulqiProvider
      publicKey="pk_test_ffb6fcd84ee589bd"
      onToken={token => {
        /* handle a successful token */
        console.log("pago correcto");
      }}
      onError={error => {
        /* handle an error during tokenization */
        console.log("hubo un error en el pago");
      }}
    >
      <Culqi>
        {({ openCulqi, setAmount, amount }) => {
          return <button onClick={openCulqi}>Open Culqi</button>;
        }}
      </Culqi>
    </CulqiProvider>
  );
};

export default App;
