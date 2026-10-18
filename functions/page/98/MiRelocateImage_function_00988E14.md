# MiRelocateImage

- RVA: `0x00988E14`–`0x0098965D` (길이 `2,121` bytes)
- VA: `0x0000000140988E14`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00097F1C`
- 디코드: `499`개 명령, `2,121/2,121` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **27**; 고유 호출 대상: **22**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00988E67` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00988EA2` → [MiLegacyImageArchitecture](../../text/49/MiLegacyImageArchitecture_function_00494454.md) (function, `0x00494454`)
- `0x00988FB8` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x00989010` → [MiMapImageInSystemSpace](../94/MiMapImageInSystemSpace_function_00941DD8.md) (function, `0x00941DD8`)
- `0x00989034` → [PsSetSystemPagePriorityThread](../../text/45/PsSetSystemPagePriorityThread_function_00459084.md) (function, `0x00459084`)
- `0x00989063` → [MiParseImageLoadConfig](../94/MiParseImageLoadConfig_function_00940D18.md) (function, `0x00940D18`)
- `0x00989073` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0098909F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009890FA` → [MiSelectImageBase](MiSelectImageBase_function_009887B0.md) (function, `0x009887B0`)
- `0x00989115` → [MiUpdateImageSystemWideBitmaps](../8C/MiUpdateImageSystemWideBitmaps_function_008CE540.md) (function, `0x008CE540`)
- `0x009891BE` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009892DF` → [MiScanRelocationPage](MiScanRelocationPage_function_00989670.md) (function, `0x00989670`)
- `0x0098930E` → [MiUnmapImageInSystemSpace](../94/MiUnmapImageInSystemSpace_function_0094206C.md) (function, `0x0094206C`)
- `0x0098931C` → [PsRevertToUserPagePriorityThread](../../text/46/PsRevertToUserPagePriorityThread_function_00462D40.md) (function, `0x00462D40`)
- `0x0098936F` → [MiLogRelocationFaults](../94/MiLogRelocationFaults_function_009418EC.md) (function, `0x009418EC`)
- `0x009893B6` → [MiCreateFileOnlyImageFixupList](MiCreateFileOnlyImageFixupList_function_00989AD0.md) (function, `0x00989AD0`)
- `0x009893D4` → [MiFreeRelocations](../93/MiFreeRelocations_function_0093F08C.md) (function, `0x0093F08C`)
- `0x00989403` → [MiOffsetToProtos](../../text/24/MiOffsetToProtos_function_0024D880.md) (function, `0x0024D880`)
- `0x00989534` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0098953E` → [MiSetDeleteOnClose](../../text/4D/MiSetDeleteOnClose_function_004DD8E8.md) (function, `0x004DD8E8`)
- `0x00989548` → [MiFreeImageLoadConfig](../93/MiFreeImageLoadConfig_function_0093F144.md) (function, `0x0093F144`)
- `0x00989552` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0098958D` → [RtlInitializeSystemOverrideDelta](../AA/RtlInitializeSystemOverrideDelta_function_00AACFB0.md) (function, `0x00AACFB0`)
- `0x00989620` → [MiCompressRelocations](../96/MiCompressRelocations_function_00966600.md) (function, `0x00966600`)
- `0x00989639` → [MiUnmapImageInSystemSpace](../94/MiUnmapImageInSystemSpace_function_0094206C.md) (function, `0x0094206C`)
- `0x00989647` → [PsRevertToUserPagePriorityThread](../../text/46/PsRevertToUserPagePriorityThread_function_00462D40.md) (function, `0x00462D40`)
- `0x00989653` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [MiCreateNewSection](MiCreateNewSection_function_00985DB0.md) at `0x00986185`
- [MiCreateNewSection](MiCreateNewSection_function_00985DB0.md) at `0x00986445`
- [sub_00B40C48](../B4/Unknown_function_00B40C48.md) at `0x00B40FF6`

