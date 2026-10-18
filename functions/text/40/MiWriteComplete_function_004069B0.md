# MiWriteComplete

- RVA: `0x004069B0`–`0x00406FF8` (길이 `1,608` bytes)
- VA: `0x00000001404069B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0009A8CC`
- 디코드: `394`개 명령, `1,608/1,608` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **29**; 고유 호출 대상: **28**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00406ADA` → [MiClearPageFileReservation](../32/MiClearPageFileReservation_function_0032B68C.md) (function, `0x0032B68C`)
- `0x00406B0F` → [MiLockPageInline](../31/MiLockPageInline_function_0031A340.md) (function, `0x0031A340`)
- `0x00406B46` → [MiStoreModifiedWriteCompletePfn](../36/MiStoreModifiedWriteCompletePfn_function_00362850.md) (function, `0x00362850`)
- `0x00406B57` → [MiWriteCompletePfn](../37/MiWriteCompletePfn_function_003737C4.md) (function, `0x003737C4`)
- `0x00406B66` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x00406BC1` → [MiDecrementModifiedWriteCount](../29/MiDecrementModifiedWriteCount_function_00298184.md) (function, `0x00298184`)
- `0x00406BFF` → [MiFreeModWriterEntry](MiFreeModWriterEntry_function_00407AE8.md) (function, `0x00407AE8`)
- `0x00406CAC` → [MmIsWriteErrorFatal](MmIsWriteErrorFatal_function_00408688.md) (function, `0x00408688`)
- `0x00406CF9` → [MiSetStoreVirtualPagefileValue](../37/MiSetStoreVirtualPagefileValue_function_00373B80.md) (function, `0x00373B80`)
- `0x00406D14` → [MiMakePagefileWriterEntryAvailable](../47/MiMakePagefileWriterEntryAvailable_function_0047EE78.md) (function, `0x0047EE78`)
- `0x00406D35` → [MiStoreDecrementOutstandingWrites](../48/MiStoreDecrementOutstandingWrites_function_0048EF68.md) (function, `0x0048EF68`)
- `0x00406D4A` → [MiStoreCheckCompleteWriteBatch](../47/MiStoreCheckCompleteWriteBatch_function_0047EC80.md) (function, `0x0047EC80`)
- `0x00406D5B` → [MiIsRetryIoStatus](MiIsRetryIoStatus_function_00408640.md) (function, `0x00408640`)
- `0x00406D9D` → [MiTransferSoftwarePte](../38/MiTransferSoftwarePte_function_003821F0.md) (function, `0x003821F0`)
- `0x00406DE3` → [MI_PAGEFILE_WRITE](../47/MI_PAGEFILE_WRITE_function_004749F4.md) (function, `0x004749F4`)
- `0x00406E18` → [MiReturnResident](../28/MiReturnResident_function_00286890.md) (function, `0x00286890`)
- `0x00406E28` → [MiReleaseWriteInProgressCharges](MiReleaseWriteInProgressCharges_function_00407B4C.md) (function, `0x00407B4C`)
- `0x00406E35` → [MiRetardMdl](MiRetardMdl_function_0040494C.md) (function, `0x0040494C`)
- `0x00406E46` → [MmUnmapLockedPages](../24/MmUnmapLockedPages_function_00246E60.md) (function, `0x00246E60`)
- `0x00406E99` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00406EA7` → [MiSetDeleteOnClose](../4D/MiSetDeleteOnClose_function_004DD8E8.md) (function, `0x004DD8E8`)
- `0x00406EFB` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)
- `0x00406F1D` → [MiNotifyUserOfLostData](../67/MiNotifyUserOfLostData_function_00678280.md) (function, `0x00678280`)
- `0x00406F2A` → [MiReleaseControlAreaWaiters](../28/MiReleaseControlAreaWaiters_function_002865F0.md) (function, `0x002865F0`)
- `0x00406F36` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00406F4F` → [MiLockPartitionMappedWriter](MiLockPartitionMappedWriter_function_00403150.md) (function, `0x00403150`)
- `0x00406F82` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x00406FCB` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x00406FEE` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)

### Direct callers
- [MiGatherPagefilePages](../37/MiGatherPagefilePages_function_00372B08.md) at `0x0037335C`
- [MiGatherMappedPages](MiGatherMappedPages_function_00404E80.md) at `0x00405179`
- [MiGatherMappedPages](MiGatherMappedPages_function_00404E80.md) at `0x004052D6`
- [MiStoreWriteModifiedCompleteApc](MiStoreWriteModifiedCompleteApc_function_00406990.md) at `0x0040699E`
- [sub_006E3DF6](../6E/Unknown_function_006E3DF6.md) at `0x006E3E79`

