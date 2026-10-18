# MiCloneVads

- RVA: `0x0022DC1C`–`0x0022E323` (길이 `1,799` bytes)
- VA: `0x000000014022DC1C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00060078`
- 디코드: `443`개 명령, `1,799/1,799` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **48**; 고유 호출 대상: **29**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0022DC77` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0022DC87` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0022DCEE` → [MiBuildNewCloneDescriptor](../../page/A6/MiBuildNewCloneDescriptor_function_00A6C744.md) (function, `0x00A6C744`)
- `0x0022DD11` → [PsChargeProcessNonPagedPoolQuota](../2A/PsChargeProcessNonPagedPoolQuota_function_002A7B80.md) (function, `0x002A7B80`)
- `0x0022DD2C` → [MiAllocatePool](../35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x0022DD4D` → [MiLockAweVadsExclusive](../4B/MiLockAweVadsExclusive_function_004BDEE4.md) (function, `0x004BDEE4`)
- `0x0022DD55` → [MiLockWorkingSetExclusive](../32/MiLockWorkingSetExclusive_function_003238A0.md) (function, `0x003238A0`)
- `0x0022DD7E` → [MiDeleteCloneZombies](../49/MiDeleteCloneZombies_function_0049A7B8.md) (function, `0x0049A7B8`)
- `0x0022DD95` → [MiUnlockWorkingSetExclusive](../27/MiUnlockWorkingSetExclusive_function_0027EC70.md) (function, `0x0027EC70`)
- `0x0022DD9D` → [MiUnlockAweVadsExclusive](../4B/MiUnlockAweVadsExclusive_function_004BDF1C.md) (function, `0x004BDF1C`)
- `0x0022DDAC` → [MiInitializeForkMaps](../../page/AD/MiInitializeForkMaps_function_00AD4A40.md) (function, `0x00AD4A40`)
- `0x0022DDBC` → [MiLockWorkingSetExclusive](../32/MiLockWorkingSetExclusive_function_003238A0.md) (function, `0x003238A0`)
- `0x0022DDDF` → [MiInsertClone](../4D/MiInsertClone_function_004D4A7C.md) (function, `0x004D4A7C`)
- `0x0022DE6D` → [MiLocateAddress](../31/MiLocateAddress_function_003168D0.md) (function, `0x003168D0`)
- `0x0022DE9F` → [MiIsVadLargePrivate](../32/MiIsVadLargePrivate_function_0032F720.md) (function, `0x0032F720`)
- `0x0022DF1A` → [MiGetNextPageTable](../2C/MiGetNextPageTable_function_002C2EE0.md) (function, `0x002C2EE0`)
- `0x0022DF28` → [MiUnlockWorkingSetExclusive](../27/MiUnlockWorkingSetExclusive_function_0027EC70.md) (function, `0x0027EC70`)
- `0x0022DF44` → [MiUpdateForkMaps](../../page/A7/MiUpdateForkMaps_function_00A7DAF8.md) (function, `0x00A7DAF8`)
- `0x0022DF57` → [MiLockWorkingSetExclusive](../32/MiLockWorkingSetExclusive_function_003238A0.md) (function, `0x003238A0`)
- `0x0022DFAC` → [MiMakeSystemAddressValid](../27/MiMakeSystemAddressValid_function_0027FF70.md) (function, `0x0027FF70`)
- `0x0022DFB6` → [MiBuildForkPte](MiBuildForkPte_function_0022E32C.md) (function, `0x0022E32C`)
- `0x0022E04E` → [RtlAvlRemoveNode](../29/RtlAvlRemoveNode_function_00296650.md) (function, `0x00296650`)
- `0x0022E05E` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x0022E063` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x0022E085` → [MiDeleteCloneZombies](../49/MiDeleteCloneZombies_function_0049A7B8.md) (function, `0x0049A7B8`)
- `0x0022E106` → [MiInsertClone](../4D/MiInsertClone_function_004D4A7C.md) (function, `0x004D4A7C`)
- `0x0022E172` → [MiUnlockWorkingSetExclusive](../27/MiUnlockWorkingSetExclusive_function_0027EC70.md) (function, `0x0027EC70`)
- `0x0022E17B` → [MiFreeForkMaps](../../page/AC/MiFreeForkMaps_function_00AC8534.md) (function, `0x00AC8534`)
- `0x0022E185` → [MiLockAweVadsExclusive](../4B/MiLockAweVadsExclusive_function_004BDEE4.md) (function, `0x004BDEE4`)
- `0x0022E18D` → [MiLockWorkingSetExclusive](../32/MiLockWorkingSetExclusive_function_003238A0.md) (function, `0x003238A0`)
- `0x0022E1A0` → [MiUnlockWorkingSetExclusive](../27/MiUnlockWorkingSetExclusive_function_0027EC70.md) (function, `0x0027EC70`)
- `0x0022E1AA` → [MiUnlockAweVadsExclusive](../4B/MiUnlockAweVadsExclusive_function_004BDF1C.md) (function, `0x004BDF1C`)
- `0x0022E1B3` → [MiFreeForkMappingPte](../../page/70/MiFreeForkMappingPte_function_00705848.md) (function, `0x00705848`)
- `0x0022E1F0` → [MiFreeCloneDescriptor](../../page/A8/MiFreeCloneDescriptor_function_00A89F0C.md) (function, `0x00A89F0C`)
- `0x0022E201` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0022E220` → [MiUnlockWorkingSetExclusive](../27/MiUnlockWorkingSetExclusive_function_0027EC70.md) (function, `0x0027EC70`)
- `0x0022E22A` → [MiUnlockAweVadsExclusive](../4B/MiUnlockAweVadsExclusive_function_004BDF1C.md) (function, `0x004BDF1C`)
- `0x0022E235` → [MiFreeCloneDescriptor](../../page/A8/MiFreeCloneDescriptor_function_00A89F0C.md) (function, `0x00A89F0C`)
- `0x0022E240` → [PsReturnProcessNonPagedPoolQuota](../41/PsReturnProcessNonPagedPoolQuota_function_0041C200.md) (function, `0x0041C200`)
- `0x0022E24A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0022E275` → [MiLocateLockedVadEvent](../2A/MiLocateLockedVadEvent_function_002A7A0C.md) (function, `0x002A7A0C`)
- `0x0022E280` → [MiLocateLockedVadEvent](../2A/MiLocateLockedVadEvent_function_002A7A0C.md) (function, `0x002A7A0C`)
- `0x0022E299` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0022E2B2` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x0022E2B7` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x0022E2D9` → [PsReturnProcessNonPagedPoolQuota](../41/PsReturnProcessNonPagedPoolQuota_function_0041C200.md) (function, `0x0041C200`)
- `0x0022E2E6` → [MiReturnFullProcessCommitment](../../page/9E/MiReturnFullProcessCommitment_function_009E5D58.md) (function, `0x009E5D58`)
- `0x0022E303` → [PsReturnProcessNonPagedPoolQuota](../41/PsReturnProcessNonPagedPoolQuota_function_0041C200.md) (function, `0x0041C200`)

### Direct callers
- [MiCloneProcessAddressSpace](../../page/AD/MiCloneProcessAddressSpace_function_00AD6F7C.md) at `0x00AD71B4`

