# PnpProcessQueryRemoveAndEject

- RVA: `0x00A05170`–`0x00A05709` (길이 `1,433` bytes)
- VA: `0x0000000140A05170`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A83CC`
- 디코드: `358`개 명령, `1,433/1,433` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **45**; 고유 호출 대상: **33**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00A05200` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00A0520E` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00A05238` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00A05244` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00A05249` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00A052C2` → [PiProcessQueryAndCancelRemoval](PiProcessQueryAndCancelRemoval_function_00A05A58.md) (function, `0x00A05A58`)
- `0x00A052F7` → [PnpNotifyUserModeDeviceRemoval](../95/PnpNotifyUserModeDeviceRemoval_function_00954258.md) (function, `0x00954258`)
- `0x00A05303` → [PiSendTargetDeviceRemoveCompleteNotification](PiSendTargetDeviceRemoveCompleteNotification_function_00A059F8.md) (function, `0x00A059F8`)
- `0x00A0533C` → [PnpInvalidateRelationsInList](PnpInvalidateRelationsInList_function_00A05DF8.md) (function, `0x00A05DF8`)
- `0x00A05344` → [IopRemoveDeviceRelationsFromList](IopRemoveDeviceRelationsFromList_function_00A05C18.md) (function, `0x00A05C18`)
- `0x00A05360` → [PiEventRemovalPostSurpriseRemove](PiEventRemovalPostSurpriseRemove_function_00A0596C.md) (function, `0x00A0596C`)
- `0x00A0536C` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00A05378` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00A0537D` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00A05397` → [PnpIsChainDereferenced](../../text/4A/PnpIsChainDereferenced_function_004ABAE8.md) (function, `0x004ABAE8`)
- `0x00A053BF` → [PnpRecordBlackboxPnpEventInformation](PnpRecordBlackboxPnpEventInformation_function_00A04EE0.md) (function, `0x00A04EE0`)
- `0x00A053DC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A053EA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A05412` → [PiDetermineDeleteType](PiDetermineDeleteType_function_00A05710.md) (function, `0x00A05710`)
- `0x00A05427` → [PiCheckRemovalPreconditions](PiCheckRemovalPreconditions_function_00A057E0.md) (function, `0x00A057E0`)
- `0x00A05449` → [PiEventAllocateVetoBuffer](PiEventAllocateVetoBuffer_function_00A05840.md) (function, `0x00A05840`)
- `0x00A05466` → [PnpBuildRemovalRelationList](PnpBuildRemovalRelationList_function_00A058D0.md) (function, `0x00A058D0`)
- `0x00A0549E` → [PiEventBuildPdoList](PiEventBuildPdoList_function_00A05C8C.md) (function, `0x00A05C8C`)
- `0x00A05517` → [PnpResizeTargetDeviceBlock](PnpResizeTargetDeviceBlock_function_00A07638.md) (function, `0x00A07638`)
- `0x00A0552B` → [PiEventAreDeviceRelationsExcluded](PiEventAreDeviceRelationsExcluded_function_00A04EC0.md) (function, `0x00A04EC0`)
- `0x00A0553A` → [PnpCompileDeviceInstancePaths](PnpCompileDeviceInstancePaths_function_00A07708.md) (function, `0x00A07708`)
- `0x00A05551` → [PnpBuildUnsafeRemovalDeviceList](../A8/PnpBuildUnsafeRemovalDeviceList_function_00A89810.md) (function, `0x00A89810`)
- `0x00A05565` → [PnpFinalizeVetoedRemove](PnpFinalizeVetoedRemove_function_00A04968.md) (function, `0x00A04968`)
- `0x00A0557F` → [PnpRecordBlackboxPnpEventInformation](PnpRecordBlackboxPnpEventInformation_function_00A04EE0.md) (function, `0x00A04EE0`)
- `0x00A0558C` → [PipAreDriversLoaded](../../text/47/PipAreDriversLoaded_function_004708D4.md) (function, `0x004708D4`)
- `0x00A0559C` → [PiProcessQueryRemoveNoFdo](../74/PiProcessQueryRemoveNoFdo_function_007442B4.md) (function, `0x007442B4`)
- `0x00A055B2` → [IopFreeRelationList](IopFreeRelationList_function_00A08310.md) (function, `0x00A08310`)
- `0x00A055CB` → [PnpFinalizeVetoedRemove](PnpFinalizeVetoedRemove_function_00A04968.md) (function, `0x00A04968`)
- `0x00A055D8` → [PpProfileBeginHardwareProfileTransition](../73/PpProfileBeginHardwareProfileTransition_function_007378E8.md) (function, `0x007378E8`)
- `0x00A05607` → [PiLogSurpriseRemoveEvent](../AC/PiLogSurpriseRemoveEvent_function_00ACEF28.md) (function, `0x00ACEF28`)
- `0x00A0562C` → [PnpDeleteLockedDeviceNodes](PnpDeleteLockedDeviceNodes_function_00A09B30.md) (function, `0x00A09B30`)
- `0x00A05643` → [PpProfileCancelHardwareProfileTransition](../73/PpProfileCancelHardwareProfileTransition_function_00737918.md) (function, `0x00737918`)
- `0x00A0566A` → [PnpNotifyUserModeDeviceRemoval](../95/PnpNotifyUserModeDeviceRemoval_function_00954258.md) (function, `0x00954258`)
- `0x00A05677` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A05697` → [PnpFinalizeDeviceRemovalForReset](../72/PnpFinalizeDeviceRemovalForReset_function_0072AD04.md) (function, `0x0072AD04`)
- `0x00A056BA` → [IopQueryDockRemovalInterface](../73/IopQueryDockRemovalInterface_function_0073DED0.md) (function, `0x0073DED0`)
- `0x00A056D9` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A056E7` → [PnpRecordBlackboxPnpEventInformation](PnpRecordBlackboxPnpEventInformation_function_00A04EE0.md) (function, `0x00A04EE0`)
- `0x00A056F3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A056FF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [PnpShutdownDevices](../72/PnpShutdownDevices_function_00723F20.md) at `0x007240E9`
- [PnpProcessTargetDeviceEvent](PnpProcessTargetDeviceEvent_function_00A046BC.md) at `0x00A0479E`

### Static image references
- `0x00A051EF` → RVA `0x00F8C4E0` (`.data`; read)
- `0x00A05207` → RVA `0x00F8C560` (`.data`; read)
- `0x00A052DC` → RVA `0x000114E8` (`.rdata`; read)
- `0x00A053C4` → RVA `0x00F8C5E4` (`.data`; read)
- `0x00A05403` → RVA `0x0001A220` (`.rdata`; read)
- `0x00A05654` → RVA `0x00026B80` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **16**
  - `0x00A05200` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00A0520E` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00A05238` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00A05244` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00A05249` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00A0536C` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00A05378` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00A0537D` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00A05397` → [PnpIsChainDereferenced](../../text/4A/PnpIsChainDereferenced_function_004ABAE8.md) (`PAGE` → `.text`)
  - `0x00A053DC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A053EA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A0558C` → [PipAreDriversLoaded](../../text/47/PipAreDriversLoaded_function_004708D4.md) (`PAGE` → `.text`)
  - `0x00A05677` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A056D9` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A056F3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A056FF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **10**
  - `0x00A05439` → [sub_00B33FE8](../B3/Unknown_function_00B33FE8.md) (`tail-transfer`)
  - `0x00A054FC` → [sub_00B33FE8 + 0x1A5](../B3/Unknown_function_00B33FE8.md) (`tail-transfer`)
  - `0x00A0550D` → [sub_00B33FE8 + 0x1A8](../B3/Unknown_function_00B33FE8.md) (`tail-transfer`)
  - `0x00A055E6` → [sub_00B33FE8 + 0x53](../B3/Unknown_function_00B33FE8.md) (`tail-transfer`)
  - `0x00A055EC` → [sub_00B33FE8 + 0x88](../B3/Unknown_function_00B33FE8.md) (`tail-transfer`)
  - `0x00A0563D` → [sub_00B33FE8 + 0x1BB](../B3/Unknown_function_00B33FE8.md) (`tail-transfer`)
  - `0x00A05649` → [sub_00B33FE8 + 0x1BB](../B3/Unknown_function_00B33FE8.md) (`tail-transfer`)
  - `0x00A056AD` → [sub_00B33FE8 + 0x1D3](../B3/Unknown_function_00B33FE8.md) (`tail-transfer`)
  - `0x00A056C6` → [sub_00B33FE8 + 0x1D7](../B3/Unknown_function_00B33FE8.md) (`tail-transfer`)
  - `0x00A056DF` → [sub_00B33FE8 + 0x1D7](../B3/Unknown_function_00B33FE8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A05170  40 55                           push rbp
00A05172  53                              push rbx
00A05173  56                              push rsi
00A05174  57                              push rdi
00A05175  41 54                           push r12
00A05177  41 55                           push r13
00A05179  41 56                           push r14
00A0517B  41 57                           push r15
00A0517D  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
00A05182  48 81 EC 98 00 00 00            sub rsp, 0x98
00A05189  48 8B 31                        mov rsi, qword ptr [rcx]
00A0518C  33 C0                           xor eax, eax
00A0518E  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
00A05192  0F 57 C0                        xorps xmm0, xmm0
00A05195  4C 8B E9                        mov r13, rcx
00A05198  48 89 45 F7                     mov qword ptr [rbp - 9], rax
00A0519C  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
00A051A0  44 8B F8                        mov r15d, eax
00A051A3  4C 8B B6 A0 00 00 00            mov r14, qword ptr [rsi + 0xa0]
00A051AA  8D 78 07                        lea edi, [rax + 7]
00A051AD  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
00A051B1  89 45 77                        mov dword ptr [rbp + 0x77], eax
00A051B4  88 45 67                        mov byte ptr [rbp + 0x67], al
00A051B7  48 89 45 FF                     mov qword ptr [rbp - 1], rax
00A051BB  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
00A051BF  88 45 6F                        mov byte ptr [rbp + 0x6f], al
00A051C2  48 89 45 7F                     mov qword ptr [rbp + 0x7f], rax
00A051C6  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
00A051CA  4C 89 75 E7                     mov qword ptr [rbp - 0x19], r14
00A051CE  0F 11 45 07                     movups xmmword ptr [rbp + 7], xmm0
00A051D2  4D 85 F6                        test r14, r14
00A051D5  0F 84 B9 00 00 00               je 0x140a05294
00A051DB  49 8B 86 38 01 00 00            mov rax, qword ptr [r14 + 0x138]
00A051E2  4C 8B 60 28                     mov r12, qword ptr [rax + 0x28]
00A051E6  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A051EF  48 8D 0D EA 72 58 00            lea rcx, [rip + 0x5872ea]
00A051F6  B2 01                           mov dl, 1
00A051F8  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00A051FF  90                              nop
00A05200  E8 1B FC 80 FF                  call 0x140214e20
00A05205  B2 01                           mov dl, 1
00A05207  48 8D 0D 52 73 58 00            lea rcx, [rip + 0x587352]
00A0520E  E8 AD C9 80 FF                  call 0x140211bc0
00A05213  41 8B 84 24 2C 01 00 00         mov eax, dword ptr [r12 + 0x12c]
00A0521B  2D 15 03 00 00                  sub eax, 0x315
00A05220  83 F8 01                        cmp eax, 1
00A05223  0F 87 E6 01 00 00               ja 0x140a0540f
00A05229  BB 56 00 00 C0                  mov ebx, 0xc0000056
00A0522E  45 33 ED                        xor r13d, r13d
00A05231  48 8D 0D 28 73 58 00            lea rcx, [rip + 0x587328]
00A05238  E8 D3 A7 85 FF                  call 0x14025fa10
00A0523D  48 8D 0D 9C 72 58 00            lea rcx, [rip + 0x58729c]
00A05244  E8 C7 A7 85 FF                  call 0x14025fa10
00A05249  E8 62 86 85 FF                  call 0x14025d8b0
00A0524E  81 FB 56 00 00 C0               cmp ebx, 0xc0000056
00A05254  0F 85 48 01 00 00               jne 0x140a053a2
00A0525A  4D 85 FF                        test r15, r15
00A0525D  0F 85 61 01 00 00               jne 0x140a053c4
00A05263  48 8B 4D 7F                     mov rcx, qword ptr [rbp + 0x7f]
00A05267  48 85 C9                        test rcx, rcx
00A0526A  0F 85 81 04 00 00               jne 0x140a056f1
00A05270  48 8B 4D C7                     mov rcx, qword ptr [rbp - 0x39]
00A05274  48 85 C9                        test rcx, rcx
00A05277  0F 85 80 04 00 00               jne 0x140a056fd
00A0527D  8B C3                           mov eax, ebx
00A0527F  48 81 C4 98 00 00 00            add rsp, 0x98
00A05286  41 5F                           pop r15
00A05288  41 5E                           pop r14
00A0528A  41 5D                           pop r13
00A0528C  41 5C                           pop r12
00A0528E  5F                              pop rdi
00A0528F  5E                              pop rsi
00A05290  5B                              pop rbx
00A05291  5D                              pop rbp
00A05292  C3                              ret
00A05293  CC                              int3
00A05294  4C 8B E0                        mov r12, rax
00A05297  E9 4A FF FF FF                  jmp 0x140a051e6
00A0529C  44 8B 6D 77                     mov r13d, dword ptr [rbp + 0x77]
00A052A0  48 8D 45 7F                     lea rax, [rbp + 0x7f]
00A052A4  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A052A9  45 8B CD                        mov r9d, r13d
00A052AC  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
00A052B0  4D 8B C6                        mov r8, r14
00A052B3  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
00A052B8  48 8B D6                        mov rdx, rsi
00A052BB  8B CF                           mov ecx, edi
00A052BD  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A052C2  E8 91 07 00 00                  call 0x140a05a58
00A052C7  8B D8                           mov ebx, eax
00A052C9  85 C0                           test eax, eax
00A052CB  0F 88 65 03 00 00               js 0x140a05636
00A052D1  33 DB                           xor ebx, ebx
00A052D3  83 FF 03                        cmp edi, 3
00A052D6  0F 84 18 01 00 00               je 0x140a053f4
00A052DC  4C 8D 05 05 C2 60 FF            lea r8, [rip - 0x9f3dfb]
00A052E3  48 8B 55 7F                     mov rdx, qword ptr [rbp + 0x7f]
00A052E7  45 33 C9                        xor r9d, r9d
00A052EA  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
00A052EF  48 8B CE                        mov rcx, rsi
00A052F2  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00A052F7  E8 5C EF F4 FF                  call 0x140954258
00A052FC  48 8B 4D C7                     mov rcx, qword ptr [rbp - 0x39]
00A05300  41 8B D5                        mov edx, r13d
00A05303  E8 F0 06 00 00                  call 0x140a059f8
00A05308  41 F7 84 24 C0 02 00 00 00 80 00 00  test dword ptr [r12 + 0x2c0], 0x8000
00A05314  0F 85 67 03 00 00               jne 0x140a05681
00A0531A  8D 47 FE                        lea eax, [rdi - 2]
00A0531D  A9 FC FF FF FF                  test eax, 0xfffffffc
00A05322  0F 85 79 03 00 00               jne 0x140a056a1
00A05328  83 FF 04                        cmp edi, 4
00A0532B  0F 84 70 03 00 00               je 0x140a056a1
00A05331  45 33 C9                        xor r9d, r9d
00A05334  41 B0 01                        mov r8b, 1
00A05337  8B D7                           mov edx, edi
00A05339  49 8B CE                        mov rcx, r14
00A0533C  E8 B7 0A 00 00                  call 0x140a05df8
00A05341  49 8B CE                        mov rcx, r14
00A05344  E8 CF 08 00 00                  call 0x140a05c18
00A05349  8D 47 FD                        lea eax, [rdi - 3]
00A0534C  A9 FD FF FF FF                  test eax, 0xfffffffd
00A05351  0F 85 4A 03 00 00               jne 0x140a056a1
00A05357  4C 8D 45 D7                     lea r8, [rbp - 0x29]
00A0535B  8B D7                           mov edx, edi
00A0535D  48 8B CE                        mov rcx, rsi
00A05360  E8 07 06 00 00                  call 0x140a0596c
00A05365  48 8D 0D F4 71 58 00            lea rcx, [rip + 0x5871f4]
00A0536C  E8 9F A6 85 FF                  call 0x14025fa10
00A05371  48 8D 0D 68 71 58 00            lea rcx, [rip + 0x587168]
00A05378  E8 93 A6 85 FF                  call 0x14025fa10
00A0537D  E8 2E 85 85 FF                  call 0x14025d8b0
00A05382  48 8B 4D C7                     mov rcx, qword ptr [rbp - 0x39]
00A05386  41 B9 01 00 00 00               mov r9d, 1
00A0538C  45 33 C0                        xor r8d, r8d
00A0538F  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00A05394  41 8B D5                        mov edx, r13d
00A05397  E8 4C 67 AA FF                  call 0x1404abae8
00A0539C  45 33 ED                        xor r13d, r13d
00A0539F  41 8B DD                        mov ebx, r13d
00A053A2  83 FF 04                        cmp edi, 4
00A053A5  0F 84 AF FE FF FF               je 0x140a0525a
00A053AB  45 33 C9                        xor r9d, r9d
00A053AE  8B D7                           mov edx, edi
00A053B0  48 8B CE                        mov rcx, rsi
00A053B3  4D 85 FF                        test r15, r15
00A053B6  0F 84 28 03 00 00               je 0x140a056e4
00A053BC  4D 8B C7                        mov r8, r15
00A053BF  E8 1C FB FF FF                  call 0x140a04ee0
00A053C4  44 39 2D 19 72 58 00            cmp dword ptr [rip + 0x587219], r13d
00A053CB  0F 85 92 FE FF FF               jne 0x140a05263
00A053D1  49 8B 4F 10                     mov rcx, qword ptr [r15 + 0x10]
00A053D5  BF 50 6E 70 4D                  mov edi, 0x4d706e50
00A053DA  8B D7                           mov edx, edi
00A053DC  E8 8F D4 17 00                  call 0x140b82870
00A053E1  8B D7                           mov edx, edi
00A053E3  4D 89 6F 10                     mov qword ptr [r15 + 0x10], r13
00A053E7  49 8B CF                        mov rcx, r15
00A053EA  E8 81 D4 17 00                  call 0x140b82870
00A053EF  E9 6F FE FF FF                  jmp 0x140a05263
00A053F4  48 8B 5D EF                     mov rbx, qword ptr [rbp - 0x11]
00A053F8  48 85 DB                        test rbx, rbx
00A053FB  0F 85 4D 02 00 00               jne 0x140a0564e
00A05401  33 DB                           xor ebx, ebx
00A05403  4C 8D 05 16 4E 61 FF            lea r8, [rip - 0x9eb1ea]
00A0540A  E9 D4 FE FF FF                  jmp 0x140a052e3
00A0540F  48 8B CE                        mov rcx, rsi
00A05412  E8 F9 02 00 00                  call 0x140a05710
00A05417  8B F8                           mov edi, eax
00A05419  83 F8 04                        cmp eax, 4
00A0541C  0F 85 52 01 00 00               jne 0x140a05574
00A05422  48 8B D6                        mov rdx, rsi
00A05425  8B CF                           mov ecx, edi
00A05427  E8 B4 03 00 00                  call 0x140a057e0
00A0542C  8B D8                           mov ebx, eax
00A0542E  85 C0                           test eax, eax
00A05430  0F 88 F8 FD FF FF               js 0x140a0522e
00A05436  83 FF 04                        cmp edi, 4
00A05439  0F 84 A9 EB 12 00               je 0x140b33fe8
00A0543F  85 FF                           test edi, edi
00A05441  0F 84 42 01 00 00               je 0x140a05589
00A05447  8B CF                           mov ecx, edi
00A05449  E8 F2 03 00 00                  call 0x140a05840
00A0544E  4C 8B F8                        mov r15, rax
00A05451  48 85 C0                        test rax, rax
00A05454  0F 84 4E 01 00 00               je 0x140a055a8
00A0545A  4C 8D 4D D7                     lea r9, [rbp - 0x29]
00A0545E  4C 8B C0                        mov r8, rax
00A05461  8B D7                           mov edx, edi
00A05463  49 8B CE                        mov rcx, r14
00A05466  E8 65 04 00 00                  call 0x140a058d0
00A0546B  85 C0                           test eax, eax
00A0546D  0F 88 E8 00 00 00               js 0x140a0555b
00A05473  4C 8B 75 D7                     mov r14, qword ptr [rbp - 0x29]
00A05477  48 8D 45 6F                     lea rax, [rbp + 0x6f]
00A0547B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A05480  4C 8D 4D 77                     lea r9, [rbp + 0x77]
00A05484  48 8D 45 67                     lea rax, [rbp + 0x67]
00A05488  4C 8B C6                        mov r8, rsi
00A0548B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A05490  8B D7                           mov edx, edi
00A05492  48 8D 45 C7                     lea rax, [rbp - 0x39]
00A05496  49 8B CE                        mov rcx, r14
00A05499  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A0549E  E8 E9 07 00 00                  call 0x140a05c8c
00A054A3  8B D8                           mov ebx, eax
00A054A5  85 C0                           test eax, eax
00A054A7  79 69                           jns 0x140a05512
00A054A9  45 33 ED                        xor r13d, r13d
00A054AC  85 DB                           test ebx, ebx
00A054AE  0F 88 FB 00 00 00               js 0x140a055af
00A054B4  44 8B 6D 77                     mov r13d, dword ptr [rbp + 0x77]
00A054B8  33 DB                           xor ebx, ebx
00A054BA  38 5D 67                        cmp byte ptr [rbp + 0x67], bl
00A054BD  0F 85 12 01 00 00               jne 0x140a055d5
00A054C3  F7 C7 FB FF FF FF               test edi, 0xfffffffb
00A054C9  0F 85 22 01 00 00               jne 0x140a055f1
00A054CF  45 33 ED                        xor r13d, r13d
00A054D2  41 8B DD                        mov ebx, r13d
00A054D5  49 8B 16                        mov rdx, qword ptr [r14]
00A054D8  3B 1A                           cmp ebx, dword ptr [rdx]
00A054DA  0F 83 BC FD FF FF               jae 0x140a0529c
00A054E0  48 85 D2                        test rdx, rdx
00A054E3  0F 84 B3 FD FF FF               je 0x140a0529c
00A054E9  0F AE E8                        lfence
00A054EC  8B C3                           mov eax, ebx
00A054EE  FF C3                           inc ebx
00A054F0  48 8D 0C 40                     lea rcx, [rax + rax*2]
00A054F4  48 8B 44 CA 10                  mov rax, qword ptr [rdx + rcx*8 + 0x10]
00A054F9  48 85 C0                        test rax, rax
00A054FC  0F 84 8B EC 12 00               je 0x140b3418d
00A05502  48 8B 80 38 01 00 00            mov rax, qword ptr [rax + 0x138]
00A05509  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00A0550D  E9 7E EC 12 00                  jmp 0x140b34190
00A05512  8B D7                           mov edx, edi
00A05514  49 8B CD                        mov rcx, r13
00A05517  E8 1C 21 00 00                  call 0x140a07638
00A0551C  49 8B 75 00                     mov rsi, qword ptr [r13]
00A05520  8B D8                           mov ebx, eax
00A05522  45 33 ED                        xor r13d, r13d
00A05525  85 C0                           test eax, eax
00A05527  78 83                           js 0x140a054ac
00A05529  8B CF                           mov ecx, edi
00A0552B  E8 90 F9 FF FF                  call 0x140a04ec0
00A05530  44 8A C0                        mov r8b, al
00A05533  4C 8D 4D 7F                     lea r9, [rbp + 0x7f]
00A05537  49 8B D6                        mov rdx, r14
00A0553A  E8 C9 21 00 00                  call 0x140a07708
00A0553F  8B D8                           mov ebx, eax
00A05541  83 FF 03                        cmp edi, 3
00A05544  0F 85 62 FF FF FF               jne 0x140a054ac
00A0554A  4C 8D 45 EF                     lea r8, [rbp - 0x11]
00A0554E  49 8B D6                        mov rdx, r14
00A05551  E8 BA 42 08 00                  call 0x140a89810
00A05556  E9 51 FF FF FF                  jmp 0x140a054ac
00A0555B  41 8B 17                        mov edx, dword ptr [r15]
00A0555E  4D 8D 47 08                     lea r8, [r15 + 8]
00A05562  48 8B CE                        mov rcx, rsi
00A05565  E8 FE F3 FF FF                  call 0x140a04968
00A0556A  BB 28 00 00 80                  mov ebx, 0x80000028
00A0556F  E9 BA FC FF FF                  jmp 0x140a0522e
00A05574  41 B1 01                        mov r9b, 1
00A05577  45 33 C0                        xor r8d, r8d
00A0557A  8B D7                           mov edx, edi
00A0557C  48 8B CE                        mov rcx, rsi
00A0557F  E8 5C F9 FF FF                  call 0x140a04ee0
00A05584  E9 99 FE FF FF                  jmp 0x140a05422
00A05589  49 8B CC                        mov rcx, r12
00A0558C  E8 43 B3 A6 FF                  call 0x1404708d4
00A05591  85 C0                           test eax, eax
00A05593  0F 85 AE FE FF FF               jne 0x140a05447
00A05599  48 8B CE                        mov rcx, rsi
00A0559C  E8 13 ED D3 FF                  call 0x1407442b4
00A055A1  8B D8                           mov ebx, eax
00A055A3  E9 86 FC FF FF                  jmp 0x140a0522e
00A055A8  45 33 C0                        xor r8d, r8d
00A055AB  33 D2                           xor edx, edx
00A055AD  EB B3                           jmp 0x140a05562
00A055AF  49 8B CE                        mov rcx, r14
00A055B2  E8 59 2D 00 00                  call 0x140a08310
00A055B7  81 FB 28 00 00 80               cmp ebx, 0x80000028
00A055BD  0F 84 6E FC FF FF               je 0x140a05231
00A055C3  45 33 C0                        xor r8d, r8d
00A055C6  33 D2                           xor edx, edx
00A055C8  48 8B CE                        mov rcx, rsi
00A055CB  E8 98 F3 FF FF                  call 0x140a04968
00A055D0  E9 5C FC FF FF                  jmp 0x140a05231
00A055D5  8A 4D 6F                        mov cl, byte ptr [rbp + 0x6f]
00A055D8  E8 0B 23 D3 FF                  call 0x1407378e8
00A055DD  41 8D 45 FF                     lea eax, [r13 - 1]
00A055E1  48 63 D8                        movsxd rbx, eax
00A055E4  85 C0                           test eax, eax
00A055E6  0F 89 4F EA 12 00               jns 0x140b3403b
00A055EC  E9 7F EA 12 00                  jmp 0x140b34070
00A055F1  8D 47 FD                        lea eax, [rdi - 3]
00A055F4  A9 FD FF FF FF                  test eax, 0xfffffffd
00A055F9  0F 85 DD FC FF FF               jne 0x140a052dc
00A055FF  4D 8B C6                        mov r8, r14
00A05602  8B D7                           mov edx, edi
00A05604  48 8B CE                        mov rcx, rsi
00A05607  E8 1C 99 0C 00                  call 0x140acef28
00A0560C  48 8B 4D E7                     mov rcx, qword ptr [rbp - 0x19]
00A05610  45 33 C9                        xor r9d, r9d
00A05613  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
00A05618  49 8B D6                        mov rdx, r14
00A0561B  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
00A05620  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
00A05624  45 8D 41 03                     lea r8d, [r9 + 3]
00A05628  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
00A0562C  E8 FF 44 00 00                  call 0x140a09b30
00A05631  E9 9D FC FF FF                  jmp 0x140a052d3
00A05636  45 33 ED                        xor r13d, r13d
00A05639  44 38 6D 67                     cmp byte ptr [rbp + 0x67], r13b
00A0563D  0F 84 60 EB 12 00               je 0x140b341a3
00A05643  E8 D0 22 D3 FF                  call 0x140737918
00A05648  90                              nop
00A05649  E9 55 EB 12 00                  jmp 0x140b341a3
00A0564E  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
00A05654  4C 8D 05 25 15 62 FF            lea r8, [rip - 0x9deadb]
00A0565B  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00A05661  45 33 C9                        xor r9d, r9d
00A05664  48 8B D3                        mov rdx, rbx
00A05667  48 8B CE                        mov rcx, rsi
00A0566A  E8 E9 EB F4 FF                  call 0x140954258
00A0566F  BA 50 6E 70 4B                  mov edx, 0x4b706e50
00A05674  48 8B CB                        mov rcx, rbx
00A05677  E8 F4 D1 17 00                  call 0x140b82870
00A0567C  E9 80 FD FF FF                  jmp 0x140a05401
00A05681  41 8B 84 24 8C 01 00 00         mov eax, dword ptr [r12 + 0x18c]
00A05689  A8 10                           test al, 0x10
00A0568B  0F 84 89 FC FF FF               je 0x140a0531a
00A05691  49 8B D6                        mov rdx, r14
00A05694  49 8B CC                        mov rcx, r12
00A05697  E8 68 56 D2 FF                  call 0x14072ad04
00A0569C  E9 79 FC FF FF                  jmp 0x140a0531a
00A056A1  41 39 9C 24 38 02 00 00         cmp dword ptr [r12 + 0x238], ebx
00A056A9  48 8B 5D E7                     mov rbx, qword ptr [rbp - 0x19]
00A056AD  0F 84 08 EB 12 00               je 0x140b341bb
00A056B3  48 8D 55 F7                     lea rdx, [rbp - 9]
00A056B7  48 8B CB                        mov rcx, rbx
00A056BA  E8 11 88 D3 FF                  call 0x14073ded0
00A056BF  4C 8B 6D F7                     mov r13, qword ptr [rbp - 9]
00A056C3  4D 85 ED                        test r13, r13
00A056C6  0F 84 F3 EA 12 00               je 0x140b341bf
00A056CC  49 8B 45 20                     mov rax, qword ptr [r13 + 0x20]
00A056D0  BA 03 00 00 00                  mov edx, 3
00A056D5  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
00A056D9  E8 F2 53 CB FF                  call 0x1406baad0
00A056DE  90                              nop
00A056DF  E9 DB EA 12 00                  jmp 0x140b341bf
00A056E4  45 33 C0                        xor r8d, r8d
00A056E7  E8 F4 F7 FF FF                  call 0x140a04ee0
00A056EC  E9 72 FB FF FF                  jmp 0x140a05263
00A056F1  33 D2                           xor edx, edx
00A056F3  E8 78 D1 17 00                  call 0x140b82870
00A056F8  E9 73 FB FF FF                  jmp 0x140a05270
00A056FD  33 D2                           xor edx, edx
00A056FF  E8 6C D1 17 00                  call 0x140b82870
00A05704  E9 74 FB FF FF                  jmp 0x140a0527d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpProcessQueryRemoveAndEject(__int64 a1)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int8 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int8 v_stack_p8;

    v_rsp = (v_rsp) - (152);
    result = 0;
    v_stack_m90 = 0;
    v_stack_m68 = 0;
    v_stack_m80 = 0;
    v_stack_m98 = 0;
    v_stack_p18 = 0;
    v_stack_p8 = 0;
    v_stack_m60 = 0;
    v_stack_m88 = 0;
    v_stack_p10 = 0;
    v_stack_p20 = 0;
    v_stack_m70 = 0;
    v_stack_m78 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 160);
    v_stack_m58 = v_xmm0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 160) == 0) goto loc_00A05294;