### Static image references
- `0x00988E29` → RVA `0x00E0A740` (`.data`; read)
- `0x0098927B` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x009894C1` → RVA `0x00FC51F0` (`ALMOSTRO`; read)
- `0x0098956A` → RVA `0x00FD8130` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **14**
  - `0x00988E67` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00988EA2` → [MiLegacyImageArchitecture](../../text/49/MiLegacyImageArchitecture_function_00494454.md) (`PAGE` → `.text`)
  - `0x00988FB8` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x00989034` → [PsSetSystemPagePriorityThread](../../text/45/PsSetSystemPagePriorityThread_function_00459084.md) (`PAGE` → `.text`)
  - `0x00989073` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0098909F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009891BE` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0098931C` → [PsRevertToUserPagePriorityThread](../../text/46/PsRevertToUserPagePriorityThread_function_00462D40.md) (`PAGE` → `.text`)
  - `0x00989403` → [MiOffsetToProtos](../../text/24/MiOffsetToProtos_function_0024D880.md) (`PAGE` → `.text`)
  - `0x00989534` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0098953E` → [MiSetDeleteOnClose](../../text/4D/MiSetDeleteOnClose_function_004DD8E8.md) (`PAGE` → `.text`)
  - `0x00989552` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00989647` → [PsRevertToUserPagePriorityThread](../../text/46/PsRevertToUserPagePriorityThread_function_00462D40.md) (`PAGE` → `.text`)
  - `0x00989653` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x009893A2` → [sub_00B2B6D0 + 0x2C](../B2/Unknown_function_00B2B6D0.md) (`tail-transfer`)
  - `0x009893BF` → [sub_00B2B6D0 + 0x2C](../B2/Unknown_function_00B2B6D0.md) (`tail-transfer`)
  - `0x009895C0` → [sub_00B2B6D0](../B2/Unknown_function_00B2B6D0.md) (`tail-transfer`)
  - `0x009895F9` → [sub_00B2B6D0 + 0x1D](../B2/Unknown_function_00B2B6D0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00988E14  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00988E19  56                              push rsi
00988E1A  41 54                           push r12
00988E1C  41 55                           push r13
00988E1E  41 56                           push r14
00988E20  41 57                           push r15
00988E22  48 81 EC 30 01 00 00            sub rsp, 0x130
00988E29  48 8B 05 10 19 48 00            mov rax, qword ptr [rip + 0x481910]
00988E30  48 33 C4                        xor rax, rsp
00988E33  48 89 84 24 20 01 00 00         mov qword ptr [rsp + 0x120], rax
00988E3B  44 89 4C 24 38                  mov dword ptr [rsp + 0x38], r9d
00988E40  41 8B F0                        mov esi, r8d
00988E43  4C 8B F2                        mov r14, rdx
00988E46  48 89 94 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rdx
00988E4E  4C 8B F9                        mov r15, rcx
00988E51  48 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rcx
00988E59  33 D2                           xor edx, edx
00988E5B  44 8D 42 50                     lea r8d, [rdx + 0x50]
00988E5F  48 8D 8C 24 D0 00 00 00         lea rcx, [rsp + 0xd0]
00988E67  E8 D4 DD D3 FF                  call 0x1406c6c40
00988E6C  48 83 64 24 78 00               and qword ptr [rsp + 0x78], 0
00988E72  48 83 A4 24 80 00 00 00 00      and qword ptr [rsp + 0x80], 0
00988E7B  8B 9C 24 88 01 00 00            mov ebx, dword ptr [rsp + 0x188]
00988E82  41 BB 01 00 00 00               mov r11d, 1
00988E88  41 23 DB                        and ebx, r11d
00988E8B  C1 E3 08                        shl ebx, 8
00988E8E  83 C3 02                        add ebx, 2
00988E91  4D 8B 47 38                     mov r8, qword ptr [r15 + 0x38]
00988E95  4C 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r8
00988E9D  41 0F B7 48 30                  movzx ecx, word ptr [r8 + 0x30]
00988EA2  E8 AD B5 B0 FF                  call 0x140494454
00988EA7  85 C0                           test eax, eax
00988EA9  0F 85 A9 05 00 00               jne 0x140989458
00988EAF  41 BC 7B 00 00 C0               mov r12d, 0xc000007b
00988EB5  41 8B 4E 58                     mov ecx, dword ptr [r14 + 0x58]
00988EB9  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00988EBD  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
00988EC1  45 8B 56 5C                     mov r10d, dword ptr [r14 + 0x5c]
00988EC5  44 89 54 24 34                  mov dword ptr [rsp + 0x34], r10d
00988ECA  44 89 54 24 7C                  mov dword ptr [rsp + 0x7c], r10d
00988ECF  85 C9                           test ecx, ecx
00988ED1  0F 84 B1 05 00 00               je 0x140989488
00988ED7  45 85 D2                        test r10d, r10d
00988EDA  0F 84 A0 05 00 00               je 0x140989480
00988EE0  41 0F B7 47 0C                  movzx eax, word ptr [r15 + 0xc]
00988EE5  66 0F BA E0 0E                  bt ax, 0xe
00988EEA  0F 82 EA 05 00 00               jb 0x1409894da
00988EF0  4D 8B 2F                        mov r13, qword ptr [r15]
00988EF3  4C 89 AC 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], r13
00988EFB  49 8B 55 60                     mov rdx, qword ptr [r13 + 0x60]
00988EFF  48 83 E2 F8                     and rdx, 0xfffffffffffffff8
00988F03  48 89 94 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rdx
00988F0B  44 8D 4E 30                     lea r9d, [rsi + 0x30]
00988F0F  44 89 4C 24 48                  mov dword ptr [rsp + 0x48], r9d
00988F14  66 C1 E8 0F                     shr ax, 0xf
00988F18  66 41 3B C3                     cmp ax, r11w
00988F1C  0F 84 77 05 00 00               je 0x140989499
00988F22  0F B7 C0                        movzx eax, ax
00988F25  41 33 C3                        xor eax, r11d
00988F28  8D 04 85 03 00 00 00            lea eax, [rax*4 + 3]
00988F2F  41 85 C1                        test r9d, eax
00988F32  0F 85 E5 05 00 00               jne 0x14098951d
00988F38  49 8B 57 20                     mov rdx, qword ptr [r15 + 0x20]
00988F3C  48 89 94 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdx
00988F44  F6 C3 40                        test bl, 0x40
00988F47  0F 85 5A 05 00 00               jne 0x1409894a7
00988F4D  41 8B 47 08                     mov eax, dword ptr [r15 + 8]
00988F51  44 8B F8                        mov r15d, eax
00988F54  8B F3                           mov esi, ebx
00988F56  83 E6 02                        and esi, 2
00988F59  0F 84 82 05 00 00               je 0x1409894e1
00988F5F  C1 E0 0C                        shl eax, 0xc
00988F62  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00988F66  45 8D 04 0A                     lea r8d, [r10 + rcx]
00988F6A  44 3B C0                        cmp r8d, eax
00988F6D  0F 87 AA 05 00 00               ja 0x14098951d
00988F73  85 F6                           test esi, esi
00988F75  0F 85 75 05 00 00               jne 0x1409894f0
00988F7B  41 8B CF                        mov ecx, r15d
00988F7E  49 83 C2 68                     add r10, 0x68
00988F82  49 8D 04 CA                     lea rax, [r10 + rcx*8]
00988F86  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00988F8B  48 83 64 24 58 00               and qword ptr [rsp + 0x58], 0
00988F91  48 83 64 24 70 00               and qword ptr [rsp + 0x70], 0
00988F97  83 64 24 50 00                  and dword ptr [rsp + 0x50], 0
00988F9C  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00988FA5  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
00988FAA  41 B8 4D 6D 52 65               mov r8d, 0x65526d4d
00988FB0  48 8B D0                        mov rdx, rax
00988FB3  B9 00 01 00 00                  mov ecx, 0x100
00988FB8  E8 83 25 9D FF                  call 0x14035b540
00988FBD  4C 8B F0                        mov r14, rax
00988FC0  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
00988FC8  48 85 C0                        test rax, rax
00988FCB  0F 84 54 05 00 00               je 0x140989525
00988FD1  48 8B C8                        mov rcx, rax
00988FD4  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
00988FD9  48 03 D0                        add rdx, rax
00988FDC  8A 01                           mov al, byte ptr [rcx]
00988FDE  48 81 C1 00 10 00 00            add rcx, 0x1000
00988FE5  48 3B CA                        cmp rcx, rdx
00988FE8  72 F2                           jb 0x140988fdc
00988FEA  41 C6 46 40 00                  mov byte ptr [r14 + 0x40], 0
00988FEF  45 89 7E 38                     mov dword ptr [r14 + 0x38], r15d
00988FF3  49 83 66 18 00                  and qword ptr [r14 + 0x18], 0
00988FF8  85 F6                           test esi, esi
00988FFA  0F 84 BE 00 00 00               je 0x1409890be
00989000  4C 8D 84 24 D0 00 00 00         lea r8, [rsp + 0xd0]
00989008  BA 03 00 00 00                  mov edx, 3
0098900D  49 8B CD                        mov rcx, r13
00989010  E8 C3 8D FB FF                  call 0x140941dd8
00989015  85 C0                           test eax, eax
00989017  0F 88 12 05 00 00               js 0x14098952f
0098901D  48 8B B4 24 D0 00 00 00         mov rsi, qword ptr [rsp + 0xd0]
00989025  48 89 74 24 70                  mov qword ptr [rsp + 0x70], rsi
0098902A  BA 01 00 00 00                  mov edx, 1
0098902F  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00989034  E8 4B 00 AD FF                  call 0x140459084
00989039  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0098903D  83 CB 01                        or ebx, 1
00989040  49 8D 4E 48                     lea rcx, [r14 + 0x48]
00989044  44 8B 8C 24 E0 00 00 00         mov r9d, dword ptr [rsp + 0xe0]
0098904C  41 C1 E1 0C                     shl r9d, 0xc
00989050  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00989055  4C 8B 84 24 A0 00 00 00         mov r8, qword ptr [rsp + 0xa0]
0098905D  48 8B D6                        mov rdx, rsi
00989060  49 8B CD                        mov rcx, r13
00989063  E8 B0 7C FB FF                  call 0x140940d18
00989068  8B F0                           mov esi, eax
0098906A  85 C0                           test eax, eax
0098906C  79 50                           jns 0x1409890be
0098906E  33 D2                           xor edx, edx
00989070  49 8B CE                        mov rcx, r14
00989073  E8 F8 97 1F 00                  call 0x140b82870
00989078  F6 C3 01                        test bl, 1
0098907B  0F 85 B0 05 00 00               jne 0x140989631
00989081  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
00989089  48 85 C9                        test rcx, rcx
0098908C  0F 85 BF 05 00 00               jne 0x140989651
00989092  8B C6                           mov eax, esi
00989094  48 8B 8C 24 20 01 00 00         mov rcx, qword ptr [rsp + 0x120]
0098909C  48 33 CC                        xor rcx, rsp
0098909F  E8 9C 35 D2 FF                  call 0x1406ac640
009890A4  48 8B 9C 24 78 01 00 00         mov rbx, qword ptr [rsp + 0x178]
009890AC  48 81 C4 30 01 00 00            add rsp, 0x130
009890B3  41 5F                           pop r15
009890B5  41 5E                           pop r14
009890B7  41 5D                           pop r13
009890B9  41 5C                           pop r12
009890BB  5E                              pop rsi
009890BC  C3                              ret
009890BD  CC                              int3
009890BE  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
009890C2  33 C0                           xor eax, eax
009890C4  81 FB 00 01 00 00               cmp ebx, 0x100
009890CA  0F 93 C0                        setae al
009890CD  44 8B C8                        mov r9d, eax
009890D0  41 83 C9 02                     or r9d, 2
009890D4  F6 84 24 88 01 00 00 02         test byte ptr [rsp + 0x188], 2
009890DC  44 0F 44 C8                     cmove r9d, eax
009890E0  48 8D 44 24 58                  lea rax, [rsp + 0x58]
009890E5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009890EA  44 8B 44 24 38                  mov r8d, dword ptr [rsp + 0x38]
009890EF  49 8B D6                        mov rdx, r14
009890F2  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
009890FA  E8 B1 F6 FF FF                  call 0x1409887b0
009890FF  8B F0                           mov esi, eax
00989101  4D 8D 46 48                     lea r8, [r14 + 0x48]
00989105  85 C0                           test eax, eax
00989107  0F 88 38 04 00 00               js 0x140989545
0098910D  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
00989112  49 8B CD                        mov rcx, r13
00989115  E8 26 54 F4 FF                  call 0x1408ce540
0098911A  8B F0                           mov esi, eax
0098911C  85 C0                           test eax, eax
0098911E  0F 88 AA 02 00 00               js 0x1409893ce
00989124  F6 C3 02                        test bl, 2
00989127  74 0D                           je 0x140989136
00989129  49 8B 4E 60                     mov rcx, qword ptr [r14 + 0x60]
0098912D  48 85 C9                        test rcx, rcx
00989130  0F 85 34 04 00 00               jne 0x14098956a
00989136  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
0098913A  41 89 46 3C                     mov dword ptr [r14 + 0x3c], eax
0098913E  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00989143  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
0098914B  48 2B C1                        sub rax, rcx
0098914E  49 89 46 28                     mov qword ptr [r14 + 0x28], rax
00989152  48 8B 84 24 80 01 00 00         mov rax, qword ptr [rsp + 0x180]
0098915A  48 83 F8 FF                     cmp rax, -1
0098915E  0F 84 9B 01 00 00               je 0x1409892ff
00989164  48 2B C1                        sub rax, rcx
00989167  49 89 46 30                     mov qword ptr [r14 + 0x30], rax
0098916B  49 8D 56 68                     lea rdx, [r14 + 0x68]
0098916F  49 89 16                        mov qword ptr [r14], rdx
00989172  41 8B C7                        mov eax, r15d
00989175  4C 8D 0C C2                     lea r9, [rdx + rax*8]
00989179  4C 89 4C 24 48                  mov qword ptr [rsp + 0x48], r9
0098917E  4D 89 4E 20                     mov qword ptr [r14 + 0x20], r9
00989182  83 CB 10                        or ebx, 0x10
00989185  49 83 7E 58 00                  cmp qword ptr [r14 + 0x58], 0
0098918A  0F 85 07 04 00 00               jne 0x140989597
00989190  8B CB                           mov ecx, ebx
00989192  0F BA EB 07                     bts ebx, 7
00989196  49 83 7E 60 00                  cmp qword ptr [r14 + 0x60], 0
0098919B  0F 44 D9                        cmove ebx, ecx
0098919E  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
009891A2  F6 C3 02                        test bl, 2
009891A5  0F 84 E2 01 00 00               je 0x14098938d
009891AB  8B 54 24 30                     mov edx, dword ptr [rsp + 0x30]
009891AF  48 03 54 24 70                  add rdx, qword ptr [rsp + 0x70]
009891B4  8B 74 24 34                     mov esi, dword ptr [rsp + 0x34]
009891B8  44 8B C6                        mov r8d, esi
009891BB  49 8B C9                        mov rcx, r9
009891BE  E8 7D D6 D3 FF                  call 0x1406c6840
009891C3  EB 1B                           jmp 0x1409891e0
009891C5  8B F0                           mov esi, eax
009891C7  8B 5C 24 40                     mov ebx, dword ptr [rsp + 0x40]
009891CB  4C 8B B4 24 A8 00 00 00         mov r14, qword ptr [rsp + 0xa8]
009891D3  4C 8B AC 24 B0 00 00 00         mov r13, qword ptr [rsp + 0xb0]
009891DB  E9 E5 01 00 00                  jmp 0x1409893c5
009891E0  45 33 FF                        xor r15d, r15d
009891E3  F6 C3 08                        test bl, 8
009891E6  0F 85 B7 03 00 00               jne 0x1409895a3
009891EC  84 DB                           test bl, bl
009891EE  79 0E                           jns 0x1409891fe
009891F0  49 8B 46 60                     mov rax, qword ptr [r14 + 0x60]
009891F4  8B 48 24                        mov ecx, dword ptr [rax + 0x24]
009891F7  44 3B F9                        cmp r15d, ecx
009891FA  44 0F 46 F9                     cmovbe r15d, ecx
009891FE  45 33 C9                        xor r9d, r9d
00989201  44 8B 54 24 60                  mov r10d, dword ptr [rsp + 0x60]
00989206  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
0098920B  B8 FF 0F 00 00                  mov eax, 0xfff
00989210  85 F6                           test esi, esi
00989212  0F 84 EE 00 00 00               je 0x140989306
00989218  83 FE 0A                        cmp esi, 0xa
0098921B  0F 82 E5 03 00 00               jb 0x140989606
00989221  41 8B 50 04                     mov edx, dword ptr [r8 + 4]
00989225  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
00989229  3B D6                           cmp edx, esi
0098922B  0F 87 1F 02 00 00               ja 0x140989450
00989231  F6 C2 01                        test dl, 1
00989234  0F 85 16 02 00 00               jne 0x140989450
0098923A  83 FA 08                        cmp edx, 8
0098923D  0F 82 0D 02 00 00               jb 0x140989450
00989243  41 8B 08                        mov ecx, dword ptr [r8]
00989246  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
0098924A  85 C8                           test eax, ecx
0098924C  0F 85 73 03 00 00               jne 0x1409895c5
00989252  8D 81 00 10 00 00               lea eax, [rcx + 0x1000]
00989258  3B C1                           cmp eax, ecx
0098925A  0F 86 F0 01 00 00               jbe 0x140989450
00989260  41 3B C2                        cmp eax, r10d
00989263  0F 87 E7 01 00 00               ja 0x140989450
00989269  41 3B C9                        cmp ecx, r9d
0098926C  0F 82 DE 01 00 00               jb 0x140989450
00989272  83 FA 08                        cmp edx, 8
00989275  0F 84 52 03 00 00               je 0x1409895cd
0098927B  48 F7 05 02 D8 63 00 00 00 02 00  test qword ptr [rip + 0x63d802], 0x20000
00989286  0F 85 52 01 00 00               jne 0x1409893de
0098928C  8B C1                           mov eax, ecx
0098928E  C1 E8 0C                        shr eax, 0xc
00989291  41 3B C7                        cmp eax, r15d
00989294  44 0F 47 F8                     cmova r15d, eax
00989298  8B C1                           mov eax, ecx
0098929A  48 C1 E8 0C                     shr rax, 0xc
0098929E  4D 09 44 C6 68                  or qword ptr [r14 + rax*8 + 0x68], r8
009892A3  8B C1                           mov eax, ecx
009892A5  25 00 F0 FF FF                  and eax, 0xfffff000
009892AA  05 00 10 00 00                  add eax, 0x1000
009892AF  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
009892B3  4D 8D 48 08                     lea r9, [r8 + 8]
009892B7  8B C2                           mov eax, edx
009892B9  4C 03 C0                        add r8, rax
009892BC  4C 89 44 24 48                  mov qword ptr [rsp + 0x48], r8
009892C1  2B F2                           sub esi, edx
009892C3  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
009892C7  44 8D 42 F8                     lea r8d, [rdx - 8]
009892CB  41 D1 E8                        shr r8d, 1
009892CE  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
009892D3  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
009892D8  8B D1                           mov edx, ecx
009892DA  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
009892DF  E8 8C 03 00 00                  call 0x140989670
009892E4  8B F0                           mov esi, eax
009892E6  85 C0                           test eax, eax
009892E8  0F 88 05 03 00 00               js 0x1409895f3
009892EE  83 CB 04                        or ebx, 4
009892F1  8B 74 24 30                     mov esi, dword ptr [rsp + 0x30]
009892F5  44 8B 4C 24 40                  mov r9d, dword ptr [rsp + 0x40]
009892FA  E9 02 FF FF FF                  jmp 0x140989201
009892FF  33 C0                           xor eax, eax
00989301  E9 61 FE FF FF                  jmp 0x140989167
00989306  48 8D 8C 24 D0 00 00 00         lea rcx, [rsp + 0xd0]
0098930E  E8 59 8D FB FF                  call 0x14094206c
00989313  8B 54 24 50                     mov edx, dword ptr [rsp + 0x50]
00989317  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0098931C  E8 1F 9A AD FF                  call 0x140462d40
00989321  83 E3 FE                        and ebx, 0xfffffffe
00989324  4D 8B 46 10                     mov r8, qword ptr [r14 + 0x10]
00989328  41 BA 00 10 00 00               mov r10d, 0x1000
0098932E  45 8D 5A FF                     lea r11d, [r10 - 1]
00989332  4D 85 C0                        test r8, r8
00989335  74 2D                           je 0x140989364
00989337  41 8B 50 0C                     mov edx, dword ptr [r8 + 0xc]
0098933B  8B C2                           mov eax, edx
0098933D  48 C1 E8 0C                     shr rax, 0xc
00989341  49 8B 4C C6 68                  mov rcx, qword ptr [r14 + rax*8 + 0x68]
00989346  8B C2                           mov eax, edx
00989348  C1 E8 0C                        shr eax, 0xc
0098934B  41 3B C7                        cmp eax, r15d
0098934E  41 0F 46 C7                     cmovbe eax, r15d
00989352  44 8B F8                        mov r15d, eax
00989355  48 83 F9 01                     cmp rcx, 1
00989359  0F 87 BB 00 00 00               ja 0x14098941a
0098935F  4D 8B 00                        mov r8, qword ptr [r8]
00989362  EB CE                           jmp 0x140989332
00989364  4D 8B C6                        mov r8, r14
00989367  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
0098936C  49 8B CD                        mov rcx, r13
0098936F  E8 78 85 FB FF                  call 0x1409418ec
00989374  41 8D 47 01                     lea eax, [r15 + 1]
00989378  41 89 46 38                     mov dword ptr [r14 + 0x38], eax
0098937C  8B C3                           mov eax, ebx
0098937E  83 E0 14                        and eax, 0x14
00989381  3C 14                           cmp al, 0x14
00989383  0F 84 90 02 00 00               je 0x140989619
00989389  49 8D 56 68                     lea rdx, [r14 + 0x68]
0098938D  41 8B 46 3C                     mov eax, dword ptr [r14 + 0x3c]
00989391  48 C1 E8 0C                     shr rax, 0xc
00989395  48 83 0C C2 01                  or qword ptr [rdx + rax*8], 1
0098939A  41 8A 45 3E                     mov al, byte ptr [r13 + 0x3e]
0098939E  24 0C                           and al, 0xc
009893A0  3C 04                           cmp al, 4
009893A2  0F 85 54 23 1A 00               jne 0x140b2b6fc
009893A8  4C 8D 84 24 80 00 00 00         lea r8, [rsp + 0x80]
009893B0  49 8B D6                        mov rdx, r14
009893B3  49 8B CD                        mov rcx, r13
009893B6  E8 15 07 00 00                  call 0x140989ad0
009893BB  8B F0                           mov esi, eax
009893BD  85 C0                           test eax, eax
009893BF  0F 89 37 23 1A 00               jns 0x140b2b6fc
009893C5  F6 C3 20                        test bl, 0x20
009893C8  0F 85 AA FC FF FF               jne 0x140989078
009893CE  49 8B D6                        mov rdx, r14
009893D1  49 8B CD                        mov rcx, r13
009893D4  E8 B3 5C FB FF                  call 0x14093f08c
009893D9  E9 9A FC FF FF                  jmp 0x140989078
009893DE  41 F7 45 5C 00 00 0C 00         test dword ptr [r13 + 0x5c], 0xc0000
009893E6  0F 84 A0 FE FF FF               je 0x14098928c
009893EC  48 83 A4 24 88 00 00 00 00      and qword ptr [rsp + 0x88], 0
009893F5  48 8B D1                        mov rdx, rcx
009893F8  4C 8D 84 24 88 00 00 00         lea r8, [rsp + 0x88]
00989400  49 8B CD                        mov rcx, r13
00989403  E8 78 44 8C FF                  call 0x14024d880
00989408  8B 40 20                        mov eax, dword ptr [rax + 0x20]
0098940B  A8 04                           test al, 4
0098940D  0F 84 CE 01 00 00               je 0x1409895e1
00989413  BE 7B 00 00 C0                  mov esi, 0xc000007b
00989418  EB AB                           jmp 0x1409893c5
0098941A  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
0098941E  8B 41 04                        mov eax, dword ptr [rcx + 4]
00989421  83 E8 08                        sub eax, 8
00989424  D1 E8                           shr eax, 1
00989426  41 23 D3                        and edx, r11d
00989429  4C 8D 49 08                     lea r9, [rcx + 8]
0098942D  85 C0                           test eax, eax
0098942F  0F 84 2A FF FF FF               je 0x14098935f
00989435  41 0F B7 09                     movzx ecx, word ptr [r9]
00989439  66 41 3B CA                     cmp cx, r10w
0098943D  73 08                           jae 0x140989447
0098943F  49 83 C1 02                     add r9, 2
00989443  FF C8                           dec eax
00989445  EB E6                           jmp 0x14098942d
00989447  66 41 23 CB                     and cx, r11w
0098944B  66 3B CA                        cmp cx, dx
0098944E  73 EF                           jae 0x14098943f
00989450  41 8B F4                        mov esi, r12d
00989453  E9 6D FF FF FF                  jmp 0x1409893c5
00989458  83 CB 40                        or ebx, 0x40
0098945B  45 84 58 2C                     test byte ptr [r8 + 0x2c], r11b
0098945F  75 79                           jne 0x1409894da
00989461  41 0F B7 40 2E                  movzx eax, word ptr [r8 + 0x2e]
00989466  BA 00 10 00 00                  mov edx, 0x1000
0098946B  66 23 C2                        and ax, dx
0098946E  66 F7 D8                        neg ax
00989471  45 1B E4                        sbb r12d, r12d
00989474  41 81 E4 7B 00 00 C0            and r12d, 0xc000007b
0098947B  E9 35 FA FF FF                  jmp 0x140988eb5
00989480  85 C9                           test ecx, ecx
00989482  0F 85 95 00 00 00               jne 0x14098951d
00989488  45 85 D2                        test r10d, r10d
0098948B  0F 85 8C 00 00 00               jne 0x14098951d
00989491  83 E3 FD                        and ebx, 0xfffffffd
00989494  E9 47 FA FF FF                  jmp 0x140988ee0
00989499  44 8D 4E 34                     lea r9d, [rsi + 0x34]
0098949D  44 89 4C 24 48                  mov dword ptr [rsp + 0x48], r9d
009894A2  E9 7B FA FF FF                  jmp 0x140988f22
009894A7  83 7C 24 38 00                  cmp dword ptr [rsp + 0x38], 0
009894AC  0F 85 9B FA FF FF               jne 0x140988f4d
009894B2  45 0F B7 40 2E                  movzx r8d, word ptr [r8 + 0x2e]
009894B7  41 F6 C0 40                     test r8b, 0x40
009894BB  0F 85 8C FA FF FF               jne 0x140988f4d
009894C1  83 3D 28 BD 63 00 FF            cmp dword ptr [rip + 0x63bd28], -1
009894C8  0F 84 7F FA FF FF               je 0x140988f4d
009894CE  66 41 0F BA E0 0C               bt r8w, 0xc
009894D4  0F 82 73 FA FF FF               jb 0x140988f4d
009894DA  33 C0                           xor eax, eax
009894DC  E9 B3 FB FF FF                  jmp 0x140989094
009894E1  45 8B F9                        mov r15d, r9d
009894E4  41 C1 EF 0C                     shr r15d, 0xc
009894E8  45 03 FB                        add r15d, r11d
009894EB  E9 6F FA FF FF                  jmp 0x140988f5f
009894F0  44 3B C1                        cmp r8d, ecx
009894F3  76 28                           jbe 0x14098951d
009894F5  85 F6                           test esi, esi
009894F7  0F 84 7E FA FF FF               je 0x140988f7b
009894FD  48 8D 04 0A                     lea rax, [rdx + rcx]
00989501  48 3B C2                        cmp rax, rdx
00989504  76 17                           jbe 0x14098951d
00989506  85 F6                           test esi, esi
00989508  0F 84 6D FA FF FF               je 0x140988f7b
0098950E  41 8B C0                        mov eax, r8d
00989511  48 03 C2                        add rax, rdx
00989514  48 3B C2                        cmp rax, rdx
00989517  0F 87 5E FA FF FF               ja 0x140988f7b
0098951D  41 8B C4                        mov eax, r12d
00989520  E9 6F FB FF FF                  jmp 0x140989094
00989525  B8 9A 00 00 C0                  mov eax, 0xc000009a
0098952A  E9 65 FB FF FF                  jmp 0x140989094
0098952F  33 D2                           xor edx, edx
00989531  49 8B CE                        mov rcx, r14
00989534  E8 37 93 1F 00                  call 0x140b82870
00989539  33 D2                           xor edx, edx
0098953B  49 8B CD                        mov rcx, r13
0098953E  E8 A5 43 B5 FF                  call 0x1404dd8e8
00989543  EB 95                           jmp 0x1409894da
00989545  49 8B C8                        mov rcx, r8
00989548  E8 F7 5B FB FF                  call 0x14093f144
0098954D  33 D2                           xor edx, edx
0098954F  49 8B CE                        mov rcx, r14
00989552  E8 19 93 1F 00                  call 0x140b82870
00989557  83 7C 24 38 00                  cmp dword ptr [rsp + 0x38], 0
0098955C  0F 85 16 FB FF FF               jne 0x140989078
00989562  41 8B F4                        mov esi, r12d
00989565  E9 0E FB FF FF                  jmp 0x140989078
0098956A  48 8B 05 BF EB 64 00            mov rax, qword ptr [rip + 0x64ebbf]
00989571  8B 50 0C                        mov edx, dword ptr [rax + 0xc]
00989574  4C 8B 48 20                     mov r9, qword ptr [rax + 0x20]
00989578  44 8B 84 24 E0 00 00 00         mov r8d, dword ptr [rsp + 0xe0]
00989580  41 C1 E0 0C                     shl r8d, 0xc
00989584  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
00989588  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
0098958D  E8 1E 3A 12 00                  call 0x140aacfb0
00989592  E9 9F FB FF FF                  jmp 0x140989136
00989597  8B 5C 24 40                     mov ebx, dword ptr [rsp + 0x40]
0098959B  83 CB 18                        or ebx, 0x18
0098959E  E9 ED FB FF FF                  jmp 0x140989190
009895A3  49 8B 4E 58                     mov rcx, qword ptr [r14 + 0x58]
009895A7  48 85 C9                        test rcx, rcx
009895AA  0F 84 3C FC FF FF               je 0x1409891ec
009895B0  44 8B BC 24 E0 00 00 00         mov r15d, dword ptr [rsp + 0xe0]
009895B8  41 C1 E7 0C                     shl r15d, 0xc
009895BC  41 C1 EF 0C                     shr r15d, 0xc
009895C0  E9 0B 21 1A 00                  jmp 0x140b2b6d0
009895C5  83 E3 EF                        and ebx, 0xffffffef
009895C8  E9 85 FC FF FF                  jmp 0x140989252
009895CD  83 C6 F8                        add esi, -8
009895D0  49 83 C0 08                     add r8, 8
009895D4  4C 89 44 24 48                  mov qword ptr [rsp + 0x48], r8
009895D9  83 E3 EF                        and ebx, 0xffffffef
009895DC  E9 2A FC FF FF                  jmp 0x14098920b
009895E1  8B 4C 24 30                     mov ecx, dword ptr [rsp + 0x30]
009895E5  8B 54 24 40                     mov edx, dword ptr [rsp + 0x40]
009895E9  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
009895EE  E9 99 FC FF FF                  jmp 0x14098928c
009895F3  81 FE 69 02 00 C0               cmp esi, 0xc0000269
009895F9  0F 85 EE 20 1A 00               jne 0x140b2b6ed
009895FF  33 F6                           xor esi, esi
00989601  E9 BF FD FF FF                  jmp 0x1409893c5
00989606  83 FE 08                        cmp esi, 8
00989609  0F 85 41 FE FF FF               jne 0x140989450
0098960F  83 44 24 34 F8                  add dword ptr [rsp + 0x34], -8
00989614  E9 ED FC FF FF                  jmp 0x140989306
00989619  8B 54 24 34                     mov edx, dword ptr [rsp + 0x34]
0098961D  49 8B CE                        mov rcx, r14
00989620  E8 DB CF FD FF                  call 0x140966600
00989625  4C 8B F0                        mov r14, rax
00989628  48 8D 50 68                     lea rdx, [rax + 0x68]
0098962C  E9 5C FD FF FF                  jmp 0x14098938d
00989631  48 8D 8C 24 D0 00 00 00         lea rcx, [rsp + 0xd0]
00989639  E8 2E 8A FB FF                  call 0x14094206c
0098963E  8B 54 24 50                     mov edx, dword ptr [rsp + 0x50]
00989642  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00989647  E8 F4 96 AD FF                  call 0x140462d40
0098964C  E9 30 FA FF FF                  jmp 0x140989081
00989651  33 D2                           xor edx, edx
00989653  E8 18 92 1F 00                  call 0x140b82870
00989658  E9 35 FA FF FF                  jmp 0x140989092
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiRelocateImage(__int64 a1, __int64 a2, int a3, int a4, __int64 a5, unsigned __int8 a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m108;
    unsigned int v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m120;
    unsigned int v_stack_m124;
    unsigned int v_stack_m128;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mDC;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned int v_stack_p34;
    unsigned int v_stack_p38;
    unsigned int v_stack_p40;
    unsigned int v_stack_p48;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pD0;
    unsigned int v_stack_pE0;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (304);
    result = (*(unsigned __int64 *)(v_rip + 4725008)) ^ (v_rsp);
    v_stack_m38 = result;
    v_stack_m120 = a4;
    v_stack_mB8 = a2;
    v_stack_mC8 = a1;
    a2 = 0;
    result = memset(v_stack_m88, a2, a2 + 80, a4);
    v_rbx = (unsigned int)(((unsigned int)(a6)) & (1));
    v_rbx = (unsigned int)((v_rbx) << (8));
    v_rbx = (unsigned int)((v_rbx) + (2));
    v_stack_m98 = *(unsigned __int64 *)(a1 + 56);
    result = MiLegacyImageArchitecture(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 56) + 48), a2, *(unsigned __int64 *)(a1 + 56), a4);
    if ((unsigned int)(result) != 0) goto loc_00989458;