### Static image references
- `0x0022DC38` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x0022DCEE` → [MiBuildNewCloneDescriptor](../../page/A6/MiBuildNewCloneDescriptor_function_00A6C744.md) (`.text` → `PAGE`)
  - `0x0022DDAC` → [MiInitializeForkMaps](../../page/AD/MiInitializeForkMaps_function_00AD4A40.md) (`.text` → `PAGE`)
  - `0x0022DF44` → [MiUpdateForkMaps](../../page/A7/MiUpdateForkMaps_function_00A7DAF8.md) (`.text` → `PAGE`)
  - `0x0022E17B` → [MiFreeForkMaps](../../page/AC/MiFreeForkMaps_function_00AC8534.md) (`.text` → `PAGE`)
  - `0x0022E1B3` → [MiFreeForkMappingPte](../../page/70/MiFreeForkMappingPte_function_00705848.md) (`.text` → `PAGE`)
  - `0x0022E1F0` → [MiFreeCloneDescriptor](../../page/A8/MiFreeCloneDescriptor_function_00A89F0C.md) (`.text` → `PAGE`)
  - `0x0022E235` → [MiFreeCloneDescriptor](../../page/A8/MiFreeCloneDescriptor_function_00A89F0C.md) (`.text` → `PAGE`)
  - `0x0022E24A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x0022E2E6` → [MiReturnFullProcessCommitment](../../page/9E/MiReturnFullProcessCommitment_function_009E5D58.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0022E2CB` → [sub_006D71DE](../6D/Unknown_function_006D71DE.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0022DC1C  40 55                           push rbp
0022DC1E  53                              push rbx
0022DC1F  56                              push rsi
0022DC20  57                              push rdi
0022DC21  41 54                           push r12
0022DC23  41 55                           push r13
0022DC25  41 56                           push r14
0022DC27  41 57                           push r15
0022DC29  48 8D AC 24 08 FF FF FF         lea rbp, [rsp - 0xf8]
0022DC31  48 81 EC F8 01 00 00            sub rsp, 0x1f8
0022DC38  48 8B 05 01 CB BD 00            mov rax, qword ptr [rip + 0xbdcb01]
0022DC3F  48 33 C4                        xor rax, rsp
0022DC42  48 89 85 E0 00 00 00            mov qword ptr [rbp + 0xe0], rax
0022DC49  48 8B BD 68 01 00 00            mov rdi, qword ptr [rbp + 0x168]
0022DC50  4C 8B E2                        mov r12, rdx
0022DC53  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
0022DC58  4C 8B F1                        mov r14, rcx
0022DC5B  48 89 54 24 60                  mov qword ptr [rsp + 0x60], rdx
0022DC60  41 B8 C8 00 00 00               mov r8d, 0xc8
0022DC66  48 89 4D 00                     mov qword ptr [rbp], rcx
0022DC6A  33 D2                           xor edx, edx
0022DC6C  48 8D 4D 10                     lea rcx, [rbp + 0x10]
0022DC70  48 89 7D F8                     mov qword ptr [rbp - 8], rdi
0022DC74  49 8B D9                        mov rbx, r9
0022DC77  E8 C4 8F 49 00                  call 0x1406c6c40
0022DC7C  33 D2                           xor edx, edx
0022DC7E  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
0022DC83  44 8D 42 70                     lea r8d, [rdx + 0x70]
0022DC87  E8 B4 8F 49 00                  call 0x1406c6c40
0022DC8C  83 27 00                        and dword ptr [rdi], 0
0022DC8F  45 33 FF                        xor r15d, r15d
0022DC92  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0022DC9B  48 83 64 24 50 00               and qword ptr [rsp + 0x50], 0
0022DCA1  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
0022DCA7  4C 21 7D C8                     and qword ptr [rbp - 0x38], r15
0022DCAB  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0022DCB0  8B 85 60 01 00 00               mov eax, dword ptr [rbp + 0x160]
0022DCB6  89 45 88                        mov dword ptr [rbp - 0x78], eax
0022DCB9  48 89 5D 80                     mov qword ptr [rbp - 0x80], rbx
0022DCBD  4C 89 74 24 70                  mov qword ptr [rsp + 0x70], r14
0022DCC2  4C 89 64 24 78                  mov qword ptr [rsp + 0x78], r12
0022DCC7  B8 01 00 00 00                  mov eax, 1
0022DCCC  49 8B 9E 88 02 00 00            mov rbx, qword ptr [r14 + 0x288]
0022DCD3  49 8B CE                        mov rcx, r14
0022DCD6  4D 8B 86 10 04 00 00            mov r8, qword ptr [r14 + 0x410]
0022DCDD  48 85 DB                        test rbx, rbx
0022DCE0  48 0F 44 D8                     cmove rbx, rax
0022DCE4  48 8B D3                        mov rdx, rbx
0022DCE7  4D 8B 80 28 04 00 00            mov r8, qword ptr [r8 + 0x428]
0022DCEE  E8 51 EA 83 00                  call 0x140a6c744
0022DCF3  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0022DCF8  4C 8B E8                        mov r13, rax
0022DCFB  48 85 C0                        test rax, rax
0022DCFE  0F 84 15 06 00 00               je 0x14022e319
0022DD04  48 FF C3                        inc rbx
0022DD07  49 8B CC                        mov rcx, r12
0022DD0A  48 C1 E3 05                     shl rbx, 5
0022DD0E  48 8B D3                        mov rdx, rbx
0022DD11  E8 6A 9E 07 00                  call 0x1402a7b80
0022DD16  85 C0                           test eax, eax
0022DD18  0F 88 F4 05 00 00               js 0x14022e312
0022DD1E  BA 70 00 00 00                  mov edx, 0x70
0022DD23  41 B8 4D 6D 43 64               mov r8d, 0x64436d4d
0022DD29  8D 4A D0                        lea ecx, [rdx - 0x30]
0022DD2C  E8 0F D8 12 00                  call 0x14035b540
0022DD31  48 8B F0                        mov rsi, rax
0022DD34  48 85 C0                        test rax, rax
0022DD37  0F 84 C0 05 00 00               je 0x14022e2fd
0022DD3D  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0022DD42  49 8D BE 00 04 00 00            lea rdi, [r14 + 0x400]
0022DD49  48 89 58 40                     mov qword ptr [rax + 0x40], rbx
0022DD4D  E8 92 01 29 00                  call 0x1404bdee4
0022DD52  48 8B CF                        mov rcx, rdi
0022DD55  E8 46 5B 0F 00                  call 0x1403238a0
0022DD5A  88 45 8C                        mov byte ptr [rbp - 0x74], al
0022DD5D  49 8B 4D 28                     mov rcx, qword ptr [r13 + 0x28]
0022DD61  49 39 8E 88 02 00 00            cmp qword ptr [r14 + 0x288], rcx
0022DD68  0F 87 AD 04 00 00               ja 0x14022e21b
0022DD6E  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
0022DD73  BA 01 00 00 00                  mov edx, 1
0022DD78  49 8B CE                        mov rcx, r14
0022DD7B  48 89 06                        mov qword ptr [rsi], rax
0022DD7E  E8 35 CA 26 00                  call 0x14049a7b8
0022DD83  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0022DD88  48 8B CF                        mov rcx, rdi
0022DD8B  8A 55 8C                        mov dl, byte ptr [rbp - 0x74]
0022DD8E  49 89 9E 70 02 00 00            mov qword ptr [r14 + 0x270], rbx
0022DD95  E8 D6 0E 05 00                  call 0x14027ec70
0022DD9A  48 8B CB                        mov rcx, rbx
0022DD9D  E8 7A 01 29 00                  call 0x1404bdf1c
0022DDA2  4C 8D 45 10                     lea r8, [rbp + 0x10]
0022DDA6  49 8B D4                        mov rdx, r12
0022DDA9  49 8B CE                        mov rcx, r14
0022DDAC  E8 8F 6C 8A 00                  call 0x140ad4a40
0022DDB1  85 C0                           test eax, eax
0022DDB3  0F 84 9B 04 00 00               je 0x14022e254
0022DDB9  48 8B CF                        mov rcx, rdi
0022DDBC  E8 DF 5A 0F 00                  call 0x1403238a0
0022DDC1  49 8B 7D 18                     mov rdi, qword ptr [r13 + 0x18]
0022DDC5  B8 01 00 00 00                  mov eax, 1
0022DDCA  48 89 7D B8                     mov qword ptr [rbp - 0x48], rdi
0022DDCE  44 8B C0                        mov r8d, eax
0022DDD1  49 8B D5                        mov rdx, r13
0022DDD4  48 89 7D F0                     mov qword ptr [rbp - 0x10], rdi
0022DDD8  49 8B CE                        mov rcx, r14
0022DDDB  49 89 45 30                     mov qword ptr [r13 + 0x30], rax
0022DDDF  E8 98 6C 2A 00                  call 0x1404d4a7c
0022DDE4  49 8B 84 24 58 05 00 00         mov rax, qword ptr [r12 + 0x558]
0022DDEC  33 DB                           xor ebx, ebx
0022DDEE  EB 06                           jmp 0x14022ddf6
0022DDF0  48 8B D8                        mov rbx, rax
0022DDF3  48 8B 00                        mov rax, qword ptr [rax]
0022DDF6  48 85 C0                        test rax, rax
0022DDF9  75 F5                           jne 0x14022ddf0
0022DDFB  48 85 DB                        test rbx, rbx
0022DDFE  0F 84 FD 01 00 00               je 0x14022e001
0022DE04  49 BD 00 00 00 00 80 F6 FF FF   movabs r13, 0xfffff68000000000
0022DE0E  4D 8D A6 00 04 00 00            lea r12, [r14 + 0x400]
0022DE15  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0022DE19  4C 8B DB                        mov r11, rbx
0022DE1C  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
0022DE21  48 8B CB                        mov rcx, rbx
0022DE24  48 85 C0                        test rax, rax
0022DE27  74 23                           je 0x14022de4c
0022DE29  48 8B 08                        mov rcx, qword ptr [rax]
0022DE2C  48 8B D8                        mov rbx, rax
0022DE2F  48 85 C9                        test rcx, rcx
0022DE32  74 22                           je 0x14022de56
0022DE34  48 8B 01                        mov rax, qword ptr [rcx]
0022DE37  48 8B D9                        mov rbx, rcx
0022DE3A  48 8B C8                        mov rcx, rax
0022DE3D  48 85 C0                        test rax, rax
0022DE40  75 F2                           jne 0x14022de34
0022DE42  EB 12                           jmp 0x14022de56
0022DE44  48 39 0B                        cmp qword ptr [rbx], rcx
0022DE47  74 0D                           je 0x14022de56
0022DE49  48 8B CB                        mov rcx, rbx
0022DE4C  48 8B 5B 10                     mov rbx, qword ptr [rbx + 0x10]
0022DE50  48 83 E3 FC                     and rbx, 0xfffffffffffffffc
0022DE54  75 EE                           jne 0x14022de44
0022DE56  41 0F B6 7B 20                  movzx edi, byte ptr [r11 + 0x20]
0022DE5B  41 8B 43 18                     mov eax, dword ptr [r11 + 0x18]
0022DE5F  48 C1 E7 20                     shl rdi, 0x20
0022DE63  48 0B F8                        or rdi, rax
0022DE66  48 C1 E7 0C                     shl rdi, 0xc
0022DE6A  48 8B CF                        mov rcx, rdi
0022DE6D  E8 5E 8A 0E 00                  call 0x1403168d0
0022DE72  41 8B 53 34                     mov edx, dword ptr [r11 + 0x34]
0022DE76  4C 8B C8                        mov r9, rax
0022DE79  45 0F B6 43 22                  movzx r8d, byte ptr [r11 + 0x22]
0022DE7E  49 C1 E0 20                     shl r8, 0x20
0022DE82  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0022DE86  4C 0B C2                        or r8, rdx
0022DE89  48 B8 FD FF FF FF 07 00 00 00   movabs rax, 0x7fffffffd
0022DE93  4C 3B C0                        cmp r8, rax
0022DE96  0F 83 4E 01 00 00               jae 0x14022dfea
0022DE9C  49 8B CB                        mov rcx, r11
0022DE9F  E8 7C 18 10 00                  call 0x14032f720
0022DEA4  85 C0                           test eax, eax
0022DEA6  0F 85 3E 01 00 00               jne 0x14022dfea
0022DEAC  48 C1 EF 09                     shr rdi, 9
0022DEB0  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0022DEBA  48 23 F8                        and rdi, rax
0022DEBD  4C 89 4D 98                     mov qword ptr [rbp - 0x68], r9
0022DEC1  4C 89 5D A0                     mov qword ptr [rbp - 0x60], r11
0022DEC5  49 8B C5                        mov rax, r13
0022DEC8  41 0F B6 4B 21                  movzx ecx, byte ptr [r11 + 0x21]
0022DECD  48 03 F8                        add rdi, rax
0022DED0  41 8B 43 1C                     mov eax, dword ptr [r11 + 0x1c]
0022DED4  48 C1 E1 20                     shl rcx, 0x20
0022DED8  48 0B C8                        or rcx, rax
0022DEDB  48 B8 FF FF FF FF 0F 00 00 00   movabs rax, 0xfffffffff
0022DEE5  48 23 C8                        and rcx, rax
0022DEE8  49 8B C5                        mov rax, r13
0022DEEB  4C 8D 3C C8                     lea r15, [rax + rcx*8]
0022DEEF  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
0022DEF4  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
0022DEF8  48 85 C9                        test rcx, rcx
0022DEFB  0F 85 5D 01 00 00               jne 0x14022e05e
0022DF01  44 8A 45 8C                     mov r8b, byte ptr [rbp - 0x74]
0022DF05  48 8D 45 E0                     lea rax, [rbp - 0x20]
0022DF09  41 B9 04 00 00 00               mov r9d, 4
0022DF0F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0022DF14  49 8B D7                        mov rdx, r15
0022DF17  48 8B CF                        mov rcx, rdi
0022DF1A  E8 C1 4F 09 00                  call 0x1402c2ee0
0022DF1F  8A 55 8C                        mov dl, byte ptr [rbp - 0x74]
0022DF22  49 8B CC                        mov rcx, r12
0022DF25  48 8B F8                        mov rdi, rax
0022DF28  E8 43 0D 05 00                  call 0x14027ec70
0022DF2D  48 85 FF                        test rdi, rdi
0022DF30  0F 84 1F 01 00 00               je 0x14022e055
0022DF36  4D 8B CE                        mov r9, r14
0022DF39  4C 8D 45 C8                     lea r8, [rbp - 0x38]
0022DF3D  48 8B D7                        mov rdx, rdi
0022DF40  48 8D 4D 10                     lea rcx, [rbp + 0x10]
0022DF44  E8 AF FB 84 00                  call 0x140a7daf8
0022DF49  48 8B F8                        mov rdi, rax
0022DF4C  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
0022DF50  49 8B CC                        mov rcx, r12
0022DF53  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
0022DF57  E8 44 59 0F 00                  call 0x1403238a0
0022DF5C  4C 8B 5C 24 48                  mov r11, qword ptr [rsp + 0x48]
0022DF61  41 8B 43 30                     mov eax, dword ptr [r11 + 0x30]
0022DF65  83 E0 70                        and eax, 0x70
0022DF68  3C 50                           cmp al, 0x50
0022DF6A  74 62                           je 0x14022dfce
0022DF6C  49 3B FF                        cmp rdi, r15
0022DF6F  0F 87 F0 02 00 00               ja 0x14022e265
0022DF75  48 8B 45 38                     mov rax, qword ptr [rbp + 0x38]
0022DF79  4C 8B FF                        mov r15, rdi
0022DF7C  44 8A 45 8C                     mov r8b, byte ptr [rbp - 0x74]
0022DF80  49 81 E7 00 F0 FF FF            and r15, 0xfffffffffffff000
0022DF87  49 81 C7 F8 0F 00 00            add r15, 0xff8
0022DF8E  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
0022DF92  4C 3B 7C 24 40                  cmp r15, qword ptr [rsp + 0x40]
0022DF97  41 B9 01 00 00 00               mov r9d, 1
0022DF9D  48 8B CF                        mov rcx, rdi
0022DFA0  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
0022DFA4  4C 0F 47 7C 24 40               cmova r15, qword ptr [rsp + 0x40]
0022DFAA  33 D2                           xor edx, edx
0022DFAC  E8 BF 1F 05 00                  call 0x14027ff70
0022DFB1  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
0022DFB6  E8 71 03 00 00                  call 0x14022e32c
0022DFBB  48 8B 7D A8                     mov rdi, qword ptr [rbp - 0x58]
0022DFBF  49 3B FF                        cmp rdi, r15
0022DFC2  76 ED                           jbe 0x14022dfb1
0022DFC4  4C 8B 7C 24 40                  mov r15, qword ptr [rsp + 0x40]
0022DFC9  4C 8B 5C 24 48                  mov r11, qword ptr [rsp + 0x48]
0022DFCE  49 3B FF                        cmp rdi, r15
0022DFD1  0F 86 1D FF FF FF               jbe 0x14022def4
0022DFD7  41 8B 43 30                     mov eax, dword ptr [r11 + 0x30]
0022DFDB  BA 00 00 60 00                  mov edx, 0x600000
0022DFE0  23 C2                           and eax, edx
0022DFE2  3B C2                           cmp eax, edx
0022DFE4  0F 84 80 02 00 00               je 0x14022e26a
0022DFEA  48 85 DB                        test rbx, rbx
0022DFED  0F 85 22 FE FF FF               jne 0x14022de15
0022DFF3  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
0022DFF8  4C 8B 64 24 60                  mov r12, qword ptr [rsp + 0x60]
0022DFFD  48 8B 7D F0                     mov rdi, qword ptr [rbp - 0x10]
0022E001  83 7D D0 00                     cmp dword ptr [rbp - 0x30], 0
0022E005  0F 85 98 02 00 00               jne 0x14022e2a3
0022E00B  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
0022E00F  48 85 C9                        test rcx, rcx
0022E012  0F 85 9A 02 00 00               jne 0x14022e2b2
0022E018  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
0022E01C  49 8B 4D 38                     mov rcx, qword ptr [r13 + 0x38]
0022E020  49 01 84 24 88 02 00 00         add qword ptr [r12 + 0x288], rax
0022E028  4C 8B 7D B8                     mov r15, qword ptr [rbp - 0x48]
0022E02C  49 8B 84 24 88 02 00 00         mov rax, qword ptr [r12 + 0x288]
0022E034  4C 2B FF                        sub r15, rdi
0022E037  49 C1 FF 05                     sar r15, 5
0022E03B  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
0022E03F  4D 85 FF                        test r15, r15
0022E042  75 2E                           jne 0x14022e072
0022E044  49 8D 8E 80 02 00 00            lea rcx, [r14 + 0x280]
0022E04B  49 8B D5                        mov rdx, r13
0022E04E  E8 FD 85 06 00                  call 0x140296650
0022E053  EB 28                           jmp 0x14022e07d
0022E055  49 8D 7F 08                     lea rdi, [r15 + 8]
0022E059  E9 EE FE FF FF                  jmp 0x14022df4c
0022E05E  E8 5D 3F 0E 00                  call 0x140311fc0
0022E063  E8 08 5C 0E 00                  call 0x140313c70
0022E068  48 83 65 D8 00                  and qword ptr [rbp - 0x28], 0
0022E06D  E9 8F FE FF FF                  jmp 0x14022df01
0022E072  4C 89 39                        mov qword ptr [rcx], r15
0022E075  4D 89 7D 30                     mov qword ptr [r13 + 0x30], r15
0022E079  4D 89 7D 28                     mov qword ptr [r13 + 0x28], r15
0022E07D  BA 01 00 00 00                  mov edx, 1
0022E082  49 8B CE                        mov rcx, r14
0022E085  E8 2E C7 26 00                  call 0x14049a7b8
0022E08A  49 8B 86 80 02 00 00            mov rax, qword ptr [r14 + 0x280]
0022E091  33 FF                           xor edi, edi
0022E093  EB 06                           jmp 0x14022e09b
0022E095  48 8B F8                        mov rdi, rax
0022E098  48 8B 00                        mov rax, qword ptr [rax]
0022E09B  48 85 C0                        test rax, rax
0022E09E  75 F5                           jne 0x14022e095
0022E0A0  48 85 FF                        test rdi, rdi
0022E0A3  0F 84 BA 00 00 00               je 0x14022e163
0022E0A9  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
0022E0AE  4C 8B 6C 24 50                  mov r13, qword ptr [rsp + 0x50]
0022E0B3  48 8B 47 38                     mov rax, qword ptr [rdi + 0x38]
0022E0B7  F0 48 FF 40 08                  lock inc qword ptr [rax + 8]
0022E0BC  0F 10 07                        movups xmm0, xmmword ptr [rdi]
0022E0BF  48 8B 1E                        mov rbx, qword ptr [rsi]
0022E0C2  45 33 C0                        xor r8d, r8d
0022E0C5  4C 03 76 40                     add r14, qword ptr [rsi + 0x40]
0022E0C9  48 8B D6                        mov rdx, rsi
0022E0CC  4C 03 6F 40                     add r13, qword ptr [rdi + 0x40]
0022E0D0  49 8B CC                        mov rcx, r12
0022E0D3  0F 11 06                        movups xmmword ptr [rsi], xmm0
0022E0D6  0F 10 4F 10                     movups xmm1, xmmword ptr [rdi + 0x10]
0022E0DA  0F 11 4E 10                     movups xmmword ptr [rsi + 0x10], xmm1
0022E0DE  0F 10 47 20                     movups xmm0, xmmword ptr [rdi + 0x20]
0022E0E2  0F 11 46 20                     movups xmmword ptr [rsi + 0x20], xmm0
0022E0E6  0F 10 4F 30                     movups xmm1, xmmword ptr [rdi + 0x30]
0022E0EA  0F 11 4E 30                     movups xmmword ptr [rsi + 0x30], xmm1
0022E0EE  0F 10 47 40                     movups xmm0, xmmword ptr [rdi + 0x40]
0022E0F2  0F 11 46 40                     movups xmmword ptr [rsi + 0x40], xmm0
0022E0F6  0F 10 4F 50                     movups xmm1, xmmword ptr [rdi + 0x50]
0022E0FA  0F 11 4E 50                     movups xmmword ptr [rsi + 0x50], xmm1
0022E0FE  0F 10 47 60                     movups xmm0, xmmword ptr [rdi + 0x60]
0022E102  0F 11 46 60                     movups xmmword ptr [rsi + 0x60], xmm0
0022E106  E8 71 69 2A 00                  call 0x1404d4a7c
0022E10B  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
0022E10F  48 8B F3                        mov rsi, rbx
0022E112  48 8B CF                        mov rcx, rdi
0022E115  48 85 C0                        test rax, rax
0022E118  74 23                           je 0x14022e13d
0022E11A  48 8B 08                        mov rcx, qword ptr [rax]
0022E11D  48 8B F8                        mov rdi, rax
0022E120  48 85 C9                        test rcx, rcx
0022E123  74 22                           je 0x14022e147
0022E125  48 8B 01                        mov rax, qword ptr [rcx]
0022E128  48 8B F9                        mov rdi, rcx
0022E12B  48 8B C8                        mov rcx, rax
0022E12E  48 85 C0                        test rax, rax
0022E131  75 F2                           jne 0x14022e125
0022E133  EB 12                           jmp 0x14022e147
0022E135  48 39 0F                        cmp qword ptr [rdi], rcx
0022E138  74 0D                           je 0x14022e147
0022E13A  48 8B CF                        mov rcx, rdi
0022E13D  48 8B 7F 10                     mov rdi, qword ptr [rdi + 0x10]
0022E141  48 83 E7 FC                     and rdi, 0xfffffffffffffffc
0022E145  75 EE                           jne 0x14022e135
0022E147  48 85 FF                        test rdi, rdi
0022E14A  0F 85 63 FF FF FF               jne 0x14022e0b3
0022E150  4C 89 6C 24 50                  mov qword ptr [rsp + 0x50], r13
0022E155  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
0022E15A  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
0022E15F  4C 8B 75 00                     mov r14, qword ptr [rbp]
0022E163  8A 55 8C                        mov dl, byte ptr [rbp - 0x74]
0022E166  49 8D 9E 00 04 00 00            lea rbx, [r14 + 0x400]
0022E16D  48 8B CB                        mov rcx, rbx
0022E170  33 FF                           xor edi, edi
0022E172  E8 F9 0A 05 00                  call 0x14027ec70
0022E177  48 8D 4D 10                     lea rcx, [rbp + 0x10]
0022E17B  E8 B4 A3 89 00                  call 0x140ac8534
0022E180  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0022E185  E8 5A FD 28 00                  call 0x1404bdee4
0022E18A  48 8B CB                        mov rcx, rbx
0022E18D  E8 0E 57 0F 00                  call 0x1403238a0
0022E192  8A 55 8C                        mov dl, byte ptr [rbp - 0x74]
0022E195  48 8B CB                        mov rcx, rbx
0022E198  49 83 A6 70 02 00 00 00         and qword ptr [r14 + 0x270], 0
0022E1A0  E8 CB 0A 05 00                  call 0x14027ec70
0022E1A5  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0022E1AA  E8 6D FD 28 00                  call 0x1404bdf1c
0022E1AF  48 8D 4D 10                     lea rcx, [rbp + 0x10]
0022E1B3  E8 90 76 4D 00                  call 0x140705848
0022E1B8  48 85 F6                        test rsi, rsi
0022E1BB  0F 85 05 01 00 00               jne 0x14022e2c6
0022E1C1  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0022E1C6  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0022E1CB  48 3B C1                        cmp rax, rcx
0022E1CE  0F 87 FC 00 00 00               ja 0x14022e2d0
0022E1D4  48 8B 55 90                     mov rdx, qword ptr [rbp - 0x70]
0022E1D8  48 85 D2                        test rdx, rdx
0022E1DB  0F 85 02 01 00 00               jne 0x14022e2e3
0022E1E1  4D 85 FF                        test r15, r15
0022E1E4  0F 85 06 01 00 00               jne 0x14022e2f0
0022E1EA  49 8B D5                        mov rdx, r13
0022E1ED  49 8B CE                        mov rcx, r14
0022E1F0  E8 17 BD 85 00                  call 0x140a89f0c
0022E1F5  8B C7                           mov eax, edi
0022E1F7  48 8B 8D E0 00 00 00            mov rcx, qword ptr [rbp + 0xe0]
0022E1FE  48 33 CC                        xor rcx, rsp
0022E201  E8 3A E4 47 00                  call 0x1406ac640
0022E206  48 81 C4 F8 01 00 00            add rsp, 0x1f8
0022E20D  41 5F                           pop r15
0022E20F  41 5E                           pop r14
0022E211  41 5D                           pop r13
0022E213  41 5C                           pop r12
0022E215  5F                              pop rdi
0022E216  5E                              pop rsi
0022E217  5B                              pop rbx
0022E218  5D                              pop rbp
0022E219  C3                              ret
0022E21A  CC                              int3
0022E21B  8A D0                           mov dl, al
0022E21D  48 8B CF                        mov rcx, rdi
0022E220  E8 4B 0A 05 00                  call 0x14027ec70
0022E225  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0022E22A  E8 ED FC 28 00                  call 0x1404bdf1c
0022E22F  49 8B D5                        mov rdx, r13
0022E232  49 8B CE                        mov rcx, r14
0022E235  E8 D2 BC 85 00                  call 0x140a89f0c
0022E23A  48 8B D3                        mov rdx, rbx
0022E23D  49 8B CC                        mov rcx, r12
0022E240  E8 BB DF 1E 00                  call 0x14041c200
0022E245  33 D2                           xor edx, edx
0022E247  48 8B CE                        mov rcx, rsi
0022E24A  E8 21 46 95 00                  call 0x140b82870
0022E24F  E9 73 FA FF FF                  jmp 0x14022dcc7
0022E254  BF 9A 00 00 C0                  mov edi, 0xc000009a
0022E259  49 8D 9E 00 04 00 00            lea rbx, [r14 + 0x400]
0022E260  E9 1B FF FF FF                  jmp 0x14022e180
0022E265  E9 6D FD FF FF                  jmp 0x14022dfd7
0022E26A  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
0022E26E  BF 04 00 00 00                  mov edi, 4
0022E273  8B D7                           mov edx, edi
0022E275  E8 92 97 07 00                  call 0x1402a7a0c
0022E27A  49 8B CB                        mov rcx, r11
0022E27D  4C 8B C8                        mov r9, rax
0022E280  E8 87 97 07 00                  call 0x1402a7a0c
0022E285  49 8B 51 18                     mov rdx, qword ptr [r9 + 0x18]
0022E289  4C 8B 40 10                     mov r8, qword ptr [rax + 0x10]
0022E28D  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
0022E291  49 83 C0 07                     add r8, 7
0022E295  49 C1 E8 03                     shr r8, 3
0022E299  E8 A2 85 49 00                  call 0x1406c6840
0022E29E  E9 47 FD FF FF                  jmp 0x14022dfea
0022E2A3  48 8B 45 F8                     mov rax, qword ptr [rbp - 8]
0022E2A7  C7 00 01 00 00 00               mov dword ptr [rax], 1
0022E2AD  E9 59 FD FF FF                  jmp 0x14022e00b
0022E2B2  E8 09 3D 0E 00                  call 0x140311fc0
0022E2B7  E8 B4 59 0E 00                  call 0x140313c70
0022E2BC  48 83 65 D8 00                  and qword ptr [rbp - 0x28], 0
0022E2C1  E9 52 FD FF FF                  jmp 0x14022e018
0022E2C6  4C 8B 64 24 38                  mov r12, qword ptr [rsp + 0x38]
0022E2CB  E9 0E 8F 4A 00                  jmp 0x1406d71de
0022E2D0  48 2B C1                        sub rax, rcx
0022E2D3  49 8B CC                        mov rcx, r12
0022E2D6  48 8B D0                        mov rdx, rax
0022E2D9  E8 22 DF 1E 00                  call 0x14041c200
0022E2DE  E9 F1 FE FF FF                  jmp 0x14022e1d4
0022E2E3  49 8B CC                        mov rcx, r12
0022E2E6  E8 6D 7A 7B 00                  call 0x1409e5d58
0022E2EB  E9 F1 FE FF FF                  jmp 0x14022e1e1
0022E2F0  85 FF                           test edi, edi
0022E2F2  0F 89 FD FE FF FF               jns 0x14022e1f5
0022E2F8  E9 ED FE FF FF                  jmp 0x14022e1ea
0022E2FD  48 8B D3                        mov rdx, rbx
0022E300  49 8B CC                        mov rcx, r12
0022E303  E8 F8 DE 1E 00                  call 0x14041c200
0022E308  BF 9A 00 00 C0                  mov edi, 0xc000009a
0022E30D  E9 D8 FE FF FF                  jmp 0x14022e1ea
0022E312  8B F8                           mov edi, eax
0022E314  E9 D1 FE FF FF                  jmp 0x14022e1ea
0022E319  B8 9A 00 00 C0                  mov eax, 0xc000009a
0022E31E  E9 D4 FE FF FF                  jmp 0x14022e1f7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCloneVads(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned int v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int8 v_stack_m1AC;
    unsigned int v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;

    v_rsp = (v_rsp) - (504);
    result = (*(unsigned __int64 *)(v_rip + 12438273)) ^ (v_rsp);
    v_stack_m58 = result;
    v_stack_m1F8 = a3;
    v_stack_m1D8 = a2;
    v_stack_m138 = a1;
    a2 = 0;
    v_stack_m140 = a6;
    result = memset(v_stack_m128, a2, 200, a4);
    a2 = 0;
    result = memset(v_stack_m1C8, a2, a2 + 112, a4);
    v_r15 = 0;
    v_stack_m208 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m1B0 = (unsigned int)((unsigned int)(a5));
    v_stack_m1B8 = a4;
    v_stack_m1C8 = a1;
    v_stack_m1C0 = 0;
loc_0022DCC7:
    v_rbx = *(unsigned __int64 *)(a1 + 648);
    if (*(unsigned __int64 *)(a1 + 648) == 0) { v_rbx = 1; }
    result = MiBuildNewCloneDescriptor(a1, v_rbx, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1040) + 1064), a4);
    v_stack_m1E0 = result;
    if (result == 0) goto loc_0022E319;
    v_rbx = (v_rbx) + 1;
    v_rbx = (v_rbx) << (5);
    result = PsChargeProcessNonPagedPoolQuota(0, v_rbx, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1040) + 1064), a4);
    if (sign_flag) goto loc_0022E312;
    result = MiAllocatePool(112 - 48, 112, (unsigned int)(0x64436D4DULL), a4);
    if (result == 0) goto loc_0022E2FD;
    *(unsigned __int64 *)(result + 64) = v_rbx;
    result = MiLockAweVadsExclusive(v_stack_m208, 112, (unsigned int)(0x64436D4DULL), a4);
    result = MiLockWorkingSetExclusive(a1 + 1024, 112, (unsigned int)(0x64436D4DULL), a4);
    v_stack_m1AC = (unsigned __int8)(result);
    if ((*(unsigned __int64 *)(a1 + 648)) > (*(unsigned __int64 *)(result + 40))) goto loc_0022E21B;
    *(unsigned __int64 *)(result) = v_stack_m1F8;
    result = MiDeleteCloneZombies(a1, 1, (unsigned int)(0x64436D4DULL), a4);
    *(unsigned __int64 *)(a1 + 624) = v_stack_m208;
    result = MiUnlockWorkingSetExclusive(a1 + 1024, v_stack_m1AC, (unsigned int)(0x64436D4DULL), a4);
    result = MiUnlockAweVadsExclusive(v_stack_m208, v_stack_m1AC, (unsigned int)(0x64436D4DULL), a4);
    result = MiInitializeForkMaps(a1, 0, v_stack_m128, a4);
    if ((unsigned int)(result) == 0) goto loc_0022E254;
    result = MiLockWorkingSetExclusive(a1 + 1024, 0, v_stack_m128, a4);
    v_stack_m180 = *(unsigned __int64 *)(result + 24);
    v_stack_m148 = *(unsigned __int64 *)(result + 24);
    *(unsigned __int64 *)(result + 48) = 1;
    result = MiInsertClone(a1, result, 1, a4);
    v_rbx = 0;
    goto loc_0022DDF6;