loc_00A051E6:
    result = ExAcquireResourceExclusiveLite(v_rip + 5796586, 1, a3, a4);
    result = ExAcquireResourceSharedLite(v_rip + 5796690, 1, a3, a4);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 160) + 312) + 40) + 300))) - (789));
    if (((unsigned int)(result)) > 1) goto loc_00A0540F;
loc_00A0522E:
    v_r13 = 0;
loc_00A05231:
    result = ExReleaseResourceLite(v_rip + 5796648, 1, a3, a4);
    result = ExReleaseResourceLite(v_rip + 5796508, 1, a3, a4);
    result = KeLeaveCriticalRegion(v_rip + 5796508, 1, a3, a4);
    if (((unsigned int)((unsigned int)(0xC0000056ULL))) != 0xC0000056ULL) goto loc_00A053A2;
loc_00A0525A:
    if (0 != 0) goto loc_00A053C4;
loc_00A05263:
    if (v_stack_p20 != 0) goto loc_00A056F1;
loc_00A05270:
    if (v_stack_m98 != 0) goto loc_00A056FD;
loc_00A0527D:
    v_rsp = (v_rsp) + (152);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000056ULL)));
loc_00A05294:
    goto loc_00A051E6;
loc_00A0529C:
    v_stack_p30 = v_stack_p20;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_m98;
    result = PiProcessQueryAndCancelRemoval((unsigned int)((unsigned int)(result + 7)), *(unsigned __int64 *)(a1), *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 160), (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))));
    if (sign_flag) goto loc_00A05636;
    v_rbx = 0;
