# FsRtlpAcknowledgeOplockBreakByCacheFlags

- RVA: `0x003F1988`–`0x003F2682` (길이 `3,322` bytes)
- VA: `0x00000001403F1988`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00096FD0`
- 디코드: `715`개 명령, `3,322/3,322` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **49**; 고유 호출 대상: **26**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x003F1ACB` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x003F1AE8` → [IofCompleteRequest](../29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x003F1AFA` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x003F1B1A` → [ExAcquireFastMutexUnsafe](ExAcquireFastMutexUnsafe_function_003F3720.md) (function, `0x003F3720`)
- `0x003F1B7D` → [IofCompleteRequest](../29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x003F1BB7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x003F1C40` → [FsRtlpOplockKeysEqual](FsRtlpOplockKeysEqual_function_003F26B0.md) (function, `0x003F26B0`)
- `0x003F1C8E` → [FsRtlpModifyThreadPriorities](../48/FsRtlpModifyThreadPriorities_function_0048B098.md) (function, `0x0048B098`)
- `0x003F1C9A` → [FsRtlpClearOwner](../26/FsRtlpClearOwner_function_00265BE8.md) (function, `0x00265BE8`)
- `0x003F1CE5` → [FsRtlpOplockPerfMoveData](../../page/71/FsRtlpOplockPerfMoveData_function_00715308.md) (function, `0x00715308`)
- `0x003F1CFA` → [FsRtlpOplockMoveAckTimeout](../../page/71/FsRtlpOplockMoveAckTimeout_function_00715108.md) (function, `0x00715108`)
- `0x003F1DA4` → [FsRtlpOplockKeysEqual](FsRtlpOplockKeysEqual_function_003F26B0.md) (function, `0x003F26B0`)
- `0x003F1DF5` → [FsRtlpOplockUpperLowerCompatible](../../page/A2/FsRtlpOplockUpperLowerCompatible_function_00A21E04.md) (function, `0x00A21E04`)
- `0x003F1E51` → [IofCompleteRequest](../29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x003F1E96` → [FsRtlpOplockUpperLowerCompatible](../../page/A2/FsRtlpOplockUpperLowerCompatible_function_00A21E04.md) (function, `0x00A21E04`)
- `0x003F1EE8` → [IofCompleteRequest](../29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x003F1F04` → [FsRtlpOplockDequeueRH](../42/FsRtlpOplockDequeueRH_function_004258FC.md) (function, `0x004258FC`)
- `0x003F1F22` → [FsRtlpOplockPerfMoveData](../../page/71/FsRtlpOplockPerfMoveData_function_00715308.md) (function, `0x00715308`)
- `0x003F1F2F` → [FsRtlpOplockMoveAckTimeout](../../page/71/FsRtlpOplockMoveAckTimeout_function_00715108.md) (function, `0x00715108`)
- `0x003F2002` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x003F2027` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x003F2036` → [FsRtlpComputeShareableOplockState](../42/FsRtlpComputeShareableOplockState_function_004256EC.md) (function, `0x004256EC`)
- `0x003F204A` → [IofCompleteRequest](../29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x003F2084` → [FsRtlpOplockPerfMoveData](../../page/71/FsRtlpOplockPerfMoveData_function_00715308.md) (function, `0x00715308`)
- `0x003F2094` → [FsRtlpOplockMoveAckTimeout](../../page/71/FsRtlpOplockMoveAckTimeout_function_00715108.md) (function, `0x00715108`)
- `0x003F20C3` → [FsRtlpRequestShareableOplock](../4E/FsRtlpRequestShareableOplock_function_004E6EC8.md) (function, `0x004E6EC8`)
- `0x003F2135` → [ObfReferenceObjectWithTag](../21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x003F2159` → [ObfReferenceObjectWithTag](../21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x003F219A` → [FsRtlpOplockPerfMoveData](../../page/71/FsRtlpOplockPerfMoveData_function_00715308.md) (function, `0x00715308`)
- `0x003F21AF` → [FsRtlpOplockMoveAckTimeout](../../page/71/FsRtlpOplockMoveAckTimeout_function_00715108.md) (function, `0x00715108`)
- `0x003F21DA` → [KeAcquireQueuedSpinLock](../27/KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x003F21F6` → [FsRtlpCancelExclusiveIrp](../4F/FsRtlpCancelExclusiveIrp_function_004F96CC.md) (function, `0x004F96CC`)
- `0x003F2210` → [KeReleaseQueuedSpinLock](../27/KeReleaseQueuedSpinLock_function_00272540.md) (function, `0x00272540`)
- `0x003F222D` → [FsRtlpModifyThreadPriorities](../48/FsRtlpModifyThreadPriorities_function_0048B098.md) (function, `0x0048B098`)
- `0x003F223A` → [FsRtlpClearOwner](../26/FsRtlpClearOwner_function_00265BE8.md) (function, `0x00265BE8`)
- `0x003F2255` → [FsRtlpOplockPerfSendData](../../page/6F/FsRtlpOplockPerfSendData_function_006FDB80.md) (function, `0x006FDB80`)
- `0x003F2260` → [FsRtlpFreeRHOpContext](../4F/FsRtlpFreeRHOpContext_function_004F2394.md) (function, `0x004F2394`)
- `0x003F22AF` → [FsRtlpReleaseIrpsWaitingForRH](../42/FsRtlpReleaseIrpsWaitingForRH_function_00425CBC.md) (function, `0x00425CBC`)
- `0x003F2380` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x003F23B5` → [IofCompleteRequest](../29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x003F2492` → [IofCompleteRequest](../29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x003F24F5` → [FsRtlpModifyThreadPriorities](../48/FsRtlpModifyThreadPriorities_function_0048B098.md) (function, `0x0048B098`)
- `0x003F2501` → [FsRtlpClearOwner](../26/FsRtlpClearOwner_function_00265BE8.md) (function, `0x00265BE8`)
- `0x003F255B` → [FsRtlpGrantAnyOplockFromExclusive](../58/FsRtlpGrantAnyOplockFromExclusive_function_00582540.md) (function, `0x00582540`)
- `0x003F2581` → [FsRtlpRemoveAndCompleteWaitingIrp](../42/FsRtlpRemoveAndCompleteWaitingIrp_function_00425FC0.md) (function, `0x00425FC0`)
- `0x003F259D` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x003F25B5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x003F2663` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x003F2674` → [ExReleaseFastMutexUnsafe](../25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)

### Direct callers
- [FsRtlpOplockFsctrlInternal](../../page/9F/FsRtlpOplockFsctrlInternal_function_009F1640.md) at `0x009F1A80`

### Static image references
- `0x003F199D` → RVA `0x00E0A740` (`.data`; read)
- `0x003F1A09` → RVA `0x00E06C50` (`.data`; read)
- `0x003F1ABD` → RVA `0x00045433` (`.rdata`; read)
- `0x003F1FF4` → RVA `0x0004574F` (`.rdata`; read)
- `0x003F21FD` → RVA `0x00582520` (`FsRtlpExclusiveIrpCancelRoutine`; read)
- `0x003F2372` → RVA `0x000456C9` (`.rdata`; read)
- `0x003F2655` → RVA `0x00045823` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **13**
  - `0x003F1BB7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x003F1CE5` → [FsRtlpOplockPerfMoveData](../../page/71/FsRtlpOplockPerfMoveData_function_00715308.md) (`.text` → `PAGE`)
  - `0x003F1CFA` → [FsRtlpOplockMoveAckTimeout](../../page/71/FsRtlpOplockMoveAckTimeout_function_00715108.md) (`.text` → `PAGE`)
  - `0x003F1DF5` → [FsRtlpOplockUpperLowerCompatible](../../page/A2/FsRtlpOplockUpperLowerCompatible_function_00A21E04.md) (`.text` → `PAGE`)
  - `0x003F1E96` → [FsRtlpOplockUpperLowerCompatible](../../page/A2/FsRtlpOplockUpperLowerCompatible_function_00A21E04.md) (`.text` → `PAGE`)
  - `0x003F1F22` → [FsRtlpOplockPerfMoveData](../../page/71/FsRtlpOplockPerfMoveData_function_00715308.md) (`.text` → `PAGE`)
  - `0x003F1F2F` → [FsRtlpOplockMoveAckTimeout](../../page/71/FsRtlpOplockMoveAckTimeout_function_00715108.md) (`.text` → `PAGE`)
  - `0x003F2084` → [FsRtlpOplockPerfMoveData](../../page/71/FsRtlpOplockPerfMoveData_function_00715308.md) (`.text` → `PAGE`)
  - `0x003F2094` → [FsRtlpOplockMoveAckTimeout](../../page/71/FsRtlpOplockMoveAckTimeout_function_00715108.md) (`.text` → `PAGE`)
  - `0x003F219A` → [FsRtlpOplockPerfMoveData](../../page/71/FsRtlpOplockPerfMoveData_function_00715308.md) (`.text` → `PAGE`)
  - `0x003F21AF` → [FsRtlpOplockMoveAckTimeout](../../page/71/FsRtlpOplockMoveAckTimeout_function_00715108.md) (`.text` → `PAGE`)
  - `0x003F2255` → [FsRtlpOplockPerfSendData](../../page/6F/FsRtlpOplockPerfSendData_function_006FDB80.md) (`.text` → `PAGE`)
  - `0x003F25B5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003F1988  4C 8B DC                        mov r11, rsp
003F198B  53                              push rbx
003F198C  56                              push rsi
003F198D  57                              push rdi
003F198E  41 54                           push r12
003F1990  41 55                           push r13
003F1992  41 56                           push r14
003F1994  41 57                           push r15
003F1996  48 81 EC 40 02 00 00            sub rsp, 0x240
003F199D  48 8B 05 9C 8D A1 00            mov rax, qword ptr [rip + 0xa18d9c]
003F19A4  48 33 C4                        xor rax, rsp
003F19A7  48 89 84 24 30 02 00 00         mov qword ptr [rsp + 0x230], rax
003F19AF  45 8B F9                        mov r15d, r9d
003F19B2  49 8B D8                        mov rbx, r8
003F19B5  48 89 94 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdx
003F19BD  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
003F19C2  48 8B 84 24 A0 02 00 00         mov rax, qword ptr [rsp + 0x2a0]
003F19CA  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
003F19D2  45 33 E4                        xor r12d, r12d
003F19D5  44 89 64 24 5C                  mov dword ptr [rsp + 0x5c], r12d
003F19DA  45 8B F4                        mov r14d, r12d
003F19DD  4C 89 64 24 70                  mov qword ptr [rsp + 0x70], r12
003F19E2  44 88 64 24 60                  mov byte ptr [rsp + 0x60], r12b
003F19E7  41 8A C4                        mov al, r12b
003F19EA  88 44 24 64                     mov byte ptr [rsp + 0x64], al
003F19EE  88 44 24 78                     mov byte ptr [rsp + 0x78], al
003F19F2  44 88 64 24 61                  mov byte ptr [rsp + 0x61], r12b
003F19F7  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
003F19FB  88 44 24 79                     mov byte ptr [rsp + 0x79], al
003F19FF  44 88 64 24 63                  mov byte ptr [rsp + 0x63], r12b
003F1A04  44 88 64 24 62                  mov byte ptr [rsp + 0x62], r12b
003F1A09  83 3D 40 52 A1 00 05            cmp dword ptr [rip + 0xa15240], 5
003F1A10  0F 86 BF 00 00 00               jbe 0x1403f1ad5
003F1A16  45 89 8B 2C FE FF FF            mov dword ptr [r11 - 0x1d4], r9d
003F1A1D  49 8D 83 2C FE FF FF            lea rax, [r11 - 0x1d4]
003F1A24  49 89 83 E8 FE FF FF            mov qword ptr [r11 - 0x118], rax
003F1A2B  49 C7 83 F0 FE FF FF 04 00 00 00  mov qword ptr [r11 - 0x110], 4
003F1A36  8B 84 24 A8 02 00 00            mov eax, dword ptr [rsp + 0x2a8]
003F1A3D  89 84 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], eax
003F1A44  49 8D 83 38 FE FF FF            lea rax, [r11 - 0x1c8]
003F1A4B  49 89 83 F8 FE FF FF            mov qword ptr [r11 - 0x108], rax
003F1A52  49 C7 83 00 FF FF FF 04 00 00 00  mov qword ptr [r11 - 0x100], 4
003F1A5D  49 89 8B 40 FE FF FF            mov qword ptr [r11 - 0x1c0], rcx
003F1A64  49 8D 83 40 FE FF FF            lea rax, [r11 - 0x1c0]
003F1A6B  49 89 83 08 FF FF FF            mov qword ptr [r11 - 0xf8], rax
003F1A72  49 C7 83 10 FF FF FF 08 00 00 00  mov qword ptr [r11 - 0xf0], 8
003F1A7D  8B 81 90 00 00 00               mov eax, dword ptr [rcx + 0x90]
003F1A83  89 84 24 84 00 00 00            mov dword ptr [rsp + 0x84], eax
003F1A8A  49 8D 83 0C FE FF FF            lea rax, [r11 - 0x1f4]
003F1A91  49 89 83 18 FF FF FF            mov qword ptr [r11 - 0xe8], rax
003F1A98  49 C7 83 20 FF FF FF 04 00 00 00  mov qword ptr [r11 - 0xe0], 4
003F1AA3  49 8D 83 C8 FE FF FF            lea rax, [r11 - 0x138]
003F1AAA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003F1AAF  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
003F1AB7  45 33 C9                        xor r9d, r9d
003F1ABA  45 33 C0                        xor r8d, r8d
003F1ABD  48 8D 15 6F 39 C5 FF            lea rdx, [rip - 0x3ac691]
003F1AC4  48 8D 0D 85 51 A1 00            lea rcx, [rip + 0xa15185]
003F1ACB  E8 10 46 03 00                  call 0x1404260e0
003F1AD0  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
003F1AD5  48 85 C9                        test rcx, rcx
003F1AD8  75 39                           jne 0x1403f1b13
003F1ADA  BF E3 00 00 C0                  mov edi, 0xc00000e3
003F1ADF  89 7B 30                        mov dword ptr [rbx + 0x30], edi
003F1AE2  8D 51 01                        lea edx, [rcx + 1]
003F1AE5  48 8B CB                        mov rcx, rbx
003F1AE8  E8 D3 9A EA FF                  call 0x14029b5c0
003F1AED  8B C7                           mov eax, edi
003F1AEF  48 8B 8C 24 30 02 00 00         mov rcx, qword ptr [rsp + 0x230]
003F1AF7  48 33 CC                        xor rcx, rsp
003F1AFA  E8 41 AB 2B 00                  call 0x1406ac640
003F1AFF  48 81 C4 40 02 00 00            add rsp, 0x240
003F1B06  41 5F                           pop r15
003F1B08  41 5E                           pop r14
003F1B0A  41 5D                           pop r13
003F1B0C  41 5C                           pop r12
003F1B0E  5F                              pop rdi
003F1B0F  5E                              pop rsi
003F1B10  5B                              pop rbx
003F1B11  C3                              ret
003F1B12  CC                              int3
003F1B13  48 8B 89 98 00 00 00            mov rcx, qword ptr [rcx + 0x98]
003F1B1A  E8 01 1C 00 00                  call 0x1403f3720
003F1B1F  BE 01 00 00 00                  mov esi, 1
003F1B24  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F1B29  8B 88 90 00 00 00               mov ecx, dword ptr [rax + 0x90]
003F1B2F  BF DF FF F0 01                  mov edi, 0x1f0ffdf
003F1B34  41 BD 00 30 00 00               mov r13d, 0x3000
003F1B3A  F7 C1 00 00 F0 00               test ecx, 0xf00000
003F1B40  75 0E                           jne 0x1403f1b50
003F1B42  8B C1                           mov eax, ecx
003F1B44  23 C7                           and eax, edi
003F1B46  41 2B C5                        sub eax, r13d
003F1B49  A9 FF 7F FF FF                  test eax, 0xffff7fff
003F1B4E  75 1B                           jne 0x1403f1b6b
003F1B50  23 CF                           and ecx, edi
003F1B52  41 2B CD                        sub ecx, r13d
003F1B55  F7 C1 FF 7F FF FF               test ecx, 0xffff7fff
003F1B5B  75 2A                           jne 0x1403f1b87
003F1B5D  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F1B62  48 83 C0 48                     add rax, 0x48
003F1B66  48 39 00                        cmp qword ptr [rax], rax
003F1B69  75 1C                           jne 0x1403f1b87
003F1B6B  BF E3 00 00 C0                  mov edi, 0xc00000e3
003F1B70  89 7C 24 5C                     mov dword ptr [rsp + 0x5c], edi
003F1B74  89 7B 30                        mov dword ptr [rbx + 0x30], edi
003F1B77  40 8A D6                        mov dl, sil
003F1B7A  48 8B CB                        mov rcx, rbx
003F1B7D  E8 3E 9A EA FF                  call 0x14029b5c0
003F1B82  E9 24 0A 00 00                  jmp 0x1403f25ab
003F1B87  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
003F1B8B  48 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rax
003F1B93  44 8B 60 08                     mov r12d, dword ptr [rax + 8]
003F1B97  41 83 E4 04                     and r12d, 4
003F1B9B  0F 95 44 24 58                  setne byte ptr [rsp + 0x58]
003F1BA0  45 33 D2                        xor r10d, r10d
003F1BA3  45 85 E4                        test r12d, r12d
003F1BA6  74 1F                           je 0x1403f1bc7
003F1BA8  41 8D 52 30                     lea edx, [r10 + 0x30]
003F1BAC  B9 20 01 00 00                  mov ecx, 0x120
003F1BB1  41 B8 46 53 72 6F               mov r8d, 0x6f725346
003F1BB7  E8 34 05 79 00                  call 0x140b820f0
003F1BBC  4C 8B F0                        mov r14, rax
003F1BBF  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
003F1BC4  45 33 D2                        xor r10d, r10d
003F1BC7  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
003F1BCC  8B 91 90 00 00 00               mov edx, dword ptr [rcx + 0x90]
003F1BD2  23 D7                           and edx, edi
003F1BD4  41 B8 40 70 30 00               mov r8d, 0x307040
003F1BDA  41 3B D0                        cmp edx, r8d
003F1BDD  0F 87 39 01 00 00               ja 0x1403f1d1c
003F1BE3  74 35                           je 0x1403f1c1a
003F1BE5  41 3B D5                        cmp edx, r13d
003F1BE8  0F 84 5F 01 00 00               je 0x1403f1d4d
003F1BEE  81 FA 00 B0 00 00               cmp edx, 0xb000
003F1BF4  0F 84 53 01 00 00               je 0x1403f1d4d
003F1BFA  81 FA 00 30 10 00               cmp edx, 0x103000
003F1C00  0F 84 47 01 00 00               je 0x1403f1d4d
003F1C06  81 FA 40 50 10 00               cmp edx, 0x105040
003F1C0C  74 0C                           je 0x1403f1c1a
003F1C0E  81 FA 40 70 10 00               cmp edx, 0x107040
003F1C14  0F 85 51 FF FF FF               jne 0x1403f1b6b
003F1C1A  4C 8B AC 24 88 00 00 00         mov r13, qword ptr [rsp + 0x88]
003F1C22  45 85 E4                        test r12d, r12d
003F1C25  74 35                           je 0x1403f1c5c
003F1C27  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F1C2C  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
003F1C30  49 8B 4D 30                     mov rcx, qword ptr [r13 + 0x30]
003F1C34  48 3B D1                        cmp rdx, rcx
003F1C37  0F 84 2E FF FF FF               je 0x1403f1b6b
003F1C3D  45 33 C0                        xor r8d, r8d
003F1C40  E8 6B 0A 00 00                  call 0x1403f26b0
003F1C45  88 44 24 66                     mov byte ptr [rsp + 0x66], al
003F1C49  84 C0                           test al, al
003F1C4B  0F 84 1A FF FF FF               je 0x1403f1b6b
003F1C51  41 B8 40 70 30 00               mov r8d, 0x307040
003F1C57  45 85 E4                        test r12d, r12d
003F1C5A  75 1C                           jne 0x1403f1c78
003F1C5C  49 8B 4D 30                     mov rcx, qword ptr [r13 + 0x30]
003F1C60  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F1C65  48 39 48 08                     cmp qword ptr [rax + 8], rcx
003F1C69  0F 85 FC FE FF FF               jne 0x1403f1b6b
003F1C6F  45 85 E4                        test r12d, r12d
003F1C72  0F 84 47 07 00 00               je 0x1403f23bf
003F1C78  45 33 E4                        xor r12d, r12d
003F1C7B  45 85 FF                        test r15d, r15d
003F1C7E  0F 85 3E 07 00 00               jne 0x1403f23c2
003F1C84  45 33 C0                        xor r8d, r8d
003F1C87  33 D2                           xor edx, edx
003F1C89  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
003F1C8E  E8 05 94 09 00                  call 0x14048b098
003F1C93  33 D2                           xor edx, edx
003F1C95  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
003F1C9A  E8 49 3F E7 FF                  call 0x140265be8
003F1C9F  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F1CA4  44 88 60 20                     mov byte ptr [rax + 0x20], r12b
003F1CA8  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F1CAD  8B 88 90 00 00 00               mov ecx, dword ptr [rax + 0x90]
003F1CB3  83 E1 20                        and ecx, 0x20
003F1CB6  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F1CBB  0B CE                           or ecx, esi
003F1CBD  89 88 90 00 00 00               mov dword ptr [rax + 0x90], ecx
003F1CC3  4C 8B 4C 24 70                  mov r9, qword ptr [rsp + 0x70]
003F1CC8  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F1CCD  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
003F1CD1  49 89 49 10                     mov qword ptr [r9 + 0x10], rcx
003F1CD5  49 8D 51 18                     lea rdx, [r9 + 0x18]
003F1CD9  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
003F1CDE  48 81 C1 A8 00 00 00            add rcx, 0xa8
003F1CE5  E8 1E 36 32 00                  call 0x140715308
003F1CEA  49 8D 51 28                     lea rdx, [r9 + 0x28]
003F1CEE  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
003F1CF3  48 81 C1 B8 00 00 00            add rcx, 0xb8
003F1CFA  E8 09 34 32 00                  call 0x140715108
003F1CFF  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
003F1D04  48 83 C1 68                     add rcx, 0x68
003F1D08  48 8B 01                        mov rax, qword ptr [rcx]
003F1D0B  48 39 48 08                     cmp qword ptr [rax + 8], rcx
003F1D0F  0F 84 AD 05 00 00               je 0x1403f22c2
003F1D15  B9 03 00 00 00                  mov ecx, 3
003F1D1A  CD 29                           int 0x29
003F1D1C  81 FA 00 30 80 00               cmp edx, 0x803000
003F1D22  74 29                           je 0x1403f1d4d
003F1D24  81 FA 40 70 50 00               cmp edx, 0x507040
003F1D2A  0F 84 EA FE FF FF               je 0x1403f1c1a
003F1D30  81 FA 40 50 80 00               cmp edx, 0x805040
003F1D36  0F 84 DE FE FF FF               je 0x1403f1c1a
003F1D3C  81 FA 40 70 80 00               cmp edx, 0x807040
003F1D42  0F 84 D2 FE FF FF               je 0x1403f1c1a
003F1D48  E9 1E FE FF FF                  jmp 0x1403f1b6b
003F1D4D  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F1D52  48 8B 78 48                     mov rdi, qword ptr [rax + 0x48]
003F1D56  48 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdi
003F1D5E  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F1D63  48 83 C0 48                     add rax, 0x48
003F1D67  48 3B F8                        cmp rdi, rax
003F1D6A  0F 84 20 05 00 00               je 0x1403f2290
003F1D70  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
003F1D78  45 85 E4                        test r12d, r12d
003F1D7B  75 13                           jne 0x1403f1d90
003F1D7D  48 8B 41 30                     mov rax, qword ptr [rcx + 0x30]
003F1D81  48 39 47 18                     cmp qword ptr [rdi + 0x18], rax
003F1D85  74 31                           je 0x1403f1db8
003F1D87  45 85 E4                        test r12d, r12d
003F1D8A  0F 84 F8 04 00 00               je 0x1403f2288
003F1D90  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
003F1D94  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
003F1D98  48 3B D1                        cmp rdx, rcx
003F1D9B  0F 84 E7 04 00 00               je 0x1403f2288
003F1DA1  45 33 C0                        xor r8d, r8d
003F1DA4  E8 07 09 00 00                  call 0x1403f26b0
003F1DA9  88 44 24 66                     mov byte ptr [rsp + 0x66], al
003F1DAD  45 33 D2                        xor r10d, r10d
003F1DB0  84 C0                           test al, al
003F1DB2  0F 84 D0 04 00 00               je 0x1403f2288
003F1DB8  40 88 74 24 60                  mov byte ptr [rsp + 0x60], sil
003F1DBD  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
003F1DC0  25 00 00 F0 00                  and eax, 0xf00000
003F1DC5  3D 00 00 80 00                  cmp eax, 0x800000
003F1DCA  0F 85 92 00 00 00               jne 0x1403f1e62
003F1DD0  44 8B AC 24 A8 02 00 00         mov r13d, dword ptr [rsp + 0x2a8]
003F1DD8  45 85 FF                        test r15d, r15d
003F1DDB  0F 84 20 01 00 00               je 0x1403f1f01
003F1DE1  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F1DE6  48 83 C0 58                     add rax, 0x58
003F1DEA  48 39 00                        cmp qword ptr [rax], rax
003F1DED  75 13                           jne 0x1403f1e02
003F1DEF  41 8B D5                        mov edx, r13d
003F1DF2  41 8B CF                        mov ecx, r15d
003F1DF5  E8 0A 00 63 00                  call 0x140a21e04
003F1DFA  84 C0                           test al, al
003F1DFC  0F 85 FF 00 00 00               jne 0x1403f1f01
003F1E02  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
003F1E06  0F 57 C0                        xorps xmm0, xmm0
003F1E09  33 C0                           xor eax, eax
003F1E0B  0F 11 01                        movups xmmword ptr [rcx], xmm0
003F1E0E  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
003F1E12  C7 41 04 03 00 00 00            mov dword ptr [rcx + 4], 3
003F1E19  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F1E1E  48 83 C0 58                     add rax, 0x58
003F1E22  48 39 00                        cmp qword ptr [rax], rax
003F1E25  41 BC 00 00 00 00               mov r12d, 0
003F1E2B  45 0F 45 EC                     cmovne r13d, r12d
003F1E2F  44 89 69 08                     mov dword ptr [rcx + 8], r13d
003F1E33  8B 41 0C                        mov eax, dword ptr [rcx + 0xc]
003F1E36  0B C6                           or eax, esi
003F1E38  89 41 0C                        mov dword ptr [rcx + 0xc], eax
003F1E3B  48 C7 43 38 18 00 00 00         mov qword ptr [rbx + 0x38], 0x18
003F1E43  BF 2E 00 00 80                  mov edi, 0x8000002e
003F1E48  89 7B 30                        mov dword ptr [rbx + 0x30], edi
003F1E4B  40 8A D6                        mov dl, sil
003F1E4E  48 8B CB                        mov rcx, rbx
003F1E51  E8 6A 97 EA FF                  call 0x14029b5c0
003F1E56  89 7C 24 5C                     mov dword ptr [rsp + 0x5c], edi
003F1E5A  40 8A FE                        mov dil, sil
003F1E5D  E9 36 04 00 00                  jmp 0x1403f2298
003F1E62  3D 00 00 10 00                  cmp eax, 0x100000
003F1E67  0F 85 8C 00 00 00               jne 0x1403f1ef9
003F1E6D  41 8B C7                        mov eax, r15d
003F1E70  25 00 70 00 00                  and eax, 0x7000
003F1E75  41 3B C5                        cmp eax, r13d
003F1E78  44 8B AC 24 A8 02 00 00         mov r13d, dword ptr [rsp + 0x2a8]
003F1E80  76 7F                           jbe 0x1403f1f01
003F1E82  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F1E87  48 83 C0 58                     add rax, 0x58
003F1E8B  48 39 00                        cmp qword ptr [rax], rax
003F1E8E  75 0F                           jne 0x1403f1e9f
003F1E90  41 8B D5                        mov edx, r13d
003F1E93  41 8B CF                        mov ecx, r15d
003F1E96  E8 69 FF 62 00                  call 0x140a21e04
003F1E9B  84 C0                           test al, al
003F1E9D  75 62                           jne 0x1403f1f01
003F1E9F  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
003F1EA3  0F 57 C0                        xorps xmm0, xmm0
003F1EA6  33 C0                           xor eax, eax
003F1EA8  0F 11 01                        movups xmmword ptr [rcx], xmm0
003F1EAB  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
003F1EAF  C7 41 04 03 00 00 00            mov dword ptr [rcx + 4], 3
003F1EB6  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F1EBB  48 83 C0 58                     add rax, 0x58
003F1EBF  48 39 00                        cmp qword ptr [rax], rax
003F1EC2  44 0F 45 EE                     cmovne r13d, esi
003F1EC6  44 89 69 08                     mov dword ptr [rcx + 8], r13d
003F1ECA  8B 41 0C                        mov eax, dword ptr [rcx + 0xc]
003F1ECD  0B C6                           or eax, esi
003F1ECF  89 41 0C                        mov dword ptr [rcx + 0xc], eax
003F1ED2  48 C7 43 38 18 00 00 00         mov qword ptr [rbx + 0x38], 0x18
003F1EDA  BF 2E 00 00 80                  mov edi, 0x8000002e
003F1EDF  89 7B 30                        mov dword ptr [rbx + 0x30], edi
003F1EE2  40 8A D6                        mov dl, sil
003F1EE5  48 8B CB                        mov rcx, rbx
003F1EE8  E8 D3 96 EA FF                  call 0x14029b5c0
003F1EED  89 7C 24 5C                     mov dword ptr [rsp + 0x5c], edi
003F1EF1  40 8A FE                        mov dil, sil
003F1EF4  E9 9C 03 00 00                  jmp 0x1403f2295
003F1EF9  44 8B AC 24 A8 02 00 00         mov r13d, dword ptr [rsp + 0x2a8]
003F1F01  48 8B CF                        mov rcx, rdi
003F1F04  E8 F3 39 03 00                  call 0x1404258fc
003F1F09  45 85 E4                        test r12d, r12d
003F1F0C  0F 84 02 01 00 00               je 0x1403f2014
003F1F12  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
003F1F16  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
003F1F1A  49 8D 56 18                     lea rdx, [r14 + 0x18]
003F1F1E  48 8D 4F 48                     lea rcx, [rdi + 0x48]
003F1F22  E8 E1 33 32 00                  call 0x140715308
003F1F27  49 8D 56 28                     lea rdx, [r14 + 0x28]
003F1F2B  48 8D 4F 58                     lea rcx, [rdi + 0x58]
003F1F2F  E8 D4 31 32 00                  call 0x140715108
003F1F34  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
003F1F39  48 83 C1 68                     add rcx, 0x68
003F1F3D  48 8B 01                        mov rax, qword ptr [rcx]
003F1F40  48 39 48 08                     cmp qword ptr [rax + 8], rcx
003F1F44  0F 85 CB FD FF FF               jne 0x1403f1d15
003F1F4A  49 89 06                        mov qword ptr [r14], rax
003F1F4D  49 89 4E 08                     mov qword ptr [r14 + 8], rcx
003F1F51  4C 89 70 08                     mov qword ptr [rax + 8], r14
003F1F55  4C 89 31                        mov qword ptr [rcx], r14
003F1F58  83 3D F1 4C A1 00 05            cmp dword ptr [rip + 0xa14cf1], 5
003F1F5F  0F 86 A5 00 00 00               jbe 0x1403f200a
003F1F65  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
003F1F69  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
003F1F71  48 8D 84 24 C0 00 00 00         lea rax, [rsp + 0xc0]
003F1F79  48 89 84 24 C0 01 00 00         mov qword ptr [rsp + 0x1c0], rax
003F1F81  48 C7 84 24 C8 01 00 00 08 00 00 00  mov qword ptr [rsp + 0x1c8], 8
003F1F8D  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F1F92  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
003F1F9A  48 8D 94 24 C8 00 00 00         lea rdx, [rsp + 0xc8]
003F1FA2  48 89 94 24 D0 01 00 00         mov qword ptr [rsp + 0x1d0], rdx
003F1FAA  48 C7 84 24 D8 01 00 00 08 00 00 00  mov qword ptr [rsp + 0x1d8], 8
003F1FB6  8B 80 90 00 00 00               mov eax, dword ptr [rax + 0x90]
003F1FBC  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
003F1FC0  48 8D 44 24 68                  lea rax, [rsp + 0x68]
003F1FC5  48 89 84 24 E0 01 00 00         mov qword ptr [rsp + 0x1e0], rax
003F1FCD  48 C7 84 24 E8 01 00 00 04 00 00 00  mov qword ptr [rsp + 0x1e8], 4
003F1FD9  48 8D 84 24 A0 01 00 00         lea rax, [rsp + 0x1a0]
003F1FE1  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003F1FE6  C7 44 24 20 05 00 00 00         mov dword ptr [rsp + 0x20], 5
003F1FEE  45 33 C9                        xor r9d, r9d
003F1FF1  45 33 C0                        xor r8d, r8d
003F1FF4  48 8D 15 54 37 C5 FF            lea rdx, [rip - 0x3ac8ac]
003F1FFB  48 8D 0D 4E 4C A1 00            lea rcx, [rip + 0xa14c4e]
003F2002  E8 D9 40 03 00                  call 0x1404260e0
003F2007  45 33 D2                        xor r10d, r10d
003F200A  4D 8B F2                        mov r14, r10
003F200D  4C 89 54 24 70                  mov qword ptr [rsp + 0x70], r10
003F2012  EB 18                           jmp 0x1403f202c
003F2014  40 88 74 24 61                  mov byte ptr [rsp + 0x61], sil
003F2019  45 85 FF                        test r15d, r15d
003F201C  75 36                           jne 0x1403f2054
003F201E  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
003F2022  BA 44 66 6C 74                  mov edx, 0x746c6644
003F2027  E8 B4 58 F0 FF                  call 0x1402f78e0
003F202C  45 85 FF                        test r15d, r15d
003F202F  75 23                           jne 0x1403f2054
003F2031  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
003F2036  E8 B1 36 03 00                  call 0x1404256ec
003F203B  44 21 7C 24 5C                  and dword ptr [rsp + 0x5c], r15d
003F2040  44 21 7B 30                     and dword ptr [rbx + 0x30], r15d
003F2044  40 8A D6                        mov dl, sil
003F2047  48 8B CB                        mov rcx, rbx
003F204A  E8 71 95 EA FF                  call 0x14029b5c0
003F204F  E9 CE 01 00 00                  jmp 0x1403f2222
003F2054  41 F7 C7 10 30 00 00            test r15d, 0x3010
003F205B  0F 95 C1                        setne cl
003F205E  41 F7 C7 40 40 00 00            test r15d, 0x4040
003F2065  0F 94 C0                        sete al
003F2068  84 C8                           test al, cl
003F206A  74 65                           je 0x1403f20d1
003F206C  4C 8B 8C 24 98 00 00 00         mov r9, qword ptr [rsp + 0x98]
003F2074  4D 85 C9                        test r9, r9
003F2077  74 20                           je 0x1403f2099
003F2079  49 8B 11                        mov rdx, qword ptr [r9]
003F207C  48 83 C2 48                     add rdx, 0x48
003F2080  48 8D 4F 48                     lea rcx, [rdi + 0x48]
003F2084  E8 7F 32 32 00                  call 0x140715308
003F2089  49 8B 11                        mov rdx, qword ptr [r9]
003F208C  48 83 C2 58                     add rdx, 0x58
003F2090  48 8D 4F 58                     lea rcx, [rdi + 0x58]
003F2094  E8 6F 30 32 00                  call 0x140715108
003F2099  44 89 6C 24 38                  mov dword ptr [rsp + 0x38], r13d
003F209E  40 88 74 24 30                  mov byte ptr [rsp + 0x30], sil
003F20A3  8A 44 24 58                     mov al, byte ptr [rsp + 0x58]
003F20A7  88 44 24 28                     mov byte ptr [rsp + 0x28], al
003F20AB  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
003F20B0  45 8B CF                        mov r9d, r15d
003F20B3  4C 8B C3                        mov r8, rbx
003F20B6  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
003F20BE  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
003F20C3  E8 00 4E 0F 00                  call 0x1404e6ec8
003F20C8  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
003F20CC  E9 51 01 00 00                  jmp 0x1403f2222
003F20D1  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F20D6  48 89 18                        mov qword ptr [rax], rbx
003F20D9  48 8B 83 B8 00 00 00            mov rax, qword ptr [rbx + 0xb8]
003F20E0  40 08 70 03                     or byte ptr [rax + 3], sil
003F20E4  C7 44 24 5C 03 01 00 00         mov dword ptr [rsp + 0x5c], 0x103
003F20EC  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F20F1  48 89 43 38                     mov qword ptr [rbx + 0x38], rax
003F20F5  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
003F20FE  48 89 8C 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rcx
003F2106  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
003F210D  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F2112  48 89 48 10                     mov qword ptr [rax + 0x10], rcx
003F2116  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
003F211F  48 89 8C 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rcx
003F2127  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F212C  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
003F2130  BA 44 66 6C 74                  mov edx, 0x746c6644
003F2135  E8 D6 E5 E1 FF                  call 0x140210710
003F213A  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F213F  C6 40 20 00                     mov byte ptr [rax + 0x20], 0
003F2143  45 85 E4                        test r12d, r12d
003F2146  74 2D                           je 0x1403f2175
003F2148  4C 8B AC 24 88 00 00 00         mov r13, qword ptr [rsp + 0x88]
003F2150  49 8B 4D 30                     mov rcx, qword ptr [r13 + 0x30]
003F2154  BA 44 66 6C 74                  mov edx, 0x746c6644
003F2159  E8 B2 E5 E1 FF                  call 0x140210710
003F215E  49 8B 4D 30                     mov rcx, qword ptr [r13 + 0x30]
003F2162  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F2167  48 89 48 08                     mov qword ptr [rax + 8], rcx
003F216B  4C 8B 8C 24 90 00 00 00         mov r9, qword ptr [rsp + 0x90]
003F2173  EB 15                           jmp 0x1403f218a
003F2175  4C 8B 8C 24 90 00 00 00         mov r9, qword ptr [rsp + 0x90]
003F217D  49 8B 49 18                     mov rcx, qword ptr [r9 + 0x18]
003F2181  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F2186  48 89 48 08                     mov qword ptr [rax + 8], rcx
003F218A  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
003F218F  48 81 C2 A8 00 00 00            add rdx, 0xa8
003F2196  49 8D 49 48                     lea rcx, [r9 + 0x48]
003F219A  E8 69 31 32 00                  call 0x140715308
003F219F  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
003F21A4  48 81 C2 B8 00 00 00            add rdx, 0xb8
003F21AB  49 8D 49 58                     lea rcx, [r9 + 0x58]
003F21AF  E8 54 2F 32 00                  call 0x140715108
003F21B4  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
003F21B9  8B 91 90 00 00 00               mov edx, dword ptr [rcx + 0x90]
003F21BF  83 E2 20                        and edx, 0x20
003F21C2  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F21C7  44 0B FA                        or r15d, edx
003F21CA  41 83 CF 40                     or r15d, 0x40
003F21CE  44 89 B8 90 00 00 00            mov dword ptr [rax + 0x90], r15d
003F21D5  B9 07 00 00 00                  mov ecx, 7
003F21DA  E8 A1 1B E8 FF                  call 0x140273d80
003F21DF  88 43 45                        mov byte ptr [rbx + 0x45], al
003F21E2  80 7B 44 00                     cmp byte ptr [rbx + 0x44], 0
003F21E6  74 15                           je 0x1403f21fd
003F21E8  44 8A 44 24 58                  mov r8b, byte ptr [rsp + 0x58]
003F21ED  44 32 C6                        xor r8b, sil
003F21F0  40 8A D6                        mov dl, sil
003F21F3  48 8B CB                        mov rcx, rbx
003F21F6  E8 D1 74 10 00                  call 0x1404f96cc
003F21FB  EB 18                           jmp 0x1403f2215
003F21FD  48 8D 05 1C 03 19 00            lea rax, [rip + 0x19031c]
003F2204  48 87 43 68                     xchg qword ptr [rbx + 0x68], rax
003F2208  8A 53 45                        mov dl, byte ptr [rbx + 0x45]
003F220B  B9 07 00 00 00                  mov ecx, 7
003F2210  E8 2B 03 E8 FF                  call 0x140272540
003F2215  48 8B BC 24 90 00 00 00         mov rdi, qword ptr [rsp + 0x90]
003F221D  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
003F2222  45 33 C0                        xor r8d, r8d
003F2225  48 8B D7                        mov rdx, rdi
003F2228  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
003F222D  E8 66 8E 09 00                  call 0x14048b098
003F2232  48 8B D7                        mov rdx, rdi
003F2235  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
003F223A  E8 A9 39 E7 FF                  call 0x140265be8
003F223F  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
003F2244  48 8D 41 48                     lea rax, [rcx + 0x48]
003F2248  48 39 00                        cmp qword ptr [rax], rax
003F224B  75 04                           jne 0x1403f2251
003F224D  C6 41 20 00                     mov byte ptr [rcx + 0x20], 0
003F2251  48 8D 4F 48                     lea rcx, [rdi + 0x48]
003F2255  E8 26 B9 30 00                  call 0x1406fdb80
003F225A  40 8A D6                        mov dl, sil
003F225D  48 8B CF                        mov rcx, rdi
003F2260  E8 2F 01 10 00                  call 0x1404f2394
003F2265  45 85 E4                        test r12d, r12d
003F2268  0F 84 83 FC FF FF               je 0x1403f1ef1
003F226E  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
003F2273  8B 81 90 00 00 00               mov eax, dword ptr [rcx + 0x90]
003F2279  0F BA E8 18                     bts eax, 0x18
003F227D  89 81 90 00 00 00               mov dword ptr [rcx + 0x90], eax
003F2283  E9 69 FC FF FF                  jmp 0x1403f1ef1
003F2288  48 8B 3F                        mov rdi, qword ptr [rdi]
003F228B  E9 C6 FA FF FF                  jmp 0x1403f1d56
003F2290  40 8A 7C 24 64                  mov dil, byte ptr [rsp + 0x64]
003F2295  45 33 E4                        xor r12d, r12d
003F2298  44 38 64 24 60                  cmp byte ptr [rsp + 0x60], r12b
003F229D  0F 84 C8 F8 FF FF               je 0x1403f1b6b
003F22A3  44 38 64 24 61                  cmp byte ptr [rsp + 0x61], r12b
003F22A8  74 0A                           je 0x1403f22b4
003F22AA  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
003F22AF  E8 08 3A 03 00                  call 0x140425cbc
003F22B4  40 84 FF                        test dil, dil
003F22B7  0F 84 AC 02 00 00               je 0x1403f2569
003F22BD  E9 E9 02 00 00                  jmp 0x1403f25ab
003F22C2  49 89 01                        mov qword ptr [r9], rax
003F22C5  49 89 49 08                     mov qword ptr [r9 + 8], rcx
003F22C9  4C 89 48 08                     mov qword ptr [rax + 8], r9
003F22CD  4C 89 09                        mov qword ptr [rcx], r9
003F22D0  83 3D 79 49 A1 00 05            cmp dword ptr [rip + 0xa14979], 5
003F22D7  0F 86 A8 00 00 00               jbe 0x1403f2385
003F22DD  49 8B 41 10                     mov rax, qword ptr [r9 + 0x10]
003F22E1  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
003F22E9  48 8D 84 24 B8 00 00 00         lea rax, [rsp + 0xb8]
003F22F1  48 89 84 24 60 01 00 00         mov qword ptr [rsp + 0x160], rax
003F22F9  48 C7 84 24 68 01 00 00 08 00 00 00  mov qword ptr [rsp + 0x168], 8
003F2305  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F230A  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
003F2312  48 8D 94 24 98 00 00 00         lea rdx, [rsp + 0x98]
003F231A  48 89 94 24 70 01 00 00         mov qword ptr [rsp + 0x170], rdx
003F2322  48 C7 84 24 78 01 00 00 08 00 00 00  mov qword ptr [rsp + 0x178], 8
003F232E  8B 80 90 00 00 00               mov eax, dword ptr [rax + 0x90]
003F2334  89 84 24 84 00 00 00            mov dword ptr [rsp + 0x84], eax
003F233B  48 8D 84 24 84 00 00 00         lea rax, [rsp + 0x84]
003F2343  48 89 84 24 80 01 00 00         mov qword ptr [rsp + 0x180], rax
003F234B  48 C7 84 24 88 01 00 00 04 00 00 00  mov qword ptr [rsp + 0x188], 4
003F2357  48 8D 84 24 40 01 00 00         lea rax, [rsp + 0x140]
003F235F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003F2364  C7 44 24 20 05 00 00 00         mov dword ptr [rsp + 0x20], 5
003F236C  45 33 C9                        xor r9d, r9d
003F236F  45 33 C0                        xor r8d, r8d
003F2372  48 8D 15 50 33 C5 FF            lea rdx, [rip - 0x3accb0]
003F2379  48 8D 0D D0 48 A1 00            lea rcx, [rip + 0xa148d0]
003F2380  E8 5B 3D 03 00                  call 0x1404260e0
003F2385  4D 8B F4                        mov r14, r12
003F2388  4C 89 64 24 70                  mov qword ptr [rsp + 0x70], r12
003F238D  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F2392  4C 89 60 08                     mov qword ptr [rax + 8], r12
003F2396  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
003F239B  8B 81 90 00 00 00               mov eax, dword ptr [rcx + 0x90]
003F23A1  0F BA E8 18                     bts eax, 0x18
003F23A5  89 81 90 00 00 00               mov dword ptr [rcx + 0x90], eax
003F23AB  44 89 63 30                     mov dword ptr [rbx + 0x30], r12d
003F23AF  40 8A D6                        mov dl, sil
003F23B2  48 8B CB                        mov rcx, rbx
003F23B5  E8 06 92 EA FF                  call 0x14029b5c0
003F23BA  E9 AA 01 00 00                  jmp 0x1403f2569
003F23BF  45 33 E4                        xor r12d, r12d
003F23C2  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F23C7  8B 90 90 00 00 00               mov edx, dword ptr [rax + 0x90]
003F23CD  8B C2                           mov eax, edx
003F23CF  23 C7                           and eax, edi
003F23D1  3D 40 50 10 00                  cmp eax, 0x105040
003F23D6  0F 84 C4 00 00 00               je 0x1403f24a0
003F23DC  3D 40 70 10 00                  cmp eax, 0x107040
003F23E1  0F 84 B9 00 00 00               je 0x1403f24a0
003F23E7  41 3B C0                        cmp eax, r8d
003F23EA  0F 84 B0 00 00 00               je 0x1403f24a0
003F23F0  3D 40 70 50 00                  cmp eax, 0x507040
003F23F5  0F 84 A5 00 00 00               je 0x1403f24a0
003F23FB  3D 40 50 80 00                  cmp eax, 0x805040
003F2400  0F 84 9A 00 00 00               je 0x1403f24a0
003F2406  3D 40 70 80 00                  cmp eax, 0x807040
003F240B  0F 84 8F 00 00 00               je 0x1403f24a0
003F2411  41 B9 00 00 20 00               mov r9d, 0x200000
003F2417  8B 4C 24 68                     mov ecx, dword ptr [rsp + 0x68]
003F241B  84 C9                           test cl, cl
003F241D  0F 84 C8 00 00 00               je 0x1403f24eb
003F2423  4C 8B 43 18                     mov r8, qword ptr [rbx + 0x18]
003F2427  0F 57 C0                        xorps xmm0, xmm0
003F242A  33 C0                           xor eax, eax
003F242C  41 0F 11 00                     movups xmmword ptr [r8], xmm0
003F2430  49 89 40 10                     mov qword ptr [r8 + 0x10], rax
003F2434  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F2439  8B 88 90 00 00 00               mov ecx, dword ptr [rax + 0x90]
003F243F  C1 E9 0C                        shr ecx, 0xc
003F2442  83 E1 07                        and ecx, 7
003F2445  41 89 48 04                     mov dword ptr [r8 + 4], ecx
003F2449  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F244E  8B 88 90 00 00 00               mov ecx, dword ptr [rax + 0x90]
003F2454  8B D1                           mov edx, ecx
003F2456  D1 EA                           shr edx, 1
003F2458  41 23 D1                        and edx, r9d
003F245B  8B C1                           mov eax, ecx
003F245D  25 00 00 10 00                  and eax, 0x100000
003F2462  0B D0                           or edx, eax
003F2464  D1 EA                           shr edx, 1
003F2466  41 23 C9                        and ecx, r9d
003F2469  0B D1                           or edx, ecx
003F246B  C1 EA 13                        shr edx, 0x13
003F246E  41 89 50 08                     mov dword ptr [r8 + 8], edx
003F2472  41 8B 40 0C                     mov eax, dword ptr [r8 + 0xc]
003F2476  0B C6                           or eax, esi
003F2478  41 89 40 0C                     mov dword ptr [r8 + 0xc], eax
003F247C  48 C7 43 38 18 00 00 00         mov qword ptr [rbx + 0x38], 0x18
003F2484  BF 2E 00 00 80                  mov edi, 0x8000002e
003F2489  89 7B 30                        mov dword ptr [rbx + 0x30], edi
003F248C  40 8A D6                        mov dl, sil
003F248F  48 8B CB                        mov rcx, rbx
003F2492  E8 29 91 EA FF                  call 0x14029b5c0
003F2497  89 7C 24 5C                     mov dword ptr [rsp + 0x5c], edi
003F249B  E9 0B 01 00 00                  jmp 0x1403f25ab
003F24A0  8B CA                           mov ecx, edx
003F24A2  D1 E9                           shr ecx, 1
003F24A4  41 B9 00 00 20 00               mov r9d, 0x200000
003F24AA  41 23 C9                        and ecx, r9d
003F24AD  8B C2                           mov eax, edx
003F24AF  25 00 00 10 00                  and eax, 0x100000
003F24B4  0B C8                           or ecx, eax
003F24B6  D1 E9                           shr ecx, 1
003F24B8  41 23 D1                        and edx, r9d
003F24BB  0B CA                           or ecx, edx
003F24BD  C1 E9 07                        shr ecx, 7
003F24C0  41 8B C7                        mov eax, r15d
003F24C3  25 00 70 00 00                  and eax, 0x7000
003F24C8  3B C1                           cmp eax, ecx
003F24CA  0F 86 47 FF FF FF               jbe 0x1403f2417
003F24D0  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F24D5  48 83 C0 58                     add rax, 0x58
003F24D9  8B 4C 24 68                     mov ecx, dword ptr [rsp + 0x68]
003F24DD  0F B6 C9                        movzx ecx, cl
003F24E0  48 39 00                        cmp qword ptr [rax], rax
003F24E3  0F 45 CE                        cmovne ecx, esi
003F24E6  E9 30 FF FF FF                  jmp 0x1403f241b
003F24EB  45 33 C0                        xor r8d, r8d
003F24EE  33 D2                           xor edx, edx
003F24F0  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
003F24F5  E8 9E 8B 09 00                  call 0x14048b098
003F24FA  33 D2                           xor edx, edx
003F24FC  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
003F2501  E8 E2 36 E7 FF                  call 0x140265be8
003F2506  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F250B  44 88 60 20                     mov byte ptr [rax + 0x20], r12b
003F250F  8B 84 24 A8 02 00 00            mov eax, dword ptr [rsp + 0x2a8]
003F2516  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
003F251A  48 8D 44 24 63                  lea rax, [rsp + 0x63]
003F251F  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
003F2524  48 8D 44 24 62                  lea rax, [rsp + 0x62]
003F2529  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
003F252E  48 8D 44 24 70                  lea rax, [rsp + 0x70]
003F2533  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
003F2538  8A 44 24 58                     mov al, byte ptr [rsp + 0x58]
003F253C  88 44 24 28                     mov byte ptr [rsp + 0x28], al
003F2540  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
003F2548  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003F254D  45 8B CF                        mov r9d, r15d
003F2550  4D 8B C5                        mov r8, r13
003F2553  48 8B D3                        mov rdx, rbx
003F2556  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
003F255B  E8 E0 FF 18 00                  call 0x140582540
003F2560  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
003F2564  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
003F2569  44 38 64 24 62                  cmp byte ptr [rsp + 0x62], r12b
003F256E  74 18                           je 0x1403f2588
003F2570  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F2575  48 83 C0 58                     add rax, 0x58
003F2579  48 8B 08                        mov rcx, qword ptr [rax]
003F257C  48 3B C8                        cmp rcx, rax
003F257F  74 07                           je 0x1403f2588
003F2581  E8 3A 3A 03 00                  call 0x140425fc0
003F2586  EB E8                           jmp 0x1403f2570
003F2588  44 38 64 24 63                  cmp byte ptr [rsp + 0x63], r12b
003F258D  74 1C                           je 0x1403f25ab
003F258F  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F2594  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
003F2598  BA 44 66 6C 74                  mov edx, 0x746c6644
003F259D  E8 3E 53 F0 FF                  call 0x1402f78e0
003F25A2  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F25A7  4C 89 60 08                     mov qword ptr [rax + 8], r12
003F25AB  4D 85 F6                        test r14, r14
003F25AE  74 0A                           je 0x1403f25ba
003F25B0  33 D2                           xor edx, edx
003F25B2  49 8B CE                        mov rcx, r14
003F25B5  E8 B6 02 79 00                  call 0x140b82870
003F25BA  83 3D 8F 46 A1 00 05            cmp dword ptr [rip + 0xa1468f], 5
003F25C1  0F 86 A1 00 00 00               jbe 0x1403f2668
003F25C7  8B 44 24 5C                     mov eax, dword ptr [rsp + 0x5c]
003F25CB  89 44 24 7C                     mov dword ptr [rsp + 0x7c], eax
003F25CF  48 8D 44 24 7C                  lea rax, [rsp + 0x7c]
003F25D4  48 89 84 24 10 01 00 00         mov qword ptr [rsp + 0x110], rax
003F25DC  48 C7 84 24 18 01 00 00 04 00 00 00  mov qword ptr [rsp + 0x118], 4
003F25E8  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003F25ED  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
003F25F5  48 8D 94 24 A8 00 00 00         lea rdx, [rsp + 0xa8]
003F25FD  48 89 94 24 20 01 00 00         mov qword ptr [rsp + 0x120], rdx
003F2605  48 C7 84 24 28 01 00 00 08 00 00 00  mov qword ptr [rsp + 0x128], 8
003F2611  8B 80 90 00 00 00               mov eax, dword ptr [rax + 0x90]
003F2617  89 84 24 80 00 00 00            mov dword ptr [rsp + 0x80], eax
003F261E  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
003F2626  48 89 84 24 30 01 00 00         mov qword ptr [rsp + 0x130], rax
003F262E  48 C7 84 24 38 01 00 00 04 00 00 00  mov qword ptr [rsp + 0x138], 4
003F263A  48 8D 84 24 F0 00 00 00         lea rax, [rsp + 0xf0]
003F2642  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003F2647  C7 44 24 20 05 00 00 00         mov dword ptr [rsp + 0x20], 5
003F264F  45 33 C9                        xor r9d, r9d
003F2652  45 33 C0                        xor r8d, r8d
003F2655  48 8D 15 C7 31 C5 FF            lea rdx, [rip - 0x3ace39]
003F265C  48 8D 0D ED 45 A1 00            lea rcx, [rip + 0xa145ed]
003F2663  E8 78 3A 03 00                  call 0x1404260e0
003F2668  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
003F266D  48 8B 89 98 00 00 00            mov rcx, qword ptr [rcx + 0x98]
003F2674  E8 27 DD E5 FF                  call 0x1402503a0
003F2679  8B 44 24 5C                     mov eax, dword ptr [rsp + 0x5c]
003F267D  E9 6D F4 FF FF                  jmp 0x1403f1aef
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlpAcknowledgeOplockBreakByCacheFlags(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5, unsigned int a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rsp;
    unsigned int v_stack_m1C8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1F0;
    unsigned int v_stack_m1F4;
    unsigned __int8 v_stack_m1FF;
    unsigned __int8 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned int v_stack_m210;
    unsigned __int8 v_stack_m214;
    unsigned __int8 v_stack_m215;
    unsigned __int8 v_stack_m216;
    unsigned __int8 v_stack_m217;
    unsigned __int8 v_stack_m218;
    unsigned int v_stack_m21C;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m250;
    unsigned int v_stack_m258;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p110;
    unsigned __int64 v_stack_p118;
    unsigned __int64 v_stack_p120;
    unsigned __int64 v_stack_p128;
    unsigned __int64 v_stack_p130;
    unsigned __int64 v_stack_p138;
    unsigned __int64 v_stack_p140;
    unsigned __int64 v_stack_p160;
    unsigned __int64 v_stack_p168;
    unsigned __int64 v_stack_p170;
    unsigned __int64 v_stack_p178;
    unsigned __int64 v_stack_p180;
    unsigned __int64 v_stack_p188;
    unsigned __int64 v_stack_p1A0;
    unsigned __int64 v_stack_p1C0;
    unsigned __int64 v_stack_p1C8;
    unsigned __int64 v_stack_p1D0;
    unsigned __int64 v_stack_p1D8;
    unsigned __int64 v_stack_p1E0;
    unsigned __int64 v_stack_p1E8;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int8 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int8 v_stack_p58;
    unsigned int v_stack_p5C;
    unsigned __int8 v_stack_p60;
    unsigned __int8 v_stack_p61;
    unsigned __int64 v_stack_p62;
    unsigned __int64 v_stack_p63;
    unsigned __int8 v_stack_p64;
    unsigned __int8 v_stack_p66;
    unsigned int v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned int v_stack_p7C;
    unsigned int v_stack_p80;
    unsigned int v_stack_p84;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB8;
    unsigned __int64 v_stack_pC0;
    unsigned __int64 v_stack_pC8;
    unsigned __int64 v_stack_pD8;
    unsigned __int64 v_stack_pE0;
    unsigned __int64 v_stack_pE8;
    unsigned __int64 v_stack_pF0;

    v_rsp = (v_rsp) - (576);
    result = (*(unsigned __int64 *)(v_rip + 10587548)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m1F0 = a2;
    v_stack_m228 = a1;
    v_stack_m1E0 = a5;
    v_r12 = 0;
    v_stack_m21C = 0;
    v_stack_m208 = 0;
    v_stack_m218 = 0;
    v_stack_m214 = 0;
    v_stack_m200 = 0;
    v_stack_m217 = 0;
    v_stack_m210 = 0;
    v_stack_m1FF = 0;
    v_stack_m215 = 0;
    v_stack_m216 = 0;
    result = 0;
    if ((*(unsigned int *)(v_rip + 10572352)) >= = 5) {
        *(unsigned int *)(v_rsp - 468) = a4;
        result = v_rsp - 468;
        *(unsigned __int64 *)(v_rsp - 280) = result;
        *(unsigned __int64 *)(v_rsp - 272) = 4;
        result = a6;
        v_stack_m1C8 = (unsigned int)(result);
        result = v_rsp - 456;
        *(unsigned __int64 *)(v_rsp - 264) = result;
        *(unsigned __int64 *)(v_rsp - 256) = 4;
        *(unsigned __int64 *)(v_rsp - 448) = a1;
        result = v_rsp - 448;
        *(unsigned __int64 *)(v_rsp - 248) = result;
        *(unsigned __int64 *)(v_rsp - 240) = 8;
        result = *(unsigned int *)(a1 + 144);
        v_stack_m1F4 = (unsigned int)(result);
        result = v_rsp - 500;
        *(unsigned __int64 *)(v_rsp - 232) = result;
        *(unsigned __int64 *)(v_rsp - 224) = 4;
        result = v_rsp - 312;
        v_stack_m250 = result;
        v_stack_m258 = 6;
        a4 = 0;
        a3 = 0;
        a2 = v_rip - 3851921;
        a1 = v_rip + 10572165;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
        a1 = v_stack_m228;
    }
    if (a1 != 0) goto loc_003F1B13;
    *(unsigned int *)(a3 + 48) = (unsigned int)((unsigned int)(0xC00000E3ULL));
    result = IofCompleteRequest(0, a1 + 1, a3, a4);
loc_003F1AEF:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a1 + 1, a3, a4);
    v_rsp = (v_rsp) + (576);
    return result;
loc_003F1B13:
    result = ExAcquireFastMutexUnsafe(*(unsigned __int64 *)(a1 + 152), a1 + 1, a3, a4);
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p50 + 144)))) & (0xF00000ULL)) != 0) goto loc_003F1B50;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p50 + 144))))) & ((unsigned int)((unsigned int)(0x1F0FFDFULL))));
    result = (unsigned int)((result) - ((unsigned int)((unsigned int)(0x3000ULL))));
    if ((((unsigned int)(result)) & (0xFFFF7FFFULL)) != 0) goto loc_003F1B6B;