loc_0022DDF0:
loc_0022DDF6:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 1368)) != 0) goto loc_0022DDF0;
    if (*(unsigned __int64 *)(a2 + 1368) == 0) goto loc_0022E001;
loc_0022DE15:
    v_stack_m1F0 = *(unsigned __int64 *)(a2 + 1368);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 1368) + 8) == 0) goto loc_0022DE4C;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 1368) + 8)) == 0) goto loc_0022DE56;
loc_0022DE34:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 1368) + 8))) != 0) goto loc_0022DE34;
    goto loc_0022DE56;
loc_0022DE44:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 1368) + 8)))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 1368) + 8))))) goto loc_0022DE56;
loc_0022DE4C:
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 1368) + 8)) + 16)) & (-4);
    if (condition_is_not_equal) goto loc_0022DE44;
loc_0022DE56:
    v_rdi = (*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 1368) + 32)) << (32);
    v_rdi = (v_rdi) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 1368) + 24)));
    v_rdi = (v_rdi) << (12);
    result = MiLocateAddress(v_rdi, result, 1, a4);
    a3 = (*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 1368) + 34)) << (32);
    v_stack_m150 = result;
    a3 = (a3) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 1368) + 52)));
    if (a3 >= result) goto loc_0022DFEA;
    result = MiIsVadLargePrivate(*(unsigned __int64 *)(a2 + 1368), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 1368) + 52)), a3, result);
    if ((unsigned int)(result) != 0) goto loc_0022DFEA;
    v_rdi = (v_rdi) >> (9);
    v_rdi = (v_rdi) & (result);
    v_stack_m1A0 = result;
    v_stack_m198 = *(unsigned __int64 *)(a2 + 1368);
    v_rdi = (v_rdi) + (result);
    a1 = (*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 1368) + 33)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 1368) + 28)));
    a1 = (a1) & ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 1368) + 28)));
    v_stack_m1F8 = result + a1 * 8;
