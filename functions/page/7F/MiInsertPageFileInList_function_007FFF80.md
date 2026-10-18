# MiInsertPageFileInList

- RVA: `0x007FFF80`–`0x0080042D` (길이 `1,197` bytes)
- VA: `0x00000001407FFF80`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D80E8`
- 디코드: `303`개 명령, `1,197/1,197` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **31**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0080000C` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00800025` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00800050` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00800058` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00800077` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x0080009F` → [MiMakePartitionActive](../../text/49/MiMakePartitionActive_function_004959B8.md) (function, `0x004959B8`)
- `0x008000BA` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x008000C2` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008000E3` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x00800112` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (function, `0x0040DD10`)
- `0x00800157` → [PsCreateSystemThreadEx](../9E/PsCreateSystemThreadEx_function_009ED120.md) (function, `0x009ED120`)
- `0x00800194` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x008001AD` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x008001C2` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008001DC` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0080020E` → [ObCloseHandle](../8A/ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)
- `0x0080021C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008002CF` → [MiIncreaseCommitLimits](../../text/68/MiIncreaseCommitLimits_function_0068CADC.md) (function, `0x0068CADC`)
- `0x00800312` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0080031A` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0080033B` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x00800351` → [MiNumberWsSwapPagefiles](../../text/2D/MiNumberWsSwapPagefiles_function_002DCFA4.md) (function, `0x002DCFA4`)
- `0x0080036A` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00800372` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00800393` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x008003A5` → [MiUpdatePageFileList](../../text/68/MiUpdatePageFileList_function_006803AC.md) (function, `0x006803AC`)
- `0x008003D5` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x008003DD` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008003FA` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x00800407` → [MiUpdateReserveClusterInfo](../../text/46/MiUpdateReserveClusterInfo_function_0046606C.md) (function, `0x0046606C`)
- `0x00800413` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)

### Direct callers
- [MiCreatePagingFile](MiCreatePagingFile_function_007FEFF4.md) at `0x007FF73E`
- [MmStoreRegister](../80/MmStoreRegister_function_0080E6D8.md) at `0x0080E8A6`
- [MiCreateSpecialPurposeMemoryPageFile](../80/MiCreateSpecialPurposeMemoryPageFile_function_0080F444.md) at `0x0080F4AF`

### Static image references
- `0x00800037` → RVA `0x00E30144` (`.data`; read)
- `0x00800142` → RVA `0x0047E5F0` (`MiModifiedPageWriter`; read)
- `0x00800177` → RVA `0x00FC6AC8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **28**
  - `0x0080000C` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00800025` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00800050` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00800058` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00800077` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
  - `0x0080009F` → [MiMakePartitionActive](../../text/49/MiMakePartitionActive_function_004959B8.md) (`PAGE` → `.text`)
  - `0x008000BA` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x008000C2` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008000E3` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
  - `0x00800112` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (`PAGE` → `.text`)
  - `0x008001AD` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x008001C2` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008001DC` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0080021C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008002CF` → [MiIncreaseCommitLimits](../../text/68/MiIncreaseCommitLimits_function_0068CADC.md) (`PAGE` → `.text`)
  - `0x00800312` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0080031A` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0080033B` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
  - `0x00800351` → [MiNumberWsSwapPagefiles](../../text/2D/MiNumberWsSwapPagefiles_function_002DCFA4.md) (`PAGE` → `.text`)
  - `0x0080036A` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00800372` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00800393` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
  - `0x008003A5` → [MiUpdatePageFileList](../../text/68/MiUpdatePageFileList_function_006803AC.md) (`PAGE` → `.text`)
  - `0x008003D5` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x008003DD` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008003FA` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
  - `0x00800407` → [MiUpdateReserveClusterInfo](../../text/46/MiUpdateReserveClusterInfo_function_0046606C.md) (`PAGE` → `.text`)
  - `0x00800413` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007FFF80  40 55                           push rbp
007FFF82  53                              push rbx
007FFF83  56                              push rsi
007FFF84  57                              push rdi
007FFF85  41 54                           push r12
007FFF87  41 56                           push r14
007FFF89  41 57                           push r15
007FFF8B  48 8B EC                        mov rbp, rsp
007FFF8E  48 81 EC 80 00 00 00            sub rsp, 0x80
007FFF95  8B 01                           mov eax, dword ptr [rcx]
007FFF97  0F 57 C0                        xorps xmm0, xmm0
007FFF9A  48 83 65 48 00                  and qword ptr [rbp + 0x48], 0
007FFF9F  41 BC 01 00 00 00               mov r12d, 1
007FFFA5  44 08 A1 AE 00 00 00            or byte ptr [rcx + 0xae], r12b
007FFFAC  45 33 C0                        xor r8d, r8d
007FFFAF  4C 8B F9                        mov r15, rcx
007FFFB2  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
007FFFB6  8B 41 04                        mov eax, dword ptr [rcx + 4]
007FFFB9  48 89 45 58                     mov qword ptr [rbp + 0x58], rax
007FFFBD  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
007FFFC1  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
007FFFC5  44 39 41 28                     cmp dword ptr [rcx + 0x28], r8d
007FFFC9  76 19                           jbe 0x1407fffe4
007FFFCB  48 8B 41 20                     mov rax, qword ptr [rcx + 0x20]
007FFFCF  4A 8B 14 C0                     mov rdx, qword ptr [rax + r8*8]
007FFFD3  B8 11 77 88 99                  mov eax, 0x99887711
007FFFD8  45 03 C4                        add r8d, r12d
007FFFDB  48 89 02                        mov qword ptr [rdx], rax
007FFFDE  44 3B 41 28                     cmp r8d, dword ptr [rcx + 0x28]
007FFFE2  72 E7                           jb 0x1407fffcb
007FFFE4  4C 8B B1 D8 00 00 00            mov r14, qword ptr [rcx + 0xd8]
007FFFEB  45 33 C0                        xor r8d, r8d
007FFFEE  65 48 8B 34 25 88 01 00 00      mov rsi, qword ptr gs:[0x188]
007FFFF7  33 D2                           xor edx, edx
007FFFF9  49 8D BE 40 04 00 00            lea rdi, [r14 + 0x440]
00800000  66 44 29 A6 E6 01 00 00         sub word ptr [rsi + 0x1e6], r12w
00800008  48 8B CF                        mov rcx, rdi
0080000B  90                              nop
0080000C  E8 1F 02 A1 FF                  call 0x140210230
00800011  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
00800017  48 8B D8                        mov rbx, rax
0080001A  73 0E                           jae 0x14080002a
0080001C  4C 8B C7                        mov r8, rdi
0080001F  48 8B D0                        mov rdx, rax
00800022  48 8B CF                        mov rcx, rdi
00800025  E8 66 FC A0 FF                  call 0x14020fc90
0080002A  48 85 DB                        test rbx, rbx
0080002D  74 04                           je 0x140800033
0080002F  44 88 63 0A                     mov byte ptr [rbx + 0xa], r12b
00800033  48 83 CB FF                     or rbx, 0xffffffffffffffff
00800037  83 3D 06 01 63 00 00            cmp dword ptr [rip + 0x630106], 0
0080003E  74 46                           je 0x140800086
00800040  F0 48 0F C1 1F                  lock xadd qword ptr [rdi], rbx
00800045  80 E3 06                        and bl, 6
00800048  80 FB 02                        cmp bl, 2
0080004B  75 08                           jne 0x140800055
0080004D  48 8B CF                        mov rcx, rdi
00800050  E8 7B 5D A6 FF                  call 0x140265dd0
00800055  48 8B CF                        mov rcx, rdi
00800058  E8 A3 15 AE FF                  call 0x1402e1600
0080005D  49 8B CC                        mov rcx, r12
00800060  90                              nop
00800061  66 01 8E E6 01 00 00            add word ptr [rsi + 0x1e6], cx
00800068  75 12                           jne 0x14080007c
0080006A  48 8D 86 98 00 00 00            lea rax, [rsi + 0x98]
00800071  90                              nop
00800072  48 39 00                        cmp qword ptr [rax], rax
00800075  74 05                           je 0x14080007c
00800077  E8 04 2C AE FF                  call 0x1402e2c80
0080007C  B8 0A 01 00 C0                  mov eax, 0xc000010a
00800081  E9 94 03 00 00                  jmp 0x14080041a
00800086  49 83 BE B0 00 00 00 00         cmp qword ptr [r14 + 0xb0], 0
0080008E  41 B4 06                        mov r12b, 6
00800091  0F 85 8A 01 00 00               jne 0x140800221
00800097  48 83 65 50 00                  and qword ptr [rbp + 0x50], 0
0080009C  49 8B CE                        mov rcx, r14
0080009F  E8 14 59 C9 FF                  call 0x1404959b8
008000A4  89 45 40                        mov dword ptr [rbp + 0x40], eax
008000A7  48 8B CB                        mov rcx, rbx
008000AA  F0 48 0F C1 0F                  lock xadd qword ptr [rdi], rcx
008000AF  41 22 CC                        and cl, r12b
008000B2  80 F9 02                        cmp cl, 2
008000B5  75 08                           jne 0x1408000bf
008000B7  48 8B CF                        mov rcx, rdi
008000BA  E8 11 5D A6 FF                  call 0x140265dd0
008000BF  48 8B CF                        mov rcx, rdi
008000C2  E8 39 15 AE FF                  call 0x1402e1600
008000C7  B9 01 00 00 00                  mov ecx, 1
008000CC  90                              nop
008000CD  66 01 8E E6 01 00 00            add word ptr [rsi + 0x1e6], cx
008000D4  75 12                           jne 0x1408000e8
008000D6  48 8D 86 98 00 00 00            lea rax, [rsi + 0x98]
008000DD  90                              nop
008000DE  48 39 00                        cmp qword ptr [rax], rax
008000E1  74 05                           je 0x1408000e8
008000E3  E8 98 2B AE FF                  call 0x1402e2c80
008000E8  83 7D 40 00                     cmp dword ptr [rbp + 0x40], 0
008000EC  75 0A                           jne 0x1408000f8
008000EE  B8 2D 01 00 C0                  mov eax, 0xc000012d
008000F3  E9 22 03 00 00                  jmp 0x14080041a
008000F8  48 83 65 F0 00                  and qword ptr [rbp - 0x10], 0
008000FD  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00800101  0F 57 C0                        xorps xmm0, xmm0
00800104  4C 89 75 D8                     mov qword ptr [rbp - 0x28], r14
00800108  45 33 C0                        xor r8d, r8d
0080010B  33 D2                           xor edx, edx
0080010D  F3 0F 7F 45 E0                  movdqu xmmword ptr [rbp - 0x20], xmm0
00800112  E8 F9 DB C0 FF                  call 0x14040dd10
00800117  49 8B 86 B8 00 00 00            mov rax, qword ptr [r14 + 0xb8]
0080011E  33 C9                           xor ecx, ecx
00800120  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
00800125  45 33 C0                        xor r8d, r8d
00800128  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
0080012D  BA FF FF 1F 00                  mov edx, 0x1fffff
00800132  4C 8B 88 80 00 00 00            mov r9, qword ptr [rax + 0x80]
00800139  48 8D 45 D8                     lea rax, [rbp - 0x28]
0080013D  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00800142  48 8D 05 A7 E4 C7 FF            lea rax, [rip - 0x381b59]
00800149  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0080014E  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00800153  48 8D 4D 48                     lea rcx, [rbp + 0x48]
00800157  E8 C4 CF 1E 00                  call 0x1409ed120
0080015C  85 C0                           test eax, eax
0080015E  0F 88 B6 02 00 00               js 0x14080041a
00800164  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
0080016A  48 8D 45 50                     lea rax, [rbp + 0x50]
0080016E  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00800174  45 33 C9                        xor r9d, r9d
00800177  4C 8B 05 4A 69 7C 00            mov r8, qword ptr [rip + 0x7c694a]
0080017E  BA FF FF 1F 00                  mov edx, 0x1fffff
00800183  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
00800187  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0080018C  C7 44 24 20 4D 6D 50 66         mov dword ptr [rsp + 0x20], 0x66506d4d
00800194  E8 B7 94 06 00                  call 0x140869650
00800199  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0080019F  48 8D 4D E0                     lea rcx, [rbp - 0x20]
008001A3  45 33 C9                        xor r9d, r9d
008001A6  45 33 C0                        xor r8d, r8d
008001A9  41 8D 51 1A                     lea edx, [r9 + 0x1a]
008001AD  E8 FE E4 A0 FF                  call 0x14020e6b0
008001B2  66 01 9E E6 01 00 00            add word ptr [rsi + 0x1e6], bx
008001B9  45 33 C0                        xor r8d, r8d
008001BC  33 D2                           xor edx, edx
008001BE  48 8B CF                        mov rcx, rdi
008001C1  90                              nop
008001C2  E8 69 00 A1 FF                  call 0x140210230
008001C7  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
008001CD  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
008001D1  73 12                           jae 0x1408001e5
008001D3  4C 8B C7                        mov r8, rdi
008001D6  48 8B D0                        mov rdx, rax
008001D9  48 8B CF                        mov rcx, rdi
008001DC  E8 AF FA A0 FF                  call 0x14020fc90
008001E1  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
008001E5  48 85 C0                        test rax, rax
008001E8  74 04                           je 0x1408001ee
008001EA  C6 40 0A 01                     mov byte ptr [rax + 0xa], 1
008001EE  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
008001F2  49 39 86 E0 03 00 00            cmp qword ptr [r14 + 0x3e0], rax
008001F9  75 0D                           jne 0x140800208
008001FB  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
008001FF  49 89 86 B0 00 00 00            mov qword ptr [r14 + 0xb0], rax
00800206  EB 0B                           jmp 0x140800213
00800208  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
0080020C  33 D2                           xor edx, edx
0080020E  E8 5D 16 0A 00                  call 0x1408a1870
00800213  48 8B 4D 50                     mov rcx, qword ptr [rbp + 0x50]
00800217  BA 4D 6D 50 66                  mov edx, 0x66506d4d
0080021C  E8 BF 76 AF FF                  call 0x1402f78e0
00800221  41 8B 8E 58 48 00 00            mov ecx, dword ptr [r14 + 0x4858]
00800228  89 4D 40                        mov dword ptr [rbp + 0x40], ecx
0080022B  83 F9 10                        cmp ecx, 0x10
0080022E  0F 83 26 01 00 00               jae 0x14080035a
00800234  41 0F B7 87 AC 00 00 00         movzx eax, word ptr [r15 + 0xac]
0080023C  45 33 C0                        xor r8d, r8d
0080023F  0F B7 D1                        movzx edx, cx
00800242  66 33 D0                        xor dx, ax
00800245  66 83 E2 0F                     and dx, 0xf
00800249  66 33 D0                        xor dx, ax
0080024C  45 8D 58 01                     lea r11d, [r8 + 1]
00800250  66 41 89 97 AC 00 00 00         mov word ptr [r15 + 0xac], dx
00800258  41 8B 86 58 48 00 00            mov eax, dword ptr [r14 + 0x4858]
0080025F  85 C0                           test eax, eax
00800261  74 44                           je 0x1408002a7
00800263  4D 8D 8E 60 48 00 00            lea r9, [r14 + 0x4860]
0080026A  44 8B D0                        mov r10d, eax
0080026D  49 8B 01                        mov rax, qword ptr [r9]
00800270  4D 8D 49 08                     lea r9, [r9 + 8]
00800274  66 0F BA A0 AC 00 00 00 0B      bt word ptr [rax + 0xac], 0xb
0080027D  41 8D 40 01                     lea eax, [r8 + 1]
00800281  41 0F 43 C0                     cmovae eax, r8d
00800285  44 8B C0                        mov r8d, eax
00800288  4D 2B D3                        sub r10, r11
0080028B  75 E0                           jne 0x14080026d
0080028D  85 C0                           test eax, eax
0080028F  74 16                           je 0x1408002a7
00800291  B8 10 08 00 00                  mov eax, 0x810
00800296  66 85 D0                        test ax, dx
00800299  75 67                           jne 0x140800302
0080029B  66 83 CA 20                     or dx, 0x20
0080029F  66 41 89 97 AC 00 00 00         mov word ptr [r15 + 0xac], dx
008002A7  41 0F B7 87 AC 00 00 00         movzx eax, word ptr [r15 + 0xac]
008002AF  A8 50                           test al, 0x50
008002B1  0F 85 93 00 00 00               jne 0x14080034a
008002B7  4C 8B 45 58                     mov r8, qword ptr [rbp + 0x58]
008002BB  45 33 C9                        xor r9d, r9d
008002BE  48 8B 55 D0                     mov rdx, qword ptr [rbp - 0x30]
008002C2  49 8B CE                        mov rcx, r14
008002C5  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
008002CA  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
008002CF  E8 08 C8 E8 FF                  call 0x14068cadc
008002D4  41 F6 87 AC 00 00 00 20         test byte ptr [r15 + 0xac], 0x20
008002DC  41 BF 01 00 00 00               mov r15d, 1
008002E2  0F 85 DD 00 00 00               jne 0x1408003c5
008002E8  41 83 BE 3C 04 00 00 00         cmp dword ptr [r14 + 0x43c], 0
008002F0  0F 85 CF 00 00 00               jne 0x1408003c5
008002F6  45 89 BE 3C 04 00 00            mov dword ptr [r14 + 0x43c], r15d
008002FD  E9 C3 00 00 00                  jmp 0x1408003c5
00800302  F0 48 0F C1 1F                  lock xadd qword ptr [rdi], rbx
00800307  41 22 DC                        and bl, r12b
0080030A  80 FB 02                        cmp bl, 2
0080030D  75 08                           jne 0x140800317
0080030F  48 8B CF                        mov rcx, rdi
00800312  E8 B9 5A A6 FF                  call 0x140265dd0
00800317  48 8B CF                        mov rcx, rdi
0080031A  E8 E1 12 AE FF                  call 0x1402e1600
0080031F  B9 01 00 00 00                  mov ecx, 1
00800324  90                              nop
00800325  66 01 8E E6 01 00 00            add word ptr [rsi + 0x1e6], cx
0080032C  75 12                           jne 0x140800340
0080032E  48 8D 86 98 00 00 00            lea rax, [rsi + 0x98]
00800335  90                              nop
00800336  48 39 00                        cmp qword ptr [rax], rax
00800339  74 05                           je 0x140800340
0080033B  E8 40 29 AE FF                  call 0x1402e2c80
00800340  B8 BB 00 00 C0                  mov eax, 0xc00000bb
00800345  E9 D0 00 00 00                  jmp 0x14080041a
0080034A  A8 10                           test al, 0x10
0080034C  74 51                           je 0x14080039f
0080034E  49 8B CE                        mov rcx, r14
00800351  E8 4E CC AD FF                  call 0x1402dcfa4
00800356  85 C0                           test eax, eax
00800358  74 45                           je 0x14080039f
0080035A  F0 48 0F C1 1F                  lock xadd qword ptr [rdi], rbx
0080035F  41 22 DC                        and bl, r12b
00800362  80 FB 02                        cmp bl, 2
00800365  75 08                           jne 0x14080036f
00800367  48 8B CF                        mov rcx, rdi
0080036A  E8 61 5A A6 FF                  call 0x140265dd0
0080036F  48 8B CF                        mov rcx, rdi
00800372  E8 89 12 AE FF                  call 0x1402e1600
00800377  B9 01 00 00 00                  mov ecx, 1
0080037C  90                              nop
0080037D  66 01 8E E6 01 00 00            add word ptr [rsi + 0x1e6], cx
00800384  75 12                           jne 0x140800398
00800386  48 8D 86 98 00 00 00            lea rax, [rsi + 0x98]
0080038D  90                              nop
0080038E  48 39 00                        cmp qword ptr [rax], rax
00800391  74 05                           je 0x140800398
00800393  E8 E8 28 AE FF                  call 0x1402e2c80
00800398  B8 97 00 00 C0                  mov eax, 0xc0000097
0080039D  EB 7B                           jmp 0x14080041a
0080039F  41 8B D3                        mov edx, r11d
008003A2  49 8B CF                        mov rcx, r15
008003A5  E8 02 00 E8 FF                  call 0x1406803ac
008003AA  8B 4D 40                        mov ecx, dword ptr [rbp + 0x40]
008003AD  4D 89 BC CE 60 48 00 00         mov qword ptr [r14 + rcx*8 + 0x4860], r15
008003B5  8D 41 01                        lea eax, [rcx + 1]
008003B8  41 89 86 58 48 00 00            mov dword ptr [r14 + 0x4858], eax
008003BF  41 BF 01 00 00 00               mov r15d, 1
008003C5  F0 48 0F C1 1F                  lock xadd qword ptr [rdi], rbx
008003CA  41 22 DC                        and bl, r12b
008003CD  80 FB 02                        cmp bl, 2
008003D0  75 08                           jne 0x1408003da
008003D2  48 8B CF                        mov rcx, rdi
008003D5  E8 F6 59 A6 FF                  call 0x140265dd0
008003DA  48 8B CF                        mov rcx, rdi
008003DD  E8 1E 12 AE FF                  call 0x1402e1600
008003E2  90                              nop
008003E3  66 44 01 BE E6 01 00 00         add word ptr [rsi + 0x1e6], r15w
008003EB  75 12                           jne 0x1408003ff
008003ED  48 8D 86 98 00 00 00            lea rax, [rsi + 0x98]
008003F4  90                              nop
008003F5  48 39 00                        cmp qword ptr [rax], rax
008003F8  74 05                           je 0x1408003ff
008003FA  E8 81 28 AE FF                  call 0x1402e2c80
008003FF  45 33 C0                        xor r8d, r8d
00800402  33 D2                           xor edx, edx
00800404  49 8B CE                        mov rcx, r14
00800407  E8 60 5C C6 FF                  call 0x14046606c
0080040C  49 8D 8E A0 03 00 00            lea rcx, [r14 + 0x3a0]
00800413  E8 F8 EE B3 FF                  call 0x14033f310
00800418  33 C0                           xor eax, eax
0080041A  48 81 C4 80 00 00 00            add rsp, 0x80
00800421  41 5F                           pop r15
00800423  41 5E                           pop r14
00800425  41 5C                           pop r12
00800427  5F                              pop rdi
00800428  5E                              pop rsi
00800429  5B                              pop rbx
0080042A  5D                              pop rbp
0080042B  C3                              ret
0080042C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiInsertPageFileInList(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;

    v_rsp = (v_rsp) - (128);
    a3 = 0;
    v_stack_m68 = (unsigned int)(*(unsigned int *)(a1));
    v_stack_p20 = (unsigned int)(*(unsigned int *)(a1 + 4));
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    if ((*(unsigned int *)(a1 + 40)) <= 0) goto loc_007FFFE4;
loc_007FFFCB:
    a3 = (unsigned int)((a3) + (1));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + a3 * 8)) = (unsigned int)(0x99887711ULL);
    if (a3 < (*(unsigned int *)(a1 + 40))) goto loc_007FFFCB;
loc_007FFFE4:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(a1 + 216) + 1088, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(a1 + 216) + 1088;
        a2 = result;
        a1 = *(unsigned __int64 *)(a1 + 216) + 1088;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_rbx = (result) | (-1);
    if ((*(unsigned int *)(v_rip + 6488326)) == 0) goto loc_00800086;
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) {
        a1 = *(unsigned __int64 *)(a1 + 216) + 1088;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(*(unsigned __int64 *)(a1 + 216) + 1088, a2, a3, a4);
    if (((unsigned __int8)(v_rbx)) != 2) goto loc_0080007C;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(1, a2, a3, a4);
    }
    goto loc_0080041A;
loc_00800086:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 216) + 176)) != 0) goto loc_00800221;
    result = MiMakePartitionActive(*(unsigned __int64 *)(a1 + 216), a2, a3, a4);
    v_stack_p8 = (unsigned int)(result);
    a1 = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(a1)) == 2) {
        a1 = *(unsigned __int64 *)(a1 + 216) + 1088;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(*(unsigned __int64 *)(a1 + 216) + 1088, a2, a3, a4);
    if (((unsigned __int8)(a1)) != 2) goto loc_008000E8;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(1, a2, a3, a4);
    }
    if (v_stack_p8 != 0) goto loc_008000F8;
    goto loc_0080041A;
loc_008000F8:
    v_stack_m60 = *(unsigned __int64 *)(a1 + 216);
    a3 = 0;
    a2 = 0;
    v_stack_m58 = v_xmm0;
    result = KeInitializeEvent(v_stack_m58, a2, a3, a4);
    a1 = 0;
    v_stack_m78 = 0;
    a3 = 0;
    v_stack_m80 = 0;
    v_stack_m88 = v_stack_m60;
    v_stack_m90 = v_rip - 3677017;
    v_stack_m98 = 0;
    result = PsCreateSystemThreadEx(v_stack_p10, (unsigned int)(0x1FFFFFULL), a3, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 216) + 184) + 128));
    if (sign_flag) goto loc_0080041A;
    a4 = 0;
    v_stack_m90 = v_stack_p18;
    v_stack_m98 = 0x66506D4DULL;
    result = ObpReferenceObjectByHandleWithTag(v_stack_p10, (unsigned int)(0x1FFFFFULL), *(unsigned __int64 *)(v_rip + 8153418), a4);
    a4 = 0;
    a3 = 0;
    result = KeWaitForSingleObject(v_stack_m58, a4 + 26, a3, a4);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(a1 + 216) + 1088, a2, a3, a4);
    v_stack_p8 = result;
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(a1 + 216) + 1088;
        a2 = result;
        a1 = *(unsigned __int64 *)(a1 + 216) + 1088;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
        result = v_stack_p8;
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 216) + 992)) != v_stack_p18) goto loc_00800208;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 216) + 176) = v_stack_p10;
    goto loc_00800213;
loc_00800208:
    a2 = 0;
    result = ObCloseHandle(v_stack_p10, a2, a3, a4);
loc_00800213:
    result = ObfDereferenceObjectWithTag(v_stack_p18, (unsigned int)(0x66506D4DULL), a3, a4);
loc_00800221:
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 216) + 18520)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 216) + 18520)))) >= 16) goto loc_0080035A;
    a3 = 0;
    a2 = (unsigned __int16)(((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 216) + 18520)))) ^ ((unsigned __int16)(*(unsigned __int16 *)(a1 + 172))));
    a2 = (unsigned __int16)((a2) & (15));
    a2 = (unsigned __int16)((a2) ^ ((unsigned __int16)(*(unsigned __int16 *)(a1 + 172))));
    *(unsigned __int16 *)(a1 + 172) = (unsigned __int16)(a2);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 216) + 18520))) == 0) goto loc_008002A7;
loc_0080026D:
    result = a3 + 1;
    if (condition_is_above_or_equal) { result = 0; }
    v_r10 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 216) + 18520))))) - (a3 + 1);
    if (condition_is_not_equal) goto loc_0080026D;
    if ((unsigned int)(result) == 0) goto loc_008002A7;
    if ((((unsigned __int16)((unsigned int)(0x810ULL))) & ((unsigned __int16)(a2))) != 0) goto loc_00800302;
    a2 = (unsigned __int16)((a2) | (32));
    *(unsigned __int16 *)(a1 + 172) = (unsigned __int16)(a2);
loc_008002A7:
    if ((((unsigned __int8)(*(unsigned __int16 *)(a1 + 172))) & (80)) != 0) goto loc_0080034A;
    a4 = 0;
    v_stack_m90 = a1;
    result = MiIncreaseCommitLimits(*(unsigned __int64 *)(a1 + 216), v_stack_m68, v_stack_p20, a4);
    if (((*(unsigned __int8 *)(a1 + 172)) & (32)) != 0) goto loc_008003C5;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 216) + 1084)) != 0) goto loc_008003C5;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 216) + 1084) = 1;
    goto loc_008003C5;
loc_00800302:
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) {
        a1 = *(unsigned __int64 *)(a1 + 216) + 1088;
        result = ExfTryToWakePushLock(a1, v_stack_m68, v_stack_p20, a4);
    }
    result = KeAbPostRelease(*(unsigned __int64 *)(a1 + 216) + 1088, v_stack_m68, v_stack_p20, a4);
    if (((unsigned __int8)(v_rbx)) != 2) goto loc_00800340;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(1, v_stack_m68, v_stack_p20, a4);
    }
    goto loc_0080041A;
loc_0080034A:
    if ((((unsigned __int8)((unsigned int)(0xC00000BBULL))) & (16)) == 0) goto loc_0080039F;
    result = MiNumberWsSwapPagefiles(*(unsigned __int64 *)(a1 + 216), v_stack_m68, v_stack_p20, a4);
    if ((unsigned int)(result) == 0) goto loc_0080039F;
loc_0080035A:
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) {
        a1 = *(unsigned __int64 *)(a1 + 216) + 1088;
        result = ExfTryToWakePushLock(a1, v_stack_m68, v_stack_p20, a4);
    }
    result = KeAbPostRelease(*(unsigned __int64 *)(a1 + 216) + 1088, v_stack_m68, v_stack_p20, a4);
    if (((unsigned __int8)(v_rbx)) != 2) goto loc_00800398;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(1, v_stack_m68, v_stack_p20, a4);
    }
    goto loc_0080041A;
loc_0080039F:
    result = MiUpdatePageFileList(1, (unsigned int)((unsigned int)(a3 + 1)), v_stack_p20, a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 216) + (unsigned int)(v_stack_p8) * 8 + 18528) = 1;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 216) + 18520) = (unsigned int)((unsigned int)(v_stack_p8) + 1);
loc_008003C5:
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    result = (unsigned int)(v_stack_p8) + 1;
    if (((unsigned __int8)(v_rbx)) == 2) {
        a1 = *(unsigned __int64 *)(a1 + 216) + 1088;
        result = ExfTryToWakePushLock(a1, (unsigned int)((unsigned int)(a3 + 1)), v_stack_p20, a4);
    }
    result = KeAbPostRelease(*(unsigned __int64 *)(a1 + 216) + 1088, (unsigned int)((unsigned int)(a3 + 1)), v_stack_p20, a4);
    if (((unsigned __int8)(v_rbx)) != 2) goto loc_008003FF;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(*(unsigned __int64 *)(a1 + 216) + 1088, (unsigned int)((unsigned int)(a3 + 1)), v_stack_p20, a4);
    }
    a3 = 0;
    a2 = 0;
    result = MiUpdateReserveClusterInfo(*(unsigned __int64 *)(a1 + 216), a2, a3, a4);
    result = KeSetEvent(*(unsigned __int64 *)(a1 + 216) + 928, a2, a3, a4);
    result = 0;
loc_0080041A:
    v_rsp = (v_rsp) + (128);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiInsertPageFileInList(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;

    local_rsp = (local_rsp) - (128);
    Arg3 = 0;
    v_stack_m68 = (uint32_t)(*(uint32_t *)(arg1));
    v_stack_p20 = (uint32_t)(*(uint32_t *)(arg1 + 0x4));
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    if ((*(uint32_t *)(arg1 + 0x28)) <= 0) goto loc_007FFFE4;
loc_007FFFCB:
    Arg3 = (uint32_t)((Arg3) + (1));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + Arg3 * 8)) = (uint32_t)(0x99887711ULL);
    if (Arg3 < (*(uint32_t *)(arg1 + 0x28))) goto loc_007FFFCB;
loc_007FFFE4:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(arg1 + 0xD8) + 1088, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(arg1 + 0xD8) + 1088;
        Arg2 = result;
        Arg1 = *(uint64_t *)(arg1 + 0xD8) + 1088;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_rbx = (result) | (-1);
    if ((*(uint32_t *)(v_rip + 0x630106)) == 0) goto loc_00800086;
    local_rbx = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(local_rbx)) == 2) {
        Arg1 = *(uint64_t *)(arg1 + 0xD8) + 1088;
        result = ExfTryToWakePushLock(Arg1, Arg2, Arg3, a4);
    }
    result = KeAbPostRelease(*(uint64_t *)(arg1 + 0xD8) + 1088, Arg2, Arg3, a4);
    if (((uint8_t)(local_rbx)) != 2) goto loc_0080007C;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(1, Arg2, Arg3, a4);
    }
    goto loc_0080041A;
loc_00800086:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0xD8) + 0xB0)) != 0) goto loc_00800221;
    result = MiMakePartitionActive(*(uint64_t *)(arg1 + 0xD8), Arg2, Arg3, a4);
    v_stack_p8 = (uint32_t)(result);
    Arg1 = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(Arg1)) == 2) {
        Arg1 = *(uint64_t *)(arg1 + 0xD8) + 1088;
        result = ExfTryToWakePushLock(Arg1, Arg2, Arg3, a4);
    }
    result = KeAbPostRelease(*(uint64_t *)(arg1 + 0xD8) + 1088, Arg2, Arg3, a4);
    if (((uint8_t)(Arg1)) != 2) goto loc_008000E8;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(1, Arg2, Arg3, a4);
    }
    if (v_stack_p8 != 0) goto loc_008000F8;
    goto loc_0080041A;
loc_008000F8:
    v_stack_m60 = *(uint64_t *)(arg1 + 0xD8);
    Arg3 = 0;
    Arg2 = 0;
    v_stack_m58 = v_xmm0;
    result = KeInitializeEvent(v_stack_m58, Arg2, Arg3, a4);
    Arg1 = 0;
    v_stack_m78 = 0;
    Arg3 = 0;
    v_stack_m80 = 0;
    v_stack_m88 = v_stack_m60;
    v_stack_m90 = v_rip - 3677017;
    v_stack_m98 = 0;
    result = PsCreateSystemThreadEx(v_stack_p10, (uint32_t)(0x1FFFFFULL), Arg3, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xD8) + 0xB8) + 0x80));
    if (sign_flag) goto loc_0080041A;
    a4 = 0;
    v_stack_m90 = v_stack_p18;
    v_stack_m98 = 0x66506D4DULL;
    result = ObpReferenceObjectByHandleWithTag(v_stack_p10, (uint32_t)(0x1FFFFFULL), *(uint64_t *)(v_rip + 0x7C694A), a4);
    a4 = 0;
    Arg3 = 0;
    result = KeWaitForSingleObject(v_stack_m58, a4 + 26, Arg3, a4);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(arg1 + 0xD8) + 1088, Arg2, Arg3, a4);
    v_stack_p8 = result;
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(arg1 + 0xD8) + 1088;
        Arg2 = result;
        Arg1 = *(uint64_t *)(arg1 + 0xD8) + 1088;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
        result = v_stack_p8;
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0xD8) + 0x3E0)) != v_stack_p18) goto loc_00800208;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0xD8) + 0xB0) = v_stack_p10;
    goto loc_00800213;
loc_00800208:
    Arg2 = 0;
    result = ObCloseHandle(v_stack_p10, Arg2, Arg3, a4);
loc_00800213:
    result = ObfDereferenceObjectWithTag(v_stack_p18, (uint32_t)(0x66506D4DULL), Arg3, a4);
loc_00800221:
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xD8) + 0x4858)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xD8) + 0x4858)))) >= 16) goto loc_0080035A;
    Arg3 = 0;
    Arg2 = (uint16_t)(((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xD8) + 0x4858)))) ^ ((uint16_t)(*(uint16_t *)(arg1 + 0xAC))));
    Arg2 = (uint16_t)((Arg2) & (15));
    Arg2 = (uint16_t)((Arg2) ^ ((uint16_t)(*(uint16_t *)(arg1 + 0xAC))));
    *(uint16_t *)(arg1 + 0xAC) = (uint16_t)(Arg2);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xD8) + 0x4858))) == 0) goto loc_008002A7;
loc_0080026D:
    result = Arg3 + 1;
    if (condition_is_above_or_equal) { result = 0; }
    local_r10 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xD8) + 0x4858))))) - (Arg3 + 1);
    if (condition_is_not_equal) goto loc_0080026D;
    if ((uint32_t)(result) == 0) goto loc_008002A7;
    if ((((uint16_t)((uint32_t)(0x810ULL))) & ((uint16_t)(Arg2))) != 0) goto loc_00800302;
    Arg2 = (uint16_t)((Arg2) | (32));
    *(uint16_t *)(arg1 + 0xAC) = (uint16_t)(Arg2);
loc_008002A7:
    if ((((uint8_t)(*(uint16_t *)(arg1 + 0xAC))) & (80)) != 0) goto loc_0080034A;
    a4 = 0;
    v_stack_m90 = Arg1;
    result = MiIncreaseCommitLimits(*(uint64_t *)(arg1 + 0xD8), v_stack_m68, v_stack_p20, a4);
    if (((*(uint8_t *)(arg1 + 0xAC)) & (32)) != 0) goto loc_008003C5;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0xD8) + 0x43C)) != 0) goto loc_008003C5;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0xD8) + 0x43C) = 1;
    goto loc_008003C5;
loc_00800302:
    local_rbx = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(local_rbx)) == 2) {
        Arg1 = *(uint64_t *)(arg1 + 0xD8) + 1088;
        result = ExfTryToWakePushLock(Arg1, v_stack_m68, v_stack_p20, a4);
    }
    result = KeAbPostRelease(*(uint64_t *)(arg1 + 0xD8) + 1088, v_stack_m68, v_stack_p20, a4);
    if (((uint8_t)(local_rbx)) != 2) goto loc_00800340;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(1, v_stack_m68, v_stack_p20, a4);
    }
    goto loc_0080041A;
loc_0080034A:
    if ((((uint8_t)((uint32_t)(0xC00000BBULL))) & (16)) == 0) goto loc_0080039F;
    result = MiNumberWsSwapPagefiles(*(uint64_t *)(arg1 + 0xD8), v_stack_m68, v_stack_p20, a4);
    if ((uint32_t)(result) == 0) goto loc_0080039F;
loc_0080035A:
    local_rbx = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(local_rbx)) == 2) {
        Arg1 = *(uint64_t *)(arg1 + 0xD8) + 1088;
        result = ExfTryToWakePushLock(Arg1, v_stack_m68, v_stack_p20, a4);
    }
    result = KeAbPostRelease(*(uint64_t *)(arg1 + 0xD8) + 1088, v_stack_m68, v_stack_p20, a4);
    if (((uint8_t)(local_rbx)) != 2) goto loc_00800398;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(1, v_stack_m68, v_stack_p20, a4);
    }
    goto loc_0080041A;
loc_0080039F:
    result = MiUpdatePageFileList(1, (uint32_t)((uint32_t)(Arg3 + 1)), v_stack_p20, a4);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0xD8) + (uint32_t)(v_stack_p8) * 8 + 0x4860) = 1;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0xD8) + 0x4858) = (uint32_t)((uint32_t)(v_stack_p8) + 1);
loc_008003C5:
    local_rbx = (uint8_t)((local_rbx) & (6));
    result = (uint32_t)(v_stack_p8) + 1;
    if (((uint8_t)(local_rbx)) == 2) {
        Arg1 = *(uint64_t *)(arg1 + 0xD8) + 1088;
        result = ExfTryToWakePushLock(Arg1, (uint32_t)((uint32_t)(Arg3 + 1)), v_stack_p20, a4);
    }
    result = KeAbPostRelease(*(uint64_t *)(arg1 + 0xD8) + 1088, (uint32_t)((uint32_t)(Arg3 + 1)), v_stack_p20, a4);
    if (((uint8_t)(local_rbx)) != 2) goto loc_008003FF;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(*(uint64_t *)(arg1 + 0xD8) + 1088, (uint32_t)((uint32_t)(Arg3 + 1)), v_stack_p20, a4);
    }
    Arg3 = 0;
    Arg2 = 0;
    result = MiUpdateReserveClusterInfo(*(uint64_t *)(arg1 + 0xD8), Arg2, Arg3, a4);
    result = KeSetEvent(*(uint64_t *)(arg1 + 0xD8) + 928, Arg2, Arg3, a4);
    result = 0;
loc_0080041A:
    local_rsp = (local_rsp) + (128);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0xAC` | `8` | `R` |
| `Arg1` | `+ 0xAC` | `16` | `R` |
| `Arg1` | `+ 0xAC` | `16` | `W` |
| `Arg1` | `+ 0xAE` | `8` | `R/W` |
| `Arg1` | `+ 0xD8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007FFF80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