loc_003F1B50:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p50 + 144))) & ((unsigned int)((unsigned int)(0x1F0FFDFULL))));
    a1 = (unsigned int)((a1) - ((unsigned int)((unsigned int)(0x3000ULL))));
    if ((((unsigned int)(a1)) & (0xFFFF7FFFULL)) != 0) goto loc_003F1B87;
    result = (v_stack_p50) + (72);
    if ((*(unsigned __int64 *)(result)) != result) goto loc_003F1B87;
loc_003F1B6B:
    v_stack_p5C = (unsigned int)((unsigned int)(0xC00000E3ULL));
    *(unsigned int *)(a3 + 48) = (unsigned int)((unsigned int)(0xC00000E3ULL));
    result = IofCompleteRequest(0, 1, a3, a4);
    goto loc_003F25AB;
loc_003F1B87:
    v_stack_pD8 = *(unsigned __int64 *)(a3 + 24);
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3 + 24) + 8))) & (4));
    v_r10 = 0;
    result = *(unsigned __int64 *)(a3 + 24);
    v_r14 = 0;
    if ((unsigned int)(v_r12) != 0) {
        a2 = v_r10 + 48;
        a1 = 288;
        a3 = 0x6F725346ULL;
        result = ExAllocatePool2(a1, a2, a3, a4);
        v_r14 = result;
        v_stack_p70 = result;
        v_r10 = 0;
    }
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p50 + 144))) & ((unsigned int)((unsigned int)(0xC00000E3ULL))));
    if (((unsigned int)(a2)) > ((unsigned int)((unsigned int)(0x307040ULL)))) goto loc_003F1D1C;
    if (((unsigned int)(a2)) == ((unsigned int)((unsigned int)(0x307040ULL)))) goto loc_003F1C1A;
    if (((unsigned int)(a2)) == ((unsigned int)((unsigned int)(0x3000ULL)))) goto loc_003F1D4D;
    if (((unsigned int)(a2)) == 0xB000ULL) goto loc_003F1D4D;
    if (((unsigned int)(a2)) == 0x103000ULL) goto loc_003F1D4D;
    if (((unsigned int)(a2)) == 0x105040ULL) goto loc_003F1C1A;
    if (((unsigned int)(a2)) != 0x107040ULL) goto loc_003F1B6B;