loc_00988EB5:
    v_stack_m128 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 88)));
    v_stack_mE0 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 88)));
    v_stack_m124 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 92)));
    v_stack_mDC = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 92)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 88))) == 0) goto loc_00989488;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 92))) == 0) goto loc_00989480;
loc_00988EE0:
    if (condition_is_below) goto loc_009894DA;
    v_stack_mA8 = *(unsigned __int64 *)(a1);
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 96)) & (-8);
    v_stack_mA0 = a2;
    v_stack_m110 = (unsigned int)((unsigned int)(a3) + 48);
    result = (unsigned __int16)((*(unsigned __int16 *)(a1 + 12)) >> (15));
    if (((unsigned __int16)(result)) == 1) goto loc_00989499;
loc_00988F22:
    result = (unsigned int)(((unsigned __int16)(result)) ^ (1));
    if ((((unsigned int)((unsigned int)(a3) + 48)) & ((unsigned int)(result * 4 + 3))) != 0) goto loc_0098951D;
    v_stack_mD0 = *(unsigned __int64 *)(a1 + 32);
    if ((((unsigned __int8)(v_rbx)) & (64)) != 0) goto loc_009894A7;
loc_00988F4D:
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (2));
    if (condition_is_equal) goto loc_009894E1;
loc_00988F5F:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 8))) << (12));
    v_stack_mF8 = (unsigned int)(result);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 92)) + (unsigned int)(*(unsigned int *)(a2 + 88)) * 1)) > ((unsigned int)(result))) goto loc_0098951D;
    if ((unsigned int)(v_rsi) != 0) goto loc_009894F0;
