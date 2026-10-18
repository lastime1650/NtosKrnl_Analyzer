# KiTryUnwaitThread

- RVA: `0x003506D0`–`0x00350A1E` (길이 `846` bytes)
- VA: `0x00000001403506D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00078D98`
- 디코드: `200`개 명령, `846/846` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **37**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x003508BE` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003508CD` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003508EE` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003508FD` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)

### Direct callers
- [KiResumeThread](../20/KiResumeThread_function_00203644.md) at `0x002036EA`
- [sub_00219EB5](../21/Unknown_function_00219EB5.md) at `0x00219FA0`
- [sub_0021A01D](../21/Unknown_function_0021A01D.md) at `0x0021A06A`
- [KiRetireDpcList](../21/KiRetireDpcList_function_0021A0B0.md) at `0x0021A5CC`
- [KiRetireDpcList](../21/KiRetireDpcList_function_0021A0B0.md) at `0x0021AF70`
- [KiTimerWaitTest](../23/KiTimerWaitTest_function_002337D0.md) at `0x00233A1E`
- [KiTimerWaitTest](../23/KiTimerWaitTest_function_002337D0.md) at `0x00233A89`
- [KiTimerWaitTest](../23/KiTimerWaitTest_function_002337D0.md) at `0x00233AF5`
- [ExReleaseFastMutexUnsafe](../25/ExReleaseFastMutexUnsafe_function_002503A0.md) at `0x00250522`
- [ExReleaseFastMutexUnsafe](../25/ExReleaseFastMutexUnsafe_function_002503A0.md) at `0x002505F8`
- [IopReleaseFileObjectLock](../25/IopReleaseFileObjectLock_function_00250A90.md) at `0x00250C0C`
- [IopReleaseFileObjectLock](../25/IopReleaseFileObjectLock_function_00250A90.md) at `0x00250E5B`
- [FsRtlReleaseHeaderMutex](../25/FsRtlReleaseHeaderMutex_function_002516C0.md) at `0x00251887`
- [FsRtlReleaseHeaderMutex](../25/FsRtlReleaseHeaderMutex_function_002516C0.md) at `0x00251965`
- [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) at `0x00251B60`
- [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) at `0x00251C36`
- [sub_0025E5F6](../25/Unknown_function_0025E5F6.md) at `0x0025E699`
- [sub_0025E5F6](../25/Unknown_function_0025E5F6.md) at `0x0025E815`
- [sub_0025EB5D](../25/Unknown_function_0025EB5D.md) at `0x0025EBDF`
- [sub_0025EB5D](../25/Unknown_function_0025EB5D.md) at `0x0025EC54`
- [sub_00260366](../26/Unknown_function_00260366.md) at `0x002608BF`
- [sub_00260366](../26/Unknown_function_00260366.md) at `0x00260A38`
- [sub_00260D5A](../26/Unknown_function_00260D5A.md) at `0x00260DE8`
- [sub_00260D5A](../26/Unknown_function_00260D5A.md) at `0x00260E5D`
- [ExReleaseFastResource](../26/ExReleaseFastResource_function_002613D0.md) at `0x0026193A`
- [ExReleaseFastResource](../26/ExReleaseFastResource_function_002613D0.md) at `0x00261B77`
- [sub_00261DFE](../26/Unknown_function_00261DFE.md) at `0x002620A7`
- [sub_00261DFE](../26/Unknown_function_00261DFE.md) at `0x002621D6`
- [sub_00262F80](../26/Unknown_function_00262F80.md) at `0x00263059`
- [sub_002630C6](../26/Unknown_function_002630C6.md) at `0x0026318F`
- [sub_0027475D](../27/Unknown_function_0027475D.md) at `0x00274D05`
- [sub_0027475D](../27/Unknown_function_0027475D.md) at `0x00274E8C`
- [sub_0027475D](../27/Unknown_function_0027475D.md) at `0x00275270`
- [sub_0027475D](../27/Unknown_function_0027475D.md) at `0x002752E5`
- [sub_00286600](../28/Unknown_function_00286600.md) at `0x002866BD`
- [sub_00286720](../28/Unknown_function_00286720.md) at `0x0028679F`
- [KeSignalGate](../2C/KeSignalGate_function_002C748C.md) at `0x002C752F`
- [KeSignalGate](../2C/KeSignalGate_function_002C748C.md) at `0x002C75B6`
- [sub_0033F9A3](../33/Unknown_function_0033F9A3.md) at `0x0033F9B6`
- [sub_0033F9A3](../33/Unknown_function_0033F9A3.md) at `0x0033F9E0`
- [KeReleaseSemaphoreEx](../34/KeReleaseSemaphoreEx_function_003468C0.md) at `0x00346BC7`
- [KeWakeWaitChain](../34/KeWakeWaitChain_function_0034F8C0.md) at `0x0034F9E6`
- [KeWakeWaitChain](../34/KeWakeWaitChain_function_0034F8C0.md) at `0x0034FAFE`
- [KeTimeOutQueueWaiters](../34/KeTimeOutQueueWaiters_function_0034FB58.md) at `0x0034FC66`
- [KeSetEventBoostPriorityEx](KeSetEventBoostPriorityEx_function_00350148.md) at `0x003501F1`
- [KeSetEventBoostPriorityEx](KeSetEventBoostPriorityEx_function_00350148.md) at `0x0035032E`
- [MiReturnWsToExpansionList](MiReturnWsToExpansionList_function_003504E0.md) at `0x003505C3`
- [MiReturnWsToExpansionList](MiReturnWsToExpansionList_function_003504E0.md) at `0x0035069F`
- [KeRundownQueueCommon](KeRundownQueueCommon_function_003515F4.md) at `0x00351655`
- [KeDeleteMutant](KeDeleteMutant_function_00351788.md) at `0x0035192F`
- [KeDeleteMutant](KeDeleteMutant_function_00351788.md) at `0x003519A9`
- [KePulseEvent](KePulseEvent_function_00351EF0.md) at `0x00351F88`
- [KePulseEvent](KePulseEvent_function_00351EF0.md) at `0x00352060`
- [KePulseEvent](KePulseEvent_function_00351EF0.md) at `0x003520D8`
- [KeSetProcess](KeSetProcess_function_003520E8.md) at `0x00352167`
- [KeTerminateThread](KeTerminateThread_function_00355138.md) at `0x003552D3`
- [AlpcpSignal](../39/AlpcpSignal_function_003955E0.md) at `0x00396142`
- [AlpcpSignal](../39/AlpcpSignal_function_003955E0.md) at `0x00396163`
- [KeReleaseMutantEx](../39/KeReleaseMutantEx_function_00396850.md) at `0x00396CC2`
- [sub_0039737C](../39/Unknown_function_0039737C.md) at `0x0039738F`
- [KiExpireTimer2](../3A/KiExpireTimer2_function_003A24E0.md) at `0x003A25F8`
- [KiExpireTimer2](../3A/KiExpireTimer2_function_003A24E0.md) at `0x003A295A`
- [KiExpireTimer2](../3A/KiExpireTimer2_function_003A24E0.md) at `0x003A2B78`
- [KiExpireTimer2](../3A/KiExpireTimer2_function_003A24E0.md) at `0x003A2C3C`
- [sub_006F59B4](../6F/Unknown_function_006F59B4.md) at `0x006F5AF4`
- [sub_006F59B4](../6F/Unknown_function_006F59B4.md) at `0x006F5C07`