loc_0022DEF4:
    if (v_stack_m160 != 0) goto loc_0022E05E;
loc_0022DF01:
    v_stack_m218 = v_stack_m158;
    result = MiGetNextPageTable(v_rdi, result + a1 * 8, v_stack_m1AC, 4);
    result = MiUnlockWorkingSetExclusive(a1 + 1024, v_stack_m1AC, v_stack_m1AC, 4);
    if (result == 0) goto loc_0022E055;
    result = MiUpdateForkMaps(v_stack_m128, result, v_stack_m170, a1);
loc_0022DF4C:
    v_stack_m178 = v_stack_mE8;
    result = MiLockWorkingSetExclusive(a1 + 1024, result, v_stack_m170, a1);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m1F0 + 48))) & (112));
    if (((unsigned __int8)(result)) == 80) goto loc_0022DFCE;
    if (result > (result + a1 * 8)) goto loc_0022E265;
    v_r15 = (result) & (0xFFFFFFFFFFFFF000ULL);
    v_r15 = (v_r15) + (0xFF8ULL);
    v_stack_m188 = v_stack_m100;
    v_stack_m190 = result;
    if (v_r15 > v_stack_m1F8) { v_r15 = v_stack_m1F8; }
    a2 = 0;
    result = MiMakeSystemAddressValid(result, a2, v_stack_m1AC, 1);