loc_00988F7B:
    v_r10 = ((unsigned int)(*(unsigned int *)(a2 + 92))) + (104);
    v_stack_m118 = v_r10 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)))))) * 8;
    v_stack_mF0 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = MiAllocatePool(256, v_r10 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)))))) * 8, (unsigned int)(0x65526D4DULL), (unsigned int)(a3) + 48);
    v_stack_mB0 = result;
    if (result == 0) goto loc_00989525;
    a2 = (v_stack_m118) + (result);
loc_00988FDC:
    a1 = (result) + (0x1000ULL);
    if (a1 < a2) goto loc_00988FDC;
    *(unsigned __int8 *)(result + 64) = 0;
    *(unsigned int *)(result + 56) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)))));
    if ((unsigned int)(v_rsi) == 0) goto loc_009890BE;
    result = MiMapImageInSystemSpace(*(unsigned __int64 *)(a1), 3, v_stack_m88, (unsigned int)(a3) + 48);
    if (sign_flag) goto loc_0098952F;
    v_stack_mE8 = v_stack_m88;
    result = PsSetSystemPagePriorityThread(v_stack_mF0, 1, v_stack_m88, (unsigned int)(a3) + 48);
    v_stack_m108 = (unsigned int)(result);
    v_rbx = (unsigned int)((v_rbx) | (1));
    a4 = (unsigned int)(((unsigned int)(v_stack_m78)) << (12));
    v_stack_m138 = result + 72;
    result = MiParseImageLoadConfig(*(unsigned __int64 *)(a1), v_stack_m88, v_stack_mB8, a4);
    if (!sign_flag) goto loc_009890BE;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_stack_mB8, a4);
