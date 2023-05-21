package si.uni_lj.fe.mis.predatordetection.data

import kotlinx.coroutines.flow.MutableSharedFlow
import si.uni_lj.fe.mis.predatordetection.util.Resource

interface ClassificationReceiveManager {

    val data: MutableSharedFlow<Resource<ClassificationResult>>

    fun reconnect()

    fun disconnect()

    fun startReceiving()

    fun closeConnection()

}