loc_003F1C1A:
    if ((unsigned int)(v_r12) == 0) goto loc_003F1C5C;
    if ((*(unsigned __int64 *)(v_stack_p50 + 8)) == (*(unsigned __int64 *)(v_stack_p88 + 48))) goto loc_003F1B6B;
    a3 = 0;
    result = FsRtlpOplockKeysEqual(*(unsigned __int64 *)(v_stack_p88 + 48), *(unsigned __int64 *)(v_stack_p50 + 8), a3, a4);
    v_stack_p66 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) == 0) goto loc_003F1B6B;
    if ((unsigned int)(v_r12) != 0) goto loc_003F1C78;
loc_003F1C5C:
    if ((*(unsigned __int64 *)(v_stack_p50 + 8)) != (*(unsigned __int64 *)(v_stack_p88 + 48))) goto loc_003F1B6B;
    if ((unsigned int)(v_r12) == 0) goto loc_003F23BF;
loc_003F1C78:
    v_r12 = 0;
    if ((unsigned int)((unsigned int)(a4)) != 0) goto loc_003F23C2;
    a3 = 0;
    a2 = 0;
    result = FsRtlpModifyThreadPriorities(v_stack_p50, a2, a3, a4);
    a2 = 0;
    result = FsRtlpClearOwner(v_stack_p50, a2, a3, a4);
    *(unsigned __int8 *)(v_stack_p50 + 32) = 0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p50 + 144))) & (32));
    a1 = (unsigned int)((a1) | (1));
    *(unsigned int *)(v_stack_p50 + 144) = (unsigned int)(a1);
    *(unsigned __int64 *)(v_stack_p70 + 16) = *(unsigned __int64 *)(v_stack_p50 + 8);
    a1 = (v_stack_p50) + (168);
    result = FsRtlpOplockPerfMoveData(a1, v_stack_p70 + 24, a3, v_stack_p70);
    a1 = (v_stack_p50) + (184);
    result = FsRtlpOplockMoveAckTimeout(a1, v_stack_p70 + 40, a3, v_stack_p70);
    a1 = (v_stack_p50) + (104);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8)) == a1) goto loc_003F22C2;