loc_00989078:
    if ((((unsigned __int8)(v_rbx)) & (1)) != 0) goto loc_00989631;
loc_00989081:
    if (v_stack_mD8 != 0) goto loc_00989651;
loc_00989092:
loc_00989094:
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_stack_mB8, a4);
    v_rsp = (v_rsp) + (304);
    return result;
loc_009890BE:
    v_stack_p40 = (unsigned int)(v_stack_p20);
    result = 0;
    result = (((unsigned int)(v_stack_p20)) >= 256) ? 1 : 0;
    a4 = (unsigned int)(((unsigned int)((unsigned int)(result))) | (2));
    if (((a6) & (2)) == 0) { a4 = (unsigned int)(result); }
    v_stack_p20 = v_stack_p58;
    result = MiSelectImageBase(v_stack_p90, result, (unsigned int)(v_stack_p38), a4);
    if (sign_flag) goto loc_00989545;
    result = MiUpdateImageSystemWideBitmaps(*(unsigned __int64 *)(a1), v_stack_p58, result + 72, a4);
    if (sign_flag) goto loc_009893CE;
    if ((((unsigned __int8)(v_stack_p20)) & (2)) == 0) goto loc_00989136;
    if (*(unsigned __int64 *)(result + 96) != 0) goto loc_0098956A;
loc_00989136:
    *(unsigned int *)(result + 60) = (unsigned int)((unsigned int)(v_stack_p48));
    result = (v_stack_p58) - (v_stack_p88);
    *(unsigned __int64 *)(result + 40) = result;
    if (a5 == -1) goto loc_009892FF;
    result = (a5) - (v_stack_p88);
loc_00989167:
    *(unsigned __int64 *)(result + 48) = result;
    *(unsigned __int64 *)(result) = result + 104;
    v_stack_p48 = result + 104 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)))))) * 8;
    *(unsigned __int64 *)(result + 32) = result + 104 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)))))) * 8;
    v_rbx = (unsigned int)((v_stack_p20) | (16));
    if ((*(unsigned __int64 *)(result + 88)) != 0) goto loc_00989597;
loc_00989190:
    if ((*(unsigned __int64 *)(result + 96)) == 0) { v_rbx = (unsigned int)((unsigned int)((unsigned int)(v_rbx))); }
    v_stack_p40 = (unsigned int)(v_rbx);
    if ((((unsigned __int8)(v_rbx)) & (2)) == 0) goto loc_0098938D;
    a2 = ((unsigned int)(v_stack_p30)) + (v_stack_p70);
    result = memcpy(result + 104 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)))))) * 8, a2, (unsigned int)((unsigned int)((unsigned int)(v_stack_p34))), result + 104 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)))))) * 8);
    goto loc_009891E0;
loc_009891E0:
    v_r15 = 0;
    if ((((unsigned __int8)(v_rbx)) & (8)) != 0) goto loc_009895A3;
loc_009891EC:
    if (sign_flag) {
        result = *(unsigned __int64 *)(result + 96);
        a1 = *(unsigned int *)(result + 36);
        if (0 <= ((unsigned int)(a1))) { v_r15 = (unsigned int)(a1); }
    }
    a4 = 0;
loc_00989201:
loc_0098920B:
    if ((unsigned int)((unsigned int)(v_stack_p34)) == 0) goto loc_00989306;
    if (((unsigned int)((unsigned int)(v_stack_p34))) < 10) goto loc_00989606;
    v_stack_p40 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48 + 4)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48 + 4)))) > ((unsigned int)((unsigned int)(v_stack_p34)))) goto loc_00989450;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p48 + 4)))) & (1)) != 0) goto loc_00989450;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48 + 4)))) < 8) goto loc_00989450;
    v_stack_p30 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48)));
    if ((((unsigned int)((unsigned int)(0xFFFULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48))))) != 0) goto loc_009895C5;
loc_00989252:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48)) + 4096)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48))))) goto loc_00989450;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48)) + 4096)) > ((unsigned int)((unsigned int)(v_stack_p60)))) goto loc_00989450;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48)))) < 0) goto loc_00989450;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48 + 4)))) == 8) goto loc_009895CD;
    if (((*(unsigned __int64 *)(v_rip + 6543362)) & (0x20000ULL)) != 0) goto loc_009893DE;
loc_0098928C:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48))))) >> (12));
    if (((unsigned int)(result)) > ((unsigned int)(v_r15))) { v_r15 = (unsigned int)(result); }
    result = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48))))) >> (12);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48))))) & (0xFFFFF000ULL));
    result = (unsigned int)((result) + (0x1000ULL));
    v_stack_p40 = (unsigned int)(result);
    a3 = (v_stack_p48) + ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48 + 4)))));
    v_stack_p48 = a3;
    v_rsi = (unsigned int)(((unsigned int)(v_stack_p34)) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48 + 4)))));
    v_stack_p30 = (unsigned int)(v_rsi);
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p48 + 4)) - 8) >> (1));
    v_stack_p28 = result;
    v_stack_p20 = *(unsigned __int64 *)(a1);
    result = MiScanRelocationPage(v_stack_p70, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48)))), a3, v_stack_p48 + 8);
    if (sign_flag) goto loc_009895F3;
    v_rbx = (unsigned int)((v_rbx) | (4));
    goto loc_00989201;
