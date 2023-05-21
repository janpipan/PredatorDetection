package si.uni_lj.fe.mis.predatordetection

import android.app.Application
import android.app.NotificationChannel
import android.app.NotificationManager
import android.content.Context
import android.os.Build
import dagger.hilt.android.HiltAndroidApp
import si.uni_lj.fe.mis.predatordetection.notifications.ClassificationNotificationService

@HiltAndroidApp
class BLEApplication : Application(){

}