loc_003F1D15:
loc_003F1D1C:
    if (((unsigned int)(v_stack_p70 + 40)) == 0x803000ULL) goto loc_003F1D4D;
    if (((unsigned int)(v_stack_p70 + 40)) == 0x507040ULL) goto loc_003F1C1A;
    if (((unsigned int)(v_stack_p70 + 40)) == 0x805040ULL) goto loc_003F1C1A;
    if (((unsigned int)(v_stack_p70 + 40)) == 0x807040ULL) goto loc_003F1C1A;
    goto loc_003F1B6B;
loc_003F1D4D:
loc_003F1D56:
    v_stack_p90 = *(unsigned __int64 *)(v_stack_p50 + 72);
    result = (v_stack_p50) + (72);
    if ((*(unsigned __int64 *)(v_stack_p50 + 72)) == result) goto loc_003F2290;
    if (0 != 0) goto loc_003F1D90;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p50 + 72) + 24)) == (*(unsigned __int64 *)(v_stack_p88 + 48))) goto loc_003F1DB8;
    if (0 == 0) goto loc_003F2288;
loc_003F1D90:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p50 + 72) + 24)) == (*(unsigned __int64 *)(v_stack_p88 + 48))) goto loc_003F2288;
    a3 = 0;
    result = FsRtlpOplockKeysEqual(*(unsigned __int64 *)(v_stack_p88 + 48), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p50 + 72) + 24), a3, v_stack_p70);
    v_stack_p66 = (unsigned __int8)(result);
    v_r10 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_003F2288;