loc_0022DFB1:
    result = MiBuildForkPte(v_stack_m1C8, a2, v_stack_m1AC, 1);
    if (v_stack_m190 <= v_r15) goto loc_0022DFB1;
loc_0022DFCE:
    if (v_stack_m190 <= v_stack_m1F8) goto loc_0022DEF4;
loc_0022DFD7:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m1F0 + 48))) & ((unsigned int)((unsigned int)(0x600000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x600000ULL)))) goto loc_0022E26A;
loc_0022DFEA:
    if (v_rbx != 0) goto loc_0022DE15;
loc_0022E001:
    if (v_stack_m168 != 0) goto loc_0022E2A3;
loc_0022E00B:
    if (v_stack_m160 != 0) goto loc_0022E2B2;
loc_0022E018:
    v_r15 = (v_stack_m180) - (v_stack_m148);
    v_r15 = (v_r15) >> (5);
    v_stack_m170 = *(unsigned __int64 *)(v_stack_m1D8 + 648);
    if (v_r15 != 0) goto loc_0022E072;
    result = RtlAvlRemoveNode(a1 + 640, v_stack_m1E0, v_stack_m1AC, 1);
    goto loc_0022E07D;
loc_0022E055:
    goto loc_0022DF4C;
loc_0022E05E:
    result = MiFlushTbList(a1 + 640, v_stack_m1E0, v_stack_m1AC, 1);
    result = MiReleaseProcessorFlushList(a1 + 640, v_stack_m1E0, v_stack_m1AC, 1);
    goto loc_0022DF01;