loc_00A052D3:
    if (((unsigned int)(result + 7)) == 3) goto loc_00A053F4;
loc_00A052DC:
loc_00A052E3:
    a4 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    result = PnpNotifyUserModeDeviceRemoval(*(unsigned __int64 *)(a1), v_stack_p20, v_rip - 10436091, a4);
    result = PiSendTargetDeviceRemoveCompleteNotification(v_stack_m98, (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), v_rip - 10436091, a4);
    if (((*(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(0xC0000056ULL))) + 704)) & (0x8000ULL)) != 0) goto loc_00A05681;
loc_00A0531A:
    if ((((unsigned int)(result + 7 - 2)) & (0xFFFFFFFCULL)) != 0) goto loc_00A056A1;
    if (((unsigned int)(result + 7)) == 4) goto loc_00A056A1;
    a4 = 0;
    result = PnpInvalidateRelationsInList(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 160), (unsigned int)((unsigned int)(result + 7)), 1, a4);
    result = IopRemoveDeviceRelationsFromList(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 160), (unsigned int)((unsigned int)(result + 7)), 1, a4);
    if ((((unsigned int)(result + 7 - 3)) & (0xFFFFFFFDULL)) != 0) goto loc_00A056A1;
    result = PiEventRemovalPostSurpriseRemove(*(unsigned __int64 *)(a1), (unsigned int)((unsigned int)(result + 7)), v_stack_m88, a4);
    result = ExReleaseResourceLite(v_rip + 5796340, (unsigned int)((unsigned int)(result + 7)), v_stack_m88, a4);
    result = ExReleaseResourceLite(v_rip + 5796200, (unsigned int)((unsigned int)(result + 7)), v_stack_m88, a4);
    result = KeLeaveCriticalRegion(v_rip + 5796200, (unsigned int)((unsigned int)(result + 7)), v_stack_m88, a4);
    a3 = 0;
    v_stack_p20 = 0;
    result = PnpIsChainDereferenced(v_stack_m98, (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), a3, 1);
    v_r13 = 0;
