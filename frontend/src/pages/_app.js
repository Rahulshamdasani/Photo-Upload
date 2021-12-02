import Head from 'next/head'

const App = ({ Component, pageProps }) => {
  return (
    <div>
      <Head>
        <title>Image Upload</title>
        <meta name="description" content=" Image upload app test" />
         <link 
         href='https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css' 
         rel='stylesheet' 
         integrity='sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3'
         crossOrigin='anonymous'
          />
      </Head>
      <div className="container">
        <Component {...pageProps} />
      </div>
    </div>
  )
}

export default App;