from typing import Optional, List
from models.vehicle import Vehicle
from core.bst_node import BSTNode

class Motorcycle:
    pass


class BinarySearchTree:
    """
    Implementación de un Árbol Binario de Búsqueda (BST) para gestionar vehículos.
    
    Un Árbol Binario de Búsqueda es una estructura de datos que mantiene los datos
    organizados de forma que permite búsquedas, inserciones y eliminaciones eficientes.
    En este caso, los vehículos se organizan por su placa (identificador único).
    
    Propiedades del BST:
    - Cada nodo tiene como máximo dos hijos (izquierdo y derecho)
    - Para cada nodo, todos los valores en el subárbol izquierdo son menores
    - Para cada nodo, todos los valores en el subárbol derecho son mayores
    - No hay duplicados (cada placa es única)
    """

    def __init__(self):
        """
        Inicializa un árbol binario de búsqueda vacío.
        
        Atributos:
            root (Optional[BSTNode]): La raíz del árbol. Inicialmente es None.
        """
        self.root: Optional[BSTNode] = None

    def insert(self, vehicle: Vehicle) -> bool:
        """
        Inserta un vehículo en el árbol binario de búsqueda.
        
        Si el árbol está vacío, el vehículo se convierte en la raíz.
        Si no, se llama a la función recursiva para encontrar la posición correcta.
        
        Complejidad de tiempo: O(log n) en promedio, O(n) en el peor caso
        
        Args:
            vehicle (Vehicle): El vehículo a insertar con su placa única.
        
        Returns:
            bool: True si el vehículo se insertó exitosamente.
                  False si ya existe un vehículo con la misma placa.
        
        Ejemplo:
            >>> bst = BinarySearchTree()
            >>> vehicle = Vehicle(plate="ABC-123", brand="Toyota", ...)
            >>> bst.insert(vehicle)
            True
        """
        if self.root is None:
            self.root = BSTNode(vehicle)
            return True
        return self._insert_recursive(self.root, vehicle)

    def _insert_recursive(self, node: BSTNode, vehicle: Vehicle) -> bool:
        """
        Función auxiliar recursiva para insertar un vehículo en el árbol.
        
        Compara la placa del vehículo con la del nodo actual:
        - Si es menor, intenta insertar en el subárbol izquierdo
        - Si es mayor, intenta insertar en el subárbol derecho
        - Si es igual, retorna False (placa duplicada)
        
        Args:
            node (BSTNode): El nodo actual donde se está evaluando la inserción.
            vehicle (Vehicle): El vehículo a insertar.
        
        Returns:
            bool: True si se insertó, False si la placa ya existe.
        """
        if vehicle.plate < node.vehicle.plate:
            # La placa es menor, va al lado izquierdo
            if node.left is None:
                node.left = BSTNode(vehicle)
                return True
            return self._insert_recursive(node.left, vehicle)
        elif vehicle.plate > node.vehicle.plate:
            # La placa es mayor, va al lado derecho
            if node.right is None:
                node.right = BSTNode(vehicle)
                return True
            return self._insert_recursive(node.right, vehicle)
        else:
            # La placa ya existe en el árbol
            return False

    def search(self, plate: str) -> Optional[Vehicle]:
        """
        Busca un vehículo por su placa en el árbol.
        
        Complejidad de tiempo: O(log n) en promedio, O(n) en el peor caso
        
        Args:
            plate (str): La placa del vehículo a buscar.
        
        Returns:
            Optional[Vehicle]: El vehículo si se encuentra, None si no existe.
        
        Ejemplo:
            >>> vehicle = bst.search("ABC-123")
            >>> if vehicle:
            ...     print(f"Encontrado: {vehicle.brand} {vehicle.model}")
        """
        node = self._search_recursive(self.root, plate)
        return node.vehicle if node else None

    def _search_recursive(self, node: Optional[BSTNode], plate: str) -> Optional[BSTNode]:
        """
        Función auxiliar recursiva para buscar un vehículo por placa.
        
        Navega por el árbol comparando la placa buscada con la del nodo actual:
        - Si es menor, busca en el subárbol izquierdo
        - Si es mayor, busca en el subárbol derecho
        - Si es igual, retorna el nodo encontrado
        
        Args:
            node (Optional[BSTNode]): El nodo actual en la búsqueda.
            plate (str): La placa a buscar.
        
        Returns:
            Optional[BSTNode]: El nodo con la placa, o None si no existe.
        """
        if node is None:
            return None

        if plate < node.vehicle.plate:
            # Buscar en el subárbol izquierdo
            return self._search_recursive(node.left, plate)
        elif plate > node.vehicle.plate:
            # Buscar en el subárbol derecho
            return self._search_recursive(node.right, plate)
        else:
            # Placa encontrada
            return node

    def delete(self, plate: str) -> bool:
        """
        Elimina un vehículo del árbol por su placa.
        
        Maneja tres casos:
        1. Nodo sin hijos (hoja): Se elimina directamente
        2. Nodo con un hijo: Se reemplaza por su hijo
        3. Nodo con dos hijos: Se reemplaza por el sucesor inorden (mínimo del subárbol derecho)
        
        Complejidad de tiempo: O(log n) en promedio, O(n) en el peor caso
        
        Args:
            plate (str): La placa del vehículo a eliminar.
        
        Returns:
            bool: True si se eliminó exitosamente, False si no se encontró.
        
        Ejemplo:
            >>> bst.delete("ABC-123")
            True
        """
        self.root, deleted = self._delete_recursive(self.root, plate)
        return deleted

    def _delete_recursive(self, node: Optional[BSTNode], plate: str) -> tuple[Optional[BSTNode], bool]:
        """
        Función auxiliar recursiva para eliminar un vehículo del árbol.
        
        Proceso:
        1. Navega hasta encontrar el nodo con la placa
        2. Maneja los tres casos de eliminación
        3. Retorna el árbol modificado y un booleano indicando si se eliminó
        
        Args:
            node (Optional[BSTNode]): El nodo actual en la búsqueda.
            plate (str): La placa del vehículo a eliminar.
        
        Returns:
            tuple[Optional[BSTNode], bool]: El árbol actualizado y si se eliminó.
        """
        if node is None:
            return None, False

        if plate < node.vehicle.plate:
            # El nodo a eliminar está en el subárbol izquierdo
            node.left, deleted = self._delete_recursive(node.left, plate)
            return node, deleted
        elif plate > node.vehicle.plate:
            # El nodo a eliminar está en el subárbol derecho
            node.right, deleted = self._delete_recursive(node.right, plate)
            return node, deleted
        else:
            # Nodo a eliminar encontrado
            
            # Caso 1: Nodo sin hijos (hoja)
            if node.left is None and node.right is None:
                return None, True
            
            # Caso 2: Nodo con solo hijo derecho
            if node.left is None:
                return node.right, True
            
            # Caso 2: Nodo con solo hijo izquierdo
            if node.right is None:
                return node.left, True
            
            # Caso 3: Nodo con dos hijos
            # Encuentra el sucesor inorden (el mínimo del subárbol derecho)
            min_node = self._find_min(node.right)
            # Reemplaza el vehículo del nodo actual con el del sucesor
            node.vehicle = min_node.vehicle
            # Elimina el sucesor del subárbol derecho
            node.right, _ = self._delete_recursive(node.right, min_node.vehicle.plate)
            return node, True

    def _find_min(self, node: BSTNode) -> BSTNode:
        """
        Encuentra el nodo con el valor mínimo en un subárbol.
        
        El nodo mínimo siempre está en el extremo izquierdo del árbol.
        Se usa para encontrar el sucesor inorden en la eliminación de nodos.
        
        Complejidad de tiempo: O(log n) en promedio, O(n) en el peor caso
        
        Args:
            node (BSTNode): La raíz del subárbol donde buscar.
        
        Returns:
            BSTNode: El nodo con la placa mínima.
        
        Ejemplo:
            >>> min_vehicle = bst._find_min(bst.root)
            >>> print(min_vehicle.vehicle.plate)
        """
        current = node
        # Continúa bajando por la izquierda hasta encontrar el nodo sin hijo izquierdo
        while current.left is not None:
            current = current.left
        return current

    def update(self, plate: str, updated_vehicle: Vehicle) -> bool:
        """
        Actualiza la información de un vehículo existente.
        
        Busca el vehículo por placa y actualiza todos sus campos excepto la placa
        (ya que la placa es la clave del árbol y no puede cambiar).
        
        Complejidad de tiempo: O(log n) en promedio, O(n) en el peor caso
        
        Args:
            plate (str): La placa del vehículo a actualizar.
            updated_vehicle (Vehicle): El vehículo con los nuevos datos.
        
        Returns:
            bool: True si se actualizó, False si el vehículo no existe.
        
        Ejemplo:
            >>> updated = Vehicle(plate="ABC-123", brand="Toyota", color="Blanco", ...)
            >>> bst.update("ABC-123", updated)
            True
        """
        node = self._search_recursive(self.root, plate)
        if node is None:
            return False
        
        # Actualiza todos los campos excepto la placa
        node.vehicle.brand = updated_vehicle.brand
        node.vehicle.color = updated_vehicle.color
        node.vehicle.model = updated_vehicle.model
        node.vehicle.price = updated_vehicle.price
        return True

    def inorder(self) -> List[Vehicle]:
        """
        Recorre el árbol en orden inorden (izquierda -> raíz -> derecha).
        
        Este recorrido devuelve los vehículos ordenados por placa de forma ascendente.
        Es el recorrido más útil para obtener datos ordenados.
        
        Complejidad de tiempo: O(n) - visita cada nodo una vez
        Complejidad de espacio: O(h) - donde h es la altura del árbol (pila de recursión)
        
        Returns:
            List[Vehicle]: Lista de vehículos ordenados por placa.
        
        Ejemplo:
            >>> vehicles = bst.inorder()
            >>> for v in vehicles:
            ...     print(f"{v.plate}: {v.brand} {v.model}")
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: Optional[BSTNode], result: List[Vehicle]) -> None:
        """
        Función auxiliar recursiva para el recorrido inorden.
        
        Orden: Izquierda -> Nodo Actual -> Derecha
        
        Esto garantiza que los vehículos se procesen en orden ascendente de placa.
        
        Args:
            node (Optional[BSTNode]): El nodo actual en el recorrido.
            result (List[Vehicle]): Lista donde se acumulan los vehículos.
        """
        if node is not None:
            # Procesa el subárbol izquierdo
            self._inorder_recursive(node.left, result)
            # Procesa el nodo actual
            result.append(node.vehicle)
            # Procesa el subárbol derecho
            self._inorder_recursive(node.right, result)

    def preorder(self) -> List[Vehicle]:
        """
        Recorre el árbol en orden preorden (raíz -> izquierda -> derecha).
        
        Este recorrido procesa el nodo antes que sus subárboles.
        Es útil para crear una copia del árbol o para serialización.
        
        Complejidad de tiempo: O(n) - visita cada nodo una vez
        Complejidad de espacio: O(h) - donde h es la altura del árbol
        
        Returns:
            List[Vehicle]: Lista de vehículos en orden preorden.
        
        Ejemplo:
            >>> vehicles = bst.preorder()
            >>> for v in vehicles:
            ...     print(v.plate)
        """
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node: Optional[BSTNode], result: List[Vehicle]) -> None:
        """
        Función auxiliar recursiva para el recorrido preorden.
        
        Orden: Nodo Actual -> Izquierda -> Derecha
        
        Args:
            node (Optional[BSTNode]): El nodo actual en el recorrido.
            result (List[Vehicle]): Lista donde se acumulan los vehículos.
        """
        if node is not None:
            # Procesa el nodo actual primero
            result.append(node.vehicle)
            # Procesa el subárbol izquierdo
            self._preorder_recursive(node.left, result)
            # Procesa el subárbol derecho
            self._preorder_recursive(node.right, result)

    def postorder(self) -> List[Vehicle]:
        """
        Recorre el árbol en orden postorden (izquierda -> derecha -> raíz).
        
        Este recorrido procesa el nodo después que sus subárboles.
        Es útil para eliminar un árbol o para operaciones que requieren procesar
        los hijos antes que el padre.
        
        Complejidad de tiempo: O(n) - visita cada nodo una vez
        Complejidad de espacio: O(h) - donde h es la altura del árbol
        
        Returns:
            List[Vehicle]: Lista de vehículos en orden postorden.
        
        Ejemplo:
            >>> vehicles = bst.postorder()
            >>> for v in vehicles:
            ...     print(v.plate)
        """
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node: Optional[BSTNode], result: List[Vehicle]) -> None:
        """
        Función auxiliar recursiva para el recorrido postorden.
        
        Orden: Izquierda -> Derecha -> Nodo Actual
        
        Args:
            node (Optional[BSTNode]): El nodo actual en el recorrido.
            result (List[Vehicle]): Lista donde se acumulan los vehículos.
        """
        if node is not None:
            # Procesa el subárbol izquierdo
            self._postorder_recursive(node.left, result)
            # Procesa el subárbol derecho
            self._postorder_recursive(node.right, result)
            # Procesa el nodo actual al final
            result.append(node.vehicle)

    def get_all(self) -> List[Vehicle]:
        """
        Obtiene todos los vehículos del árbol ordenados por placa.
        
        Es un método de conveniencia que llama a inorder() para obtener
        todos los vehículos en orden ascendente.
        
        Complejidad de tiempo: O(n)
        
        Returns:
            List[Vehicle]: Lista de todos los vehículos ordenados por placa.
        
        Ejemplo:
            >>> all_vehicles = bst.get_all()
            >>> print(f"Total de vehículos: {len(all_vehicles)}")
        """
        return self.inorder()