loc_003F1DB8:
    v_stack_p60 = 1;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p50 + 72) + 48))) & (0xF00000ULL));
    if (((unsigned int)(result)) != 0x800000ULL) goto loc_003F1E62;
    if ((unsigned int)((unsigned int)(a4)) == 0) goto loc_003F1F01;
    result = (v_stack_p50) + (88);
    if ((*(unsigned __int64 *)(result)) != result) goto loc_003F1E02;
    result = FsRtlpOplockUpperLowerCompatible((unsigned int)((unsigned int)((unsigned int)(a4))), (unsigned int)((unsigned int)((unsigned int)(a6))), a3, v_stack_p70);
    if ((unsigned __int8)(result) != 0) goto loc_003F1F01;
loc_003F1E02:
    result = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 24)) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 24) + 16) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(a3 + 24) + 4) = 3;
    result = (v_stack_p50) + (88);
    v_r13 = (unsigned int)(a6);
    if ((*(unsigned __int64 *)(result)) != result) { v_r13 = 0; }
    *(unsigned int *)(*(unsigned __int64 *)(a3 + 24) + 8) = (unsigned int)(v_r13);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3 + 24) + 12))) | (1));
    *(unsigned int *)(*(unsigned __int64 *)(a3 + 24) + 12) = (unsigned int)(result);
    *(unsigned __int64 *)(a3 + 56) = 24;
    *(unsigned int *)(a3 + 48) = (unsigned int)((unsigned int)(0x8000002EULL));
    result = IofCompleteRequest(0, 1, a3, v_stack_p70);
    v_stack_p5C = (unsigned int)((unsigned int)(0x8000002EULL));
    goto loc_003F2298;
loc_003F1E62:
    if (((unsigned int)(result)) != 0x100000ULL) goto loc_003F1EF9;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & (0x7000ULL));
    if (((unsigned int)(result)) <= ((unsigned int)(v_r13))) goto loc_003F1F01;
    result = (v_stack_p50) + (88);
    if ((*(unsigned __int64 *)(result)) != result) goto loc_003F1E9F;
    result = FsRtlpOplockUpperLowerCompatible((unsigned int)((unsigned int)((unsigned int)(a4))), (unsigned int)((unsigned int)((unsigned int)(a6))), a3, v_stack_p70);
    if ((unsigned __int8)(result) != 0) goto loc_003F1F01;
loc_003F1E9F:
    result = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 24)) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 24) + 16) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(a3 + 24) + 4) = 3;
    result = (v_stack_p50) + (88);
    v_r13 = (unsigned int)(a6);
    if ((*(unsigned __int64 *)(result)) != result) { v_r13 = 1; }
    *(unsigned int *)(*(unsigned __int64 *)(a3 + 24) + 8) = (unsigned int)(v_r13);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3 + 24) + 12))) | (1));
    *(unsigned int *)(*(unsigned __int64 *)(a3 + 24) + 12) = (unsigned int)(result);
    *(unsigned __int64 *)(a3 + 56) = 24;
    *(unsigned int *)(a3 + 48) = (unsigned int)((unsigned int)(0x8000002EULL));
    result = IofCompleteRequest(0, 1, a3, v_stack_p70);
    v_stack_p5C = (unsigned int)((unsigned int)(0x8000002EULL));
loc_003F1EF1:
    goto loc_003F2295;
loc_003F1EF9:
loc_003F1F01:
    result = FsRtlpOplockDequeueRH(1, 1, a3, v_stack_p70);
    if (0 == 0) goto loc_003F2014;
    *(unsigned __int64 *)(v_r14 + 16) = *(unsigned __int64 *)(1 + 24);
    result = FsRtlpOplockPerfMoveData(1 + 72, v_r14 + 24, a3, v_stack_p70);
    result = FsRtlpOplockMoveAckTimeout(1 + 88, v_r14 + 40, a3, v_stack_p70);
    a1 = (v_stack_p50) + (104);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8)) != a1) goto loc_003F1D15;
    *(unsigned __int64 *)(v_r14) = *(unsigned __int64 *)(a1);
    *(unsigned __int64 *)(v_r14 + 8) = a1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) = v_r14;
    *(unsigned __int64 *)(a1) = v_r14;
    result = *(unsigned __int64 *)(a1);
    if ((*(unsigned int *)(v_rip + 10570993)) >= = 5) {
        result = *(unsigned __int64 *)(v_r14 + 16);
        v_stack_pC0 = result;
        result = v_stack_pC0;
        v_stack_p1C0 = result;
        v_stack_p1C8 = 8;
        result = v_stack_p50;
        v_stack_pC8 = result;
        a2 = v_stack_pC8;
        v_stack_p1D0 = a2;
        v_stack_p1D8 = 8;
        result = *(unsigned int *)(result + 144);
        v_stack_p68 = (unsigned int)(result);
        result = v_stack_p68;
        v_stack_p1E0 = result;
        v_stack_p1E8 = 4;
        result = v_stack_p1A0;
        v_stack_p28 = result;
        v_stack_p20 = 5;
        a4 = 0;
        a3 = 0;
        a2 = v_rip - 3852460;
        a1 = v_rip + 10570830;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
        v_r10 = 0;
    }
    v_stack_p70 = 0;
    goto loc_003F202C;
loc_003F2014:
    v_stack_p61 = 1;
    if ((unsigned int)((unsigned int)(a4)) != 0) goto loc_003F2054;
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(1 + 24), (unsigned int)(0x746C6644ULL), a3, a4);
loc_003F202C:
    if ((unsigned int)((unsigned int)(a4)) != 0) goto loc_003F2054;
    result = FsRtlpComputeShareableOplockState(v_stack_p50, (unsigned int)(0x746C6644ULL), a3, a4);
    result = IofCompleteRequest(0, 1, a3, a4);
    goto loc_003F2222;