loc_0022E072:
    *(unsigned __int64 *)(a1 + 640) = v_r15;
    *(unsigned __int64 *)(v_stack_m1E0 + 48) = v_r15;
    *(unsigned __int64 *)(v_stack_m1E0 + 40) = v_r15;
loc_0022E07D:
    result = MiDeleteCloneZombies(a1, 1, v_stack_m1AC, 1);
    v_rdi = 0;
    goto loc_0022E09B;
loc_0022E095:
loc_0022E09B:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 640)) != 0) goto loc_0022E095;
    if (*(unsigned __int64 *)(a1 + 640) == 0) goto loc_0022E163;
loc_0022E0B3:
    a3 = 0;
    v_r14 = (v_stack_m200) + (*(unsigned __int64 *)(result + 64));
    v_r13 = (v_stack_m1E8) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 640) + 64));
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(result + 16) = v_xmm1;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    *(unsigned __int64 *)(result + 48) = v_xmm1;
    *(unsigned __int64 *)(result + 64) = v_xmm0;
    *(unsigned __int64 *)(result + 80) = v_xmm1;
    *(unsigned __int64 *)(result + 96) = v_xmm0;
    result = MiInsertClone(v_stack_m1D8, result, a3, 1);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 640) + 8) == 0) goto loc_0022E13D;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 640) + 8)) == 0) goto loc_0022E147;
loc_0022E125:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 640) + 8))) != 0) goto loc_0022E125;
    goto loc_0022E147;
loc_0022E135:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 640) + 8)))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 640) + 8))))) goto loc_0022E147;
loc_0022E13D:
    v_rdi = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 640) + 8)) + 16)) & (-4);
    if (condition_is_not_equal) goto loc_0022E135;
loc_0022E147:
    if (v_rdi != 0) goto loc_0022E0B3;
    v_stack_m1E8 = v_r13;
    v_stack_m200 = v_r14;
loc_0022E163:
    v_rdi = 0;
    result = MiUnlockWorkingSetExclusive(v_stack_m138 + 1024, v_stack_m1AC, a3, 1);
    result = MiFreeForkMaps(v_stack_m128, v_stack_m1AC, a3, 1);
loc_0022E180:
    result = MiLockAweVadsExclusive(v_stack_m208, v_stack_m1AC, a3, 1);
    result = MiLockWorkingSetExclusive(v_stack_m138 + 1024, v_stack_m1AC, a3, 1);
    result = MiUnlockWorkingSetExclusive(v_stack_m138 + 1024, v_stack_m1AC, a3, 1);
    result = MiUnlockAweVadsExclusive(v_stack_m208, v_stack_m1AC, a3, 1);
    result = MiFreeForkMappingPte(v_stack_m128, v_stack_m1AC, a3, 1);
    if (*(unsigned __int64 *)(result) != 0) goto loc_0022E2C6;
    if (v_stack_m200 > v_stack_m1E8) goto loc_0022E2D0;
loc_0022E1D4:
    if (v_stack_m1A8 != 0) goto loc_0022E2E3;
loc_0022E1E1:
    if (v_r15 != 0) goto loc_0022E2F0;
loc_0022E1EA:
    result = MiFreeCloneDescriptor(v_stack_m138, v_stack_m1E0, a3, 1);
loc_0022E1F5:
loc_0022E1F7:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m1E0, a3, 1);
    v_rsp = (v_rsp) + (504);
    return result;
loc_0022E21B:
    result = MiUnlockWorkingSetExclusive(0, (unsigned __int8)(result), a3, 1);
    result = MiUnlockAweVadsExclusive(v_stack_p30, (unsigned __int8)(result), a3, 1);
    result = MiFreeCloneDescriptor(v_stack_m138, v_stack_m1E0, a3, 1);
    result = PsReturnProcessNonPagedPoolQuota(v_stack_m1D8, v_stack_m138 + 1024, a3, 1);
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(result), a2, a3, 1);
    goto loc_0022DCC7;
loc_0022E254:
    goto loc_0022E180;
loc_0022E265:
    goto loc_0022DFD7;