### Static image references
- `0x0035070E` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x003508B0` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003506D0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
003506D5  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
003506DA  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
003506DF  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
003506E4  41 54                           push r12
003506E6  41 56                           push r14
003506E8  41 57                           push r15
003506EA  48 83 EC 40                     sub rsp, 0x40
003506EE  48 8B 5A 18                     mov rbx, qword ptr [rdx + 0x18]
003506F2  40 32 F6                        xor sil, sil
003506F5  33 FF                           xor edi, edi
003506F7  4D 8B F9                        mov r15, r9
003506FA  4D 8B E0                        mov r12, r8
003506FD  48 8B EA                        mov rbp, rdx
00350700  4C 8B F1                        mov r14, rcx
00350703  F0 48 0F BA 6B 40 00            lock bts qword ptr [rbx + 0x40], 0
0035070A  73 1B                           jae 0x140350727
0035070C  FF C7                           inc edi
0035070E  85 3D 98 4B C7 00               test dword ptr [rip + 0xc74b98], edi
00350714  0F 84 96 01 00 00               je 0x1403508b0
0035071A  F3 90                           pause
0035071C  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
00350720  48 85 C0                        test rax, rax
00350723  74 DE                           je 0x140350703
00350725  EB E5                           jmp 0x14035070c
00350727  0F B6 83 84 01 00 00            movzx eax, byte ptr [rbx + 0x184]
0035072E  3C 05                           cmp al, 5
00350730  0F 85 20 01 00 00               jne 0x140350856
00350736  0F B6 4B 70                     movzx ecx, byte ptr [rbx + 0x70]
0035073A  8B C1                           mov eax, ecx
0035073C  83 E0 07                        and eax, 7
0035073F  83 F8 01                        cmp eax, 1
00350742  0F 85 6D 02 00 00               jne 0x1403509b5
00350748  48 8B 93 E8 00 00 00            mov rdx, qword ptr [rbx + 0xe8]
0035074F  48 85 D2                        test rdx, rdx
00350752  74 11                           je 0x140350765
00350754  0F B6 02                        movzx eax, byte ptr [rdx]
00350757  24 7F                           and al, 0x7f
00350759  3C 15                           cmp al, 0x15
0035075B  0F 84 33 01 00 00               je 0x140350894
00350761  F0 FF 42 28                     lock inc dword ptr [rdx + 0x28]
00350765  48 8B BB C8 02 00 00            mov rdi, qword ptr [rbx + 0x2c8]
0035076C  48 85 FF                        test rdi, rdi
0035076F  74 73                           je 0x1403507e4
00350771  33 F6                           xor esi, esi
00350773  F0 48 0F BA AF D0 83 00 00 00   lock bts qword ptr [rdi + 0x83d0], 0
0035077D  73 1E                           jae 0x14035079d
0035077F  FF C6                           inc esi
00350781  85 35 25 4B C7 00               test dword ptr [rip + 0xc74b25], esi
00350787  0F 84 53 01 00 00               je 0x1403508e0
0035078D  F3 90                           pause
0035078F  48 8B 87 D0 83 00 00            mov rax, qword ptr [rdi + 0x83d0]
00350796  48 85 C0                        test rax, rax
00350799  74 D8                           je 0x140350773
0035079B  EB E2                           jmp 0x14035077f
0035079D  48 8B 83 C8 02 00 00            mov rax, qword ptr [rbx + 0x2c8]
003507A4  48 85 C0                        test rax, rax
003507A7  74 32                           je 0x1403507db
003507A9  48 8D 83 D8 00 00 00            lea rax, [rbx + 0xd8]
003507B0  48 8B 10                        mov rdx, qword ptr [rax]
003507B3  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
003507B7  48 39 42 08                     cmp qword ptr [rdx + 8], rax
003507BB  75 05                           jne 0x1403507c2
003507BD  48 39 01                        cmp qword ptr [rcx], rax
003507C0  74 07                           je 0x1403507c9
003507C2  B9 03 00 00 00                  mov ecx, 3
003507C7  CD 29                           int 0x29
003507C9  48 89 11                        mov qword ptr [rcx], rdx
003507CC  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
003507D0  48 C7 83 C8 02 00 00 00 00 00 00  mov qword ptr [rbx + 0x2c8], 0
003507DB  F0 48 83 A7 D0 83 00 00 00      lock and qword ptr [rdi + 0x83d0], 0
003507E4  0F B6 83 84 01 00 00            movzx eax, byte ptr [rbx + 0x184]
003507EB  3C 01                           cmp al, 1
003507ED  0F 84 E4 00 00 00               je 0x1403508d7
003507F3  3C 05                           cmp al, 5
003507F5  75 22                           jne 0x140350819
003507F7  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
00350801  8B 08                           mov ecx, dword ptr [rax]
00350803  2B 8B B4 01 00 00               sub ecx, dword ptr [rbx + 0x1b4]
00350809  80 BB 87 01 00 00 00            cmp byte ptr [rbx + 0x187], 0
00350810  74 79                           je 0x14035088b
00350812  48 01 8B E8 03 00 00            add qword ptr [rbx + 0x3e8], rcx
00350819  C6 83 84 01 00 00 07            mov byte ptr [rbx + 0x184], 7
00350820  48 8D 8B D8 00 00 00            lea rcx, [rbx + 0xd8]
00350827  49 8B 86 08 2D 00 00            mov rax, qword ptr [r14 + 0x2d08]
0035082E  48 89 01                        mov qword ptr [rcx], rax
00350831  49 89 8E 08 2D 00 00            mov qword ptr [r14 + 0x2d08], rcx
00350838  4C 89 A3 C8 00 00 00            mov qword ptr [rbx + 0xc8], r12
0035083F  48 C7 83 D0 03 00 00 00 00 00 00  mov qword ptr [rbx + 0x3d0], 0
0035084A  40 B6 01                        mov sil, 1
0035084D  4D 85 FF                        test r15, r15
00350850  0F 85 B1 00 00 00               jne 0x140350907
00350856  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
0035085B  40 0F B6 C6                     movzx eax, sil
0035085F  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00350864  48 C7 43 40 00 00 00 00         mov qword ptr [rbx + 0x40], 0
0035086C  0F B6 4D 11                     movzx ecx, byte ptr [rbp + 0x11]
00350870  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00350875  FE C1                           inc cl
00350877  88 4D 11                        mov byte ptr [rbp + 0x11], cl
0035087A  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
0035087F  48 83 C4 40                     add rsp, 0x40
00350883  41 5F                           pop r15
00350885  41 5E                           pop r14
00350887  41 5C                           pop r12
00350889  C3                              ret
0035088A  CC                              int3
0035088B  48 01 8B E0 03 00 00            add qword ptr [rbx + 0x3e0], rcx
00350892  EB 85                           jmp 0x140350819
00350894  8B 83 1C 02 00 00               mov eax, dword ptr [rbx + 0x21c]
0035089A  0F B6 C0                        movzx eax, al
0035089D  89 83 1C 02 00 00               mov dword ptr [rbx + 0x21c], eax
003508A3  F0 FF 84 82 18 02 00 00         lock inc dword ptr [rdx + rax*4 + 0x218]
003508AB  E9 B5 FE FF FF                  jmp 0x140350765
003508B0  8B 05 02 62 C7 00               mov eax, dword ptr [rip + 0xc76202]
003508B6  A8 40                           test al, 0x40
003508B8  0F 84 5C FE FF FF               je 0x14035071a
003508BE  E8 CD EB FB FF                  call 0x14030f490
003508C3  84 C0                           test al, al
003508C5  0F 84 4F FE FF FF               je 0x14035071a
003508CB  8B CF                           mov ecx, edi
003508CD  E8 8E EB FB FF                  call 0x14030f460
003508D2  E9 45 FE FF FF                  jmp 0x14035071c
003508D7  83 4B 74 02                     or dword ptr [rbx + 0x74], 2
003508DB  E9 39 FF FF FF                  jmp 0x140350819
003508E0  8B 05 D2 61 C7 00               mov eax, dword ptr [rip + 0xc761d2]
003508E6  A8 40                           test al, 0x40
003508E8  0F 84 9F FE FF FF               je 0x14035078d
003508EE  E8 9D EB FB FF                  call 0x14030f490
003508F3  84 C0                           test al, al
003508F5  0F 84 92 FE FF FF               je 0x14035078d
003508FB  8B CE                           mov ecx, esi
003508FD  E8 5E EB FB FF                  call 0x14030f460
00350902  E9 88 FE FF FF                  jmp 0x14035078f
00350907  49 89 1F                        mov qword ptr [r15], rbx
0035090A  48 8B 4D 20                     mov rcx, qword ptr [rbp + 0x20]
0035090E  0F B6 01                        movzx eax, byte ptr [rcx]
00350911  24 7F                           and al, 0x7f
00350913  3C 02                           cmp al, 2
00350915  0F 85 3B FF FF FF               jne 0x140350856
0035091B  80 79 31 00                     cmp byte ptr [rcx + 0x31], 0
0035091F  74 07                           je 0x140350928
00350921  66 FF 8B E4 01 00 00            dec word ptr [rbx + 0x1e4]
00350928  49 39 5E 08                     cmp qword ptr [r14 + 8], rbx
0035092C  0F 85 C7 00 00 00               jne 0x1403509f9
00350932  41 0F B6 96 BA 38 00 00         movzx edx, byte ptr [r14 + 0x38ba]
0035093A  33 C0                           xor eax, eax
0035093C  0F 57 C0                        xorps xmm0, xmm0
0035093F  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00350944  8B 01                           mov eax, dword ptr [rcx]
00350946  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0035094B  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0035094F  88 54 24 22                     mov byte ptr [rsp + 0x22], dl
00350953  8B 44 24 20                     mov eax, dword ptr [rsp + 0x20]
00350957  89 01                           mov dword ptr [rcx], eax
00350959  0F B6 41 30                     movzx eax, byte ptr [rcx + 0x30]
0035095D  48 89 59 28                     mov qword ptr [rcx + 0x28], rbx
00350961  A8 01                           test al, 1
00350963  74 10                           je 0x140350975
00350965  24 FE                           and al, 0xfe
00350967  88 41 30                        mov byte ptr [rcx + 0x30], al
0035096A  48 81 8B C8 00 00 00 80 00 00 00  or qword ptr [rbx + 0xc8], 0x80
00350975  F6 41 30 02                     test byte ptr [rcx + 0x30], 2
00350979  0F 85 93 00 00 00               jne 0x140350a12
0035097F  48 C7 83 D0 03 00 00 00 00 00 00  mov qword ptr [rbx + 0x3d0], 0
0035098A  48 8D 83 08 03 00 00            lea rax, [rbx + 0x308]
00350991  48 8D 51 18                     lea rdx, [rcx + 0x18]
00350995  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00350999  48 39 01                        cmp qword ptr [rcx], rax
0035099C  0F 85 20 FE FF FF               jne 0x1403507c2
003509A2  48 89 02                        mov qword ptr [rdx], rax
003509A5  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
003509A9  48 89 11                        mov qword ptr [rcx], rdx
003509AC  48 89 50 08                     mov qword ptr [rax + 8], rdx
003509B0  E9 A1 FE FF FF                  jmp 0x140350856
003509B5  83 F8 04                        cmp eax, 4
003509B8  0F 84 8A FD FF FF               je 0x140350748
003509BE  85 C0                           test eax, eax
003509C0  75 24                           jne 0x1403509e6
003509C2  80 E1 FA                        and cl, 0xfa
003509C5  80 C9 02                        or cl, 2
003509C8  88 4B 70                        mov byte ptr [rbx + 0x70], cl
003509CB  4C 89 A3 C8 00 00 00            mov qword ptr [rbx + 0xc8], r12
003509D2  48 C7 83 D0 03 00 00 00 00 00 00  mov qword ptr [rbx + 0x3d0], 0
003509DD  40 88 75 11                     mov byte ptr [rbp + 0x11], sil
003509E1  E9 64 FE FF FF                  jmp 0x14035084a
003509E6  83 F8 05                        cmp eax, 5
003509E9  75 15                           jne 0x140350a00
003509EB  80 E1 FE                        and cl, 0xfe
003509EE  80 C9 06                        or cl, 6
003509F1  88 4B 70                        mov byte ptr [rbx + 0x70], cl
003509F4  E9 5D FE FF FF                  jmp 0x140350856
003509F9  32 D2                           xor dl, dl
003509FB  E9 3A FF FF FF                  jmp 0x14035093a
00350A00  83 F8 03                        cmp eax, 3
00350A03  0F 85 4D FE FF FF               jne 0x140350856
00350A09  C6 45 11 02                     mov byte ptr [rbp + 0x11], 2
00350A0D  E9 44 FE FF FF                  jmp 0x140350856
00350A12  48 89 8B D0 03 00 00            mov qword ptr [rbx + 0x3d0], rcx
00350A19  E9 6C FF FF FF                  jmp 0x14035098a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiTryUnwaitThread(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p22;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_stack_p20 = v_rdi;
    v_rsp = (v_rsp) - (64);
    v_rsi = 0;
    v_rdi = 0;
loc_00350703:
    if (condition_is_above_or_equal) goto loc_00350727;
loc_0035070C:
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (((*(unsigned int *)(v_rip + 13061016)) & ((unsigned int)(v_rdi))) == 0) goto loc_003508B0;
loc_0035071A:
loc_0035071C:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24) + 64) == 0) goto loc_00350703;
    goto loc_0035070C;
loc_00350727:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 24) + 388))) != 5) goto loc_00350856;
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 24) + 112)))) & (7));
    if (((unsigned int)(result)) != 1) goto loc_003509B5;
loc_00350748:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24) + 232) == 0) goto loc_00350765;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24) + 232))) & (127));
    if (((unsigned __int8)(result)) == 21) goto loc_00350894;
loc_00350765:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24) + 712) == 0) goto loc_003507E4;
    v_rsi = 0;
loc_00350773:
    if (condition_is_above_or_equal) goto loc_0035079D;
loc_0035077F:
    v_rsi = (unsigned int)((v_rsi) + 1);
    if (((*(unsigned int *)(v_rip + 13060901)) & ((unsigned int)(v_rsi))) == 0) goto loc_003508E0;
loc_0035078D:
loc_0035078F:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24) + 712) + 33744) == 0) goto loc_00350773;
    goto loc_0035077F;
loc_0035079D:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24) + 712) == 0) goto loc_003507DB;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24) + 216) + 8)) != (*(unsigned __int64 *)(a2 + 24) + 216)) goto loc_003507C2;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24) + 216 + 8))) != (*(unsigned __int64 *)(a2 + 24) + 216)) {
        a1 = 3;
    }
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24) + 216);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24) + 216) + 8) = a1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24) + 712) = 0;
loc_003507DB:
loc_003507E4:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 24) + 388))) == 1) goto loc_003508D7;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 24) + 388))) != 5) goto loc_00350819;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 24) + 388)))) - (*(unsigned int *)(*(unsigned __int64 *)(a2 + 24) + 436)));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 24) + 391)) == 0) goto loc_0035088B;
loc_00350819:
    *(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 24) + 388) = 7;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24) + 216) = *(unsigned __int64 *)(a1 + 11528);
    *(unsigned __int64 *)(a1 + 11528) = *(unsigned __int64 *)(a2 + 24) + 216;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24) + 200) = a3;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24) + 976) = 0;
loc_0035084A:
    if (a4 != 0) goto loc_00350907;
loc_00350856:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24) + 64) = 0;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(a2 + 17)) + 1);
    *(unsigned __int8 *)(a2 + 17) = (unsigned __int8)(a1);
    v_rsp = (v_rsp) + (64);
    return 1;
loc_0035088B:
    goto loc_00350819;
loc_00350894:
    *(unsigned int *)(v_stack_p8 + 540) = (unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 540))));
    goto loc_00350765;
loc_003508B0:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13066754)))) & (64)) == 0) goto loc_0035071A;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24) + 216), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0035071A;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_stack_p20)), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24) + 216), a3, a4);
    goto loc_0035071C;
loc_003508D7:
    goto loc_00350819;
loc_003508E0:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13066706)))) & (64)) == 0) goto loc_0035078D;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_stack_p20)), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24) + 216), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0035078D;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_stack_p18)), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24) + 216), a3, a4);
    goto loc_0035078F;
loc_00350907:
    *(unsigned __int64 *)(a4) = v_stack_p8;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p10 + 32))) & (127));
    if (((unsigned __int8)(result)) != 2) goto loc_00350856;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p10 + 32) + 49)) != 0) {
    }
    if ((*(unsigned __int64 *)(a1 + 8)) != v_stack_p8) goto loc_003509F9;
loc_0035093A:
    result = 0;
    v_stack_p30 = 0;
    v_stack_p20 = v_xmm0;
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 32))));
    v_stack_p22 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 14522));
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 32)) = (unsigned int)((unsigned int)(v_stack_p20));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 32) + 40) = v_stack_p8;
    result = *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p10 + 32) + 48);
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p10 + 32) + 48))) & (1)) != 0) {
        result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p10 + 32) + 48)) & (254));
        *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p10 + 32) + 48) = (unsigned __int8)(result);
    }
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p10 + 32) + 48)) & (2)) != 0) goto loc_00350A12;
    *(unsigned __int64 *)(v_stack_p8 + 976) = 0;
loc_0035098A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 776 + 8))) != (v_stack_p8 + 776)) goto loc_003507C2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 32) + 24) = v_stack_p8 + 776;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 32) + 24 + 8) = *(unsigned __int64 *)(v_stack_p8 + 776 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 776 + 8)) = *(unsigned __int64 *)(v_stack_p10 + 32) + 24;
    *(unsigned __int64 *)(v_stack_p8 + 776 + 8) = *(unsigned __int64 *)(v_stack_p10 + 32) + 24;
    goto loc_00350856;
loc_003509B5:
    if (((unsigned int)(v_stack_p8 + 776)) == 4) goto loc_00350748;
    if ((unsigned int)(v_stack_p8 + 776) != 0) goto loc_003509E6;
    a1 = (unsigned __int8)((*(unsigned __int64 *)(v_stack_p8 + 776 + 8)) & (250));
    a1 = (unsigned __int8)((a1) | (2));
    *(unsigned __int8 *)(v_stack_p8 + 112) = (unsigned __int8)(a1);
    *(unsigned __int64 *)(v_stack_p8 + 200) = a3;
    *(unsigned __int64 *)(v_stack_p8 + 976) = 0;
    *(unsigned __int8 *)(v_stack_p10 + 17) = (unsigned __int8)(v_stack_p18);
    goto loc_0035084A;
loc_003509E6:
    if (((unsigned int)(v_stack_p8 + 776)) != 5) goto loc_00350A00;
    a1 = (unsigned __int8)((a1) & (254));
    a1 = (unsigned __int8)((a1) | (6));
    *(unsigned __int8 *)(v_stack_p8 + 112) = (unsigned __int8)(a1);
    goto loc_00350856;
loc_003509F9:
    a2 = 0;
    goto loc_0035093A;
loc_00350A00:
    if (((unsigned int)(v_stack_p8 + 776)) != 3) goto loc_00350856;
    *(unsigned __int8 *)(v_stack_p10 + 17) = 2;
    goto loc_00350856;
loc_00350A12:
    *(unsigned __int64 *)(v_stack_p8 + 976) = a1;
    goto loc_0035098A;
}
```