loc_003F2054:
    a1 = ((((unsigned int)((unsigned int)(a4))) & (0x3010ULL)) != 0) ? 1 : 0;
    result = ((((unsigned int)((unsigned int)(a4))) & (0x4040ULL)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_003F20D1;
    if (v_stack_p98 != 0) {
        a2 = *(unsigned __int64 *)(v_stack_p98);
        a2 = (a2) + (72);
        a1 = 1 + 72;
        result = FsRtlpOplockPerfMoveData(a1, a2, a3, v_stack_p98);
        a2 = *(unsigned __int64 *)(v_stack_p98);
        a2 = (a2) + (88);
        a1 = 1 + 88;
        result = FsRtlpOplockMoveAckTimeout(a1, a2, a3, v_stack_p98);
    }
    v_stack_p38 = (unsigned int)((unsigned int)(a6));
    v_stack_p30 = 1;
    v_stack_p28 = (unsigned __int8)(v_stack_p58);
    v_stack_p20 = v_stack_p98;
    result = FsRtlpRequestShareableOplock(v_stack_p50, v_stack_p88, 0, (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_stack_p5C = (unsigned int)(result);
    goto loc_003F2222;
loc_003F20D1:
    *(unsigned __int64 *)(v_stack_p50) = 0;
    v_stack_p5C = 259;
    *(unsigned __int64 *)(a3 + 56) = v_stack_p50;
    v_stack_pE0 = *(unsigned __int64 *)(gs_base + (0 + 392));
    *(unsigned __int64 *)(v_stack_p50 + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    v_stack_pE8 = *(unsigned __int64 *)(gs_base + (0 + 392));
    *(unsigned __int64 *)(v_stack_p50 + 24) = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = ObfReferenceObjectWithTag(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(0x746C6644ULL), 0, (unsigned int)((unsigned int)((unsigned int)(a4))));
    *(unsigned __int8 *)(v_stack_p50 + 32) = 0;
    if (0 == 0) goto loc_003F2175;
    result = ObfReferenceObjectWithTag(*(unsigned __int64 *)(v_stack_p88 + 48), (unsigned int)(0x746C6644ULL), 0, (unsigned int)((unsigned int)((unsigned int)(a4))));
    *(unsigned __int64 *)(v_stack_p50 + 8) = *(unsigned __int64 *)(v_stack_p88 + 48);
    goto loc_003F218A;
loc_003F2175:
    *(unsigned __int64 *)(v_stack_p50 + 8) = *(unsigned __int64 *)(v_stack_p90 + 24);
loc_003F218A:
    a2 = (v_stack_p50) + (168);
    result = FsRtlpOplockPerfMoveData(v_stack_p90 + 72, a2, 0, v_stack_p90);
    a2 = (v_stack_p50) + (184);
    result = FsRtlpOplockMoveAckTimeout(v_stack_p90 + 88, a2, 0, v_stack_p90);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p50 + 144))) & (32));
    v_r15 = (unsigned int)(((unsigned int)(a4)) | ((unsigned int)(a2)));
    v_r15 = (unsigned int)((v_r15) | (64));
    *(unsigned int *)(v_stack_p50 + 144) = (unsigned int)(v_r15);
    result = KeAcquireQueuedSpinLock(7, a2, 0, v_stack_p90);
    *(unsigned __int8 *)(a3 + 69) = (unsigned __int8)(result);
    if ((*(unsigned __int8 *)(a3 + 68)) == 0) goto loc_003F21FD;
    a3 = (unsigned __int8)((v_stack_p58) ^ (1));
    result = FsRtlpCancelExclusiveIrp(a3, 1, a3, v_stack_p90);
    goto loc_003F2215;
loc_003F21FD:
    result = KeReleaseQueuedSpinLock(7, *(unsigned __int8 *)(a3 + 69), a3, v_stack_p90);
loc_003F2215:
loc_003F2222:
    a3 = 0;
    result = FsRtlpModifyThreadPriorities(v_stack_p50, v_stack_p90, a3, v_stack_p90);
    result = FsRtlpClearOwner(v_stack_p50, v_stack_p90, a3, v_stack_p90);
    if ((*(unsigned __int64 *)(v_stack_p50 + 72)) == (v_stack_p50 + 72)) {
        *(unsigned __int8 *)(v_stack_p50 + 32) = 0;
    }
    result = FsRtlpOplockPerfSendData(v_stack_p90 + 72, v_stack_p90, a3, v_stack_p90);
    result = FsRtlpFreeRHOpContext(v_stack_p90, 1, a3, v_stack_p90);
    if (0 == 0) goto loc_003F1EF1;
    *(unsigned int *)(v_stack_p50 + 144) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p50 + 144)));
    goto loc_003F1EF1;
loc_003F2288:
    goto loc_003F1D56;
loc_003F2290:
loc_003F2295:
    v_r12 = 0;
loc_003F2298:
    if (v_stack_p60 == 0) goto loc_003F1B6B;
    result = (unsigned int)(*(unsigned int *)(v_stack_p50 + 144));
    if (v_stack_p61 != 0) {
        a1 = v_stack_p50;
        result = FsRtlpReleaseIrpsWaitingForRH(a1, 1, a3, v_stack_p90);
    }
    if ((unsigned __int8)(v_stack_p64) == 0) goto loc_003F2569;
    goto loc_003F25AB;
loc_003F22C2:
    *(unsigned __int64 *)(v_stack_p90) = result;
    *(unsigned __int64 *)(v_stack_p90 + 8) = a1;
    *(unsigned __int64 *)(result + 8) = v_stack_p90;
    *(unsigned __int64 *)(a1) = v_stack_p90;
    if ((*(unsigned int *)(v_rip + 10570105)) >= = 5) {
        result = *(unsigned __int64 *)(v_stack_p90 + 16);
        v_stack_pB8 = result;
        result = v_stack_pB8;
        v_stack_p160 = result;
        v_stack_p168 = 8;
        result = v_stack_p50;
        v_stack_p98 = result;
        a2 = v_stack_p98;
        v_stack_p170 = a2;
        v_stack_p178 = 8;
        result = *(unsigned int *)(result + 144);
        v_stack_p84 = (unsigned int)(result);
        result = v_stack_p84;
        v_stack_p180 = result;
        v_stack_p188 = 4;
        result = v_stack_p140;
        v_stack_p28 = result;
        v_stack_p20 = 5;
        a4 = 0;
        a3 = 0;
        a2 = v_rip - 3853488;
        a1 = v_rip + 10569936;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    v_stack_p70 = 0;
    *(unsigned __int64 *)(v_stack_p50 + 8) = 0;
    *(unsigned int *)(v_stack_p50 + 144) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p50 + 144)));
    *(unsigned int *)(a3 + 48) = 0;
    result = IofCompleteRequest(0, 1, a3, a4);
    goto loc_003F2569;
loc_003F23BF:
    v_r12 = 0;
loc_003F23C2:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p50 + 144))))) & ((unsigned int)(v_stack_p64)));
    if (((unsigned int)(result)) == 0x105040ULL) goto loc_003F24A0;
    if (((unsigned int)(result)) == 0x107040ULL) goto loc_003F24A0;
    if (((unsigned int)(result)) == 0) goto loc_003F24A0;
    if (((unsigned int)(result)) == 0x507040ULL) goto loc_003F24A0;
    if (((unsigned int)(result)) == 0x805040ULL) goto loc_003F24A0;
    if (((unsigned int)(result)) == 0x807040ULL) goto loc_003F24A0;
loc_003F2417:
loc_003F241B:
    if ((unsigned __int8)((unsigned int)(v_stack_p68)) == 0) goto loc_003F24EB;
    result = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 24)) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 24) + 16) = 0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p50 + 144))) >> (12));
    a1 = (unsigned int)((a1) & (7));
    *(unsigned int *)(*(unsigned __int64 *)(a3 + 24) + 4) = (unsigned int)(a1);
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p50 + 144))))) >> (1));
    a2 = (unsigned int)((a2) & ((unsigned int)((unsigned int)(0x200000ULL))));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p50 + 144))))) & (0x100000ULL));
    a2 = (unsigned int)((a2) | ((unsigned int)(result)));
    a2 = (unsigned int)((a2) >> (1));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p50 + 144))) & ((unsigned int)((unsigned int)(0x200000ULL))));
    a2 = (unsigned int)((a2) | ((unsigned int)(a1)));
    a2 = (unsigned int)((a2) >> (19));
    *(unsigned int *)(*(unsigned __int64 *)(a3 + 24) + 8) = (unsigned int)(a2);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3 + 24) + 12))) | (1));
    *(unsigned int *)(*(unsigned __int64 *)(a3 + 24) + 12) = (unsigned int)(result);
    *(unsigned __int64 *)(a3 + 56) = 24;
    *(unsigned int *)(a3 + 48) = (unsigned int)((unsigned int)(0x8000002EULL));
    result = IofCompleteRequest(0, 1, *(unsigned __int64 *)(a3 + 24), (unsigned int)(0x200000ULL));
    v_stack_p5C = (unsigned int)((unsigned int)(0x8000002EULL));
    goto loc_003F25AB;
loc_003F24A0:
    a1 = (unsigned int)((1) >> (1));
    a1 = (unsigned int)((a1) & ((unsigned int)((unsigned int)(0x200000ULL))));
    result = (unsigned int)((1) & (0x100000ULL));
    a1 = (unsigned int)((a1) | ((unsigned int)(result)));
    a1 = (unsigned int)((a1) >> (1));
    a2 = (unsigned int)((1) & ((unsigned int)((unsigned int)(0x200000ULL))));
    a1 = (unsigned int)((a1) | ((unsigned int)(a2)));
    a1 = (unsigned int)((a1) >> (7));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) & (0x7000ULL));
    if (((unsigned int)(result)) <= ((unsigned int)(a1))) goto loc_003F2417;
    result = (v_stack_p50) + (88);
    a1 = (unsigned __int8)((unsigned int)(v_stack_p68));
    if ((*(unsigned __int64 *)(result)) != result) { a1 = 1; }
    goto loc_003F241B;
loc_003F24EB:
    a3 = 0;
    a2 = 0;
    result = FsRtlpModifyThreadPriorities(v_stack_p50, a2, a3, (unsigned int)(0x200000ULL));
    a2 = 0;
    result = FsRtlpClearOwner(v_stack_p50, a2, a3, (unsigned int)(0x200000ULL));
    *(unsigned __int8 *)(v_stack_p50 + 32) = 0;
    v_stack_p48 = (unsigned int)((unsigned int)(a6));
    v_stack_p40 = v_stack_p63;
    v_stack_p38 = v_stack_p62;
    v_stack_p30 = v_stack_p70;
    v_stack_p28 = (unsigned __int8)(v_stack_p58);
    v_stack_p20 = v_stack_p98;
    result = FsRtlpGrantAnyOplockFromExclusive(v_stack_p50, 0, v_stack_p88, (unsigned int)((unsigned int)(v_r15)));
    v_stack_p5C = (unsigned int)(result);
loc_003F2569:
    if (v_stack_p62 == 0) goto loc_003F2588;
loc_003F2570:
    result = (v_stack_p50) + (88);
    if ((*(unsigned __int64 *)(result)) == result) goto loc_003F2588;
    result = FsRtlpRemoveAndCompleteWaitingIrp(*(unsigned __int64 *)(result), 0, v_stack_p88, (unsigned int)((unsigned int)(v_r15)));
    goto loc_003F2570;
loc_003F2588:
    if (v_stack_p63 != 0) {
        result = v_stack_p50;
        a1 = *(unsigned __int64 *)(result + 8);
        a2 = 0x746C6644ULL;
        result = ObfDereferenceObjectWithTag(a1, a2, v_stack_p88, (unsigned int)((unsigned int)(v_r15)));
        result = v_stack_p50;
        *(unsigned __int64 *)(result + 8) = 0;
    }
    if (v_stack_p70 != 0) {
        a2 = 0;
        a1 = v_stack_p70;
        result = ExFreePoolWithTag(a1, a2, v_stack_p88, (unsigned int)((unsigned int)(v_r15)));
    }
    if ((*(unsigned int *)(v_rip + 10569359)) >= = 5) {
        result = v_stack_p5C;
        v_stack_p7C = (unsigned int)(result);
        result = v_stack_p7C;
        v_stack_p110 = result;
        v_stack_p118 = 4;
        result = v_stack_p50;
        v_stack_pA8 = result;
        a2 = v_stack_pA8;
        v_stack_p120 = a2;
        v_stack_p128 = 8;
        result = *(unsigned int *)(result + 144);
        v_stack_p80 = (unsigned int)(result);
        result = v_stack_p80;
        v_stack_p130 = result;
        v_stack_p138 = 4;
        result = v_stack_pF0;
        v_stack_p28 = result;
        v_stack_p20 = 5;
        a4 = 0;
        a3 = 0;
        a2 = v_rip - 3853881;
        a1 = v_rip + 10569197;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    result = ExReleaseFastMutexUnsafe(*(unsigned __int64 *)(v_stack_p50 + 152), a2, a3, a4);
    goto loc_003F1AEF;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlpAcknowledgeOplockBreakByCacheFlags(void *Arg1, int64_t Arg2, void *Arg3, int32_t Arg4, int64_t Arg5, uint32_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rsp;
    uint32_t v_stack_m1C8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1F0;
    uint32_t v_stack_m1F4;
    uint8_t v_stack_m1FF;
    uint8_t v_stack_m200;
    uint64_t v_stack_m208;
    uint32_t v_stack_m210;
    uint8_t v_stack_m214;
    uint8_t v_stack_m215;
    uint8_t v_stack_m216;
    uint8_t v_stack_m217;
    uint8_t v_stack_m218;
    uint32_t v_stack_m21C;
    uint64_t v_stack_m228;
    uint64_t v_stack_m250;
    uint32_t v_stack_m258;
    uint64_t v_stack_m48;
    uint64_t v_stack_p110;
    uint64_t v_stack_p118;
    uint64_t v_stack_p120;
    uint64_t v_stack_p128;
    uint64_t v_stack_p130;
    uint64_t v_stack_p138;
    uint64_t v_stack_p140;
    uint64_t v_stack_p160;
    uint64_t v_stack_p168;
    uint64_t v_stack_p170;
    uint64_t v_stack_p178;
    uint64_t v_stack_p180;
    uint64_t v_stack_p188;
    uint64_t v_stack_p1A0;
    uint64_t v_stack_p1C0;
    uint64_t v_stack_p1C8;
    uint64_t v_stack_p1D0;
    uint64_t v_stack_p1D8;
    uint64_t v_stack_p1E0;
    uint64_t v_stack_p1E8;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint8_t v_stack_p30;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint32_t v_stack_p48;
    uint64_t v_stack_p50;
    uint8_t v_stack_p58;
    uint32_t v_stack_p5C;
    uint8_t v_stack_p60;
    uint8_t v_stack_p61;
    uint64_t v_stack_p62;
    uint64_t v_stack_p63;
    uint8_t v_stack_p64;
    uint8_t v_stack_p66;
    uint32_t v_stack_p68;
    uint64_t v_stack_p70;
    uint32_t v_stack_p7C;
    uint32_t v_stack_p80;
    uint32_t v_stack_p84;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB8;
    uint64_t v_stack_pC0;
    uint64_t v_stack_pC8;
    uint64_t v_stack_pD8;
    uint64_t v_stack_pE0;
    uint64_t v_stack_pE8;
    uint64_t v_stack_pF0;

    local_rsp = (local_rsp) - (576);
    result = (*(uint64_t *)(v_rip + 0xA18D9C)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m1F0 = Arg2;
    v_stack_m228 = Arg1;
    v_stack_m1E0 = Arg5;
    local_r12 = 0;
    v_stack_m21C = 0;
    v_stack_m208 = 0;
    v_stack_m218 = 0;
    v_stack_m214 = 0;
    v_stack_m200 = 0;
    v_stack_m217 = 0;
    v_stack_m210 = 0;
    v_stack_m1FF = 0;
    v_stack_m215 = 0;
    v_stack_m216 = 0;
    result = 0;
    if ((*(uint32_t *)(v_rip + 0xA15240)) >= = 5) {
        *(uint32_t *)(local_rsp - 0x1D4) = Arg4;
        result = local_rsp - 468;
        *(uint64_t *)(local_rsp - 0x118) = result;
        *(uint64_t *)(local_rsp - 0x110) = 4;
        result = Arg6;
        v_stack_m1C8 = (uint32_t)(result);
        result = local_rsp - 456;
        *(uint64_t *)(local_rsp - 0x108) = result;
        *(uint64_t *)(local_rsp - 0x100) = 4;
        *(void **)(local_rsp - 0x1C0) = Arg1;
        result = local_rsp - 448;
        *(uint64_t *)(local_rsp - 0xF8) = result;
        *(uint64_t *)(local_rsp - 0xF0) = 8;
        result = *(uint32_t *)(arg1 + 0x90);
        v_stack_m1F4 = (uint32_t)(result);
        result = local_rsp - 500;
        *(uint64_t *)(local_rsp - 0xE8) = result;
        *(uint64_t *)(local_rsp - 0xE0) = 4;
        result = local_rsp - 312;
        v_stack_m250 = result;
        v_stack_m258 = 6;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_rip - 3851921;
        Arg1 = v_rip + 10572165;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
        Arg1 = v_stack_m228;
    }
    if (Arg1 != NULL) goto loc_003F1B13;
    *(uint32_t *)(arg3 + 0x30) = (uint32_t)((uint32_t)(0xC00000E3ULL));
    result = IofCompleteRequest(0, Arg1 + 1, Arg3, Arg4);
loc_003F1AEF:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg1 + 1, Arg3, Arg4);
    local_rsp = (local_rsp) + (576);
    return result;
loc_003F1B13:
    result = ExAcquireFastMutexUnsafe(*(uint64_t *)(arg1 + 0x98), Arg1 + 1, Arg3, Arg4);
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p50 + 0x90)))) & (0xF00000ULL)) != 0) goto loc_003F1B50;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p50 + 0x90))))) & ((uint32_t)((uint32_t)(0x1F0FFDFULL))));
    result = (uint32_t)((result) - ((uint32_t)((uint32_t)(0x3000ULL))));
    if ((((uint32_t)(result)) & (0xFFFF7FFFULL)) != 0) goto loc_003F1B6B;