loc_00A053A2:
    if (((unsigned int)(result + 7)) == 4) goto loc_00A0525A;
    a4 = 0;
    if (0 == 0) goto loc_00A056E4;
    result = PnpRecordBlackboxPnpEventInformation(*(unsigned __int64 *)(a1), (unsigned int)((unsigned int)(result + 7)), 0, a4);
loc_00A053C4:
    if ((*(unsigned int *)(v_rip + 5796377)) != 0) goto loc_00A05263;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(0 + 16), (unsigned int)((unsigned int)((unsigned int)(0x4D706E50ULL))), 0, a4);
    *(unsigned __int64 *)(0 + 16) = 0;
    result = ExFreePoolWithTag(0, (unsigned int)((unsigned int)((unsigned int)(0x4D706E50ULL))), 0, a4);
    goto loc_00A05263;
loc_00A053F4:
    if (v_stack_m70 != 0) goto loc_00A0564E;
loc_00A05401:
    v_rbx = 0;
    goto loc_00A052E3;
loc_00A0540F:
    result = PiDetermineDeleteType(*(unsigned __int64 *)(a1), (unsigned int)((unsigned int)((unsigned int)(0x4D706E50ULL))), v_rip - 10400234, a4);
    if (((unsigned int)(result)) != 4) goto loc_00A05574;