loc_009892FF:
    result = 0;
    goto loc_00989167;
loc_00989306:
    result = MiUnmapImageInSystemSpace(v_stack_pD0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48)))), a3, (unsigned int)(v_stack_p40));
    result = PsRevertToUserPagePriorityThread(v_stack_p68, (unsigned int)(v_stack_p50), a3, (unsigned int)(v_stack_p40));
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFFEULL));
loc_00989332:
    if (*(unsigned __int64 *)(result + 16) == 0) goto loc_00989364;
    result = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 16) + 12))))) >> (12);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 16) + 12))))) >> (12));
    if (((unsigned int)(result)) <= ((unsigned int)(v_r15))) { result = (unsigned int)(v_r15); }
    if ((*(unsigned __int64 *)(result + result * 8 + 104)) > 1) goto loc_0098941A;
loc_0098935F:
    goto loc_00989332;
loc_00989364:
    result = MiLogRelocationFaults(*(unsigned __int64 *)(a1), v_stack_p78, result, (unsigned int)(v_stack_p40));
    *(unsigned int *)(result + 56) = (unsigned int)((unsigned int)((unsigned int)(result)) + 1);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (20));
    if (((unsigned __int8)(result)) == 20) goto loc_00989619;
loc_0098938D:
    result = ((unsigned int)(*(unsigned int *)(result + 60))) >> (12);
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 62)) & (12));
    result = MiCreateFileOnlyImageFixupList(*(unsigned __int64 *)(a1), result, v_stack_p80, (unsigned int)(v_stack_p40));
loc_009893C5:
    if ((((unsigned __int8)(v_rbx)) & (32)) != 0) goto loc_00989078;
loc_009893CE:
    result = MiFreeRelocations(*(unsigned __int64 *)(a1), result, v_stack_p80, (unsigned int)(v_stack_p40));
    goto loc_00989078;
loc_009893DE:
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1) + 92)) & (0xC0000ULL)) == 0) goto loc_0098928C;
    result = MiOffsetToProtos(*(unsigned __int64 *)(a1), *(unsigned __int64 *)(a1), v_stack_p88, (unsigned int)(v_stack_p40));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 32)))) & (4)) == 0) goto loc_009895E1;
    goto loc_009893C5;
loc_0098941A:
    a1 = (*(unsigned __int64 *)(a1)) & (-2);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 4))) - (8));
    result = (unsigned int)((result) >> (1));
    a2 = (unsigned int)((*(unsigned __int64 *)(a1)) & ((unsigned int)((unsigned int)(0x1000ULL) - 1)));
loc_0098942D:
    if ((unsigned int)(result) == 0) goto loc_0098935F;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 8))) >= ((unsigned __int16)((unsigned int)(0x1000ULL)))) goto loc_00989447;
loc_0098943F:
    a4 = (a1 + 8) + (2);
    result = (unsigned int)((result) - 1);
    goto loc_0098942D;
loc_00989447:
    a1 = (unsigned __int16)((*(unsigned __int16 *)(a1 + 8)) & ((unsigned __int16)((unsigned int)(0x1000ULL) - 1)));
    if (((unsigned __int16)(a1)) >= ((unsigned __int16)(a2))) goto loc_0098943F;
loc_00989450:
    goto loc_009893C5;
loc_00989458:
    v_rbx = (unsigned int)((v_rbx) | (64));
    if (((*(unsigned __int8 *)(v_stack_p88 + 44)) & ((unsigned __int8)((unsigned int)(0x1000ULL) - 1))) != 0) goto loc_009894DA;
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_p88 + 46)) & ((unsigned __int16)((unsigned int)(0x1000ULL))));
    result = (unsigned __int16)(-(result));
    v_r12 = (unsigned int)(((unsigned int)(0xC000007BULL)) & (0xC000007BULL));
    goto loc_00988EB5;
loc_00989480:
    if ((unsigned int)(a1) != 0) goto loc_0098951D;
loc_00989488:
    if ((unsigned int)((unsigned int)(0x1000ULL)) != 0) goto loc_0098951D;
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFFDULL));
    goto loc_00988EE0;
loc_00989499:
    v_stack_p48 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000007BULL))) + 52);
    goto loc_00988F22;
loc_009894A7:
    if (v_stack_p38 != 0) goto loc_00988F4D;
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_stack_p88 + 46))) & (64)) != 0) goto loc_00988F4D;
    if ((*(unsigned int *)(v_rip + 6536488)) == -1) goto loc_00988F4D;
    if ((*(unsigned int *)(v_rip + 6536488)) < -1) goto loc_00988F4D;
loc_009894DA:
    result = 0;
    goto loc_00989094;
loc_009894E1:
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000007BULL))) + 52))) >> (12));
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)((unsigned int)(0x1000ULL) - 1)));
    goto loc_00988F5F;
loc_009894F0:
    if (((unsigned int)(*(unsigned __int16 *)(v_stack_p88 + 46))) <= ((unsigned int)(a1))) goto loc_0098951D;
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000007BULL)))) == 0) goto loc_00988F7B;
    if (((unsigned int)(0x1000ULL) + a1 * 1) <= ((unsigned int)(0x1000ULL))) goto loc_0098951D;
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000007BULL)))) == 0) goto loc_00988F7B;
    result = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_p88 + 46)))) + ((unsigned int)(0x1000ULL));
    if (result > ((unsigned int)(0x1000ULL))) goto loc_00988F7B;
loc_0098951D:
    goto loc_00989094;
loc_00989525:
    goto loc_00989094;
loc_0098952F:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, *(unsigned __int16 *)(v_stack_p88 + 46), (unsigned int)((unsigned int)((unsigned int)(0xC000007BULL))) + 52);
    a2 = 0;
    result = MiSetDeleteOnClose(*(unsigned __int64 *)(a1), a2, *(unsigned __int16 *)(v_stack_p88 + 46), (unsigned int)((unsigned int)((unsigned int)(0xC000007BULL))) + 52);
    goto loc_009894DA;
loc_00989545:
    result = MiFreeImageLoadConfig(*(unsigned __int16 *)(v_stack_p88 + 46), a2, *(unsigned __int16 *)(v_stack_p88 + 46), (unsigned int)((unsigned int)((unsigned int)(0xC000007BULL))) + 52);
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, *(unsigned __int16 *)(v_stack_p88 + 46), (unsigned int)((unsigned int)((unsigned int)(0xC000007BULL))) + 52);
    if (v_stack_p38 != 0) goto loc_00989078;
    goto loc_00989078;
loc_0098956A:
    a3 = (unsigned int)(((unsigned int)(v_stack_pE0)) << (12));
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 6613951) + 12)));
    result = RtlInitializeSystemOverrideDelta(result, v_stack_p58, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6613951) + 32));
    goto loc_00989136;
loc_00989597:
    v_rbx = (unsigned int)(((unsigned int)(v_stack_p40)) | (24));
    goto loc_00989190;
loc_009895A3:
    if (*(unsigned __int64 *)(result + 88) == 0) goto loc_009891EC;
    v_r15 = (unsigned int)(((unsigned int)(v_stack_pE0)) << (12));
    v_r15 = (unsigned int)((v_r15) >> (12));
loc_009895C5:
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFEFULL));
    goto loc_00989252;
loc_009895CD:
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) + (-8));
    a3 = (a3) + (8);
    v_stack_p48 = a3;
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFEFULL));
    goto loc_0098920B;
loc_009895E1:
    goto loc_0098928C;
loc_009895F3:
    v_rsi = 0;
    goto loc_009893C5;
loc_00989606:
    if (0 != 8) goto loc_00989450;
    goto loc_00989306;
loc_00989619:
    result = MiCompressRelocations(result, (unsigned int)(v_stack_p34), v_stack_p48, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6613951) + 32));
    goto loc_0098938D;
loc_00989631:
    result = MiUnmapImageInSystemSpace(v_stack_pD0, result + 104, v_stack_p48, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6613951) + 32));
    result = PsRevertToUserPagePriorityThread(v_stack_p68, (unsigned int)(v_stack_p50), v_stack_p48, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6613951) + 32));
    goto loc_00989081;