loc_003F1B50:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p50 + 0x90))) & ((uint32_t)((uint32_t)(0x1F0FFDFULL))));
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)((uint32_t)(0x3000ULL))));
    if ((((uint32_t)(Arg1)) & (0xFFFF7FFFULL)) != 0) goto loc_003F1B87;
    result = (v_stack_p50) + (72);
    if ((*(uint64_t *)(result)) != result) goto loc_003F1B87;
loc_003F1B6B:
    v_stack_p5C = (uint32_t)((uint32_t)(0xC00000E3ULL));
    *(uint32_t *)(arg3 + 0x30) = (uint32_t)((uint32_t)(0xC00000E3ULL));
    result = IofCompleteRequest(0, 1, Arg3, Arg4);
    goto loc_003F25AB;
loc_003F1B87:
    v_stack_pD8 = *(uint64_t *)(arg3 + 0x18);
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg3 + 0x18) + 0x8))) & (4));
    local_r10 = 0;
    result = *(uint64_t *)(arg3 + 0x18);
    local_r14 = 0;
    if ((uint32_t)(local_r12) != 0) {
        Arg2 = local_r10 + 48;
        Arg1 = 288;
        Arg3 = 0x6F725346ULL;
        result = ExAllocatePool2(Arg1, Arg2, Arg3, Arg4);
        local_r14 = result;
        v_stack_p70 = result;
        local_r10 = 0;
    }
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p50 + 0x90))) & ((uint32_t)((uint32_t)(0xC00000E3ULL))));
    if (((uint32_t)(Arg2)) > ((uint32_t)((uint32_t)(0x307040ULL)))) goto loc_003F1D1C;
    if (((uint32_t)(Arg2)) == ((uint32_t)((uint32_t)(0x307040ULL)))) goto loc_003F1C1A;
    if (((uint32_t)(Arg2)) == ((uint32_t)((uint32_t)(0x3000ULL)))) goto loc_003F1D4D;
    if (((uint32_t)(Arg2)) == 0xB000ULL) goto loc_003F1D4D;
    if (((uint32_t)(Arg2)) == 0x103000ULL) goto loc_003F1D4D;
    if (((uint32_t)(Arg2)) == 0x105040ULL) goto loc_003F1C1A;
    if (((uint32_t)(Arg2)) != 0x107040ULL) goto loc_003F1B6B;
loc_003F1C1A:
    if ((uint32_t)(local_r12) == 0) goto loc_003F1C5C;
    if ((*(uint64_t *)(v_stack_p50 + 0x8)) == (*(uint64_t *)(v_stack_p88 + 0x30))) goto loc_003F1B6B;
    Arg3 = 0;
    result = FsRtlpOplockKeysEqual(*(uint64_t *)(v_stack_p88 + 0x30), *(uint64_t *)(v_stack_p50 + 0x8), Arg3, Arg4);
    v_stack_p66 = (uint8_t)(result);
    if ((uint8_t)(result) == 0) goto loc_003F1B6B;
    if ((uint32_t)(local_r12) != 0) goto loc_003F1C78;
loc_003F1C5C:
    if ((*(uint64_t *)(v_stack_p50 + 0x8)) != (*(uint64_t *)(v_stack_p88 + 0x30))) goto loc_003F1B6B;
    if ((uint32_t)(local_r12) == 0) goto loc_003F23BF;
loc_003F1C78:
    local_r12 = 0;
    if ((uint32_t)((uint32_t)(Arg4)) != 0) goto loc_003F23C2;
    Arg3 = 0;
    Arg2 = 0;
    result = FsRtlpModifyThreadPriorities(v_stack_p50, Arg2, Arg3, Arg4);
    Arg2 = 0;
    result = FsRtlpClearOwner(v_stack_p50, Arg2, Arg3, Arg4);
    *(uint8_t *)(v_stack_p50 + 0x20) = 0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p50 + 0x90))) & (32));
    Arg1 = (uint32_t)((Arg1) | (1));
    *(uint32_t *)(v_stack_p50 + 0x90) = (uint32_t)(Arg1);
    *(uint64_t *)(v_stack_p70 + 0x10) = *(uint64_t *)(v_stack_p50 + 0x8);
    Arg1 = (v_stack_p50) + (168);
    result = FsRtlpOplockPerfMoveData(Arg1, v_stack_p70 + 24, Arg3, v_stack_p70);
    Arg1 = (v_stack_p50) + (184);
    result = FsRtlpOplockMoveAckTimeout(Arg1, v_stack_p70 + 40, Arg3, v_stack_p70);
    Arg1 = (v_stack_p50) + (104);
    if ((*(uint64_t *)(*(uint64_t *)(arg1) + 0x8)) == Arg1) goto loc_003F22C2;
loc_003F1D15:
loc_003F1D1C:
    if (((uint32_t)(v_stack_p70 + 40)) == 0x803000ULL) goto loc_003F1D4D;
    if (((uint32_t)(v_stack_p70 + 40)) == 0x507040ULL) goto loc_003F1C1A;
    if (((uint32_t)(v_stack_p70 + 40)) == 0x805040ULL) goto loc_003F1C1A;
    if (((uint32_t)(v_stack_p70 + 40)) == 0x807040ULL) goto loc_003F1C1A;
    goto loc_003F1B6B;
loc_003F1D4D:
loc_003F1D56:
    v_stack_p90 = *(uint64_t *)(v_stack_p50 + 0x48);
    result = (v_stack_p50) + (72);
    if ((*(uint64_t *)(v_stack_p50 + 0x48)) == result) goto loc_003F2290;
    if (0 != 0) goto loc_003F1D90;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p50 + 0x48) + 0x18)) == (*(uint64_t *)(v_stack_p88 + 0x30))) goto loc_003F1DB8;
    if (0 == 0) goto loc_003F2288;
loc_003F1D90:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p50 + 0x48) + 0x18)) == (*(uint64_t *)(v_stack_p88 + 0x30))) goto loc_003F2288;
    Arg3 = 0;
    result = FsRtlpOplockKeysEqual(*(uint64_t *)(v_stack_p88 + 0x30), *(uint64_t *)(*(uint64_t *)(v_stack_p50 + 0x48) + 0x18), Arg3, v_stack_p70);
    v_stack_p66 = (uint8_t)(result);
    local_r10 = 0;
    if ((uint8_t)(result) == 0) goto loc_003F2288;
loc_003F1DB8:
    v_stack_p60 = 1;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p50 + 0x48) + 0x30))) & (0xF00000ULL));
    if (((uint32_t)(result)) != 0x800000ULL) goto loc_003F1E62;
    if ((uint32_t)((uint32_t)(Arg4)) == 0) goto loc_003F1F01;
    result = (v_stack_p50) + (88);
    if ((*(uint64_t *)(result)) != result) goto loc_003F1E02;
    result = FsRtlpOplockUpperLowerCompatible((uint32_t)((uint32_t)((uint32_t)(Arg4))), (uint32_t)((uint32_t)((uint32_t)(Arg6))), Arg3, v_stack_p70);
    if ((uint8_t)(result) != 0) goto loc_003F1F01;
loc_003F1E02:
    result = 0;
    *(uint64_t *)(*(uint64_t *)(arg3 + 0x18)) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(arg3 + 0x18) + 0x10) = 0;
    *(uint32_t *)(*(uint64_t *)(arg3 + 0x18) + 0x4) = 3;
    result = (v_stack_p50) + (88);
    local_r13 = (uint32_t)(Arg6);
    if ((*(uint64_t *)(result)) != result) { local_r13 = 0; }
    *(uint32_t *)(*(uint64_t *)(arg3 + 0x18) + 0x8) = (uint32_t)(local_r13);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg3 + 0x18) + 0xC))) | (1));
    *(uint32_t *)(*(uint64_t *)(arg3 + 0x18) + 0xC) = (uint32_t)(result);
    *(uint64_t *)(arg3 + 0x38) = 24;
    *(uint32_t *)(arg3 + 0x30) = (uint32_t)((uint32_t)(0x8000002EULL));
    result = IofCompleteRequest(0, 1, Arg3, v_stack_p70);
    v_stack_p5C = (uint32_t)((uint32_t)(0x8000002EULL));
    goto loc_003F2298;
loc_003F1E62:
    if (((uint32_t)(result)) != 0x100000ULL) goto loc_003F1EF9;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & (0x7000ULL));
    if (((uint32_t)(result)) <= ((uint32_t)(local_r13))) goto loc_003F1F01;
    result = (v_stack_p50) + (88);
    if ((*(uint64_t *)(result)) != result) goto loc_003F1E9F;
    result = FsRtlpOplockUpperLowerCompatible((uint32_t)((uint32_t)((uint32_t)(Arg4))), (uint32_t)((uint32_t)((uint32_t)(Arg6))), Arg3, v_stack_p70);
    if ((uint8_t)(result) != 0) goto loc_003F1F01;
loc_003F1E9F:
    result = 0;
    *(uint64_t *)(*(uint64_t *)(arg3 + 0x18)) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(arg3 + 0x18) + 0x10) = 0;
    *(uint32_t *)(*(uint64_t *)(arg3 + 0x18) + 0x4) = 3;
    result = (v_stack_p50) + (88);
    local_r13 = (uint32_t)(Arg6);
    if ((*(uint64_t *)(result)) != result) { local_r13 = 1; }
    *(uint32_t *)(*(uint64_t *)(arg3 + 0x18) + 0x8) = (uint32_t)(local_r13);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg3 + 0x18) + 0xC))) | (1));
    *(uint32_t *)(*(uint64_t *)(arg3 + 0x18) + 0xC) = (uint32_t)(result);
    *(uint64_t *)(arg3 + 0x38) = 24;
    *(uint32_t *)(arg3 + 0x30) = (uint32_t)((uint32_t)(0x8000002EULL));
    result = IofCompleteRequest(0, 1, Arg3, v_stack_p70);
    v_stack_p5C = (uint32_t)((uint32_t)(0x8000002EULL));
loc_003F1EF1:
    goto loc_003F2295;
loc_003F1EF9:
loc_003F1F01:
    result = FsRtlpOplockDequeueRH(1, 1, Arg3, v_stack_p70);
    if (0 == 0) goto loc_003F2014;
    *(uint64_t *)(local_r14 + 0x10) = *(uint64_t *)(1 + 0x18);
    result = FsRtlpOplockPerfMoveData(1 + 72, local_r14 + 24, Arg3, v_stack_p70);
    result = FsRtlpOplockMoveAckTimeout(1 + 88, local_r14 + 40, Arg3, v_stack_p70);
    Arg1 = (v_stack_p50) + (104);
    if ((*(uint64_t *)(*(uint64_t *)(arg1) + 0x8)) != Arg1) goto loc_003F1D15;
    *(uint64_t *)(local_r14) = *(uint64_t *)(arg1);
    *(void **)(local_r14 + 0x8) = Arg1;
    *(uint64_t *)(*(uint64_t *)(arg1) + 0x8) = local_r14;
    *(uint64_t *)(arg1) = local_r14;
    result = *(uint64_t *)(arg1);
    if ((*(uint32_t *)(v_rip + 0xA14CF1)) >= = 5) {
        result = *(uint64_t *)(local_r14 + 0x10);
        v_stack_pC0 = result;
        result = v_stack_pC0;
        v_stack_p1C0 = result;
        v_stack_p1C8 = 8;
        result = v_stack_p50;
        v_stack_pC8 = result;
        Arg2 = v_stack_pC8;
        v_stack_p1D0 = Arg2;
        v_stack_p1D8 = 8;
        result = *(uint32_t *)(result + 0x90);
        v_stack_p68 = (uint32_t)(result);
        result = v_stack_p68;
        v_stack_p1E0 = result;
        v_stack_p1E8 = 4;
        result = v_stack_p1A0;
        v_stack_p28 = result;
        v_stack_p20 = 5;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_rip - 3852460;
        Arg1 = v_rip + 10570830;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
        local_r10 = 0;
    }
    v_stack_p70 = 0;
    goto loc_003F202C;