loc_00A05422:
    result = PiCheckRemovalPreconditions((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), *(unsigned __int64 *)(a1), v_rip - 10400234, a4);
    if (sign_flag) goto loc_00A0522E;
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_00A05589;
loc_00A05447:
    result = PiEventAllocateVetoBuffer((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), *(unsigned __int64 *)(a1), v_rip - 10400234, a4);
    if (result == 0) goto loc_00A055A8;
    result = PnpBuildRemovalRelationList(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 160), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), result, v_stack_m88);
    if (sign_flag) goto loc_00A0555B;
    v_stack_p30 = v_stack_p10;
    v_stack_p28 = v_stack_p8;
    v_stack_p20 = v_stack_m98;
    result = PiEventBuildPdoList(v_stack_m88, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), *(unsigned __int64 *)(a1), v_stack_p18);
    if (!sign_flag) goto loc_00A05512;
    v_r13 = 0;
loc_00A054AC:
    if (sign_flag) goto loc_00A055AF;
    v_rbx = 0;
    if (v_stack_p8 != 0) goto loc_00A055D5;
    if ((((unsigned int)((unsigned int)((unsigned int)(result)))) & (0xFFFFFFFBULL)) != 0) goto loc_00A055F1;
    v_r13 = 0;
    if (0 >= (*(unsigned int *)(*(unsigned __int64 *)(v_stack_m88)))) goto loc_00A0529C;
    if (*(unsigned __int64 *)(v_stack_m88) == 0) goto loc_00A0529C;
    v_rbx = (unsigned int)((0) + 1);