loc_00989651:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_p68, a2, v_stack_p48, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6613951) + 32));
    goto loc_00989092;
}
```

## 5. (Beta) C Style

```c
int64_t MiRelocateImage(void *Arg1, void *Arg2, void *Arg3, int32_t Arg4, int64_t Arg5, uint8_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m108;
    uint32_t v_stack_m110;
    uint64_t v_stack_m118;
    uint32_t v_stack_m120;
    uint32_t v_stack_m124;
    uint32_t v_stack_m128;
    uint64_t v_stack_m138;
    uint64_t v_stack_m38;
    uint32_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mDC;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint32_t v_stack_p34;
    uint32_t v_stack_p38;
    uint32_t v_stack_p40;
    uint32_t v_stack_p48;
    uint32_t v_stack_p50;
    uint64_t v_stack_p58;
    uint32_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p80;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pD0;
    uint32_t v_stack_pE0;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (304);
    result = (*(uint64_t *)(v_rip + 0x481910)) ^ (local_rsp);
    v_stack_m38 = result;
    v_stack_m120 = Arg4;
    v_stack_mB8 = Arg2;
    v_stack_mC8 = Arg1;
    Arg2 = 0;
    result = memset(v_stack_m88, Arg2, Arg2 + 80, Arg4);
    local_rbx = (uint32_t)(((uint32_t)(Arg6)) & (1));
    local_rbx = (uint32_t)((local_rbx) << (8));
    local_rbx = (uint32_t)((local_rbx) + (2));
    v_stack_m98 = *(uint64_t *)(arg1 + 0x38);
    result = MiLegacyImageArchitecture(*(uint16_t *)(*(uint64_t *)(arg1 + 0x38) + 0x30), Arg2, *(uint64_t *)(arg1 + 0x38), Arg4);
    if ((uint32_t)(result) != 0) goto loc_00989458;
loc_00988EB5:
    v_stack_m128 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x58)));
    v_stack_mE0 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x58)));
    v_stack_m124 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x5C)));
    v_stack_mDC = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x5C)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x58))) == 0) goto loc_00989488;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x5C))) == 0) goto loc_00989480;
loc_00988EE0:
    if (condition_is_below) goto loc_009894DA;
    v_stack_mA8 = *(uint64_t *)(arg1);
    Arg2 = (*(uint64_t *)(*(uint64_t *)(arg1) + 0x60)) & (-8);
    v_stack_mA0 = Arg2;
    v_stack_m110 = (uint32_t)((uint32_t)(Arg3) + 48);
    result = (uint16_t)((*(uint16_t *)(arg1 + 0xC)) >> (15));
    if (((uint16_t)(result)) == 1) goto loc_00989499;
loc_00988F22:
    result = (uint32_t)(((uint16_t)(result)) ^ (1));
    if ((((uint32_t)((uint32_t)(Arg3) + 48)) & ((uint32_t)(result * 4 + 3))) != 0) goto loc_0098951D;
    v_stack_mD0 = *(uint64_t *)(arg1 + 0x20);
    if ((((uint8_t)(local_rbx)) & (64)) != 0) goto loc_009894A7;
loc_00988F4D:
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (2));
    if (condition_is_equal) goto loc_009894E1;
loc_00988F5F:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x8))) << (12));
    v_stack_mF8 = (uint32_t)(result);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x5C)) + (uint32_t)(*(uint32_t *)(arg2 + 0x58)) * 1)) > ((uint32_t)(result))) goto loc_0098951D;
    if ((uint32_t)(local_rsi) != 0) goto loc_009894F0;
loc_00988F7B:
    local_r10 = ((uint32_t)(*(uint32_t *)(arg2 + 0x5C))) + (104);
    v_stack_m118 = local_r10 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)))))) * 8;
    v_stack_mF0 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = MiAllocatePool(256, local_r10 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)))))) * 8, (uint32_t)(0x65526D4DULL), (uint32_t)(Arg3) + 48);
    v_stack_mB0 = result;
    if (result == 0) goto loc_00989525;
    Arg2 = (v_stack_m118) + (result);
loc_00988FDC:
    Arg1 = (result) + (0x1000ULL);
    if (Arg1 < Arg2) goto loc_00988FDC;
    *(uint8_t *)(result + 0x40) = 0;
    *(uint32_t *)(result + 0x38) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)))));
    if ((uint32_t)(local_rsi) == 0) goto loc_009890BE;
    result = MiMapImageInSystemSpace(*(uint64_t *)(arg1), 3, v_stack_m88, (uint32_t)(Arg3) + 48);
    if (sign_flag) goto loc_0098952F;
    v_stack_mE8 = v_stack_m88;
    result = PsSetSystemPagePriorityThread(v_stack_mF0, 1, v_stack_m88, (uint32_t)(Arg3) + 48);
    v_stack_m108 = (uint32_t)(result);
    local_rbx = (uint32_t)((local_rbx) | (1));
    Arg4 = (uint32_t)(((uint32_t)(v_stack_m78)) << (12));
    v_stack_m138 = result + 72;
    result = MiParseImageLoadConfig(*(uint64_t *)(arg1), v_stack_m88, v_stack_mB8, Arg4);
    if (!sign_flag) goto loc_009890BE;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, v_stack_mB8, Arg4);
loc_00989078:
    if ((((uint8_t)(local_rbx)) & (1)) != 0) goto loc_00989631;
loc_00989081:
    if (v_stack_mD8 != 0) goto loc_00989651;
loc_00989092:
loc_00989094:
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_stack_mB8, Arg4);
    local_rsp = (local_rsp) + (304);
    return result;
loc_009890BE:
    v_stack_p40 = (uint32_t)(v_stack_p20);
    result = 0;
    result = (((uint32_t)(v_stack_p20)) >= 256) ? 1 : 0;
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)(result))) | (2));
    if (((Arg6) & (2)) == 0) { Arg4 = (uint32_t)(result); }
    v_stack_p20 = v_stack_p58;
    result = MiSelectImageBase(v_stack_p90, result, (uint32_t)(v_stack_p38), Arg4);
    if (sign_flag) goto loc_00989545;
    result = MiUpdateImageSystemWideBitmaps(*(uint64_t *)(arg1), v_stack_p58, result + 72, Arg4);
    if (sign_flag) goto loc_009893CE;
    if ((((uint8_t)(v_stack_p20)) & (2)) == 0) goto loc_00989136;
    if (*(uint64_t *)(result + 0x60) != 0) goto loc_0098956A;
loc_00989136:
    *(uint32_t *)(result + 0x3C) = (uint32_t)((uint32_t)(v_stack_p48));
    result = (v_stack_p58) - (v_stack_p88);
    *(uint64_t *)(result + 0x28) = result;
    if (Arg5 == -1) goto loc_009892FF;
    result = (Arg5) - (v_stack_p88);
loc_00989167:
    *(uint64_t *)(result + 0x30) = result;
    *(uint64_t *)(result) = result + 104;
    v_stack_p48 = result + 104 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)))))) * 8;
    *(uint64_t *)(result + 0x20) = result + 104 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)))))) * 8;
    local_rbx = (uint32_t)((v_stack_p20) | (16));
    if ((*(uint64_t *)(result + 0x58)) != 0) goto loc_00989597;
loc_00989190:
    if ((*(uint64_t *)(result + 0x60)) == 0) { local_rbx = (uint32_t)((uint32_t)((uint32_t)(local_rbx))); }
    v_stack_p40 = (uint32_t)(local_rbx);
    if ((((uint8_t)(local_rbx)) & (2)) == 0) goto loc_0098938D;
    Arg2 = ((uint32_t)(v_stack_p30)) + (v_stack_p70);
    result = memcpy(result + 104 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)))))) * 8, Arg2, (uint32_t)((uint32_t)((uint32_t)(v_stack_p34))), result + 104 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)))))) * 8);
    goto loc_009891E0;
loc_009891E0:
    local_r15 = 0;
    if ((((uint8_t)(local_rbx)) & (8)) != 0) goto loc_009895A3;
loc_009891EC:
    if (sign_flag) {
        result = *(uint64_t *)(result + 0x60);
        Arg1 = *(uint32_t *)(result + 0x24);
        if (0 <= ((uint32_t)(Arg1))) { local_r15 = (uint32_t)(Arg1); }
    }
    Arg4 = 0;
loc_00989201:
loc_0098920B:
    if ((uint32_t)((uint32_t)(v_stack_p34)) == 0) goto loc_00989306;
    if (((uint32_t)((uint32_t)(v_stack_p34))) < 10) goto loc_00989606;
    v_stack_p40 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48 + 0x4)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48 + 0x4)))) > ((uint32_t)((uint32_t)(v_stack_p34)))) goto loc_00989450;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p48 + 0x4)))) & (1)) != 0) goto loc_00989450;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48 + 0x4)))) < 8) goto loc_00989450;
    v_stack_p30 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48)));
    if ((((uint32_t)((uint32_t)(0xFFFULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48))))) != 0) goto loc_009895C5;
loc_00989252:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48)) + 4096)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48))))) goto loc_00989450;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48)) + 4096)) > ((uint32_t)((uint32_t)(v_stack_p60)))) goto loc_00989450;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48)))) < 0) goto loc_00989450;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48 + 0x4)))) == 8) goto loc_009895CD;
    if (((*(uint64_t *)(v_rip + 0x63D802)) & (0x20000ULL)) != 0) goto loc_009893DE;
loc_0098928C:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48))))) >> (12));
    if (((uint32_t)(result)) > ((uint32_t)(local_r15))) { local_r15 = (uint32_t)(result); }
    result = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48))))) >> (12);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48))))) & (0xFFFFF000ULL));
    result = (uint32_t)((result) + (0x1000ULL));
    v_stack_p40 = (uint32_t)(result);
    Arg3 = (v_stack_p48) + ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48 + 0x4)))));
    v_stack_p48 = Arg3;
    local_rsi = (uint32_t)(((uint32_t)(v_stack_p34)) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48 + 0x4)))));
    v_stack_p30 = (uint32_t)(local_rsi);
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p48 + 0x4)) - 8) >> (1));
    v_stack_p28 = result;
    v_stack_p20 = *(uint64_t *)(arg1);
    result = MiScanRelocationPage(v_stack_p70, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48)))), Arg3, v_stack_p48 + 8);
    if (sign_flag) goto loc_009895F3;
    local_rbx = (uint32_t)((local_rbx) | (4));
    goto loc_00989201;