loc_003F2014:
    v_stack_p61 = 1;
    if ((uint32_t)((uint32_t)(Arg4)) != 0) goto loc_003F2054;
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(1 + 0x18), (uint32_t)(0x746C6644ULL), Arg3, Arg4);
loc_003F202C:
    if ((uint32_t)((uint32_t)(Arg4)) != 0) goto loc_003F2054;
    result = FsRtlpComputeShareableOplockState(v_stack_p50, (uint32_t)(0x746C6644ULL), Arg3, Arg4);
    result = IofCompleteRequest(0, 1, Arg3, Arg4);
    goto loc_003F2222;
loc_003F2054:
    Arg1 = ((((uint32_t)((uint32_t)(Arg4))) & (0x3010ULL)) != 0) ? 1 : 0;
    result = ((((uint32_t)((uint32_t)(Arg4))) & (0x4040ULL)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_003F20D1;
    if (v_stack_p98 != 0) {
        Arg2 = *(uint64_t *)(v_stack_p98);
        Arg2 = (Arg2) + (72);
        Arg1 = 1 + 72;
        result = FsRtlpOplockPerfMoveData(Arg1, Arg2, Arg3, v_stack_p98);
        Arg2 = *(uint64_t *)(v_stack_p98);
        Arg2 = (Arg2) + (88);
        Arg1 = 1 + 88;
        result = FsRtlpOplockMoveAckTimeout(Arg1, Arg2, Arg3, v_stack_p98);
    }
    v_stack_p38 = (uint32_t)((uint32_t)(Arg6));
    v_stack_p30 = 1;
    v_stack_p28 = (uint8_t)(v_stack_p58);
    v_stack_p20 = v_stack_p98;
    result = FsRtlpRequestShareableOplock(v_stack_p50, v_stack_p88, 0, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    v_stack_p5C = (uint32_t)(result);
    goto loc_003F2222;
loc_003F20D1:
    *(uint64_t *)(v_stack_p50) = 0;
    v_stack_p5C = 259;
    *(uint64_t *)(arg3 + 0x38) = v_stack_p50;
    v_stack_pE0 = *(uint64_t *)(gs_base + (0 + 0x188));
    *(uint64_t *)(v_stack_p50 + 0x10) = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    v_stack_pE8 = *(uint64_t *)(gs_base + (0 + 0x188));
    *(uint64_t *)(v_stack_p50 + 0x18) = *(uint64_t *)(gs_base + (0 + 0x188));
    result = ObfReferenceObjectWithTag(*(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(0x746C6644ULL), 0, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    *(uint8_t *)(v_stack_p50 + 0x20) = 0;
    if (0 == 0) goto loc_003F2175;
    result = ObfReferenceObjectWithTag(*(uint64_t *)(v_stack_p88 + 0x30), (uint32_t)(0x746C6644ULL), 0, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    *(uint64_t *)(v_stack_p50 + 0x8) = *(uint64_t *)(v_stack_p88 + 0x30);
    goto loc_003F218A;
loc_003F2175:
    *(uint64_t *)(v_stack_p50 + 0x8) = *(uint64_t *)(v_stack_p90 + 0x18);
loc_003F218A:
    Arg2 = (v_stack_p50) + (168);
    result = FsRtlpOplockPerfMoveData(v_stack_p90 + 72, Arg2, 0, v_stack_p90);
    Arg2 = (v_stack_p50) + (184);
    result = FsRtlpOplockMoveAckTimeout(v_stack_p90 + 88, Arg2, 0, v_stack_p90);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p50 + 0x90))) & (32));
    local_r15 = (uint32_t)(((uint32_t)(Arg4)) | ((uint32_t)(Arg2)));
    local_r15 = (uint32_t)((local_r15) | (64));
    *(uint32_t *)(v_stack_p50 + 0x90) = (uint32_t)(local_r15);
    result = KeAcquireQueuedSpinLock(7, Arg2, 0, v_stack_p90);
    *(uint8_t *)(arg3 + 0x45) = (uint8_t)(result);
    if ((*(uint8_t *)(arg3 + 0x44)) == 0) goto loc_003F21FD;
    Arg3 = (uint8_t)((v_stack_p58) ^ (1));
    result = FsRtlpCancelExclusiveIrp(Arg3, 1, Arg3, v_stack_p90);
    goto loc_003F2215;
loc_003F21FD:
    result = KeReleaseQueuedSpinLock(7, *(uint8_t *)(arg3 + 0x45), Arg3, v_stack_p90);
loc_003F2215:
loc_003F2222:
    Arg3 = 0;
    result = FsRtlpModifyThreadPriorities(v_stack_p50, v_stack_p90, Arg3, v_stack_p90);
    result = FsRtlpClearOwner(v_stack_p50, v_stack_p90, Arg3, v_stack_p90);
    if ((*(uint64_t *)(v_stack_p50 + 0x48)) == (v_stack_p50 + 72)) {
        *(uint8_t *)(v_stack_p50 + 0x20) = 0;
    }
    result = FsRtlpOplockPerfSendData(v_stack_p90 + 72, v_stack_p90, Arg3, v_stack_p90);
    result = FsRtlpFreeRHOpContext(v_stack_p90, 1, Arg3, v_stack_p90);
    if (0 == 0) goto loc_003F1EF1;
    *(uint32_t *)(v_stack_p50 + 0x90) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p50 + 0x90)));
    goto loc_003F1EF1;
loc_003F2288:
    goto loc_003F1D56;
loc_003F2290:
loc_003F2295:
    local_r12 = 0;
loc_003F2298:
    if (v_stack_p60 == 0) goto loc_003F1B6B;
    result = (uint32_t)(*(uint32_t *)(v_stack_p50 + 0x90));
    if (v_stack_p61 != 0) {
        Arg1 = v_stack_p50;
        result = FsRtlpReleaseIrpsWaitingForRH(Arg1, 1, Arg3, v_stack_p90);
    }
    if ((uint8_t)(v_stack_p64) == 0) goto loc_003F2569;
    goto loc_003F25AB;
loc_003F22C2:
    *(uint64_t *)(v_stack_p90) = result;
    *(void **)(v_stack_p90 + 0x8) = Arg1;
    *(uint64_t *)(result + 0x8) = v_stack_p90;
    *(uint64_t *)(arg1) = v_stack_p90;
    if ((*(uint32_t *)(v_rip + 0xA14979)) >= = 5) {
        result = *(uint64_t *)(v_stack_p90 + 0x10);
        v_stack_pB8 = result;
        result = v_stack_pB8;
        v_stack_p160 = result;
        v_stack_p168 = 8;
        result = v_stack_p50;
        v_stack_p98 = result;
        Arg2 = v_stack_p98;
        v_stack_p170 = Arg2;
        v_stack_p178 = 8;
        result = *(uint32_t *)(result + 0x90);
        v_stack_p84 = (uint32_t)(result);
        result = v_stack_p84;
        v_stack_p180 = result;
        v_stack_p188 = 4;
        result = v_stack_p140;
        v_stack_p28 = result;
        v_stack_p20 = 5;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_rip - 3853488;
        Arg1 = v_rip + 10569936;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_p70 = 0;
    *(uint64_t *)(v_stack_p50 + 0x8) = 0;
    *(uint32_t *)(v_stack_p50 + 0x90) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p50 + 0x90)));
    *(uint32_t *)(arg3 + 0x30) = 0;
    result = IofCompleteRequest(0, 1, Arg3, Arg4);
    goto loc_003F2569;
loc_003F23BF:
    local_r12 = 0;
loc_003F23C2:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p50 + 0x90))))) & ((uint32_t)(v_stack_p64)));
    if (((uint32_t)(result)) == 0x105040ULL) goto loc_003F24A0;
    if (((uint32_t)(result)) == 0x107040ULL) goto loc_003F24A0;
    if (((uint32_t)(result)) == 0) goto loc_003F24A0;
    if (((uint32_t)(result)) == 0x507040ULL) goto loc_003F24A0;
    if (((uint32_t)(result)) == 0x805040ULL) goto loc_003F24A0;
    if (((uint32_t)(result)) == 0x807040ULL) goto loc_003F24A0;
loc_003F2417:
loc_003F241B:
    if ((uint8_t)((uint32_t)(v_stack_p68)) == 0) goto loc_003F24EB;
    result = 0;
    *(uint64_t *)(*(uint64_t *)(arg3 + 0x18)) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(arg3 + 0x18) + 0x10) = 0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p50 + 0x90))) >> (12));
    Arg1 = (uint32_t)((Arg1) & (7));
    *(uint32_t *)(*(uint64_t *)(arg3 + 0x18) + 0x4) = (uint32_t)(Arg1);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p50 + 0x90))))) >> (1));
    Arg2 = (uint32_t)((Arg2) & ((uint32_t)((uint32_t)(0x200000ULL))));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p50 + 0x90))))) & (0x100000ULL));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(result)));
    Arg2 = (uint32_t)((Arg2) >> (1));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p50 + 0x90))) & ((uint32_t)((uint32_t)(0x200000ULL))));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(Arg1)));
    Arg2 = (uint32_t)((Arg2) >> (19));
    *(uint32_t *)(*(uint64_t *)(arg3 + 0x18) + 0x8) = (uint32_t)(Arg2);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg3 + 0x18) + 0xC))) | (1));
    *(uint32_t *)(*(uint64_t *)(arg3 + 0x18) + 0xC) = (uint32_t)(result);
    *(uint64_t *)(arg3 + 0x38) = 24;
    *(uint32_t *)(arg3 + 0x30) = (uint32_t)((uint32_t)(0x8000002EULL));
    result = IofCompleteRequest(0, 1, *(uint64_t *)(arg3 + 0x18), (uint32_t)(0x200000ULL));
    v_stack_p5C = (uint32_t)((uint32_t)(0x8000002EULL));
    goto loc_003F25AB;
loc_003F24A0:
    Arg1 = (uint32_t)((1) >> (1));
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)((uint32_t)(0x200000ULL))));
    result = (uint32_t)((1) & (0x100000ULL));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) >> (1));
    Arg2 = (uint32_t)((1) & ((uint32_t)((uint32_t)(0x200000ULL))));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(Arg2)));
    Arg1 = (uint32_t)((Arg1) >> (7));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) & (0x7000ULL));
    if (((uint32_t)(result)) <= ((uint32_t)(Arg1))) goto loc_003F2417;
    result = (v_stack_p50) + (88);
    Arg1 = (uint8_t)((uint32_t)(v_stack_p68));
    if ((*(uint64_t *)(result)) != result) { Arg1 = 1; }
    goto loc_003F241B;
loc_003F24EB:
    Arg3 = 0;
    Arg2 = 0;
    result = FsRtlpModifyThreadPriorities(v_stack_p50, Arg2, Arg3, (uint32_t)(0x200000ULL));
    Arg2 = 0;
    result = FsRtlpClearOwner(v_stack_p50, Arg2, Arg3, (uint32_t)(0x200000ULL));
    *(uint8_t *)(v_stack_p50 + 0x20) = 0;
    v_stack_p48 = (uint32_t)((uint32_t)(Arg6));
    v_stack_p40 = v_stack_p63;
    v_stack_p38 = v_stack_p62;
    v_stack_p30 = v_stack_p70;
    v_stack_p28 = (uint8_t)(v_stack_p58);
    v_stack_p20 = v_stack_p98;
    result = FsRtlpGrantAnyOplockFromExclusive(v_stack_p50, 0, v_stack_p88, (uint32_t)((uint32_t)(local_r15)));
    v_stack_p5C = (uint32_t)(result);
loc_003F2569:
    if (v_stack_p62 == 0) goto loc_003F2588;
loc_003F2570:
    result = (v_stack_p50) + (88);
    if ((*(uint64_t *)(result)) == result) goto loc_003F2588;
    result = FsRtlpRemoveAndCompleteWaitingIrp(*(uint64_t *)(result), 0, v_stack_p88, (uint32_t)((uint32_t)(local_r15)));
    goto loc_003F2570;
loc_003F2588:
    if (v_stack_p63 != 0) {
        result = v_stack_p50;
        Arg1 = *(uint64_t *)(result + 0x8);
        Arg2 = 0x746C6644ULL;
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, v_stack_p88, (uint32_t)((uint32_t)(local_r15)));
        result = v_stack_p50;
        *(uint64_t *)(result + 0x8) = 0;
    }
    if (v_stack_p70 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_p70;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_p88, (uint32_t)((uint32_t)(local_r15)));
    }
    if ((*(uint32_t *)(v_rip + 0xA1468F)) >= = 5) {
        result = v_stack_p5C;
        v_stack_p7C = (uint32_t)(result);
        result = v_stack_p7C;
        v_stack_p110 = result;
        v_stack_p118 = 4;
        result = v_stack_p50;
        v_stack_pA8 = result;
        Arg2 = v_stack_pA8;
        v_stack_p120 = Arg2;
        v_stack_p128 = 8;
        result = *(uint32_t *)(result + 0x90);
        v_stack_p80 = (uint32_t)(result);
        result = v_stack_p80;
        v_stack_p130 = result;
        v_stack_p138 = 4;
        result = v_stack_pF0;
        v_stack_p28 = result;
        v_stack_p20 = 5;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_rip - 3853881;
        Arg1 = v_rip + 10569197;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    result = ExReleaseFastMutexUnsafe(*(uint64_t *)(v_stack_p50 + 0x98), Arg2, Arg3, Arg4);
    goto loc_003F1AEF;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x90` | `32` | `R` |
| `Arg3` | `+ 0x18` | `64` | `R` |
| `Arg3` | `+ 0x30` | `32` | `R/W` |
| `Arg3` | `+ 0x30` | `32` | `W` |
| `Arg3` | `+ 0x38` | `64` | `W` |
| `Arg3` | `+ 0x44` | `8` | `R` |
| `Arg3` | `+ 0x45` | `8` | `R` |
| `Arg3` | `+ 0x45` | `8` | `W` |
| `Arg3` | `+ 0x68` | `64` | `R/W` |
| `Arg3` | `+ 0xB8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003F1988&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