loc_00A05512:
    result = PnpResizeTargetDeviceBlock(0, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), *(unsigned __int64 *)(a1), v_stack_p18);
    v_r13 = 0;
    if (sign_flag) goto loc_00A054AC;
    result = PiEventAreDeviceRelationsExcluded((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), *(unsigned __int64 *)(a1), v_stack_p18);
    result = PnpCompileDeviceInstancePaths((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_m88, (unsigned __int8)(result), v_stack_p20);
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 3) goto loc_00A054AC;
    result = PnpBuildUnsafeRemovalDeviceList((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_m88, v_stack_m70, v_stack_p20);
    goto loc_00A054AC;
loc_00A0555B:
loc_00A05562:
    result = PnpFinalizeVetoedRemove(*(unsigned __int64 *)(v_r13), (unsigned int)(*(unsigned int *)(result)), result + 8, v_stack_p20);
    goto loc_00A0522E;
loc_00A05574:
    a3 = 0;
    result = PnpRecordBlackboxPnpEventInformation(*(unsigned __int64 *)(v_r13), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a3, 1);
    goto loc_00A05422;
loc_00A05589:
    result = PipAreDriversLoaded((unsigned int)((unsigned int)((unsigned int)(0xC0000056ULL))), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a3, 1);
    if ((unsigned int)(result) != 0) goto loc_00A05447;
    result = PiProcessQueryRemoveNoFdo(*(unsigned __int64 *)(v_r13), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a3, 1);
    goto loc_00A0522E;
loc_00A055A8:
    a3 = 0;
    a2 = 0;
    goto loc_00A05562;
loc_00A055AF:
    result = IopFreeRelationList(v_stack_m88, a2, a3, 1);
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0x80000028ULL) goto loc_00A05231;
    a3 = 0;
    a2 = 0;
    result = PnpFinalizeVetoedRemove(*(unsigned __int64 *)(v_r13), a2, a3, 1);
    goto loc_00A05231;
loc_00A055D5:
    result = PpProfileBeginHardwareProfileTransition(v_stack_p10, a2, a3, 1);
loc_00A055F1:
    if ((((unsigned int)((unsigned int)((unsigned int)(result)) - 3)) & (0xFFFFFFFDULL)) != 0) goto loc_00A052DC;
    result = PiLogSurpriseRemoveEvent(*(unsigned __int64 *)(v_r13), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_m88, 1);
    a4 = 0;
    v_stack_p38 = (int)((unsigned int)(v_r13 - 1));
    v_stack_p30 = (int)((unsigned int)(v_r13 - 1));
    v_stack_p28 = (unsigned int)((int)((unsigned int)(v_r13 - 1)));
    v_stack_p20 = (unsigned int)((int)((unsigned int)(v_r13 - 1)));
    result = PnpDeleteLockedDeviceNodes(v_stack_m78, v_stack_m88, a4 + 3, a4);
    goto loc_00A052D3;