loc_0022E26A:
    result = MiLocateLockedVadEvent(v_stack_m150, 4, a3, 1);
    result = MiLocateLockedVadEvent(v_stack_m1F0, 4, a3, result);
    a3 = (*(unsigned __int64 *)(result + 16)) + (7);
    a3 = (a3) >> (3);
    result = memcpy(*(unsigned __int64 *)(result + 24), *(unsigned __int64 *)(result + 24), a3, result);
    goto loc_0022DFEA;
loc_0022E2A3:
    *(unsigned int *)(v_stack_m140) = 1;
    goto loc_0022E00B;
loc_0022E2B2:
    result = MiFlushTbList(*(unsigned __int64 *)(result + 24), *(unsigned __int64 *)(result + 24), a3, result);
    result = MiReleaseProcessorFlushList(*(unsigned __int64 *)(result + 24), *(unsigned __int64 *)(result + 24), a3, result);
    goto loc_0022E018;
loc_0022E2C6:
loc_0022E2D0:
    result = (result) - (*(unsigned __int64 *)(result + 24));
    result = PsReturnProcessNonPagedPoolQuota(v_stack_p38, result, a3, result);
    goto loc_0022E1D4;
loc_0022E2E3:
    result = MiReturnFullProcessCommitment(v_stack_p38, result, a3, result);
    goto loc_0022E1E1;
loc_0022E2F0:
    if (!sign_flag) goto loc_0022E1F5;
    goto loc_0022E1EA;
loc_0022E2FD:
    result = PsReturnProcessNonPagedPoolQuota(v_stack_p38, v_stack_m138 + 1024, a3, result);
    goto loc_0022E1EA;
loc_0022E312:
    goto loc_0022E1EA;
loc_0022E319:
    goto loc_0022E1F7;
}
```

## 5. (Beta) C Style

```c
int64_t MiCloneVads(void *Arg1, void *Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, void *Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m128;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint32_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint8_t v_stack_m1AC;
    uint32_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint64_t v_stack_m218;
    uint64_t v_stack_m58;
    uint64_t v_stack_mE8;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;

    local_rsp = (local_rsp) - (504);
    result = (*(uint64_t *)(v_rip + 0xBDCB01)) ^ (local_rsp);
    v_stack_m58 = result;
    v_stack_m1F8 = Arg3;
    v_stack_m1D8 = Arg2;
    v_stack_m138 = Arg1;
    Arg2 = 0;
    v_stack_m140 = Arg6;
    result = memset(v_stack_m128, Arg2, 200, Arg4);
    Arg2 = 0;
    result = memset(v_stack_m1C8, Arg2, Arg2 + 112, Arg4);
    local_r15 = 0;
    v_stack_m208 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m1B0 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m1B8 = Arg4;
    v_stack_m1C8 = Arg1;
    v_stack_m1C0 = 0;
loc_0022DCC7:
    local_rbx = *(uint64_t *)(arg1 + 0x288);
    if (*(uint64_t *)(arg1 + 0x288) == 0) { local_rbx = 1; }
    result = MiBuildNewCloneDescriptor(Arg1, local_rbx, *(uint64_t *)(*(uint64_t *)(arg1 + 0x410) + 0x428), Arg4);
    v_stack_m1E0 = result;
    if (result == 0) goto loc_0022E319;
    local_rbx = (local_rbx) + 1;
    local_rbx = (local_rbx) << (5);
    result = PsChargeProcessNonPagedPoolQuota(0, local_rbx, *(uint64_t *)(*(uint64_t *)(arg1 + 0x410) + 0x428), Arg4);
    if (sign_flag) goto loc_0022E312;
    result = MiAllocatePool(112 - 48, 112, (uint32_t)(0x64436D4DULL), Arg4);
    if (result == 0) goto loc_0022E2FD;
    *(uint64_t *)(result + 0x40) = local_rbx;
    result = MiLockAweVadsExclusive(v_stack_m208, 112, (uint32_t)(0x64436D4DULL), Arg4);
    result = MiLockWorkingSetExclusive(Arg1 + 1024, 112, (uint32_t)(0x64436D4DULL), Arg4);
    v_stack_m1AC = (uint8_t)(result);
    if ((*(uint64_t *)(arg1 + 0x288)) > (*(uint64_t *)(result + 0x28))) goto loc_0022E21B;
    *(uint64_t *)(result) = v_stack_m1F8;
    result = MiDeleteCloneZombies(Arg1, 1, (uint32_t)(0x64436D4DULL), Arg4);
    *(uint64_t *)(arg1 + 0x270) = v_stack_m208;
    result = MiUnlockWorkingSetExclusive(Arg1 + 1024, v_stack_m1AC, (uint32_t)(0x64436D4DULL), Arg4);
    result = MiUnlockAweVadsExclusive(v_stack_m208, v_stack_m1AC, (uint32_t)(0x64436D4DULL), Arg4);
    result = MiInitializeForkMaps(Arg1, 0, v_stack_m128, Arg4);
    if ((uint32_t)(result) == 0) goto loc_0022E254;
    result = MiLockWorkingSetExclusive(Arg1 + 1024, 0, v_stack_m128, Arg4);
    v_stack_m180 = *(uint64_t *)(result + 0x18);
    v_stack_m148 = *(uint64_t *)(result + 0x18);
    *(uint64_t *)(result + 0x30) = 1;
    result = MiInsertClone(Arg1, result, 1, Arg4);
    local_rbx = 0;
    goto loc_0022DDF6;
loc_0022DDF0:
loc_0022DDF6:
    if (*(uint64_t *)(*(uint64_t *)(arg2 + 0x558)) != 0) goto loc_0022DDF0;
    if (*(uint64_t *)(arg2 + 0x558) == 0) goto loc_0022E001;
loc_0022DE15:
    v_stack_m1F0 = *(uint64_t *)(arg2 + 0x558);
    if (*(uint64_t *)(*(uint64_t *)(arg2 + 0x558) + 0x8) == 0) goto loc_0022DE4C;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x558) + 0x8)) == 0) goto loc_0022DE56;
loc_0022DE34:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x558) + 0x8))) != 0) goto loc_0022DE34;
    goto loc_0022DE56;
loc_0022DE44:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x558) + 0x8)))) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x558) + 0x8))))) goto loc_0022DE56;
loc_0022DE4C:
    local_rbx = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x558) + 0x8)) + 0x10)) & (-4);
    if (condition_is_not_equal) goto loc_0022DE44;
loc_0022DE56:
    local_rdi = (*(uint8_t *)(*(uint64_t *)(arg2 + 0x558) + 0x20)) << (32);
    local_rdi = (local_rdi) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x558) + 0x18)));
    local_rdi = (local_rdi) << (12);
    result = MiLocateAddress(local_rdi, result, 1, Arg4);
    Arg3 = (*(uint8_t *)(*(uint64_t *)(arg2 + 0x558) + 0x22)) << (32);
    v_stack_m150 = result;
    Arg3 = (Arg3) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x558) + 0x34)));
    if (Arg3 >= result) goto loc_0022DFEA;
    result = MiIsVadLargePrivate(*(uint64_t *)(arg2 + 0x558), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x558) + 0x34)), Arg3, result);
    if ((uint32_t)(result) != 0) goto loc_0022DFEA;
    local_rdi = (local_rdi) >> (9);
    local_rdi = (local_rdi) & (result);
    v_stack_m1A0 = result;
    v_stack_m198 = *(uint64_t *)(arg2 + 0x558);
    local_rdi = (local_rdi) + (result);
    Arg1 = (*(uint8_t *)(*(uint64_t *)(arg2 + 0x558) + 0x21)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x558) + 0x1C)));
    Arg1 = (Arg1) & ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x558) + 0x1C)));
    v_stack_m1F8 = result + Arg1 * 8;
loc_0022DEF4:
    if (v_stack_m160 != 0) goto loc_0022E05E;
loc_0022DF01:
    v_stack_m218 = v_stack_m158;
    result = MiGetNextPageTable(local_rdi, result + Arg1 * 8, v_stack_m1AC, 4);
    result = MiUnlockWorkingSetExclusive(Arg1 + 1024, v_stack_m1AC, v_stack_m1AC, 4);
    if (result == 0) goto loc_0022E055;
    result = MiUpdateForkMaps(v_stack_m128, result, v_stack_m170, Arg1);
