"""
Pre-initialization for FloorPlan5 task.
FloorPlan5: bread and tomato don't need to be moved
egg needs to be taken out of sink and placed on
countertop
- move the spoon out of the way and put lettuce at the position of spoon
"""


class SceneInitializer:
    def __init__(self) -> None:
        pass

    def preinit(self, event, controller):
        """Pre-initialize the environment for the task.

        Args:
            event: env.event object
            controller: ai2thor.controller object

        Returns:
            event: env.event object
        """

        # initialization function - autogenerated

        event = controller.step(
            action="PlaceObjectAtPoint",
            objectId="Bread|-01.15|+00.98|-00.19",
            position={
                "x": -1.1480002403259277,
                "y": 0.9816430807113647,
                "z": -0.19300001859664917,
            },
        )

        event = controller.step(
            action="PlaceObjectAtPoint",
            objectId="Tomato|-01.15|+00.96|-01.66",
            position={
                "x": -1.147734522819519,
                "y": 0.9576706290245056,
                "z": -1.6584954261779785,
            },
        )

        event = controller.step(
            action="PlaceObjectAtPoint",
            objectId="Egg|-00.15|+00.78|-01.94",
            position={
                "x": -0.87480002403259277,
                "y": 0.9816430807113647,
                "z": -0.2500001859664917,
            },
        )

        event = controller.step(
            action="PlaceObjectAtPoint",
            objectId="Spoon|-00.06|+00.90|+00.10",
            position={
                "x": 0.6180002403259277,
                "y": 0.9816430807113647,
                "z": 0.1300001859664917,
            },
        )

        event = controller.step(
            action="PlaceObjectAtPoint",
            objectId="Lettuce|-00.25|+00.81|-01.92",
            position={
                "x": -0.062007419764995575,
                "y": 0.9002927541732788,
                "z": 0.10399211943149567,
            },
        )

        return event