loc_00A05636:
    v_r13 = 0;
    result = PpProfileCancelHardwareProfileTransition(v_stack_m78, v_stack_m88, a4 + 3, a4);
loc_00A0564E:
    a4 = 0;
    result = PnpNotifyUserModeDeviceRemoval(*(unsigned __int64 *)(v_r13), (int)((unsigned int)(v_r13 - 1)), v_rip - 10349275, a4);
    result = ExFreePoolWithTag((int)((unsigned int)(v_r13 - 1)), (unsigned int)(0x4B706E50ULL), v_rip - 10349275, a4);
    goto loc_00A05401;
loc_00A05681:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(0xC0000056ULL))) + 396)))) & (16)) == 0) goto loc_00A0531A;
    result = PnpFinalizeDeviceRemovalForReset((unsigned int)((unsigned int)((unsigned int)(0xC0000056ULL))), v_stack_m88, v_rip - 10349275, a4);
    goto loc_00A0531A;
loc_00A056A1:
    result = IopQueryDockRemovalInterface(v_stack_m78, v_stack_m68, v_rip - 10349275, a4);
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_stack_m68 + 8), 3, v_rip - 10349275, a4);
loc_00A056E4:
    a3 = 0;
    result = PnpRecordBlackboxPnpEventInformation(*(unsigned __int64 *)(v_stack_m68 + 8), 3, a3, a4);
    goto loc_00A05263;
loc_00A056F1:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m68 + 8), a2, a3, a4);
    goto loc_00A05270;
loc_00A056FD:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m68 + 8), a2, a3, a4);
    goto loc_00A0527D;
}
```

## 5. (Beta) C Style

```c
int64_t PnpProcessQueryRemoveAndEject(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint8_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint8_t v_stack_p8;

    local_rsp = (local_rsp) - (152);
    result = 0;
    v_stack_m90 = 0;
    v_stack_m68 = 0;
    v_stack_m80 = 0;
    v_stack_m98 = 0;
    v_stack_p18 = 0;
    v_stack_p8 = 0;
    v_stack_m60 = 0;
    v_stack_m88 = 0;
    v_stack_p10 = 0;
    v_stack_p20 = 0;
    v_stack_m70 = 0;
    v_stack_m78 = *(uint64_t *)(*(uint64_t *)(arg1) + 0xA0);
    v_stack_m58 = v_xmm0;
    if (*(uint64_t *)(*(uint64_t *)(arg1) + 0xA0) == 0) goto loc_00A05294;
loc_00A051E6:
    result = ExAcquireResourceExclusiveLite(v_rip + 5796586, 1, a3, a4);
    result = ExAcquireResourceSharedLite(v_rip + 5796690, 1, a3, a4);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0xA0) + 0x138) + 0x28) + 0x12C))) - (789));
    if (((uint32_t)(result)) > 1) goto loc_00A0540F;
loc_00A0522E:
    local_r13 = 0;
loc_00A05231:
    result = ExReleaseResourceLite(v_rip + 5796648, 1, a3, a4);
    result = ExReleaseResourceLite(v_rip + 5796508, 1, a3, a4);
    result = KeLeaveCriticalRegion(v_rip + 5796508, 1, a3, a4);
    if (((uint32_t)((uint32_t)(0xC0000056ULL))) != 0xC0000056ULL) goto loc_00A053A2;
loc_00A0525A:
    if (0 != 0) goto loc_00A053C4;
loc_00A05263:
    if (v_stack_p20 != 0) goto loc_00A056F1;
loc_00A05270:
    if (v_stack_m98 != 0) goto loc_00A056FD;
loc_00A0527D:
    local_rsp = (local_rsp) + (152);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000056ULL)));
loc_00A05294:
    goto loc_00A051E6;
loc_00A0529C:
    v_stack_p30 = v_stack_p20;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_m98;
    result = PiProcessQueryAndCancelRemoval((uint32_t)((uint32_t)(result + 7)), *(uint64_t *)(arg1), *(uint64_t *)(*(uint64_t *)(arg1) + 0xA0), (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))));
    if (sign_flag) goto loc_00A05636;
    local_rbx = 0;
loc_00A052D3:
    if (((uint32_t)(result + 7)) == 3) goto loc_00A053F4;
loc_00A052DC:
loc_00A052E3:
    a4 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    result = PnpNotifyUserModeDeviceRemoval(*(uint64_t *)(arg1), v_stack_p20, v_rip - 10436091, a4);
    result = PiSendTargetDeviceRemoveCompleteNotification(v_stack_m98, (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), v_rip - 10436091, a4);
    if (((*(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(0xC0000056ULL))) + 0x2C0)) & (0x8000ULL)) != 0) goto loc_00A05681;
loc_00A0531A:
    if ((((uint32_t)(result + 7 - 2)) & (0xFFFFFFFCULL)) != 0) goto loc_00A056A1;
    if (((uint32_t)(result + 7)) == 4) goto loc_00A056A1;
    a4 = 0;
    result = PnpInvalidateRelationsInList(*(uint64_t *)(*(uint64_t *)(arg1) + 0xA0), (uint32_t)((uint32_t)(result + 7)), 1, a4);
    result = IopRemoveDeviceRelationsFromList(*(uint64_t *)(*(uint64_t *)(arg1) + 0xA0), (uint32_t)((uint32_t)(result + 7)), 1, a4);
    if ((((uint32_t)(result + 7 - 3)) & (0xFFFFFFFDULL)) != 0) goto loc_00A056A1;
    result = PiEventRemovalPostSurpriseRemove(*(uint64_t *)(arg1), (uint32_t)((uint32_t)(result + 7)), v_stack_m88, a4);
    result = ExReleaseResourceLite(v_rip + 5796340, (uint32_t)((uint32_t)(result + 7)), v_stack_m88, a4);
    result = ExReleaseResourceLite(v_rip + 5796200, (uint32_t)((uint32_t)(result + 7)), v_stack_m88, a4);
    result = KeLeaveCriticalRegion(v_rip + 5796200, (uint32_t)((uint32_t)(result + 7)), v_stack_m88, a4);
    a3 = 0;
    v_stack_p20 = 0;
    result = PnpIsChainDereferenced(v_stack_m98, (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), a3, 1);
    local_r13 = 0;
loc_00A053A2:
    if (((uint32_t)(result + 7)) == 4) goto loc_00A0525A;
    a4 = 0;
    if (0 == 0) goto loc_00A056E4;
    result = PnpRecordBlackboxPnpEventInformation(*(uint64_t *)(arg1), (uint32_t)((uint32_t)(result + 7)), 0, a4);