loc_0022DF4C:
    v_stack_m178 = v_stack_mE8;
    result = MiLockWorkingSetExclusive(Arg1 + 1024, result, v_stack_m170, Arg1);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m1F0 + 0x30))) & (112));
    if (((uint8_t)(result)) == 80) goto loc_0022DFCE;
    if (result > (result + Arg1 * 8)) goto loc_0022E265;
    local_r15 = (result) & (0xFFFFFFFFFFFFF000ULL);
    local_r15 = (local_r15) + (0xFF8ULL);
    v_stack_m188 = v_stack_m100;
    v_stack_m190 = result;
    if (local_r15 > v_stack_m1F8) { local_r15 = v_stack_m1F8; }
    Arg2 = 0;
    result = MiMakeSystemAddressValid(result, Arg2, v_stack_m1AC, 1);
loc_0022DFB1:
    result = MiBuildForkPte(v_stack_m1C8, Arg2, v_stack_m1AC, 1);
    if (v_stack_m190 <= local_r15) goto loc_0022DFB1;
loc_0022DFCE:
    if (v_stack_m190 <= v_stack_m1F8) goto loc_0022DEF4;
loc_0022DFD7:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m1F0 + 0x30))) & ((uint32_t)((uint32_t)(0x600000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x600000ULL)))) goto loc_0022E26A;
loc_0022DFEA:
    if (local_rbx != 0) goto loc_0022DE15;
loc_0022E001:
    if (v_stack_m168 != 0) goto loc_0022E2A3;
loc_0022E00B:
    if (v_stack_m160 != 0) goto loc_0022E2B2;
loc_0022E018:
    local_r15 = (v_stack_m180) - (v_stack_m148);
    local_r15 = (local_r15) >> (5);
    v_stack_m170 = *(uint64_t *)(v_stack_m1D8 + 0x288);
    if (local_r15 != 0) goto loc_0022E072;
    result = RtlAvlRemoveNode(Arg1 + 640, v_stack_m1E0, v_stack_m1AC, 1);
    goto loc_0022E07D;
loc_0022E055:
    goto loc_0022DF4C;
loc_0022E05E:
    result = MiFlushTbList(Arg1 + 640, v_stack_m1E0, v_stack_m1AC, 1);
    result = MiReleaseProcessorFlushList(Arg1 + 640, v_stack_m1E0, v_stack_m1AC, 1);
    goto loc_0022DF01;
loc_0022E072:
    *(uint64_t *)(arg1 + 0x280) = local_r15;
    *(uint64_t *)(v_stack_m1E0 + 0x30) = local_r15;
    *(uint64_t *)(v_stack_m1E0 + 0x28) = local_r15;
loc_0022E07D:
    result = MiDeleteCloneZombies(Arg1, 1, v_stack_m1AC, 1);
    local_rdi = 0;
    goto loc_0022E09B;
loc_0022E095:
loc_0022E09B:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x280)) != 0) goto loc_0022E095;
    if (*(uint64_t *)(arg1 + 0x280) == 0) goto loc_0022E163;
loc_0022E0B3:
    Arg3 = 0;
    local_r14 = (v_stack_m200) + (*(uint64_t *)(result + 0x40));
    local_r13 = (v_stack_m1E8) + (*(uint64_t *)(*(uint64_t *)(arg1 + 0x280) + 0x40));
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(result + 0x10) = v_xmm1;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    *(uint64_t *)(result + 0x30) = v_xmm1;
    *(uint64_t *)(result + 0x40) = v_xmm0;
    *(uint64_t *)(result + 0x50) = v_xmm1;
    *(uint64_t *)(result + 0x60) = v_xmm0;
    result = MiInsertClone(v_stack_m1D8, result, Arg3, 1);
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x280) + 0x8) == 0) goto loc_0022E13D;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x280) + 0x8)) == 0) goto loc_0022E147;
loc_0022E125:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x280) + 0x8))) != 0) goto loc_0022E125;
    goto loc_0022E147;
loc_0022E135:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x280) + 0x8)))) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x280) + 0x8))))) goto loc_0022E147;
loc_0022E13D:
    local_rdi = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x280) + 0x8)) + 0x10)) & (-4);
    if (condition_is_not_equal) goto loc_0022E135;
loc_0022E147:
    if (local_rdi != 0) goto loc_0022E0B3;
    v_stack_m1E8 = local_r13;
    v_stack_m200 = local_r14;
loc_0022E163:
    local_rdi = 0;
    result = MiUnlockWorkingSetExclusive(v_stack_m138 + 1024, v_stack_m1AC, Arg3, 1);
    result = MiFreeForkMaps(v_stack_m128, v_stack_m1AC, Arg3, 1);
loc_0022E180:
    result = MiLockAweVadsExclusive(v_stack_m208, v_stack_m1AC, Arg3, 1);
    result = MiLockWorkingSetExclusive(v_stack_m138 + 1024, v_stack_m1AC, Arg3, 1);
    result = MiUnlockWorkingSetExclusive(v_stack_m138 + 1024, v_stack_m1AC, Arg3, 1);
    result = MiUnlockAweVadsExclusive(v_stack_m208, v_stack_m1AC, Arg3, 1);
    result = MiFreeForkMappingPte(v_stack_m128, v_stack_m1AC, Arg3, 1);
    if (*(uint64_t *)(result) != 0) goto loc_0022E2C6;
    if (v_stack_m200 > v_stack_m1E8) goto loc_0022E2D0;
loc_0022E1D4:
    if (v_stack_m1A8 != 0) goto loc_0022E2E3;
loc_0022E1E1:
    if (local_r15 != 0) goto loc_0022E2F0;
loc_0022E1EA:
    result = MiFreeCloneDescriptor(v_stack_m138, v_stack_m1E0, Arg3, 1);
loc_0022E1F5:
loc_0022E1F7:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m1E0, Arg3, 1);
    local_rsp = (local_rsp) + (504);
    return result;
loc_0022E21B:
    result = MiUnlockWorkingSetExclusive(0, (uint8_t)(result), Arg3, 1);
    result = MiUnlockAweVadsExclusive(v_stack_p30, (uint8_t)(result), Arg3, 1);
    result = MiFreeCloneDescriptor(v_stack_m138, v_stack_m1E0, Arg3, 1);
    result = PsReturnProcessNonPagedPoolQuota(v_stack_m1D8, v_stack_m138 + 1024, Arg3, 1);
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(result), Arg2, Arg3, 1);
    goto loc_0022DCC7;
loc_0022E254:
    goto loc_0022E180;
loc_0022E265:
    goto loc_0022DFD7;
loc_0022E26A:
    result = MiLocateLockedVadEvent(v_stack_m150, 4, Arg3, 1);
    result = MiLocateLockedVadEvent(v_stack_m1F0, 4, Arg3, result);
    Arg3 = (*(uint64_t *)(result + 0x10)) + (7);
    Arg3 = (Arg3) >> (3);
    result = memcpy(*(uint64_t *)(result + 0x18), *(uint64_t *)(result + 0x18), Arg3, result);
    goto loc_0022DFEA;
loc_0022E2A3:
    *(uint32_t *)(v_stack_m140) = 1;
    goto loc_0022E00B;
loc_0022E2B2:
    result = MiFlushTbList(*(uint64_t *)(result + 0x18), *(uint64_t *)(result + 0x18), Arg3, result);
    result = MiReleaseProcessorFlushList(*(uint64_t *)(result + 0x18), *(uint64_t *)(result + 0x18), Arg3, result);
    goto loc_0022E018;
loc_0022E2C6:
loc_0022E2D0:
    result = (result) - (*(uint64_t *)(result + 0x18));
    result = PsReturnProcessNonPagedPoolQuota(v_stack_p38, result, Arg3, result);
    goto loc_0022E1D4;
loc_0022E2E3:
    result = MiReturnFullProcessCommitment(v_stack_p38, result, Arg3, result);
    goto loc_0022E1E1;
loc_0022E2F0:
    if (!sign_flag) goto loc_0022E1F5;
    goto loc_0022E1EA;
loc_0022E2FD:
    result = PsReturnProcessNonPagedPoolQuota(v_stack_p38, v_stack_m138 + 1024, Arg3, result);
    goto loc_0022E1EA;
loc_0022E312:
    goto loc_0022E1EA;
loc_0022E319:
    goto loc_0022E1F7;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x270` | `64` | `W` |
| `Arg1` | `+ 0x280` | `64` | `R` |
| `Arg1` | `+ 0x288` | `64` | `R` |
| `Arg1` | `+ 0x400` | `64` | `R` |
| `Arg1` | `+ 0x410` | `64` | `R` |
| `Arg2` | `+ 0x558` | `64` | `R` |
| `Arg6` | `+ 0x0` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0022DC1C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