## 5. (Beta) C Style

```c
int64_t KiTryUnwaitThread(void *Arg1, void *Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p22;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    v_stack_p20 = local_rdi;
    local_rsp = (local_rsp) - (64);
    local_rsi = 0;
    local_rdi = 0;
loc_00350703:
    if (condition_is_above_or_equal) goto loc_00350727;
loc_0035070C:
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (((*(uint32_t *)(v_rip + 0xC74B98)) & ((uint32_t)(local_rdi))) == 0) goto loc_003508B0;
loc_0035071A:
loc_0035071C:
    if (*(uint64_t *)(*(uint64_t *)(arg2 + 0x18) + 0x40) == 0) goto loc_00350703;
    goto loc_0035070C;
loc_00350727:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x18) + 0x184))) != 5) goto loc_00350856;
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x18) + 0x70)))) & (7));
    if (((uint32_t)(result)) != 1) goto loc_003509B5;
loc_00350748:
    if (*(uint64_t *)(*(uint64_t *)(arg2 + 0x18) + 0xE8) == 0) goto loc_00350765;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x18) + 0xE8))) & (127));
    if (((uint8_t)(result)) == 21) goto loc_00350894;
loc_00350765:
    if (*(uint64_t *)(*(uint64_t *)(arg2 + 0x18) + 0x2C8) == 0) goto loc_003507E4;
    local_rsi = 0;
loc_00350773:
    if (condition_is_above_or_equal) goto loc_0035079D;
loc_0035077F:
    local_rsi = (uint32_t)((local_rsi) + 1);
    if (((*(uint32_t *)(v_rip + 0xC74B25)) & ((uint32_t)(local_rsi))) == 0) goto loc_003508E0;
loc_0035078D:
loc_0035078F:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x18) + 0x2C8) + 0x83D0) == 0) goto loc_00350773;
    goto loc_0035077F;
loc_0035079D:
    if (*(uint64_t *)(*(uint64_t *)(arg2 + 0x18) + 0x2C8) == 0) goto loc_003507DB;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x18) + 0xD8) + 0x8)) != (*(uint64_t *)(arg2 + 0x18) + 216)) goto loc_003507C2;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x18) + 0xD8 + 0x8))) != (*(uint64_t *)(arg2 + 0x18) + 216)) {
        Arg1 = 3;
    }
    *(uint64_t *)(arg1) = *(uint64_t *)(*(uint64_t *)(arg2 + 0x18) + 0xD8);
    *(void **)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x18) + 0xD8) + 0x8) = Arg1;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x18) + 0x2C8) = 0;
loc_003507DB:
loc_003507E4:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x18) + 0x184))) == 1) goto loc_003508D7;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x18) + 0x184))) != 5) goto loc_00350819;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x18) + 0x184)))) - (*(uint32_t *)(*(uint64_t *)(arg2 + 0x18) + 0x1B4)));
    if ((*(uint8_t *)(*(uint64_t *)(arg2 + 0x18) + 0x187)) == 0) goto loc_0035088B;
loc_00350819:
    *(uint8_t *)(*(uint64_t *)(arg2 + 0x18) + 0x184) = 7;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x18) + 0xD8) = *(uint64_t *)(arg1 + 0x2D08);
    *(uint64_t *)(arg1 + 0x2D08) = *(uint64_t *)(arg2 + 0x18) + 216;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x18) + 0xC8) = Arg3;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x18) + 0x3D0) = 0;
loc_0035084A:
    if (Arg4 != 0) goto loc_00350907;
loc_00350856:
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x18) + 0x40) = 0;
    Arg1 = (uint8_t)((*(uint8_t *)(arg2 + 0x11)) + 1);
    *(uint8_t *)(arg2 + 0x11) = (uint8_t)(Arg1);
    local_rsp = (local_rsp) + (64);
    return 1;
loc_0035088B:
    goto loc_00350819;
loc_00350894:
    *(uint32_t *)(v_stack_p8 + 0x21C) = (uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x21C))));
    goto loc_00350765;
loc_003508B0:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC76202)))) & (64)) == 0) goto loc_0035071A;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, *(uint64_t *)(*(uint64_t *)(arg2 + 0x18) + 0xD8), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0035071A;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(v_stack_p20)), *(uint64_t *)(*(uint64_t *)(arg2 + 0x18) + 0xD8), Arg3, Arg4);
    goto loc_0035071C;
loc_003508D7:
    goto loc_00350819;
loc_003508E0:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC761D2)))) & (64)) == 0) goto loc_0035078D;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(v_stack_p20)), *(uint64_t *)(*(uint64_t *)(arg2 + 0x18) + 0xD8), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0035078D;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(v_stack_p18)), *(uint64_t *)(*(uint64_t *)(arg2 + 0x18) + 0xD8), Arg3, Arg4);
    goto loc_0035078F;
loc_00350907:
    *(uint64_t *)(Arg4) = v_stack_p8;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(v_stack_p10 + 0x20))) & (127));
    if (((uint8_t)(result)) != 2) goto loc_00350856;
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_p10 + 0x20) + 0x31)) != 0) {
    }
    if ((*(uint64_t *)(arg1 + 0x8)) != v_stack_p8) goto loc_003509F9;
loc_0035093A:
    result = 0;
    v_stack_p30 = 0;
    v_stack_p20 = v_xmm0;
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x20))));
    v_stack_p22 = (uint8_t)(*(uint8_t *)(arg1 + 0x38BA));
    *(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x20)) = (uint32_t)((uint32_t)(v_stack_p20));
    *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x20) + 0x28) = v_stack_p8;
    result = *(uint8_t *)(*(uint64_t *)(v_stack_p10 + 0x20) + 0x30);
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_p10 + 0x20) + 0x30))) & (1)) != 0) {
        result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(v_stack_p10 + 0x20) + 0x30)) & (254));
        *(uint8_t *)(*(uint64_t *)(v_stack_p10 + 0x20) + 0x30) = (uint8_t)(result);
    }
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_p10 + 0x20) + 0x30)) & (2)) != 0) goto loc_00350A12;
    *(uint64_t *)(v_stack_p8 + 0x3D0) = 0;
loc_0035098A:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x308 + 0x8))) != (v_stack_p8 + 776)) goto loc_003507C2;
    *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x20) + 0x18) = v_stack_p8 + 776;
    *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x20) + 0x18 + 0x8) = *(uint64_t *)(v_stack_p8 + 0x308 + 0x8);
    *(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x308 + 0x8)) = *(uint64_t *)(v_stack_p10 + 0x20) + 24;
    *(uint64_t *)(v_stack_p8 + 0x308 + 0x8) = *(uint64_t *)(v_stack_p10 + 0x20) + 24;
    goto loc_00350856;
loc_003509B5:
    if (((uint32_t)(v_stack_p8 + 776)) == 4) goto loc_00350748;
    if ((uint32_t)(v_stack_p8 + 776) != 0) goto loc_003509E6;
    Arg1 = (uint8_t)((*(uint64_t *)(v_stack_p8 + 0x308 + 0x8)) & (250));
    Arg1 = (uint8_t)((Arg1) | (2));
    *(uint8_t *)(v_stack_p8 + 0x70) = (uint8_t)(Arg1);
    *(uint64_t *)(v_stack_p8 + 0xC8) = Arg3;
    *(uint64_t *)(v_stack_p8 + 0x3D0) = 0;
    *(uint8_t *)(v_stack_p10 + 0x11) = (uint8_t)(v_stack_p18);
    goto loc_0035084A;
loc_003509E6:
    if (((uint32_t)(v_stack_p8 + 776)) != 5) goto loc_00350A00;
    Arg1 = (uint8_t)((Arg1) & (254));
    Arg1 = (uint8_t)((Arg1) | (6));
    *(uint8_t *)(v_stack_p8 + 0x70) = (uint8_t)(Arg1);
    goto loc_00350856;
loc_003509F9:
    Arg2 = 0;
    goto loc_0035093A;
loc_00350A00:
    if (((uint32_t)(v_stack_p8 + 776)) != 3) goto loc_00350856;
    *(uint8_t *)(v_stack_p10 + 0x11) = 2;
    goto loc_00350856;
loc_00350A12:
    *(void **)(v_stack_p8 + 0x3D0) = Arg1;
    goto loc_0035098A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x2D08` | `64` | `R` |
| `Arg1` | `+ 0x2D08` | `64` | `W` |
| `Arg1` | `+ 0x38BA` | `8` | `R` |
| `Arg2` | `+ 0x11` | `8` | `R` |
| `Arg2` | `+ 0x11` | `8` | `W` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003506D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