loc_009892FF:
    result = 0;
    goto loc_00989167;
loc_00989306:
    result = MiUnmapImageInSystemSpace(v_stack_pD0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48)))), Arg3, (uint32_t)(v_stack_p40));
    result = PsRevertToUserPagePriorityThread(v_stack_p68, (uint32_t)(v_stack_p50), Arg3, (uint32_t)(v_stack_p40));
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFFEULL));
loc_00989332:
    if (*(uint64_t *)(result + 0x10) == 0) goto loc_00989364;
    result = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x10) + 0xC))))) >> (12);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x10) + 0xC))))) >> (12));
    if (((uint32_t)(result)) <= ((uint32_t)(local_r15))) { result = (uint32_t)(local_r15); }
    if ((*(uint64_t *)(result + result * 8 + 0x68)) > 1) goto loc_0098941A;
loc_0098935F:
    goto loc_00989332;
loc_00989364:
    result = MiLogRelocationFaults(*(uint64_t *)(arg1), v_stack_p78, result, (uint32_t)(v_stack_p40));
    *(uint32_t *)(result + 0x38) = (uint32_t)((uint32_t)((uint32_t)(result)) + 1);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (20));
    if (((uint8_t)(result)) == 20) goto loc_00989619;
loc_0098938D:
    result = ((uint32_t)(*(uint32_t *)(result + 0x3C))) >> (12);
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1) + 0x3E)) & (12));
    result = MiCreateFileOnlyImageFixupList(*(uint64_t *)(arg1), result, v_stack_p80, (uint32_t)(v_stack_p40));
loc_009893C5:
    if ((((uint8_t)(local_rbx)) & (32)) != 0) goto loc_00989078;
loc_009893CE:
    result = MiFreeRelocations(*(uint64_t *)(arg1), result, v_stack_p80, (uint32_t)(v_stack_p40));
    goto loc_00989078;
loc_009893DE:
    if (((*(uint32_t *)(*(uint64_t *)(arg1) + 0x5C)) & (0xC0000ULL)) == 0) goto loc_0098928C;
    result = MiOffsetToProtos(*(uint64_t *)(arg1), *(uint64_t *)(arg1), v_stack_p88, (uint32_t)(v_stack_p40));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x20)))) & (4)) == 0) goto loc_009895E1;
    goto loc_009893C5;
loc_0098941A:
    Arg1 = (*(uint64_t *)(arg1)) & (-2);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x4))) - (8));
    result = (uint32_t)((result) >> (1));
    Arg2 = (uint32_t)((*(uint64_t *)(arg1)) & ((uint32_t)((uint32_t)(0x1000ULL) - 1)));
loc_0098942D:
    if ((uint32_t)(result) == 0) goto loc_0098935F;
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x8))) >= ((uint16_t)((uint32_t)(0x1000ULL)))) goto loc_00989447;
loc_0098943F:
    Arg4 = (Arg1 + 8) + (2);
    result = (uint32_t)((result) - 1);
    goto loc_0098942D;
loc_00989447:
    Arg1 = (uint16_t)((*(uint16_t *)(arg1 + 0x8)) & ((uint16_t)((uint32_t)(0x1000ULL) - 1)));
    if (((uint16_t)(Arg1)) >= ((uint16_t)(Arg2))) goto loc_0098943F;
loc_00989450:
    goto loc_009893C5;
loc_00989458:
    local_rbx = (uint32_t)((local_rbx) | (64));
    if (((*(uint8_t *)(v_stack_p88 + 0x2C)) & ((uint8_t)((uint32_t)(0x1000ULL) - 1))) != 0) goto loc_009894DA;
    result = (uint16_t)((*(uint16_t *)(v_stack_p88 + 0x2E)) & ((uint16_t)((uint32_t)(0x1000ULL))));
    result = (uint16_t)(-(result));
    local_r12 = (uint32_t)(((uint32_t)(0xC000007BULL)) & (0xC000007BULL));
    goto loc_00988EB5;
loc_00989480:
    if ((uint32_t)(Arg1) != 0) goto loc_0098951D;
loc_00989488:
    if ((uint32_t)((uint32_t)(0x1000ULL)) != 0) goto loc_0098951D;
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFFDULL));
    goto loc_00988EE0;
loc_00989499:
    v_stack_p48 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000007BULL))) + 52);
    goto loc_00988F22;
loc_009894A7:
    if (v_stack_p38 != 0) goto loc_00988F4D;
    if ((((uint8_t)(*(uint16_t *)(v_stack_p88 + 0x2E))) & (64)) != 0) goto loc_00988F4D;
    if ((*(uint32_t *)(v_rip + 0x63BD28)) == -1) goto loc_00988F4D;
    if ((*(uint32_t *)(v_rip + 0x63BD28)) < -1) goto loc_00988F4D;
loc_009894DA:
    result = 0;
    goto loc_00989094;
loc_009894E1:
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000007BULL))) + 52))) >> (12));
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)((uint32_t)(0x1000ULL) - 1)));
    goto loc_00988F5F;
loc_009894F0:
    if (((uint32_t)(*(uint16_t *)(v_stack_p88 + 0x2E))) <= ((uint32_t)(Arg1))) goto loc_0098951D;
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000007BULL)))) == 0) goto loc_00988F7B;
    if (((uint32_t)(0x1000ULL) + Arg1 * 1) <= ((uint32_t)(0x1000ULL))) goto loc_0098951D;
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000007BULL)))) == 0) goto loc_00988F7B;
    result = ((uint32_t)((uint32_t)(*(uint16_t *)(v_stack_p88 + 0x2E)))) + ((uint32_t)(0x1000ULL));
    if (result > ((uint32_t)(0x1000ULL))) goto loc_00988F7B;
loc_0098951D:
    goto loc_00989094;
loc_00989525:
    goto loc_00989094;
loc_0098952F:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, *(uint16_t *)(v_stack_p88 + 0x2E), (uint32_t)((uint32_t)((uint32_t)(0xC000007BULL))) + 52);
    Arg2 = 0;
    result = MiSetDeleteOnClose(*(uint64_t *)(arg1), Arg2, *(uint16_t *)(v_stack_p88 + 0x2E), (uint32_t)((uint32_t)((uint32_t)(0xC000007BULL))) + 52);
    goto loc_009894DA;
loc_00989545:
    result = MiFreeImageLoadConfig(*(uint16_t *)(v_stack_p88 + 0x2E), Arg2, *(uint16_t *)(v_stack_p88 + 0x2E), (uint32_t)((uint32_t)((uint32_t)(0xC000007BULL))) + 52);
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, *(uint16_t *)(v_stack_p88 + 0x2E), (uint32_t)((uint32_t)((uint32_t)(0xC000007BULL))) + 52);
    if (v_stack_p38 != 0) goto loc_00989078;
    goto loc_00989078;
loc_0098956A:
    Arg3 = (uint32_t)(((uint32_t)(v_stack_pE0)) << (12));
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x64EBBF) + 0xC)));
    result = RtlInitializeSystemOverrideDelta(result, v_stack_p58, Arg3, *(uint64_t *)(*(uint64_t *)(v_rip + 0x64EBBF) + 0x20));
    goto loc_00989136;
loc_00989597:
    local_rbx = (uint32_t)(((uint32_t)(v_stack_p40)) | (24));
    goto loc_00989190;
loc_009895A3:
    if (*(uint64_t *)(result + 0x58) == 0) goto loc_009891EC;
    local_r15 = (uint32_t)(((uint32_t)(v_stack_pE0)) << (12));
    local_r15 = (uint32_t)((local_r15) >> (12));
loc_009895C5:
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFEFULL));
    goto loc_00989252;
loc_009895CD:
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) + (-8));
    Arg3 = (Arg3) + (8);
    v_stack_p48 = Arg3;
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFEFULL));
    goto loc_0098920B;
loc_009895E1:
    goto loc_0098928C;
loc_009895F3:
    local_rsi = 0;
    goto loc_009893C5;
loc_00989606:
    if (0 != 8) goto loc_00989450;
    goto loc_00989306;
loc_00989619:
    result = MiCompressRelocations(result, (uint32_t)(v_stack_p34), v_stack_p48, *(uint64_t *)(*(uint64_t *)(v_rip + 0x64EBBF) + 0x20));
    goto loc_0098938D;
loc_00989631:
    result = MiUnmapImageInSystemSpace(v_stack_pD0, result + 104, v_stack_p48, *(uint64_t *)(*(uint64_t *)(v_rip + 0x64EBBF) + 0x20));
    result = PsRevertToUserPagePriorityThread(v_stack_p68, (uint32_t)(v_stack_p50), v_stack_p48, *(uint64_t *)(*(uint64_t *)(v_rip + 0x64EBBF) + 0x20));
    goto loc_00989081;
loc_00989651:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_p68, Arg2, v_stack_p48, *(uint64_t *)(*(uint64_t *)(v_rip + 0x64EBBF) + 0x20));
    goto loc_00989092;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0xC` | `16` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg2` | `+ 0x58` | `32` | `R` |
| `Arg2` | `+ 0x5C` | `32` | `R` |
| `Arg3` | `+ 0x30` | `32` | `R` |
| `Arg3` | `+ 0x34` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00988E14&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
