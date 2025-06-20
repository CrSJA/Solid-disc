# Fundamentos Físicos del Simulador de Partículas

El sistema simula el comportamiento dinámico de partículas en interacción dentro de un espacio confinado, representando un modelo físicamente consistente de un gas ideal bidimensional. Cada disco actúa como una partícula que interactúa exclusivamente mediante **colisiones elásticas**, conservando dos principios fundamentales:

1. **Conservación del momento lineal**:  
    \begin{equation}
    \sum m_iv_i = constante
    \end{equation}
   La suma vectorial de los momentos se mantiene invariable antes y después de cada colisión, garantizando que el momento total del sistema se preserve.

2. **Conservación de energía cinética**:  
   \begin{equation}
   \sum \frac{1}{2}m_iv_i^2 = constante
   \end{equation}
   Todas las colisiones son perfectamente elásticas, sin pérdida de energía durante las interacciones.

En este estado, las propiedades totales del sistema se estabilizan mientras las partículas mantienen un movimiento constante y perpetuo, ilustrando comportamientos colectivos a partir de interacciones individuales básicas.

El modelo presenta ciertas limitaciones que deben considerarse en su interpretación:

* La dimensionalidad 2D altera las estadísticas de colisiones respecto a gases reales tridimensionales
* La escala reducida (decenas o cientos de partículas) dista significativamente del número de partículas en sistemas macroscópicos reales

Estas características hacen que el simulador sea especialmente adecuado para estudiar gases ideales clásicos, donde las únicas interacciones relevantes son colisiones instantáneas entre partículas.