loc_00A053C4:
    if ((*(uint32_t *)(v_rip + 0x587219)) != 0) goto loc_00A05263;
    result = ExFreePoolWithTag(*(uint64_t *)(0 + 0x10), (uint32_t)((uint32_t)((uint32_t)(0x4D706E50ULL))), 0, a4);
    *(uint64_t *)(0 + 0x10) = 0;
    result = ExFreePoolWithTag(0, (uint32_t)((uint32_t)((uint32_t)(0x4D706E50ULL))), 0, a4);
    goto loc_00A05263;
loc_00A053F4:
    if (v_stack_m70 != 0) goto loc_00A0564E;
loc_00A05401:
    local_rbx = 0;
    goto loc_00A052E3;
loc_00A0540F:
    result = PiDetermineDeleteType(*(uint64_t *)(arg1), (uint32_t)((uint32_t)((uint32_t)(0x4D706E50ULL))), v_rip - 10400234, a4);
    if (((uint32_t)(result)) != 4) goto loc_00A05574;
loc_00A05422:
    result = PiCheckRemovalPreconditions((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), *(uint64_t *)(arg1), v_rip - 10400234, a4);
    if (sign_flag) goto loc_00A0522E;
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_00A05589;
loc_00A05447:
    result = PiEventAllocateVetoBuffer((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), *(uint64_t *)(arg1), v_rip - 10400234, a4);
    if (result == 0) goto loc_00A055A8;
    result = PnpBuildRemovalRelationList(*(uint64_t *)(*(uint64_t *)(arg1) + 0xA0), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), result, v_stack_m88);
    if (sign_flag) goto loc_00A0555B;
    v_stack_p30 = v_stack_p10;
    v_stack_p28 = v_stack_p8;
    v_stack_p20 = v_stack_m98;
    result = PiEventBuildPdoList(v_stack_m88, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), *(uint64_t *)(arg1), v_stack_p18);
    if (!sign_flag) goto loc_00A05512;
    local_r13 = 0;
loc_00A054AC:
    if (sign_flag) goto loc_00A055AF;
    local_rbx = 0;
    if (v_stack_p8 != 0) goto loc_00A055D5;
    if ((((uint32_t)((uint32_t)((uint32_t)(result)))) & (0xFFFFFFFBULL)) != 0) goto loc_00A055F1;
    local_r13 = 0;
    if (0 >= (*(uint32_t *)(*(uint64_t *)(v_stack_m88)))) goto loc_00A0529C;
    if (*(uint64_t *)(v_stack_m88) == 0) goto loc_00A0529C;
    local_rbx = (uint32_t)((0) + 1);
loc_00A05512:
    result = PnpResizeTargetDeviceBlock(0, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), *(uint64_t *)(arg1), v_stack_p18);
    local_r13 = 0;
    if (sign_flag) goto loc_00A054AC;
    result = PiEventAreDeviceRelationsExcluded((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), *(uint64_t *)(arg1), v_stack_p18);
    result = PnpCompileDeviceInstancePaths((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_m88, (uint8_t)(result), v_stack_p20);
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 3) goto loc_00A054AC;
    result = PnpBuildUnsafeRemovalDeviceList((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_m88, v_stack_m70, v_stack_p20);
    goto loc_00A054AC;
loc_00A0555B:
loc_00A05562:
    result = PnpFinalizeVetoedRemove(*(uint64_t *)(local_r13), (uint32_t)(*(uint32_t *)(result)), result + 8, v_stack_p20);
    goto loc_00A0522E;
loc_00A05574:
    a3 = 0;
    result = PnpRecordBlackboxPnpEventInformation(*(uint64_t *)(local_r13), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), a3, 1);
    goto loc_00A05422;
loc_00A05589:
    result = PipAreDriversLoaded((uint32_t)((uint32_t)((uint32_t)(0xC0000056ULL))), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), a3, 1);
    if ((uint32_t)(result) != 0) goto loc_00A05447;
    result = PiProcessQueryRemoveNoFdo(*(uint64_t *)(local_r13), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), a3, 1);
    goto loc_00A0522E;
loc_00A055A8:
    a3 = 0;
    a2 = 0;
    goto loc_00A05562;
loc_00A055AF:
    result = IopFreeRelationList(v_stack_m88, a2, a3, 1);
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0x80000028ULL) goto loc_00A05231;
    a3 = 0;
    a2 = 0;
    result = PnpFinalizeVetoedRemove(*(uint64_t *)(local_r13), a2, a3, 1);
    goto loc_00A05231;
loc_00A055D5:
    result = PpProfileBeginHardwareProfileTransition(v_stack_p10, a2, a3, 1);
loc_00A055F1:
    if ((((uint32_t)((uint32_t)((uint32_t)(result)) - 3)) & (0xFFFFFFFDULL)) != 0) goto loc_00A052DC;
    result = PiLogSurpriseRemoveEvent(*(uint64_t *)(local_r13), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_m88, 1);
    a4 = 0;
    v_stack_p38 = (int32_t)((uint32_t)(local_r13 - 1));
    v_stack_p30 = (int32_t)((uint32_t)(local_r13 - 1));
    v_stack_p28 = (uint32_t)((int32_t)((uint32_t)(local_r13 - 1)));
    v_stack_p20 = (uint32_t)((int32_t)((uint32_t)(local_r13 - 1)));
    result = PnpDeleteLockedDeviceNodes(v_stack_m78, v_stack_m88, a4 + 3, a4);
    goto loc_00A052D3;
loc_00A05636:
    local_r13 = 0;
    result = PpProfileCancelHardwareProfileTransition(v_stack_m78, v_stack_m88, a4 + 3, a4);
loc_00A0564E:
    a4 = 0;
    result = PnpNotifyUserModeDeviceRemoval(*(uint64_t *)(local_r13), (int32_t)((uint32_t)(local_r13 - 1)), v_rip - 10349275, a4);
    result = ExFreePoolWithTag((int32_t)((uint32_t)(local_r13 - 1)), (uint32_t)(0x4B706E50ULL), v_rip - 10349275, a4);
    goto loc_00A05401;
loc_00A05681:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(0xC0000056ULL))) + 0x18C)))) & (16)) == 0) goto loc_00A0531A;
    result = PnpFinalizeDeviceRemovalForReset((uint32_t)((uint32_t)((uint32_t)(0xC0000056ULL))), v_stack_m88, v_rip - 10349275, a4);
    goto loc_00A0531A;
loc_00A056A1:
    result = IopQueryDockRemovalInterface(v_stack_m78, v_stack_m68, v_rip - 10349275, a4);
    result = guard_dispatch_icall(*(uint64_t *)(v_stack_m68 + 0x8), 3, v_rip - 10349275, a4);
loc_00A056E4:
    a3 = 0;
    result = PnpRecordBlackboxPnpEventInformation(*(uint64_t *)(v_stack_m68 + 0x8), 3, a3, a4);
    goto loc_00A05263;
loc_00A056F1:
    a2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m68 + 0x8), a2, a3, a4);
    goto loc_00A05270;
loc_00A056FD:
    a2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m68 + 0x8), a2, a3, a4);
    goto loc_00A0527D;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A05170&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