### Static image references
- `0x00406AE6` → RVA `0x00E37478` (`.data`; read)
- `0x00406CE9` → RVA `0x00010880` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00406F36` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **12**
  - `0x00406D84` → [sub_006EC582 + 0x10B](../6E/Unknown_function_006EC582.md) (`tail-transfer`)
  - `0x00406E5C` → [sub_006EC582](../6E/Unknown_function_006EC582.md) (`tail-transfer`)
  - `0x00406E66` → [sub_006EC582 + 0x17](../6E/Unknown_function_006EC582.md) (`tail-transfer`)
  - `0x00406E82` → [sub_006EC582 + 0x4E](../6E/Unknown_function_006EC582.md) (`tail-transfer`)
  - `0x00406F62` → [sub_006EC582 + 0x90](../6E/Unknown_function_006EC582.md) (`tail-transfer`)
  - `0x00406F8D` → [sub_006EC582 + 0xF9](../6E/Unknown_function_006EC582.md) (`tail-transfer`)
  - `0x00406F97` → [sub_006EC582 + 0xD0](../6E/Unknown_function_006EC582.md) (`tail-transfer`)
  - `0x00406FA0` → [sub_006EC582 + 0xF9](../6E/Unknown_function_006EC582.md) (`tail-transfer`)
  - `0x00406FAA` → [sub_006EC582 + 0xDB](../6E/Unknown_function_006EC582.md) (`tail-transfer`)
  - `0x00406FB6` → [sub_006EC582 + 0x10B](../6E/Unknown_function_006EC582.md) (`tail-transfer`)
  - `0x00406FD6` → [sub_006EC582 + 0xE0](../6E/Unknown_function_006EC582.md) (`tail-transfer`)
  - `0x00406FE1` → [sub_006EC582 + 0xF9](../6E/Unknown_function_006EC582.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
004069B0  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
004069B5  55                              push rbp
004069B6  53                              push rbx
004069B7  56                              push rsi
004069B8  57                              push rdi
004069B9  41 54                           push r12
004069BB  41 55                           push r13
004069BD  41 56                           push r14
004069BF  41 57                           push r15
004069C1  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
004069C6  48 81 EC 88 00 00 00            sub rsp, 0x88
004069CD  48 8B 71 60                     mov rsi, qword ptr [rcx + 0x60]
004069D1  33 FF                           xor edi, edi
004069D3  21 7D 6F                        and dword ptr [rbp + 0x6f], edi
004069D6  4C 8B EA                        mov r13, rdx
004069D9  8B 41 2C                        mov eax, dword ptr [rcx + 0x2c]
004069DC  4C 8B F9                        mov r15, rcx
004069DF  4C 8B 71 38                     mov r14, qword ptr [rcx + 0x38]
004069E3  66 0F BA 66 0A 09               bt word ptr [rsi + 0xa], 9
004069E9  89 45 7F                        mov dword ptr [rbp + 0x7f], eax
004069EC  0F 82 40 04 00 00               jb 0x140406e32
004069F2  F6 46 0A 01                     test byte ptr [rsi + 0xa], 1
004069F6  0F 85 43 04 00 00               jne 0x140406e3f
004069FC  4D 63 6D 00                     movsxd r13, dword ptr [r13]
00406A00  41 8B 47 28                     mov eax, dword ptr [r15 + 0x28]
00406A04  44 89 6D EF                     mov dword ptr [rbp - 0x11], r13d
00406A08  A8 20                           test al, 0x20
00406A0A  0F 85 97 03 00 00               jne 0x140406da7
00406A10  49 8B 57 48                     mov rdx, qword ptr [r15 + 0x48]
00406A14  BB 80 00 00 00                  mov ebx, 0x80
00406A19  4D 8B 67 50                     mov r12, qword ptr [r15 + 0x50]
00406A1D  45 33 C9                        xor r9d, r9d
00406A20  48 89 55 C7                     mov qword ptr [rbp - 0x39], rdx
00406A24  89 5D 6F                        mov dword ptr [rbp + 0x6f], ebx
00406A27  4C 89 4D D7                     mov qword ptr [rbp - 0x29], r9
00406A2B  44 8B 55 7F                     mov r10d, dword ptr [rbp + 0x7f]
00406A2F  4C 8D 46 30                     lea r8, [rsi + 0x30]
00406A33  41 F7 C2 FF 0F 00 00            test r10d, 0xfff
00406A3A  4C 89 45 E7                     mov qword ptr [rbp - 0x19], r8
00406A3E  41 8B C9                        mov ecx, r9d
00406A41  41 8B C2                        mov eax, r10d
00406A44  0F 95 C1                        setne cl
00406A47  C1 F8 0C                        sar eax, 0xc
00406A4A  03 C1                           add eax, ecx
00406A4C  48 98                           cdqe
00406A4E  49 8D 04 C0                     lea rax, [r8 + rax*8]
00406A52  48 89 45 F7                     mov qword ptr [rbp - 9], rax
00406A56  4D 85 E4                        test r12, r12
00406A59  0F 85 F1 03 00 00               jne 0x140406e50
00406A5F  45 85 ED                        test r13d, r13d
00406A62  0F 88 2A 02 00 00               js 0x140406c92
00406A68  4C 8B 65 C7                     mov r12, qword ptr [rbp - 0x39]
00406A6C  4C 89 4D DF                     mov qword ptr [rbp - 0x21], r9
00406A70  85 FF                           test edi, edi
00406A72  0F 85 27 04 00 00               jne 0x140406e9f
00406A78  49 8B 57 58                     mov rdx, qword ptr [r15 + 0x58]
00406A7C  8B CF                           mov ecx, edi
00406A7E  41 8B 47 28                     mov eax, dword ptr [r15 + 0x28]
00406A82  4C 8B 55 D7                     mov r10, qword ptr [rbp - 0x29]
00406A86  48 C1 EA 0C                     shr rdx, 0xc
00406A8A  48 89 55 07                     mov qword ptr [rbp + 7], rdx
00406A8E  4C 89 4D CF                     mov qword ptr [rbp - 0x31], r9
00406A92  4C 89 4D FF                     mov qword ptr [rbp - 1], r9
00406A96  A8 20                           test al, 0x20
00406A98  0F 85 16 04 00 00               jne 0x140406eb4
00406A9E  48 8B 45 F7                     mov rax, qword ptr [rbp - 9]
00406AA2  49 8B F1                        mov rsi, r9
00406AA5  48 39 45 E7                     cmp qword ptr [rbp - 0x19], rax
00406AA9  0F 83 E9 00 00 00               jae 0x140406b98
00406AAF  4C 8B 6D E7                     mov r13, qword ptr [rbp - 0x19]
00406AB3  45 8B E1                        mov r12d, r9d
00406AB6  41 8B 47 28                     mov eax, dword ptr [r15 + 0x28]
00406ABA  A8 20                           test al, 0x20
00406ABC  74 24                           je 0x140406ae2
00406ABE  A8 40                           test al, 0x40
00406AC0  0F 84 15 02 00 00               je 0x140406cdb
00406AC6  49 8B 47 48                     mov rax, qword ptr [r15 + 0x48]
00406ACA  41 8B CC                        mov ecx, r12d
00406ACD  48 8B 4C C8 60                  mov rcx, qword ptr [rax + rcx*8 + 0x60]
00406AD2  48 89 4D CF                     mov qword ptr [rbp - 0x31], rcx
00406AD6  48 8D 4D CF                     lea rcx, [rbp - 0x31]
00406ADA  E8 AD 4B F2 FF                  call 0x14032b68c
00406ADF  45 33 C9                        xor r9d, r9d
00406AE2  49 8B 45 00                     mov rax, qword ptr [r13]
00406AE6  48 3B 05 8B 09 A3 00            cmp rax, qword ptr [rip + 0xa3098b]
00406AED  0F 84 E2 03 00 00               je 0x140406ed5
00406AF3  48 8D 34 40                     lea rsi, [rax + rax*2]
00406AF7  48 C1 E6 04                     shl rsi, 4
00406AFB  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00406B05  48 03 F0                        add rsi, rax
00406B08  48 8B CE                        mov rcx, rsi
00406B0B  48 89 75 E7                     mov qword ptr [rbp - 0x19], rsi
00406B0F  E8 2C 38 F1 FF                  call 0x14031a340
00406B14  88 45 67                        mov byte ptr [rbp + 0x67], al
00406B17  F6 C3 01                        test bl, 1
00406B1A  75 11                           jne 0x140406b2d
00406B1C  84 DB                           test bl, bl
00406B1E  78 0D                           js 0x140406b2d
00406B20  F6 46 22 10                     test byte ptr [rsi + 0x22], 0x10
00406B24  0F 85 C0 03 00 00               jne 0x140406eea
00406B2A  83 E3 FD                        and ebx, 0xfffffffd
00406B2D  41 8B 47 28                     mov eax, dword ptr [r15 + 0x28]
00406B31  83 E3 F3                        and ebx, 0xfffffff3
00406B34  89 5D 6F                        mov dword ptr [rbp + 0x6f], ebx
00406B37  A8 40                           test al, 0x40
00406B39  0F 84 1A 01 00 00               je 0x140406c59
00406B3F  48 8D 55 6F                     lea rdx, [rbp + 0x6f]
00406B43  48 8B CE                        mov rcx, rsi
00406B46  E8 05 BD F5 FF                  call 0x140362850
00406B4B  8B 5D 6F                        mov ebx, dword ptr [rbp + 0x6f]
00406B4E  4C 8B 45 FF                     mov r8, qword ptr [rbp - 1]
00406B52  8B D3                           mov edx, ebx
00406B54  48 8B CE                        mov rcx, rsi
00406B57  E8 68 CC F6 FF                  call 0x1403737c4
00406B5C  8A 55 67                        mov dl, byte ptr [rbp + 0x67]
00406B5F  48 8B F0                        mov rsi, rax
00406B62  48 8B 4D E7                     mov rcx, qword ptr [rbp - 0x19]
00406B66  E8 75 38 F1 FF                  call 0x14031a3e0
00406B6B  45 33 C9                        xor r9d, r9d
00406B6E  48 85 F6                        test rsi, rsi
00406B71  0F 85 7B 03 00 00               jne 0x140406ef2
00406B77  48 8B 55 07                     mov rdx, qword ptr [rbp + 7]
00406B7B  49 83 C5 08                     add r13, 8
00406B7F  4C 8B 55 D7                     mov r10, qword ptr [rbp - 0x29]
00406B83  41 FF C4                        inc r12d
00406B86  4C 3B 6D F7                     cmp r13, qword ptr [rbp - 9]
00406B8A  0F 82 26 FF FF FF               jb 0x140406ab6
00406B90  44 8B 6D EF                     mov r13d, dword ptr [rbp - 0x11]
00406B94  4C 8B 65 C7                     mov r12, qword ptr [rbp - 0x39]
00406B98  41 8B 47 30                     mov eax, dword ptr [r15 + 0x30]
00406B9C  33 F6                           xor esi, esi
00406B9E  85 C0                           test eax, eax
00406BA0  0F 85 64 02 00 00               jne 0x140406e0a
00406BA6  41 8B 47 28                     mov eax, dword ptr [r15 + 0x28]
00406BAA  A8 20                           test al, 0x20
00406BAC  0F 85 55 01 00 00               jne 0x140406d07
00406BB2  40 F6 C7 01                     test dil, 1
00406BB6  0F 85 5B 03 00 00               jne 0x140406f17
00406BBC  33 D2                           xor edx, edx
00406BBE  49 8B CC                        mov rcx, r12
00406BC1  E8 BE 15 E9 FF                  call 0x140298184
00406BC6  48 85 C0                        test rax, rax
00406BC9  0F 85 58 03 00 00               jne 0x140406f27
00406BCF  F0 41 FF 8E A0 02 00 00         lock dec dword ptr [r14 + 0x2a0]
00406BD7  49 8D 47 68                     lea rax, [r15 + 0x68]
00406BDB  49 8B 4F 60                     mov rcx, qword ptr [r15 + 0x60]
00406BDF  48 3B C8                        cmp rcx, rax
00406BE2  0F 85 4C 03 00 00               jne 0x140406f34
00406BE8  41 8B 47 28                     mov eax, dword ptr [r15 + 0x28]
00406BEC  A8 01                           test al, 1
00406BEE  0F 85 4C 03 00 00               jne 0x140406f40
00406BF4  BA 01 00 00 00                  mov edx, 1
00406BF9  49 89 37                        mov qword ptr [r15], rsi
00406BFC  49 8B CF                        mov rcx, r15
00406BFF  E8 E4 0E 00 00                  call 0x140407ae8
00406C04  48 8B 45 D7                     mov rax, qword ptr [rbp - 0x29]
00406C08  48 F7 D8                        neg rax
00406C0B  48 1B DB                        sbb rbx, rbx
00406C0E  48 83 E3 FD                     and rbx, 0xfffffffffffffffd
00406C12  48 81 C3 1B 04 00 00            add rbx, 0x41b
00406C19  49 03 DE                        add rbx, r14
00406C1C  45 85 ED                        test r13d, r13d
00406C1F  0F 88 2F 01 00 00               js 0x140406d54
00406C25  4D 85 E4                        test r12, r12
00406C28  0F 85 41 03 00 00               jne 0x140406f6f
00406C2E  40 38 33                        cmp byte ptr [rbx], sil
00406C31  0F 85 44 03 00 00               jne 0x140406f7b
00406C37  48 8B 45 DF                     mov rax, qword ptr [rbp - 0x21]
00406C3B  48 85 C0                        test rax, rax
00406C3E  0F 85 A2 03 00 00               jne 0x140406fe6
00406C44  48 81 C4 88 00 00 00            add rsp, 0x88
00406C4B  41 5F                           pop r15
00406C4D  41 5E                           pop r14
00406C4F  41 5D                           pop r13
00406C51  41 5C                           pop r12
00406C53  5F                              pop rdi
00406C54  5E                              pop rsi
00406C55  5B                              pop rbx
00406C56  5D                              pop rbp
00406C57  C3                              ret
00406C58  CC                              int3
00406C59  40 F6 C7 02                     test dil, 2
00406C5D  0F 84 EB FE FF FF               je 0x140406b4e
00406C63  F6 C3 02                        test bl, 2
00406C66  0F 85 E2 FE FF FF               jne 0x140406b4e
00406C6C  F6 C3 01                        test bl, 1
00406C6F  0F 85 D9 FE FF FF               jne 0x140406b4e
00406C75  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
00406C79  48 0F BA E0 3E                  bt rax, 0x3e
00406C7E  0F 82 C7 FE FF FF               jb 0x140406b4b
00406C84  8B 5D 6F                        mov ebx, dword ptr [rbp + 0x6f]
00406C87  83 CB 08                        or ebx, 8
00406C8A  89 5D 6F                        mov dword ptr [rbp + 0x6f], ebx
00406C8D  E9 BC FE FF FF                  jmp 0x140406b4e
00406C92  45 8B 67 28                     mov r12d, dword ptr [r15 + 0x28]
00406C96  41 8B C9                        mov ecx, r9d
00406C99  41 D1 EC                        shr r12d, 1
00406C9C  45 8B C5                        mov r8d, r13d
00406C9F  41 83 E4 01                     and r12d, 1
00406CA3  48 85 D2                        test rdx, rdx
00406CA6  41 8B D4                        mov edx, r12d
00406CA9  0F 95 C1                        setne cl
00406CAC  E8 D7 19 00 00                  call 0x140408688
00406CB1  45 33 C9                        xor r9d, r9d
00406CB4  85 C0                           test eax, eax
00406CB6  0F 85 BF 01 00 00               jne 0x140406e7b
00406CBC  4C 8B 65 C7                     mov r12, qword ptr [rbp - 0x39]
00406CC0  83 CB 01                        or ebx, 1
00406CC3  89 5D 6F                        mov dword ptr [rbp + 0x6f], ebx
00406CC6  4D 85 E4                        test r12, r12
00406CC9  0F 84 9C 01 00 00               je 0x140406e6b
00406CCF  45 89 AE D8 02 00 00            mov dword ptr [r14 + 0x2d8], r13d
00406CD6  E9 8D FD FF FF                  jmp 0x140406a68
00406CDB  41 F6 82 AC 00 00 00 40         test byte ptr [r10 + 0xac], 0x40
00406CE3  0F 84 A0 00 00 00               je 0x140406d89
00406CE9  48 8B 15 90 9B C0 FF            mov rdx, qword ptr [rip - 0x3f6470]
00406CF0  41 B8 04 00 00 00               mov r8d, 4
00406CF6  49 8B CE                        mov rcx, r14
00406CF9  E8 82 CE F6 FF                  call 0x140373b80
00406CFE  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
00406D02  E9 D8 FD FF FF                  jmp 0x140406adf
00406D07  24 1C                           and al, 0x1c
00406D09  3C 08                           cmp al, 8
00406D0B  0F 82 FA 01 00 00               jb 0x140406f0b
00406D11  49 8B CF                        mov rcx, r15
00406D14  E8 5F 81 07 00                  call 0x14047ee78
00406D19  41 38 B6 D1 02 00 00            cmp byte ptr [r14 + 0x2d1], sil
00406D20  0F 85 D4 00 00 00               jne 0x140406dfa
00406D26  41 8B 47 28                     mov eax, dword ptr [r15 + 0x28]
00406D2A  A8 40                           test al, 0x40
00406D2C  0F 84 D2 FE FF FF               je 0x140406c04
00406D32  49 8B CE                        mov rcx, r14
00406D35  E8 2E 82 08 00                  call 0x14048ef68
00406D3A  41 38 B6 D2 02 00 00            cmp byte ptr [r14 + 0x2d2], sil
00406D41  0F 85 BD FE FF FF               jne 0x140406c04
00406D47  49 8B CE                        mov rcx, r14
00406D4A  E8 31 7F 07 00                  call 0x14047ec80
00406D4F  E9 B0 FE FF FF                  jmp 0x140406c04
00406D54  48 63 55 7F                     movsxd rdx, dword ptr [rbp + 0x7f]
00406D58  41 8B CD                        mov ecx, r13d
00406D5B  E8 E0 18 00 00                  call 0x140408640
00406D60  39 75 77                        cmp dword ptr [rbp + 0x77], esi
00406D63  0F 84 46 02 00 00               je 0x140406faf
00406D69  4D 85 E4                        test r12, r12
00406D6C  0F 84 C5 FE FF FF               je 0x140406c37
00406D72  40 F6 C7 01                     test dil, 1
00406D76  0F 85 BB FE FF FF               jne 0x140406c37
00406D7C  85 C0                           test eax, eax
00406D7E  0F 85 B3 FE FF FF               jne 0x140406c37
00406D84  E9 04 59 2E 00                  jmp 0x1406ec68d
00406D89  48 8B 0D F0 9A C0 FF            mov rcx, qword ptr [rip - 0x3f6510]
00406D90  46 8D 04 22                     lea r8d, [rdx + r12]
00406D94  49 8B D2                        mov rdx, r10
00406D97  41 B9 01 00 00 00               mov r9d, 1
00406D9D  E8 4E B4 F7 FF                  call 0x1403821f0
00406DA2  E9 57 FF FF FF                  jmp 0x140406cfe
00406DA7  49 8B 47 40                     mov rax, qword ptr [r15 + 0x40]
00406DAB  49 B8 B0 03 00 00 80 F7 FF FF   movabs r8, 0xfffff780000003b0
00406DB5  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
00406DB9  49 B9 08 00 00 00 80 F7 FF FF   movabs r9, 0xfffff78000000008
00406DC3  49 8B 08                        mov rcx, qword ptr [r8]
00406DC6  49 8B 11                        mov rdx, qword ptr [r9]
00406DC9  49 8B 00                        mov rax, qword ptr [r8]
00406DCC  48 3B C8                        cmp rcx, rax
00406DCF  75 F2                           jne 0x140406dc3
00406DD1  45 33 C9                        xor r9d, r9d
00406DD4  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
00406DD9  48 2B D1                        sub rdx, rcx
00406DDC  49 8B CF                        mov rcx, r15
00406DDF  45 8D 41 05                     lea r8d, [r9 + 5]
00406DE3  E8 0C DC 06 00                  call 0x1404749f4
00406DE8  8B 5D 6F                        mov ebx, dword ptr [rbp + 0x6f]
00406DEB  45 8B E1                        mov r12d, r9d
00406DEE  4C 89 4D C7                     mov qword ptr [rbp - 0x39], r9
00406DF2  48 8B D7                        mov rdx, rdi
00406DF5  E9 31 FC FF FF                  jmp 0x140406a2b
00406DFA  49 8D 86 C8 03 00 00            lea rax, [r14 + 0x3c8]
00406E01  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
00406E05  E9 1C FF FF FF                  jmp 0x140406d26
00406E0A  48 8B D0                        mov rdx, rax
00406E0D  49 8B CE                        mov rcx, r14
00406E10  41 8B 47 28                     mov eax, dword ptr [r15 + 0x28]
00406E14  A8 20                           test al, 0x20
00406E16  74 0A                           je 0x140406e22
00406E18  E8 73 FA E7 FF                  call 0x140286890
00406E1D  E9 84 FD FF FF                  jmp 0x140406ba6
00406E22  41 B8 01 00 00 00               mov r8d, 1
00406E28  E8 1F 0D 00 00                  call 0x140407b4c
00406E2D  E9 74 FD FF FF                  jmp 0x140406ba6
00406E32  48 8B CE                        mov rcx, rsi
00406E35  E8 12 DB FF FF                  call 0x14040494c
00406E3A  E9 B3 FB FF FF                  jmp 0x1404069f2
00406E3F  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
00406E43  48 8B D6                        mov rdx, rsi
00406E46  E8 15 00 E4 FF                  call 0x140246e60
00406E4B  E9 AC FB FF FF                  jmp 0x1404069fc
00406E50  49 8B 47 40                     mov rax, qword ptr [r15 + 0x40]
00406E54  48 89 45 67                     mov qword ptr [rbp + 0x67], rax
00406E58  41 F6 C4 01                     test r12b, 1
00406E5C  0F 84 20 57 2E 00               je 0x1406ec582
00406E62  49 83 E4 FE                     and r12, 0xfffffffffffffffe
00406E66  E9 2E 57 2E 00                  jmp 0x1406ec599
00406E6B  45 89 AE D4 02 00 00            mov dword ptr [r14 + 0x2d4], r13d
00406E72  4C 89 4D DF                     mov qword ptr [rbp - 0x21], r9
00406E76  E9 FD FB FF FF                  jmp 0x140406a78
00406E7B  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
00406E7F  48 85 C0                        test rax, rax
00406E82  0F 85 48 57 2E 00               jne 0x1406ec5d0
00406E88  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00406E8D  8D 50 20                        lea edx, [rax + 0x20]
00406E90  4C 8B CE                        mov r9, rsi
00406E93  8D 48 7A                        lea ecx, [rax + 0x7a]
00406E96  4D 8B C5                        mov r8, r13
00406E99  E8 C2 67 0F 00                  call 0x1404fd660
00406E9E  CC                              int3
00406E9F  BA 01 00 00 00                  mov edx, 1
00406EA4  49 8B CC                        mov rcx, r12
00406EA7  E8 3C 6A 0D 00                  call 0x1404dd8e8
00406EAC  45 33 C9                        xor r9d, r9d
00406EAF  E9 C4 FB FF FF                  jmp 0x140406a78
00406EB4  83 CF 02                        or edi, 2
00406EB7  48 8D 45 CF                     lea rax, [rbp - 0x31]
00406EBB  41 B8 00 08 00 00               mov r8d, 0x800
00406EC1  48 89 45 FF                     mov qword ptr [rbp - 1], rax
00406EC5  66 45 85 82 AC 00 00 00         test word ptr [r10 + 0xac], r8w
00406ECD  0F 44 F9                        cmove edi, ecx
00406ED0  E9 C9 FB FF FF                  jmp 0x140406a9e
00406ED5  41 8B 47 28                     mov eax, dword ptr [r15 + 0x28]
00406ED9  A8 40                           test al, 0x40
00406EDB  0F 85 8D FC FF FF               jne 0x140406b6e
00406EE1  48 8B 75 CF                     mov rsi, qword ptr [rbp - 0x31]
00406EE5  E9 84 FC FF FF                  jmp 0x140406b6e
00406EEA  83 CB 02                        or ebx, 2
00406EED  E9 3B FC FF FF                  jmp 0x140406b2d
00406EF2  45 33 C0                        xor r8d, r8d
00406EF5  48 8B D6                        mov rdx, rsi
00406EF8  49 8B CE                        mov rcx, r14
00406EFB  E8 D0 D0 E7 FF                  call 0x140283fd0
00406F00  45 33 C9                        xor r9d, r9d
00406F03  41 8B F1                        mov esi, r9d
00406F06  E9 6C FC FF FF                  jmp 0x140406b77
00406F0B  41 FF 8E E4 02 00 00            dec dword ptr [r14 + 0x2e4]
00406F12  E9 FA FD FF FF                  jmp 0x140406d11
00406F17  41 8B D5                        mov edx, r13d
00406F1A  49 8B CC                        mov rcx, r12
00406F1D  E8 5E 13 27 00                  call 0x140678280
00406F22  E9 95 FC FF FF                  jmp 0x140406bbc
00406F27  48 8B C8                        mov rcx, rax
00406F2A  E8 C1 F6 E7 FF                  call 0x1402865f0
00406F2F  E9 9B FC FF FF                  jmp 0x140406bcf
00406F34  33 D2                           xor edx, edx
00406F36  E8 35 B9 77 00                  call 0x140b82870
00406F3B  E9 A8 FC FF FF                  jmp 0x140406be8
00406F40  65 48 8B 1C 25 88 01 00 00      mov rbx, qword ptr gs:[0x188]
00406F49  49 8B CE                        mov rcx, r14
00406F4C  48 8B D3                        mov rdx, rbx
00406F4F  E8 FC C1 FF FF                  call 0x140403150
00406F54  49 8D 86 A8 02 00 00            lea rax, [r14 + 0x2a8]
00406F5B  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00406F5F  48 39 01                        cmp qword ptr [rcx], rax
00406F62  0F 84 AA 56 2E 00               je 0x1406ec612
00406F68  B9 03 00 00 00                  mov ecx, 3
00406F6D  CD 29                           int 0x29
00406F6F  41 88 B6 38 04 00 00            mov byte ptr [r14 + 0x438], sil
00406F76  E9 B3 FC FF FF                  jmp 0x140406c2e
00406F7B  49 8D 8E 14 04 00 00            lea rcx, [r14 + 0x414]
00406F82  E8 09 17 E4 FF                  call 0x140248690
00406F87  8A 0B                           mov cl, byte ptr [rbx]
00406F89  8A D0                           mov dl, al
00406F8B  84 C9                           test cl, cl
00406F8D  0F 84 E8 56 2E 00               je 0x1406ec67b
00406F93  40 38 73 02                     cmp byte ptr [rbx + 2], sil
00406F97  0F 84 B5 56 2E 00               je 0x1406ec652
00406F9D  80 F9 01                        cmp cl, 1
00406FA0  0F 86 D5 56 2E 00               jbe 0x1406ec67b
00406FA6  40 88 73 02                     mov byte ptr [rbx + 2], sil
00406FAA  E9 AE 56 2E 00                  jmp 0x1406ec65d
00406FAF  41 81 FD 54 00 00 C0            cmp r13d, 0xc0000054
00406FB6  0F 84 D1 56 2E 00               je 0x1406ec68d
00406FBC  85 C0                           test eax, eax
00406FBE  0F 84 73 FC FF FF               je 0x140406c37
00406FC4  49 8D 8E 14 04 00 00            lea rcx, [r14 + 0x414]
00406FCB  E8 C0 16 E4 FF                  call 0x140248690
00406FD0  8A 0B                           mov cl, byte ptr [rbx]
00406FD2  8A D0                           mov dl, al
00406FD4  84 C9                           test cl, cl
00406FD6  0F 85 86 56 2E 00               jne 0x1406ec662
00406FDC  66 C7 03 10 10                  mov word ptr [rbx], 0x1010
00406FE1  E9 95 56 2E 00                  jmp 0x1406ec67b
00406FE6  45 33 C0                        xor r8d, r8d
00406FE9  33 D2                           xor edx, edx
00406FEB  48 8B C8                        mov rcx, rax
00406FEE  E8 1D 83 F3 FF                  call 0x14033f310
00406FF3  E9 4C FC FF FF                  jmp 0x140406c44
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiWriteComplete(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int8 v_stack_p8;

    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (136);
    v_rdi = 0;
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 44)));
    if (condition_is_below) goto loc_00406E32;
loc_004069F2:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 96) + 10)) & (1)) != 0) goto loc_00406E3F;
loc_004069FC:
    v_stack_m70 = (unsigned int)((int)(*(unsigned int *)(a2)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 40)))) & (32)) != 0) goto loc_00406DA7;
    a4 = 0;
    v_stack_m98 = *(unsigned __int64 *)(a1 + 72);
    v_stack_p10 = 128;
    v_stack_m88 = 0;
loc_00406A2B:
    v_stack_m78 = *(unsigned __int64 *)(a1 + 96) + 48;
    a1 = ((((unsigned int)((unsigned int)(v_stack_p20))) & (0xFFFULL)) != 0) ? 1 : 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p20)))) >> (12));
    result = (unsigned int)((result) + ((unsigned int)(a1)));
    v_stack_m68 = *(unsigned __int64 *)(a1 + 96) + 48 + result * 8;
    if (*(unsigned __int64 *)(a1 + 80) != 0) goto loc_00406E50;
    if (sign_flag) goto loc_00406C92;
loc_00406A68:
    v_stack_m80 = 0;
    if (0 != 0) goto loc_00406E9F;
loc_00406A78:
    a2 = (*(unsigned __int64 *)(a1 + 88)) >> (12);
    v_stack_m58 = a2;
    v_stack_m90 = 0;
    v_stack_m60 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 40)))) & (32)) != 0) goto loc_00406EB4;
loc_00406A9E:
    if (v_stack_m78 >= v_stack_m68) goto loc_00406B98;
loc_00406AB6:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 40)))) & (32)) == 0) goto loc_00406AE2;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 40)))) & (64)) == 0) goto loc_00406CDB;
    v_stack_m90 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 0 * 8 + 96);
    result = MiClearPageFileReservation(v_stack_m90, a2, *(unsigned __int64 *)(a1 + 96) + 48, a4);
loc_00406ADF:
    a4 = 0;
loc_00406AE2:
    if ((*(unsigned __int64 *)(v_stack_m78)) == (*(unsigned __int64 *)(v_rip + 10684811))) goto loc_00406ED5;
    v_rsi = (*(unsigned __int64 *)(v_stack_m78) + *(unsigned __int64 *)(v_stack_m78) * 2) << (4);
    v_rsi = (v_rsi) + (*(unsigned __int64 *)(v_stack_m78));
    v_stack_m78 = v_rsi;
    result = MiLockPageInline(v_rsi, a2, *(unsigned __int64 *)(a1 + 96) + 48, a4);
    v_stack_p8 = (unsigned __int8)(result);
    if (((128) & (1)) != 0) goto loc_00406B2D;
    if (sign_flag) goto loc_00406B2D;
    if (((*(unsigned __int8 *)(v_rsi + 34)) & (16)) != 0) goto loc_00406EEA;
    v_rbx = (unsigned int)((128) & (0xFFFFFFFDULL));
loc_00406B2D:
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFF3ULL));
    v_stack_p10 = (unsigned int)(v_rbx);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 40)))) & (64)) == 0) goto loc_00406C59;
    result = MiStoreModifiedWriteCompletePfn(v_rsi, v_stack_p10, *(unsigned __int64 *)(a1 + 96) + 48, a4);
loc_00406B4B:
loc_00406B4E:
    result = MiWriteCompletePfn(v_rsi, (unsigned int)((unsigned int)((unsigned int)(v_stack_p10))), v_stack_m60, a4);
    result = MiUnlockPage(v_stack_m78, v_stack_p8, v_stack_m60, a4);
    a4 = 0;
loc_00406B6E:
    if (result != 0) goto loc_00406EF2;
loc_00406B77:
    v_r13 = (v_stack_m78) + (8);
    v_r12 = (unsigned int)((0) + 1);
    if (v_r13 < v_stack_m68) goto loc_00406AB6;
loc_00406B98:
    v_rsi = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48))) != 0) goto loc_00406E0A;
loc_00406BA6:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 40)))) & (32)) != 0) goto loc_00406D07;
    if (((0) & (1)) != 0) goto loc_00406F17;
loc_00406BBC:
    a2 = 0;
    result = MiDecrementModifiedWriteCount(v_stack_m98, a2, v_stack_m60, a4);
    if (result != 0) goto loc_00406F27;
loc_00406BCF:
    if ((*(unsigned __int64 *)(a1 + 96)) != (a1 + 104)) goto loc_00406F34;
loc_00406BE8:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 40)))) & (1)) != 0) goto loc_00406F40;
    *(unsigned __int64 *)(a1) = 0;
    result = MiFreeModWriterEntry(a1, 1, v_stack_m60, a4);
loc_00406C04:
    result = -(v_stack_m88);
    v_rbx = ((unsigned int)(v_stack_p10)) & (-3);
    v_rbx = (v_rbx) + (0x41BULL);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(a1 + 56));
    if (sign_flag) goto loc_00406D54;
    if (v_stack_m98 != 0) goto loc_00406F6F;
loc_00406C2E:
    if ((*(unsigned __int8 *)(v_rbx)) != 0) goto loc_00406F7B;
loc_00406C37:
    if (v_stack_m80 != 0) goto loc_00406FE6;
loc_00406C44:
    v_rsp = (v_rsp) + (136);
    return v_stack_m80;
loc_00406C59:
    if (((0) & (2)) == 0) goto loc_00406B4E;
    if ((((unsigned __int8)(v_rbx)) & (2)) != 0) goto loc_00406B4E;
    if ((((unsigned __int8)(v_rbx)) & (1)) != 0) goto loc_00406B4E;
    if (condition_is_below) goto loc_00406B4B;
    v_rbx = (unsigned int)(((unsigned int)(v_stack_p10)) | (8));
    v_stack_p10 = (unsigned int)(v_rbx);
    goto loc_00406B4E;
loc_00406C92:
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 40))) >> (1));
    v_r12 = (unsigned int)((v_r12) & (1));
    a1 = (1 != 0) ? 1 : 0;
    result = MmIsWriteErrorFatal(a1, (unsigned int)((unsigned int)(v_r12)), (unsigned int)((unsigned int)((unsigned int)(v_stack_m70))), a4);
    a4 = 0;
    if ((unsigned int)(result) != 0) goto loc_00406E7B;
    v_rbx = (unsigned int)((v_rbx) | (1));
    v_stack_p10 = (unsigned int)(v_rbx);
    if (v_stack_m98 == 0) goto loc_00406E6B;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 56) + 728) = (unsigned int)((unsigned int)(v_stack_m70));
    goto loc_00406A68;
loc_00406CDB:
    if (((*(unsigned __int8 *)(v_stack_m88 + 172)) & (64)) == 0) goto loc_00406D89;
    result = MiSetStoreVirtualPagefileValue(*(unsigned __int64 *)(a1 + 56), *(unsigned __int64 *)(v_rip - 4154480), 4, a4);
loc_00406CFE:
    v_stack_m90 = result;
    goto loc_00406ADF;
loc_00406D07:
    result = (unsigned __int8)((result) & (28));
    if (((unsigned __int8)(result)) < 8) goto loc_00406F0B;
loc_00406D11:
    result = MiMakePagefileWriterEntryAvailable(a1, *(unsigned __int64 *)(v_rip - 4154480), 4, a4);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 56) + 721)) != 0) goto loc_00406DFA;
loc_00406D26:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 40)))) & (64)) == 0) goto loc_00406C04;
    result = MiStoreDecrementOutstandingWrites(*(unsigned __int64 *)(a1 + 56), *(unsigned __int64 *)(v_rip - 4154480), 4, a4);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 56) + 722)) != 0) goto loc_00406C04;
    result = MiStoreCheckCompleteWriteBatch(*(unsigned __int64 *)(a1 + 56), *(unsigned __int64 *)(v_rip - 4154480), 4, a4);
    goto loc_00406C04;
loc_00406D54:
    result = MiIsRetryIoStatus((unsigned int)((unsigned int)((unsigned int)(v_stack_m70))), (int)(v_stack_p20), 4, a4);
    if (v_stack_p18 == 0) goto loc_00406FAF;
    if (v_stack_m98 == 0) goto loc_00406C37;
    if (((0) & (1)) != 0) goto loc_00406C37;
    if ((unsigned int)(result) != 0) goto loc_00406C37;
loc_00406D89:
    result = MiTransferSoftwarePte(*(unsigned __int64 *)(v_rip - 4154640), v_stack_m88, (int)(v_stack_p20) + v_stack_m98 * 1, 1);
    goto loc_00406CFE;
loc_00406DA7:
    v_stack_m88 = *(unsigned __int64 *)(a1 + 64);
loc_00406DC3:
    if ((*(unsigned __int64 *)((int)(v_stack_p20) + v_stack_m98 * 1)) != (*(unsigned __int64 *)((int)(v_stack_p20) + v_stack_m98 * 1))) goto loc_00406DC3;
    a4 = 0;
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_m70));
    a2 = (*(unsigned __int64 *)(1)) - (*(unsigned __int64 *)((int)(v_stack_p20) + v_stack_m98 * 1));
    result = MI_PAGEFILE_WRITE(a1, a2, a4 + 5, a4);
    v_stack_m98 = 0;
    goto loc_00406A2B;
loc_00406DFA:
    v_stack_m80 = *(unsigned __int64 *)(a1 + 56) + 968;
    goto loc_00406D26;
loc_00406E0A:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 40)))) & (32)) == 0) goto loc_00406E22;
    result = MiReturnResident(*(unsigned __int64 *)(a1 + 56), *(unsigned __int64 *)(a1 + 56) + 968, a4 + 5, a4);
    goto loc_00406BA6;
loc_00406E22:
    result = MiReleaseWriteInProgressCharges(*(unsigned __int64 *)(a1 + 56), *(unsigned __int64 *)(a1 + 56) + 968, 1, a4);
    goto loc_00406BA6;
loc_00406E32:
    result = MiRetardMdl(0, *(unsigned __int64 *)(a1 + 56) + 968, 1, a4);
    goto loc_004069F2;
loc_00406E3F:
    result = MmUnmapLockedPages(*(unsigned __int64 *)(v_rsi + 24), 0, 1, a4);
    goto loc_004069FC;
loc_00406E50:
    v_stack_p8 = *(unsigned __int64 *)(a1 + 64);
    v_r12 = (0) & (-2);
loc_00406E6B:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 56) + 724) = (unsigned int)((unsigned int)(v_stack_m70));
    v_stack_m80 = 0;
    goto loc_00406A78;
loc_00406E7B:
    v_stack_p20 = 0;
    result = KeBugCheckEx(v_stack_m98 + 122, v_stack_m98 + 32, (unsigned int)(v_stack_m70), 0);
loc_00406E9F:
    result = MiSetDeleteOnClose(v_r12, 1, (unsigned int)(v_stack_m70), 0);
    a4 = 0;
    goto loc_00406A78;
loc_00406EB4:
    v_rdi = (unsigned int)((v_rdi) | (2));
    v_stack_m60 = v_stack_m90;
    if (((*(unsigned __int16 *)(v_stack_m88 + 172)) & ((unsigned __int16)((unsigned int)(0x800ULL)))) == 0) { v_rdi = (unsigned int)(v_r12); }
    goto loc_00406A9E;
loc_00406ED5:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 40)))) & (64)) != 0) goto loc_00406B6E;
    goto loc_00406B6E;
loc_00406EEA:
    v_rbx = (unsigned int)(((unsigned int)(v_stack_p10)) | (2));
    goto loc_00406B2D;
loc_00406EF2:
    a3 = 0;
    result = MiReleasePageFileInfo(*(unsigned __int64 *)(a1 + 56), v_stack_m90, a3, a4);
    a4 = 0;
    goto loc_00406B77;
loc_00406F0B:
    goto loc_00406D11;
loc_00406F17:
    result = MiNotifyUserOfLostData(v_r12, (unsigned int)((unsigned int)((unsigned int)(v_stack_m70))), a3, a4);
    goto loc_00406BBC;
loc_00406F27:
    result = MiReleaseControlAreaWaiters(result, (unsigned int)((unsigned int)((unsigned int)(v_stack_m70))), a3, a4);
    goto loc_00406BCF;
loc_00406F34:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
    goto loc_00406BE8;
loc_00406F40:
    result = MiLockPartitionMappedWriter(*(unsigned __int64 *)(a1 + 56), *(unsigned __int64 *)(gs_base + (0 + 392)), a3, a4);
loc_00406F6F:
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 56) + 1080) = 0;
    goto loc_00406C2E;
loc_00406F7B:
    result = ExAcquireSpinLockExclusive(*(unsigned __int64 *)(a1 + 56) + 1044, *(unsigned __int64 *)(gs_base + (0 + 392)), a3, a4);
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 2) = 0;
loc_00406FAF:
    if ((unsigned int)(result) == 0) goto loc_00406C37;
    result = ExAcquireSpinLockExclusive(*(unsigned __int64 *)(a1 + 56) + 1044, (unsigned __int8)(result), a3, a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392))) = 0x1010ULL;
loc_00406FE6:
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(result, a2, a3, a4);
    goto loc_00406C44;
}
```

## 5. (Beta) C Style

```c
int64_t MiWriteComplete(void *Arg1, void *Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint8_t v_stack_p8;

    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (136);
    local_rdi = 0;
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2C)));
    if (condition_is_below) goto loc_00406E32;
loc_004069F2:
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x60) + 0xA)) & (1)) != 0) goto loc_00406E3F;
loc_004069FC:
    v_stack_m70 = (uint32_t)((int32_t)(*(uint32_t *)(arg2)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) & (32)) != 0) goto loc_00406DA7;
    Arg4 = 0;
    v_stack_m98 = *(uint64_t *)(arg1 + 0x48);
    v_stack_p10 = 128;
    v_stack_m88 = 0;
loc_00406A2B:
    v_stack_m78 = *(uint64_t *)(arg1 + 0x60) + 48;
    Arg1 = ((((uint32_t)((uint32_t)(v_stack_p20))) & (0xFFFULL)) != 0) ? 1 : 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p20)))) >> (12));
    result = (uint32_t)((result) + ((uint32_t)(Arg1)));
    v_stack_m68 = *(uint64_t *)(arg1 + 0x60) + 48 + result * 8;
    if (*(uint64_t *)(arg1 + 0x50) != 0) goto loc_00406E50;
    if (sign_flag) goto loc_00406C92;
loc_00406A68:
    v_stack_m80 = 0;
    if (0 != 0) goto loc_00406E9F;
loc_00406A78:
    Arg2 = (*(uint64_t *)(arg1 + 0x58)) >> (12);
    v_stack_m58 = Arg2;
    v_stack_m90 = 0;
    v_stack_m60 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) & (32)) != 0) goto loc_00406EB4;
loc_00406A9E:
    if (v_stack_m78 >= v_stack_m68) goto loc_00406B98;
loc_00406AB6:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) & (32)) == 0) goto loc_00406AE2;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) & (64)) == 0) goto loc_00406CDB;
    v_stack_m90 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x0 * 8 + 0x60);
    result = MiClearPageFileReservation(v_stack_m90, Arg2, *(uint64_t *)(arg1 + 0x60) + 48, Arg4);
loc_00406ADF:
    Arg4 = 0;
loc_00406AE2:
    if ((*(uint64_t *)(v_stack_m78)) == (*(uint64_t *)(v_rip + 0xA3098B))) goto loc_00406ED5;
    local_rsi = (*(uint64_t *)(v_stack_m78) + *(uint64_t *)(v_stack_m78) * 2) << (4);
    local_rsi = (local_rsi) + (*(uint64_t *)(v_stack_m78));
    v_stack_m78 = local_rsi;
    result = MiLockPageInline(local_rsi, Arg2, *(uint64_t *)(arg1 + 0x60) + 48, Arg4);
    v_stack_p8 = (uint8_t)(result);
    if (((128) & (1)) != 0) goto loc_00406B2D;
    if (sign_flag) goto loc_00406B2D;
    if (((*(uint8_t *)(local_rsi + 0x22)) & (16)) != 0) goto loc_00406EEA;
    local_rbx = (uint32_t)((128) & (0xFFFFFFFDULL));
loc_00406B2D:
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFF3ULL));
    v_stack_p10 = (uint32_t)(local_rbx);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) & (64)) == 0) goto loc_00406C59;
    result = MiStoreModifiedWriteCompletePfn(local_rsi, v_stack_p10, *(uint64_t *)(arg1 + 0x60) + 48, Arg4);
loc_00406B4B:
loc_00406B4E:
    result = MiWriteCompletePfn(local_rsi, (uint32_t)((uint32_t)((uint32_t)(v_stack_p10))), v_stack_m60, Arg4);
    result = MiUnlockPage(v_stack_m78, v_stack_p8, v_stack_m60, Arg4);
    Arg4 = 0;
loc_00406B6E:
    if (result != 0) goto loc_00406EF2;
loc_00406B77:
    local_r13 = (v_stack_m78) + (8);
    local_r12 = (uint32_t)((0) + 1);
    if (local_r13 < v_stack_m68) goto loc_00406AB6;
loc_00406B98:
    local_rsi = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30))) != 0) goto loc_00406E0A;
loc_00406BA6:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) & (32)) != 0) goto loc_00406D07;
    if (((0) & (1)) != 0) goto loc_00406F17;
loc_00406BBC:
    Arg2 = 0;
    result = MiDecrementModifiedWriteCount(v_stack_m98, Arg2, v_stack_m60, Arg4);
    if (result != 0) goto loc_00406F27;
loc_00406BCF:
    if ((*(uint64_t *)(arg1 + 0x60)) != (Arg1 + 104)) goto loc_00406F34;
loc_00406BE8:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) & (1)) != 0) goto loc_00406F40;
    *(uint64_t *)(arg1) = 0;
    result = MiFreeModWriterEntry(Arg1, 1, v_stack_m60, Arg4);
loc_00406C04:
    result = -(v_stack_m88);
    local_rbx = ((uint32_t)(v_stack_p10)) & (-3);
    local_rbx = (local_rbx) + (0x41BULL);
    local_rbx = (local_rbx) + (*(uint64_t *)(arg1 + 0x38));
    if (sign_flag) goto loc_00406D54;
    if (v_stack_m98 != 0) goto loc_00406F6F;
loc_00406C2E:
    if ((*(uint8_t *)(local_rbx)) != 0) goto loc_00406F7B;
loc_00406C37:
    if (v_stack_m80 != 0) goto loc_00406FE6;
loc_00406C44:
    local_rsp = (local_rsp) + (136);
    return v_stack_m80;
loc_00406C59:
    if (((0) & (2)) == 0) goto loc_00406B4E;
    if ((((uint8_t)(local_rbx)) & (2)) != 0) goto loc_00406B4E;
    if ((((uint8_t)(local_rbx)) & (1)) != 0) goto loc_00406B4E;
    if (condition_is_below) goto loc_00406B4B;
    local_rbx = (uint32_t)(((uint32_t)(v_stack_p10)) | (8));
    v_stack_p10 = (uint32_t)(local_rbx);
    goto loc_00406B4E;
loc_00406C92:
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x28))) >> (1));
    local_r12 = (uint32_t)((local_r12) & (1));
    Arg1 = (1 != 0) ? 1 : 0;
    result = MmIsWriteErrorFatal(Arg1, (uint32_t)((uint32_t)(local_r12)), (uint32_t)((uint32_t)((uint32_t)(v_stack_m70))), Arg4);
    Arg4 = 0;
    if ((uint32_t)(result) != 0) goto loc_00406E7B;
    local_rbx = (uint32_t)((local_rbx) | (1));
    v_stack_p10 = (uint32_t)(local_rbx);
    if (v_stack_m98 == 0) goto loc_00406E6B;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x38) + 0x2D8) = (uint32_t)((uint32_t)(v_stack_m70));
    goto loc_00406A68;
loc_00406CDB:
    if (((*(uint8_t *)(v_stack_m88 + 0xAC)) & (64)) == 0) goto loc_00406D89;
    result = MiSetStoreVirtualPagefileValue(*(uint64_t *)(arg1 + 0x38), *(uint64_t *)(v_rip - 0x3F6470), 4, Arg4);
loc_00406CFE:
    v_stack_m90 = result;
    goto loc_00406ADF;
loc_00406D07:
    result = (uint8_t)((result) & (28));
    if (((uint8_t)(result)) < 8) goto loc_00406F0B;
loc_00406D11:
    result = MiMakePagefileWriterEntryAvailable(Arg1, *(uint64_t *)(v_rip - 0x3F6470), 4, Arg4);
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x38) + 0x2D1)) != 0) goto loc_00406DFA;
loc_00406D26:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) & (64)) == 0) goto loc_00406C04;
    result = MiStoreDecrementOutstandingWrites(*(uint64_t *)(arg1 + 0x38), *(uint64_t *)(v_rip - 0x3F6470), 4, Arg4);
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x38) + 0x2D2)) != 0) goto loc_00406C04;
    result = MiStoreCheckCompleteWriteBatch(*(uint64_t *)(arg1 + 0x38), *(uint64_t *)(v_rip - 0x3F6470), 4, Arg4);
    goto loc_00406C04;
loc_00406D54:
    result = MiIsRetryIoStatus((uint32_t)((uint32_t)((uint32_t)(v_stack_m70))), (int32_t)(v_stack_p20), 4, Arg4);
    if (v_stack_p18 == 0) goto loc_00406FAF;
    if (v_stack_m98 == 0) goto loc_00406C37;
    if (((0) & (1)) != 0) goto loc_00406C37;
    if ((uint32_t)(result) != 0) goto loc_00406C37;
loc_00406D89:
    result = MiTransferSoftwarePte(*(uint64_t *)(v_rip - 0x3F6510), v_stack_m88, (int32_t)(v_stack_p20) + v_stack_m98 * 1, 1);
    goto loc_00406CFE;
loc_00406DA7:
    v_stack_m88 = *(uint64_t *)(arg1 + 0x40);
loc_00406DC3:
    if ((*(uint64_t *)((int32_t)(v_stack_p20) + v_stack_m98 * 1)) != (*(uint64_t *)((int32_t)(v_stack_p20) + v_stack_m98 * 1))) goto loc_00406DC3;
    Arg4 = 0;
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_m70));
    Arg2 = (*(uint64_t *)(1)) - (*(uint64_t *)((int32_t)(v_stack_p20) + v_stack_m98 * 1));
    result = MI_PAGEFILE_WRITE(Arg1, Arg2, Arg4 + 5, Arg4);
    v_stack_m98 = 0;
    goto loc_00406A2B;
loc_00406DFA:
    v_stack_m80 = *(uint64_t *)(arg1 + 0x38) + 968;
    goto loc_00406D26;
loc_00406E0A:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) & (32)) == 0) goto loc_00406E22;
    result = MiReturnResident(*(uint64_t *)(arg1 + 0x38), *(uint64_t *)(arg1 + 0x38) + 968, Arg4 + 5, Arg4);
    goto loc_00406BA6;
loc_00406E22:
    result = MiReleaseWriteInProgressCharges(*(uint64_t *)(arg1 + 0x38), *(uint64_t *)(arg1 + 0x38) + 968, 1, Arg4);
    goto loc_00406BA6;
loc_00406E32:
    result = MiRetardMdl(0, *(uint64_t *)(arg1 + 0x38) + 968, 1, Arg4);
    goto loc_004069F2;
loc_00406E3F:
    result = MmUnmapLockedPages(*(uint64_t *)(local_rsi + 0x18), 0, 1, Arg4);
    goto loc_004069FC;
loc_00406E50:
    v_stack_p8 = *(uint64_t *)(arg1 + 0x40);
    local_r12 = (0) & (-2);
loc_00406E6B:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x38) + 0x2D4) = (uint32_t)((uint32_t)(v_stack_m70));
    v_stack_m80 = 0;
    goto loc_00406A78;
loc_00406E7B:
    v_stack_p20 = 0;
    result = KeBugCheckEx(v_stack_m98 + 122, v_stack_m98 + 32, (uint32_t)(v_stack_m70), 0);
loc_00406E9F:
    result = MiSetDeleteOnClose(local_r12, 1, (uint32_t)(v_stack_m70), 0);
    Arg4 = 0;
    goto loc_00406A78;
loc_00406EB4:
    local_rdi = (uint32_t)((local_rdi) | (2));
    v_stack_m60 = v_stack_m90;
    if (((*(uint16_t *)(v_stack_m88 + 0xAC)) & ((uint16_t)((uint32_t)(0x800ULL)))) == 0) { local_rdi = (uint32_t)(local_r12); }
    goto loc_00406A9E;
loc_00406ED5:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) & (64)) != 0) goto loc_00406B6E;
    goto loc_00406B6E;
loc_00406EEA:
    local_rbx = (uint32_t)(((uint32_t)(v_stack_p10)) | (2));
    goto loc_00406B2D;
loc_00406EF2:
    Arg3 = 0;
    result = MiReleasePageFileInfo(*(uint64_t *)(arg1 + 0x38), v_stack_m90, Arg3, Arg4);
    Arg4 = 0;
    goto loc_00406B77;
loc_00406F0B:
    goto loc_00406D11;
loc_00406F17:
    result = MiNotifyUserOfLostData(local_r12, (uint32_t)((uint32_t)((uint32_t)(v_stack_m70))), Arg3, Arg4);
    goto loc_00406BBC;
loc_00406F27:
    result = MiReleaseControlAreaWaiters(result, (uint32_t)((uint32_t)((uint32_t)(v_stack_m70))), Arg3, Arg4);
    goto loc_00406BCF;
loc_00406F34:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg3, Arg4);
    goto loc_00406BE8;
loc_00406F40:
    result = MiLockPartitionMappedWriter(*(uint64_t *)(arg1 + 0x38), *(uint64_t *)(gs_base + (0 + 0x188)), Arg3, Arg4);
loc_00406F6F:
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x38) + 0x438) = 0;
    goto loc_00406C2E;
loc_00406F7B:
    result = ExAcquireSpinLockExclusive(*(uint64_t *)(arg1 + 0x38) + 1044, *(uint64_t *)(gs_base + (0 + 0x188)), Arg3, Arg4);
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x2) = 0;
loc_00406FAF:
    if ((uint32_t)(result) == 0) goto loc_00406C37;
    result = ExAcquireSpinLockExclusive(*(uint64_t *)(arg1 + 0x38) + 1044, (uint8_t)(result), Arg3, Arg4);
    *(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188))) = 0x1010ULL;
loc_00406FE6:
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(result, Arg2, Arg3, Arg4);
    goto loc_00406C44;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x2C` | `32` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004069B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
