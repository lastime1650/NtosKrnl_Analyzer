# NtMapCMFModule

- RVA: `0x007D4310`–`0x007D4CEA` (길이 `2,522` bytes)
- VA: `0x00000001407D4310`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D5B1C`
- 디코드: `564`개 명령, `2,522/2,522` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **28**; 고유 호출 대상: **21**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **13**

### Outgoing calls
- `0x007D43FE` → [MUIInitializeResourceLock](../9E/MUIInitializeResourceLock_function_009ECB08.md) (function, `0x009ECB08`)
- `0x007D447E` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x007D44DC` → [CMFCheckAccess](CMFCheckAccess_function_007D28B4.md) (function, `0x007D28B4`)
- `0x007D4554` → [MmMapViewInSessionSpace](../98/MmMapViewInSessionSpace_function_00982480.md) (function, `0x00982480`)
- `0x007D459B` → [MiRemoveFromSystemSpace](../../text/29/MiRemoveFromSystemSpace_function_002962FC.md) (function, `0x002962FC`)
- `0x007D45BA` → [CMFUnmapModules](CMFUnmapModules_function_007D4090.md) (function, `0x007D4090`)
- `0x007D45C4` → [CMFRegisterEventTime](CMFRegisterEventTime_function_007D382C.md) (function, `0x007D382C`)
- `0x007D45D4` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x007D45D9` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x007D4604` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x007D4743` → [CMFRegisterEventTime](CMFRegisterEventTime_function_007D382C.md) (function, `0x007D382C`)
- `0x007D47B2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007D47D6` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007D47FC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007D48C8` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x007D48D7` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x007D4987` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (function, `0x0040DD10`)
- `0x007D4A0E` → [PsCreateSystemThreadEx](../9E/PsCreateSystemThreadEx_function_009ED120.md) (function, `0x009ED120`)
- `0x007D4A31` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007D4A4B` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x007D4A95` → [CMFRegisterEventTime](CMFRegisterEventTime_function_007D382C.md) (function, `0x007D382C`)
- `0x007D4AA8` → [ExConvertExclusiveToSharedLite](../../text/34/ExConvertExclusiveToSharedLite_function_0034F700.md) (function, `0x0034F700`)
- `0x007D4AE7` → [CMFCheckAccess](CMFCheckAccess_function_007D28B4.md) (function, `0x007D28B4`)
- `0x007D4B63` → [MmMapViewOfSection](../98/MmMapViewOfSection_function_00981680.md) (function, `0x00981680`)
- `0x007D4BC9` → [CMFFlushHitsFile](CMFFlushHitsFile_function_007D3140.md) (function, `0x007D3140`)
- `0x007D4BFD` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x007D4C02` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x007D4CCD` → [MiUnmapViewOfSection](../88/MiUnmapViewOfSection_function_0088A4C4.md) (function, `0x0088A4C4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x007D43D3` → RVA `0x00FC41C4` (`.data`; read)
- `0x007D43F7` → RVA `0x00EEEF90` (`.data`; read)
- `0x007D4447` → RVA `0x00EEEFD0` (`.data`; read)
- `0x007D4495` → RVA `0x00EEEFA0` (`.data`; read)
- `0x007D44FE` → RVA `0x00EEEFD0` (`.data`; write)
- `0x007D4722` → RVA `0x00E0EC04` (`.data`; read)
- `0x007D4736` → RVA `0x00E0EC00` (`.data`; read)
- `0x007D4748` → RVA `0x00E0EC00` (`.data`; write)
- `0x007D4798` → RVA `0x00EEEFC0` (`.data`; read)
- `0x007D4869` → RVA `0x00EEEF98` (`.data`; read)
- `0x007D4895` → RVA `0x00EEEFA8` (`.data`; write)
- `0x007D49E5` → RVA `0x007D3A70` (`CMFSystemThreadRoutine`; read)
- `0x007D4B88` → RVA `0x00EEEFA8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **16**
  - `0x007D447E` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x007D459B` → [MiRemoveFromSystemSpace](../../text/29/MiRemoveFromSystemSpace_function_002962FC.md) (`PAGE` → `.text`)
  - `0x007D45D4` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x007D45D9` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x007D4604` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x007D47B2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007D47D6` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007D47FC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007D48C8` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x007D48D7` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x007D4987` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (`PAGE` → `.text`)
  - `0x007D4A31` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007D4A4B` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x007D4AA8` → [ExConvertExclusiveToSharedLite](../../text/34/ExConvertExclusiveToSharedLite_function_0034F700.md) (`PAGE` → `.text`)
  - `0x007D4BFD` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x007D4C02` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007D4310  4C 8B DC                        mov r11, rsp
007D4313  4D 89 4B 20                     mov qword ptr [r11 + 0x20], r9
007D4317  4D 89 43 18                     mov qword ptr [r11 + 0x18], r8
007D431B  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
007D431F  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
007D4323  53                              push rbx
007D4324  56                              push rsi
007D4325  57                              push rdi
007D4326  41 54                           push r12
007D4328  41 55                           push r13
007D432A  41 56                           push r14
007D432C  41 57                           push r15
007D432E  48 81 EC 40 01 00 00            sub rsp, 0x140
007D4335  4D 8B F9                        mov r15, r9
007D4338  4D 8B E0                        mov r12, r8
007D433B  8B F2                           mov esi, edx
007D433D  33 FF                           xor edi, edi
007D433F  89 7C 24 58                     mov dword ptr [rsp + 0x58], edi
007D4343  89 7C 24 6C                     mov dword ptr [rsp + 0x6c], edi
007D4347  33 C0                           xor eax, eax
007D4349  0F 57 C0                        xorps xmm0, xmm0
007D434C  0F 11 84 24 E0 00 00 00         movups xmmword ptr [rsp + 0xe0], xmm0
007D4354  0F 11 84 24 F0 00 00 00         movups xmmword ptr [rsp + 0xf0], xmm0
007D435C  49 89 43 88                     mov qword ptr [r11 - 0x78], rax
007D4360  41 89 43 90                     mov dword ptr [r11 - 0x70], eax
007D4364  49 89 BB 10 FF FF FF            mov qword ptr [r11 - 0xf0], rdi
007D436B  41 0F 11 43 98                  movups xmmword ptr [r11 - 0x68], xmm0
007D4370  49 89 43 A8                     mov qword ptr [r11 - 0x58], rax
007D4374  49 89 BB 28 FF FF FF            mov qword ptr [r11 - 0xd8], rdi
007D437B  0F 11 84 24 A8 00 00 00         movups xmmword ptr [rsp + 0xa8], xmm0
007D4383  0F 11 84 24 B8 00 00 00         movups xmmword ptr [rsp + 0xb8], xmm0
007D438B  0F 11 84 24 C8 00 00 00         movups xmmword ptr [rsp + 0xc8], xmm0
007D4393  49 89 83 60 FF FF FF            mov qword ptr [r11 - 0xa0], rax
007D439A  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
007D439F  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
007D43A4  89 7C 24 58                     mov dword ptr [rsp + 0x58], edi
007D43A8  89 7C 24 6C                     mov dword ptr [rsp + 0x6c], edi
007D43AC  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007D43B5  44 8A A8 32 02 00 00            mov r13b, byte ptr [rax + 0x232]
007D43BC  44 88 6C 24 68                  mov byte ptr [rsp + 0x68], r13b
007D43C1  45 84 ED                        test r13b, r13b
007D43C4  75 0D                           jne 0x1407d43d3
007D43C6  C7 44 24 50 01 00 00 C0         mov dword ptr [rsp + 0x50], 0xc0000001
007D43CE  E9 D8 08 00 00                  jmp 0x1407d4cab
007D43D3  39 3D EB FD 7E 00               cmp dword ptr [rip + 0x7efdeb], edi
007D43D9  75 EB                           jne 0x1407d43c6
007D43DB  8B 9C 24 80 01 00 00            mov ebx, dword ptr [rsp + 0x180]
007D43E2  F7 C3 81 FE E0 FF               test ebx, 0xffe0fe81
007D43E8  74 0D                           je 0x1407d43f7
007D43EA  C7 44 24 50 0D 00 00 C0         mov dword ptr [rsp + 0x50], 0xc000000d
007D43F2  E9 B4 08 00 00                  jmp 0x1407d4cab
007D43F7  48 8D 0D 92 AB 71 00            lea rcx, [rip + 0x71ab92]
007D43FE  E8 05 87 21 00                  call 0x1409ecb08
007D4403  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
007D4407  B9 00 00 00 C0                  mov ecx, 0xc0000000
007D440C  23 C1                           and eax, ecx
007D440E  3B C1                           cmp eax, ecx
007D4410  0F 84 95 08 00 00               je 0x1407d4cab
007D4416  0F BA E3 11                     bt ebx, 0x11
007D441A  0F 83 C3 01 00 00               jae 0x1407d45e3
007D4420  44 8B C3                        mov r8d, ebx
007D4423  BA 00 00 18 00                  mov edx, 0x180000
007D4428  44 23 C2                        and r8d, edx
007D442B  0F 95 C1                        setne cl
007D442E  0F BA E3 12                     bt ebx, 0x12
007D4432  0F 92 C0                        setb al
007D4435  84 C8                           test al, cl
007D4437  75 B1                           jne 0x1407d43ea
007D4439  44 3B C2                        cmp r8d, edx
007D443C  74 AC                           je 0x1407d43ea
007D443E  41 BF 00 00 1C 00               mov r15d, 0x1c0000
007D4444  41 23 DF                        and ebx, r15d
007D4447  8B 05 83 AB 71 00               mov eax, dword ptr [rip + 0x71ab83]
007D444D  41 23 C7                        and eax, r15d
007D4450  3B D8                           cmp ebx, eax
007D4452  75 09                           jne 0x1407d445d
007D4454  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
007D4458  E9 4E 08 00 00                  jmp 0x1407d4cab
007D445D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007D4466  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
007D446D  90                              nop
007D446E  41 BE 01 00 00 00               mov r14d, 1
007D4474  41 8A D6                        mov dl, r14b
007D4477  48 8B 0D 12 AB 71 00            mov rcx, qword ptr [rip + 0x71ab12]
007D447E  E8 9D 09 A4 FF                  call 0x140214e20
007D4483  90                              nop
007D4484  8B 0D 46 AB 71 00               mov ecx, dword ptr [rip + 0x71ab46]
007D448A  41 23 CF                        and ecx, r15d
007D448D  3B D9                           cmp ebx, ecx
007D448F  0F 84 34 01 00 00               je 0x1407d45c9
007D4495  4C 8B 0D 04 AB 71 00            mov r9, qword ptr [rip + 0x71ab04]
007D449C  4D 85 C9                        test r9, r9
007D449F  74 4E                           je 0x1407d44ef
007D44A1  85 DB                           test ebx, ebx
007D44A3  75 0D                           jne 0x1407d44b2
007D44A5  C7 44 24 50 BB 00 00 C0         mov dword ptr [rsp + 0x50], 0xc00000bb
007D44AD  E9 1B 01 00 00                  jmp 0x1407d45cd
007D44B2  4D 85 C9                        test r9, r9
007D44B5  74 38                           je 0x1407d44ef
007D44B7  B8 00 00 00 80                  mov eax, 0x80000000
007D44BC  89 84 24 98 00 00 00            mov dword ptr [rsp + 0x98], eax
007D44C3  85 C9                           test ecx, ecx
007D44C5  BE 00 00 00 C0                  mov esi, 0xc0000000
007D44CA  0F 45 C6                        cmovne eax, esi
007D44CD  89 84 24 98 00 00 00            mov dword ptr [rsp + 0x98], eax
007D44D4  45 8A C5                        mov r8b, r13b
007D44D7  8B D0                           mov edx, eax
007D44D9  49 8B C9                        mov rcx, r9
007D44DC  E8 D3 E3 FF FF                  call 0x1407d28b4
007D44E1  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
007D44E5  23 C6                           and eax, esi
007D44E7  3B C6                           cmp eax, esi
007D44E9  0F 84 DE 00 00 00               je 0x1407d45cd
007D44EF  8B 05 DB AA 71 00               mov eax, dword ptr [rip + 0x71aadb]
007D44F5  41 BC FF FF E3 FF               mov r12d, 0xffe3ffff
007D44FB  41 23 C4                        and eax, r12d
007D44FE  89 05 CC AA 71 00               mov dword ptr [rip + 0x71aacc], eax
007D4504  0B D8                           or ebx, eax
007D4506  89 1D C4 AA 71 00               mov dword ptr [rip + 0x71aac4], ebx
007D450C  48 8B 0D 8D AA 71 00            mov rcx, qword ptr [rip + 0x71aa8d]
007D4513  48 85 C9                        test rcx, rcx
007D4516  0F 84 AD 00 00 00               je 0x1407d45c9
007D451C  41 BF 00 00 08 00               mov r15d, 0x80000
007D4522  BE 00 00 10 00                  mov esi, 0x100000
007D4527  41 85 DF                        test r15d, ebx
007D452A  75 08                           jne 0x1407d4534
007D452C  85 DE                           test esi, ebx
007D452E  0F 84 95 00 00 00               je 0x1407d45c9
007D4534  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
007D4539  48 C7 44 24 78 68 00 00 00      mov qword ptr [rsp + 0x78], 0x68
007D4542  48 89 BC 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdi
007D454A  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
007D454F  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
007D4554  E8 27 DF 1A 00                  call 0x140982480
007D4559  85 C0                           test eax, eax
007D455B  78 48                           js 0x1407d45a5
007D455D  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
007D4562  48 85 C9                        test rcx, rcx
007D4565  74 3E                           je 0x1407d45a5
007D4567  48 83 7C 24 78 68               cmp qword ptr [rsp + 0x78], 0x68
007D456D  72 29                           jb 0x1407d4598
007D456F  44 21 61 30                     and dword ptr [rcx + 0x30], r12d
007D4573  8B 05 57 AA 71 00               mov eax, dword ptr [rip + 0x71aa57]
007D4579  41 23 C7                        and eax, r15d
007D457C  F7 D8                           neg eax
007D457E  45 1B C0                        sbb r8d, r8d
007D4581  41 81 E0 00 00 F8 FF            and r8d, 0xfff80000
007D4588  44 03 C6                        add r8d, esi
007D458B  44 0B 41 30                     or r8d, dword ptr [rcx + 0x30]
007D458F  44 89 41 30                     mov dword ptr [rcx + 0x30], r8d
007D4593  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
007D4598  41 8B D6                        mov edx, r14d
007D459B  E8 5C 1D AC FF                  call 0x1402962fc
007D45A0  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
007D45A5  8B 05 25 AA 71 00               mov eax, dword ptr [rip + 0x71aa25]
007D45AB  23 C6                           and eax, esi
007D45AD  F7 D8                           neg eax
007D45AF  1B C9                           sbb ecx, ecx
007D45B1  81 E1 10 01 00 00               and ecx, 0x110
007D45B7  83 C1 20                        add ecx, 0x20
007D45BA  E8 D1 FA FF FF                  call 0x1407d4090
007D45BF  B9 04 00 00 00                  mov ecx, 4
007D45C4  E8 63 F2 FF FF                  call 0x1407d382c
007D45C9  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
007D45CD  48 8B 0D BC A9 71 00            mov rcx, qword ptr [rip + 0x71a9bc]
007D45D4  E8 37 B4 A8 FF                  call 0x14025fa10
007D45D9  E8 D2 92 A8 FF                  call 0x14025d8b0
007D45DE  E9 C8 06 00 00                  jmp 0x1407d4cab
007D45E3  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007D45EC  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
007D45F3  90                              nop
007D45F4  41 BE 01 00 00 00               mov r14d, 1
007D45FA  41 8A D6                        mov dl, r14b
007D45FD  48 8B 0D 8C A9 71 00            mov rcx, qword ptr [rip + 0x71a98c]
007D4604  E8 B7 D5 A3 FF                  call 0x140211bc0
007D4609  90                              nop
007D460A  8B 05 C0 A9 71 00               mov eax, dword ptr [rip + 0x71a9c0]
007D4610  8B 9C 24 80 01 00 00            mov ebx, dword ptr [rsp + 0x180]
007D4617  85 C0                           test eax, eax
007D4619  0F 84 95 00 00 00               je 0x1407d46b4
007D461F  8B C8                           mov ecx, eax
007D4621  83 E1 0F                        and ecx, 0xf
007D4624  74 0E                           je 0x1407d4634
007D4626  83 E3 F0                        and ebx, 0xfffffff0
007D4629  89 9C 24 80 01 00 00            mov dword ptr [rsp + 0x180], ebx
007D4630  0B D9                           or ebx, ecx
007D4632  EB 03                           jmp 0x1407d4637
007D4634  41 0B DE                        or ebx, r14d
007D4637  89 9C 24 80 01 00 00            mov dword ptr [rsp + 0x180], ebx
007D463E  BE 00 00 10 00                  mov esi, 0x100000
007D4643  85 C6                           test esi, eax
007D4645  74 1D                           je 0x1407d4664
007D4647  0F BA E3 10                     bt ebx, 0x10
007D464B  72 13                           jb 0x1407d4660
007D464D  C7 44 24 50 98 00 00 C0         mov dword ptr [rsp + 0x50], 0xc0000098
007D4655  41 BD 00 00 00 C0               mov r13d, 0xc0000000
007D465B  E9 96 05 00 00                  jmp 0x1407d4bf6
007D4660  0B DE                           or ebx, esi
007D4662  EB 40                           jmp 0x1407d46a4
007D4664  41 BF 00 00 08 00               mov r15d, 0x80000
007D466A  41 85 C7                        test r15d, eax
007D466D  74 2A                           je 0x1407d4699
007D466F  8B C3                           mov eax, ebx
007D4671  25 30 01 00 00                  and eax, 0x130
007D4676  83 F8 20                        cmp eax, 0x20
007D4679  75 19                           jne 0x1407d4694
007D467B  0F BA E3 10                     bt ebx, 0x10
007D467F  72 13                           jb 0x1407d4694
007D4681  C7 44 24 50 98 00 00 C0         mov dword ptr [rsp + 0x50], 0xc0000098
007D4689  41 BD 00 00 00 C0               mov r13d, 0xc0000000
007D468F  E9 5A 05 00 00                  jmp 0x1407d4bee
007D4694  41 0B DF                        or ebx, r15d
007D4697  EB 0B                           jmp 0x1407d46a4
007D4699  B9 00 00 04 00                  mov ecx, 0x40000
007D469E  85 C1                           test ecx, eax
007D46A0  74 09                           je 0x1407d46ab
007D46A2  0B D9                           or ebx, ecx
007D46A4  89 9C 24 80 01 00 00            mov dword ptr [rsp + 0x180], ebx
007D46AB  8B B4 24 88 01 00 00            mov esi, dword ptr [rsp + 0x188]
007D46B2  EB 0A                           jmp 0x1407d46be
007D46B4  41 0B DE                        or ebx, r14d
007D46B7  89 9C 24 80 01 00 00            mov dword ptr [rsp + 0x180], ebx
007D46BE  44 8B E3                        mov r12d, ebx
007D46C1  41 81 E4 CF FE FF FF            and r12d, 0xfffffecf
007D46C8  44 89 64 24 6C                  mov dword ptr [rsp + 0x6c], r12d
007D46CD  81 E3 30 01 00 00               and ebx, 0x130
007D46D3  89 9C 24 80 01 00 00            mov dword ptr [rsp + 0x180], ebx
007D46DA  41 8B CC                        mov ecx, r12d
007D46DD  83 E1 40                        and ecx, 0x40
007D46E0  8B C1                           mov eax, ecx
007D46E2  F7 D8                           neg eax
007D46E4  1B C0                           sbb eax, eax
007D46E6  83 E0 02                        and eax, 2
007D46E9  83 C0 02                        add eax, 2
007D46EC  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
007D46F0  F7 D9                           neg ecx
007D46F2  45 1B FF                        sbb r15d, r15d
007D46F5  41 81 E7 00 00 00 40            and r15d, 0x40000000
007D46FC  B8 00 00 00 80                  mov eax, 0x80000000
007D4701  44 03 F8                        add r15d, eax
007D4704  44 89 BC 24 80 00 00 00         mov dword ptr [rsp + 0x80], r15d
007D470C  BA 10 27 00 00                  mov edx, 0x2710
007D4711  89 54 24 58                     mov dword ptr [rsp + 0x58], edx
007D4715  40 0F B6 CF                     movzx ecx, dil
007D4719  88 4C 24 54                     mov byte ptr [rsp + 0x54], cl
007D471D  83 FB 10                        cmp ebx, 0x10
007D4720  75 5A                           jne 0x1407d477c
007D4722  8B 05 DC A4 63 00               mov eax, dword ptr [rip + 0x63a4dc]
007D4728  3B C2                           cmp eax, edx
007D472A  73 06                           jae 0x1407d4732
007D472C  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
007D4730  EB 2E                           jmp 0x1407d4760
007D4732  3B F2                           cmp esi, edx
007D4734  72 26                           jb 0x1407d475c
007D4736  8A 05 C4 A4 63 00               mov al, byte ptr [rip + 0x63a4c4]
007D473C  84 C0                           test al, al
007D473E  74 0F                           je 0x1407d474f
007D4740  41 8B CE                        mov ecx, r14d
007D4743  E8 E4 F0 FF FF                  call 0x1407d382c
007D4748  40 88 3D B1 A4 63 00            mov byte ptr [rip + 0x63a4b1], dil
007D474F  C7 44 24 50 0D 00 00 C0         mov dword ptr [rsp + 0x50], 0xc000000d
007D4757  E9 84 04 00 00                  jmp 0x1407d4be0
007D475C  89 74 24 58                     mov dword ptr [rsp + 0x58], esi
007D4760  41 F6 C4 02                     test r12b, 2
007D4764  44 8B E9                        mov r13d, ecx
007D4767  45 0F 45 EE                     cmovne r13d, r14d
007D476B  44 88 6C 24 54                  mov byte ptr [rsp + 0x54], r13b
007D4770  48 8D 35 29 A8 71 00            lea rsi, [rip + 0x71a829]
007D4777  E9 B9 00 00 00                  jmp 0x1407d4835
007D477C  83 FB 20                        cmp ebx, 0x20
007D477F  0F 85 BD 00 00 00               jne 0x1407d4842
007D4785  83 FE 1E                        cmp esi, 0x1e
007D4788  73 C5                           jae 0x1407d474f
007D478A  8B 05 74 A4 63 00               mov eax, dword ptr [rip + 0x63a474]
007D4790  3B C2                           cmp eax, edx
007D4792  74 BB                           je 0x1407d474f
007D4794  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
007D4798  48 83 3D 20 A8 71 00 00         cmp qword ptr [rip + 0x71a820], 0
007D47A0  75 74                           jne 0x1407d4816
007D47A2  BB F0 00 00 00                  mov ebx, 0xf0
007D47A7  41 B8 50 66 6D 63               mov r8d, 0x636d6650
007D47AD  8B D3                           mov edx, ebx
007D47AF  8D 4B 10                        lea ecx, [rbx + 0x10]
007D47B2  E8 39 D9 3A 00                  call 0x140b820f0
007D47B7  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
007D47BC  48 85 C0                        test rax, rax
007D47BF  75 0D                           jne 0x1407d47ce
007D47C1  C7 44 24 50 17 00 00 C0         mov dword ptr [rsp + 0x50], 0xc0000017
007D47C9  E9 12 04 00 00                  jmp 0x1407d4be0
007D47CE  4C 8B C3                        mov r8, rbx
007D47D1  33 D2                           xor edx, edx
007D47D3  48 8B C8                        mov rcx, rax
007D47D6  E8 65 24 EF FF                  call 0x1406c6c40
007D47DB  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
007D47E0  33 C0                           xor eax, eax
007D47E2  F0 48 0F B1 0D D5 A7 71 00      lock cmpxchg qword ptr [rip + 0x71a7d5], rcx
007D47EB  48 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], rax
007D47F3  74 0C                           je 0x1407d4801
007D47F5  33 D2                           xor edx, edx
007D47F7  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
007D47FC  E8 6F E0 3A 00                  call 0x140b82870
007D4801  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
007D4806  8B 9C 24 80 01 00 00            mov ebx, dword ptr [rsp + 0x180]
007D480D  8A 4C 24 54                     mov cl, byte ptr [rsp + 0x54]
007D4811  44 8B 64 24 6C                  mov r12d, dword ptr [rsp + 0x6c]
007D4816  41 F6 C4 04                     test r12b, 4
007D481A  0F B6 C1                        movzx eax, cl
007D481D  41 0F 45 C6                     cmovne eax, r14d
007D4821  44 8A E8                        mov r13b, al
007D4824  88 44 24 54                     mov byte ptr [rsp + 0x54], al
007D4828  8B CE                           mov ecx, esi
007D482A  48 8B 05 8F A7 71 00            mov rax, qword ptr [rip + 0x71a78f]
007D4831  48 8D 34 C8                     lea rsi, [rax + rcx*8]
007D4835  48 89 B4 24 90 00 00 00         mov qword ptr [rsp + 0x90], rsi
007D483D  48 8B 06                        mov rax, qword ptr [rsi]
007D4840  EB 76                           jmp 0x1407d48b8
007D4842  81 FB 00 01 00 00               cmp ebx, 0x100
007D4848  0F 85 01 FF FF FF               jne 0x1407d474f
007D484E  8B 05 B0 A3 63 00               mov eax, dword ptr [rip + 0x63a3b0]
007D4854  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
007D4858  41 F6 C4 08                     test r12b, 8
007D485C  8B C1                           mov eax, ecx
007D485E  41 0F 45 C6                     cmovne eax, r14d
007D4862  44 8A E8                        mov r13b, al
007D4865  88 44 24 54                     mov byte ptr [rsp + 0x54], al
007D4869  48 8D 35 28 A7 71 00            lea rsi, [rip + 0x71a728]
007D4870  48 89 B4 24 90 00 00 00         mov qword ptr [rsp + 0x90], rsi
007D4878  48 8B 05 19 A7 71 00            mov rax, qword ptr [rip + 0x71a719]
007D487F  48 85 C0                        test rax, rax
007D4882  0F 85 27 02 00 00               jne 0x1407d4aaf
007D4888  48 B9 14 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000014
007D4892  48 8B 01                        mov rax, qword ptr [rcx]
007D4895  48 89 05 0C A7 71 00            mov qword ptr [rip + 0x71a70c], rax
007D489C  48 8B 06                        mov rax, qword ptr [rsi]
007D489F  8B 9C 24 80 01 00 00            mov ebx, dword ptr [rsp + 0x180]
007D48A6  44 8A 6C 24 54                  mov r13b, byte ptr [rsp + 0x54]
007D48AB  44 8B 64 24 6C                  mov r12d, dword ptr [rsp + 0x6c]
007D48B0  48 8B B4 24 90 00 00 00         mov rsi, qword ptr [rsp + 0x90]
007D48B8  48 85 C0                        test rax, rax
007D48BB  0F 85 EE 01 00 00               jne 0x1407d4aaf
007D48C1  48 8B 0D C8 A6 71 00            mov rcx, qword ptr [rip + 0x71a6c8]
007D48C8  E8 43 B1 A8 FF                  call 0x14025fa10
007D48CD  41 8A D6                        mov dl, r14b
007D48D0  48 8B 0D B9 A6 71 00            mov rcx, qword ptr [rip + 0x71a6b9]
007D48D7  E8 44 05 A4 FF                  call 0x140214e20
007D48DC  41 8B C4                        mov eax, r12d
007D48DF  8B 0D EB A6 71 00               mov ecx, dword ptr [rip + 0x71a6eb]
007D48E5  33 C1                           xor eax, ecx
007D48E7  41 BF 00 00 1C 00               mov r15d, 0x1c0000
007D48ED  41 85 C7                        test r15d, eax
007D48F0  74 16                           je 0x1407d4908
007D48F2  BA 00 00 18 00                  mov edx, 0x180000
007D48F7  85 CA                           test edx, ecx
007D48F9  74 0D                           je 0x1407d4908
007D48FB  C7 44 24 50 01 00 00 C0         mov dword ptr [rsp + 0x50], 0xc0000001
007D4903  E9 D8 02 00 00                  jmp 0x1407d4be0
007D4908  44 8B BC 24 80 00 00 00         mov r15d, dword ptr [rsp + 0x80]
007D4910  48 39 3E                        cmp qword ptr [rsi], rdi
007D4913  0F 85 83 01 00 00               jne 0x1407d4a9c
007D4919  C7 84 24 A8 00 00 00 00 00 00 08  mov dword ptr [rsp + 0xa8], 0x8000000
007D4924  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
007D4928  89 84 24 AC 00 00 00            mov dword ptr [rsp + 0xac], eax
007D492F  44 89 BC 24 B0 00 00 00         mov dword ptr [rsp + 0xb0], r15d
007D4937  44 88 AC 24 B4 00 00 00         mov byte ptr [rsp + 0xb4], r13b
007D493F  48 89 BC 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rdi
007D4947  44 89 A4 24 C0 00 00 00         mov dword ptr [rsp + 0xc0], r12d
007D494F  8B 84 24 88 01 00 00            mov eax, dword ptr [rsp + 0x188]
007D4956  89 84 24 C4 00 00 00            mov dword ptr [rsp + 0xc4], eax
007D495D  44 8B 64 24 70                  mov r12d, dword ptr [rsp + 0x70]
007D4962  44 89 A4 24 C8 00 00 00         mov dword ptr [rsp + 0xc8], r12d
007D496A  48 89 B4 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rsi
007D4972  89 9C 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], ebx
007D4979  45 33 C0                        xor r8d, r8d
007D497C  41 8B D6                        mov edx, r14d
007D497F  48 8D 8C 24 10 01 00 00         lea rcx, [rsp + 0x110]
007D4987  E8 84 93 C3 FF                  call 0x14040dd10
007D498C  48 8D 84 24 10 01 00 00         lea rax, [rsp + 0x110]
007D4994  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
007D499C  C7 84 24 E0 00 00 00 30 00 00 00  mov dword ptr [rsp + 0xe0], 0x30
007D49A7  48 89 BC 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rdi
007D49AF  C7 84 24 F8 00 00 00 00 02 00 00  mov dword ptr [rsp + 0xf8], 0x200
007D49BA  48 89 BC 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rdi
007D49C2  0F 57 C0                        xorps xmm0, xmm0
007D49C5  F3 0F 7F 84 24 00 01 00 00      movdqu xmmword ptr [rsp + 0x100], xmm0
007D49CE  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
007D49D3  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
007D49D8  48 8D 84 24 A8 00 00 00         lea rax, [rsp + 0xa8]
007D49E0  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007D49E5  48 8D 05 84 F0 FF FF            lea rax, [rip - 0xf7c]
007D49EC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007D49F1  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
007D49F6  45 33 C9                        xor r9d, r9d
007D49F9  4C 8D 84 24 E0 00 00 00         lea r8, [rsp + 0xe0]
007D4A01  BA FF FF 1F 00                  mov edx, 0x1fffff
007D4A06  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
007D4A0E  E8 0D 87 21 00                  call 0x1409ed120
007D4A13  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
007D4A17  41 BD 00 00 00 C0               mov r13d, 0xc0000000
007D4A1D  41 23 C5                        and eax, r13d
007D4A20  41 3B C5                        cmp eax, r13d
007D4A23  0F 84 BD 01 00 00               je 0x1407d4be6
007D4A29  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
007D4A31  E8 7A 88 ED FF                  call 0x1406ad2b0
007D4A36  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
007D4A3B  45 33 C9                        xor r9d, r9d
007D4A3E  45 33 C0                        xor r8d, r8d
007D4A41  33 D2                           xor edx, edx
007D4A43  48 8D 8C 24 10 01 00 00         lea rcx, [rsp + 0x110]
007D4A4B  E8 60 9C A3 FF                  call 0x14020e6b0
007D4A50  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
007D4A54  85 C0                           test eax, eax
007D4A56  74 13                           je 0x1407d4a6b
007D4A58  0F 88 88 01 00 00               js 0x1407d4be6
007D4A5E  C7 44 24 50 01 00 00 C0         mov dword ptr [rsp + 0x50], 0xc0000001
007D4A66  E9 7B 01 00 00                  jmp 0x1407d4be6
007D4A6B  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
007D4A72  89 44 24 6C                     mov dword ptr [rsp + 0x6c], eax
007D4A76  8B 84 24 CC 00 00 00            mov eax, dword ptr [rsp + 0xcc]
007D4A7D  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
007D4A81  41 23 C5                        and eax, r13d
007D4A84  41 3B C5                        cmp eax, r13d
007D4A87  0F 84 59 01 00 00               je 0x1407d4be6
007D4A8D  83 FB 10                        cmp ebx, 0x10
007D4A90  75 0F                           jne 0x1407d4aa1
007D4A92  8D 4B F2                        lea ecx, [rbx - 0xe]
007D4A95  E8 92 ED FF FF                  call 0x1407d382c
007D4A9A  EB 05                           jmp 0x1407d4aa1
007D4A9C  44 8B 64 24 70                  mov r12d, dword ptr [rsp + 0x70]
007D4AA1  48 8B 0D E8 A4 71 00            mov rcx, qword ptr [rip + 0x71a4e8]
007D4AA8  E8 53 AC B7 FF                  call 0x14034f700
007D4AAD  EB 05                           jmp 0x1407d4ab4
007D4AAF  44 8B 64 24 70                  mov r12d, dword ptr [rsp + 0x70]
007D4AB4  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
007D4AB9  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
007D4ABE  48 89 BC 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdi
007D4AC6  48 39 BC 24 A8 01 00 00         cmp qword ptr [rsp + 0x1a8], rdi
007D4ACE  0F 84 0C 01 00 00               je 0x1407d4be0
007D4AD4  81 FB 00 01 00 00               cmp ebx, 0x100
007D4ADA  74 28                           je 0x1407d4b04
007D4ADC  44 8A 44 24 68                  mov r8b, byte ptr [rsp + 0x68]
007D4AE1  41 8B D7                        mov edx, r15d
007D4AE4  48 8B 0E                        mov rcx, qword ptr [rsi]
007D4AE7  E8 C8 DD FF FF                  call 0x1407d28b4
007D4AEC  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
007D4AF0  41 BD 00 00 00 C0               mov r13d, 0xc0000000
007D4AF6  41 23 C5                        and eax, r13d
007D4AF9  41 3B C5                        cmp eax, r13d
007D4AFC  0F 84 E4 00 00 00               je 0x1407d4be6
007D4B02  EB 06                           jmp 0x1407d4b0a
007D4B04  41 BD 00 00 00 C0               mov r13d, 0xc0000000
007D4B0A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007D4B13  48 89 84 24 30 01 00 00         mov qword ptr [rsp + 0x130], rax
007D4B1B  48 8B 90 B8 00 00 00            mov rdx, qword ptr [rax + 0xb8]
007D4B22  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
007D4B27  C7 44 24 40 00 00 40 00         mov dword ptr [rsp + 0x40], 0x400000
007D4B2F  44 89 74 24 38                  mov dword ptr [rsp + 0x38], r14d
007D4B34  48 8D 44 24 78                  lea rax, [rsp + 0x78]
007D4B39  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007D4B3E  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
007D4B46  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007D4B4B  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
007D4B50  45 33 C9                        xor r9d, r9d
007D4B53  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
007D4B58  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
007D4B60  48 8B 09                        mov rcx, qword ptr [rcx]
007D4B63  E8 18 CB 1A 00                  call 0x140981680
007D4B68  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
007D4B6C  41 23 C5                        and eax, r13d
007D4B6F  41 3B C5                        cmp eax, r13d
007D4B72  75 07                           jne 0x1407d4b7b
007D4B74  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
007D4B79  EB 6B                           jmp 0x1407d4be6
007D4B7B  81 BC 24 80 01 00 00 00 01 00 00  cmp dword ptr [rsp + 0x180], 0x100
007D4B86  75 5E                           jne 0x1407d4be6
007D4B88  48 8B 35 19 A4 71 00            mov rsi, qword ptr [rip + 0x71a419]
007D4B8F  48 BB 14 00 00 00 80 F7 FF FF   movabs rbx, 0xfffff78000000014
007D4B99  48 8B 1B                        mov rbx, qword ptr [rbx]
007D4B9C  48 B8 00 68 C4 61 08 00 00 00   movabs rax, 0x861c46800
007D4BA6  48 03 C6                        add rax, rsi
007D4BA9  48 3B D8                        cmp rbx, rax
007D4BAC  7E 38                           jle 0x1407d4be6
007D4BAE  48 8B C6                        mov rax, rsi
007D4BB1  F0 48 0F B1 1D EE A3 71 00      lock cmpxchg qword ptr [rip + 0x71a3ee], rbx
007D4BBA  48 3B F0                        cmp rsi, rax
007D4BBD  75 27                           jne 0x1407d4be6
007D4BBF  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
007D4BC4  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
007D4BC9  E8 72 E5 FF FF                  call 0x1407d3140
007D4BCE  85 C0                           test eax, eax
007D4BD0  79 14                           jns 0x1407d4be6
007D4BD2  48 8B C3                        mov rax, rbx
007D4BD5  F0 48 0F B1 35 CA A3 71 00      lock cmpxchg qword ptr [rip + 0x71a3ca], rsi
007D4BDE  EB 06                           jmp 0x1407d4be6
007D4BE0  41 BD 00 00 00 C0               mov r13d, 0xc0000000
007D4BE6  4C 8B A4 24 90 01 00 00         mov r12, qword ptr [rsp + 0x190]
007D4BEE  4C 8B BC 24 98 01 00 00         mov r15, qword ptr [rsp + 0x198]
007D4BF6  48 8B 0D 93 A3 71 00            mov rcx, qword ptr [rip + 0x71a393]
007D4BFD  E8 0E AE A8 FF                  call 0x14025fa10
007D4C02  E8 A9 8C A8 FF                  call 0x14025d8b0
007D4C07  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
007D4C0B  41 23 C5                        and eax, r13d
007D4C0E  41 3B C5                        cmp eax, r13d
007D4C11  0F 84 94 00 00 00               je 0x1407d4cab
007D4C17  4C 8B 84 24 A8 01 00 00         mov r8, qword ptr [rsp + 0x1a8]
007D4C1F  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
007D4C29  4D 85 C0                        test r8, r8
007D4C2C  74 1D                           je 0x1407d4c4b
007D4C2E  48 8B CA                        mov rcx, rdx
007D4C31  4C 3B C2                        cmp r8, rdx
007D4C34  49 0F 42 C8                     cmovb rcx, r8
007D4C38  48 8B 01                        mov rax, qword ptr [rcx]
007D4C3B  48 89 01                        mov qword ptr [rcx], rax
007D4C3E  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
007D4C43  49 89 00                        mov qword ptr [r8], rax
007D4C46  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
007D4C4B  4C 8B 84 24 A0 01 00 00         mov r8, qword ptr [rsp + 0x1a0]
007D4C53  4D 85 C0                        test r8, r8
007D4C56  74 16                           je 0x1407d4c6e
007D4C58  48 8B CA                        mov rcx, rdx
007D4C5B  4C 3B C2                        cmp r8, rdx
007D4C5E  49 0F 42 C8                     cmovb rcx, r8
007D4C62  8B 01                           mov eax, dword ptr [rcx]
007D4C64  89 01                           mov dword ptr [rcx], eax
007D4C66  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
007D4C6B  41 89 00                        mov dword ptr [r8], eax
007D4C6E  4D 85 E4                        test r12, r12
007D4C71  74 16                           je 0x1407d4c89
007D4C73  48 8B CA                        mov rcx, rdx
007D4C76  4C 3B E2                        cmp r12, rdx
007D4C79  49 0F 42 CC                     cmovb rcx, r12
007D4C7D  8B 01                           mov eax, dword ptr [rcx]
007D4C7F  89 01                           mov dword ptr [rcx], eax
007D4C81  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
007D4C85  41 89 04 24                     mov dword ptr [r12], eax
007D4C89  4D 85 FF                        test r15, r15
007D4C8C  74 12                           je 0x1407d4ca0
007D4C8E  4C 3B FA                        cmp r15, rdx
007D4C91  49 0F 42 D7                     cmovb rdx, r15
007D4C95  8B 02                           mov eax, dword ptr [rdx]
007D4C97  89 02                           mov dword ptr [rdx], eax
007D4C99  8B 44 24 6C                     mov eax, dword ptr [rsp + 0x6c]
007D4C9D  41 89 07                        mov dword ptr [r15], eax
007D4CA0  E9 AF F7 FF FF                  jmp 0x1407d4454
007D4CA5  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
007D4CA9  33 FF                           xor edi, edi
007D4CAB  48 39 7C 24 60                  cmp qword ptr [rsp + 0x60], rdi
007D4CB0  74 20                           je 0x1407d4cd2
007D4CB2  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007D4CBB  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
007D4CC2  45 33 C9                        xor r9d, r9d
007D4CC5  45 33 C0                        xor r8d, r8d
007D4CC8  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
007D4CCD  E8 F2 57 0B 00                  call 0x14088a4c4
007D4CD2  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
007D4CD6  48 81 C4 40 01 00 00            add rsp, 0x140
007D4CDD  41 5F                           pop r15
007D4CDF  41 5E                           pop r14
007D4CE1  41 5D                           pop r13
007D4CE3  41 5C                           pop r12
007D4CE5  5F                              pop rdi
007D4CE6  5E                              pop rsi
007D4CE7  5B                              pop rbx
007D4CE8  C3                              ret
007D4CE9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtMapCMFModule(int a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m108;
    unsigned int v_stack_m10C;
    unsigned __int8 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m120;
    unsigned __int8 v_stack_m124;
    unsigned int v_stack_m128;
    unsigned int v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mAC;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int8 v_stack_mC4;
    unsigned int v_stack_mC8;
    unsigned int v_stack_mCC;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF8;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (320);
    v_rdi = 0;
    v_stack_m120 = 0;
    v_stack_m10C = 0;
    result = 0;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 120) = 0;
    *(unsigned int *)(v_rsp - 112) = 0;
    *(unsigned __int64 *)(v_rsp - 240) = 0;
    *(unsigned __int64 *)(v_rsp - 104) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 88) = 0;
    *(unsigned __int64 *)(v_rsp - 216) = 0;
    v_stack_mD0 = v_xmm0;
    v_stack_mC0 = v_xmm0;
    v_stack_mB0 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 160) = 0;
    v_stack_m118 = 0;
    v_stack_m100 = 0;
    v_stack_m120 = 0;
    v_stack_m10C = 0;
    v_stack_m110 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 0) goto loc_007D43D3;
loc_007D43C6:
    v_stack_m128 = 0xC0000001ULL;
    goto loc_007D4CAB;
loc_007D43D3:
    if ((*(unsigned int *)(v_rip + 8322539)) != 0) goto loc_007D43C6;
    if ((((unsigned int)((unsigned int)(v_stack_p8))) & (0xFFE0FE81ULL)) == 0) goto loc_007D43F7;
loc_007D43EA:
    v_stack_m128 = 0xC000000DULL;
    goto loc_007D4CAB;
loc_007D43F7:
    result = MUIInitializeResourceLock(v_rip + 7449490, a2, a3, a4);
    v_stack_m128 = (unsigned int)(result);
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xC0000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_007D4CAB;
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_007D45E3;
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p8)))) & ((unsigned int)((unsigned int)(0x180000ULL))));
    a1 = (condition_is_not_equal) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_007D43EA;
    if (((unsigned int)(a3)) == ((unsigned int)((unsigned int)(0x180000ULL)))) goto loc_007D43EA;
    v_rbx = (unsigned int)(((unsigned int)(v_stack_p8)) & ((unsigned int)((unsigned int)(0x1C0000ULL))));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 7449475))) & ((unsigned int)((unsigned int)(0x1C0000ULL))));
    if (((unsigned int)(v_rbx)) != ((unsigned int)(result))) goto loc_007D445D;
loc_007D4454:
    v_stack_m128 = 0;
    goto loc_007D4CAB;
loc_007D445D:
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(v_rip + 7449362), 1, a3, a4);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 7449414))) & ((unsigned int)((unsigned int)(0x1C0000ULL))));
    if (((unsigned int)(v_rbx)) == a1) goto loc_007D45C9;
    if (*(unsigned __int64 *)(v_rip + 7449348) == 0) goto loc_007D44EF;
    if ((unsigned int)(v_rbx) != 0) goto loc_007D44B2;
    v_stack_m128 = 0xC00000BBULL;
    goto loc_007D45CD;
loc_007D44B2:
    if (*(unsigned __int64 *)(v_rip + 7449348) == 0) goto loc_007D44EF;
    v_stack_mE0 = (unsigned int)((unsigned int)(0x80000000ULL));
    result = (unsigned int)(0x80000000ULL);
    if (a1 != 0) { result = (unsigned int)((unsigned int)(0xC0000000ULL)); }
    v_stack_mE0 = (unsigned int)(result);
    result = CMFCheckAccess(*(unsigned __int64 *)(v_rip + 7449348), (unsigned int)((unsigned int)(result)), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), *(unsigned __int64 *)(v_rip + 7449348));
    v_stack_m128 = (unsigned int)(result);
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xC0000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_007D45CD;
loc_007D44EF:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 7449307))) & ((unsigned int)((unsigned int)(0xFFE3FFFFULL))));
    *(unsigned int *)(v_rip + 7449292) = (unsigned int)(result);
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)(result)));
    *(unsigned int *)(v_rip + 7449284) = (unsigned int)(v_rbx);
    if (*(unsigned __int64 *)(v_rip + 7449229) == 0) goto loc_007D45C9;
    if ((((unsigned int)((unsigned int)(0x80000ULL))) & ((unsigned int)(v_rbx))) != 0) goto loc_007D4534;
    if ((((unsigned int)((unsigned int)(0x100000ULL))) & ((unsigned int)(v_rbx))) == 0) goto loc_007D45C9;
loc_007D4534:
    v_stack_m118 = 0;
    v_stack_m100 = 104;
    v_stack_mF0 = 0;
    result = MmMapViewInSessionSpace(*(unsigned __int64 *)(v_rip + 7449229), v_stack_m118, v_stack_m100, *(unsigned __int64 *)(v_rip + 7449348));
    if (sign_flag) goto loc_007D45A5;
    if (v_stack_m118 == 0) goto loc_007D45A5;
    if (v_stack_m100 >= 104) {
        result = *(unsigned int *)(v_rip + 7449175);
        result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0x80000ULL))));
        result = (unsigned int)(-(result));
        a3 = (unsigned int)((v_stack_m100) & (0xFFF80000ULL));
        a3 = (unsigned int)((a3) + ((unsigned int)((unsigned int)(0x100000ULL))));
        a3 = (unsigned int)((a3) | (*(unsigned int *)(v_stack_m118 + 48)));
        *(unsigned int *)(v_stack_m118 + 48) = (unsigned int)(a3);
        a1 = v_stack_m118;
    }
    result = MiRemoveFromSystemSpace(a1, 1, a3, *(unsigned __int64 *)(v_rip + 7449348));
    v_stack_m118 = 0;
loc_007D45A5:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 7449125))) & ((unsigned int)((unsigned int)(0x100000ULL))));
    result = (unsigned int)(-(result));
    a1 = (unsigned int)((a1) & (272));
    a1 = (unsigned int)((a1) + (32));
    result = CMFUnmapModules(a1, 1, a3, *(unsigned __int64 *)(v_rip + 7449348));
    result = CMFRegisterEventTime(4, 1, a3, *(unsigned __int64 *)(v_rip + 7449348));
loc_007D45C9:
    v_stack_m128 = 0;
loc_007D45CD:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_rip + 7449020), 1, a3, *(unsigned __int64 *)(v_rip + 7449348));
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_rip + 7449020), 1, a3, *(unsigned __int64 *)(v_rip + 7449348));
    goto loc_007D4CAB;
loc_007D45E3:
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_rip + 7448972), 1, a3, *(unsigned __int64 *)(v_rip + 7449348));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 7449024))) == 0) goto loc_007D46B4;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 7449024))))) & (15));
    if (condition_is_equal) goto loc_007D4634;
    v_rbx = (unsigned int)(((unsigned int)(v_stack_p8)) & (0xFFFFFFF0ULL));
    v_stack_p8 = (unsigned int)(v_rbx);
    v_rbx = (unsigned int)((v_rbx) | (a1));
    goto loc_007D4637;
loc_007D4634:
    v_rbx = (unsigned int)((v_rbx) | (1));
loc_007D4637:
    v_stack_p8 = (unsigned int)(v_rbx);
    if ((((unsigned int)((unsigned int)(0x100000ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 7449024))))) == 0) goto loc_007D4664;
    if (condition_is_below) goto loc_007D4660;
    v_stack_m128 = 0xC0000098ULL;
    goto loc_007D4BF6;
loc_007D4660:
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)((unsigned int)(0x100000ULL))));
    goto loc_007D46A4;
loc_007D4664:
    if ((((unsigned int)((unsigned int)(0x80000ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 7449024))))) == 0) goto loc_007D4699;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (304));
    if (((unsigned int)(result)) != 32) goto loc_007D4694;
    if (((unsigned int)(result)) < 32) goto loc_007D4694;
    v_stack_m128 = 0xC0000098ULL;
    goto loc_007D4BEE;
loc_007D4694:
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)((unsigned int)(0x80000ULL))));
    goto loc_007D46A4;
loc_007D4699:
    if ((((unsigned int)((unsigned int)(0x40000ULL))) & ((unsigned int)(result))) == 0) goto loc_007D46AB;
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)((unsigned int)(0x40000ULL))));
loc_007D46A4:
    v_stack_p8 = (unsigned int)(v_rbx);
loc_007D46AB:
    goto loc_007D46BE;
loc_007D46B4:
    v_rbx = (unsigned int)((v_rbx) | (1));
    v_stack_p8 = (unsigned int)(v_rbx);
loc_007D46BE:
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (0xFFFFFECFULL));
    v_stack_m10C = (unsigned int)(v_r12);
    v_rbx = (unsigned int)((v_rbx) & (304));
    v_stack_p8 = (unsigned int)(v_rbx);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) & (64));
    result = (unsigned int)(-((unsigned int)(a1)));
    result = (unsigned int)((result) & (2));
    result = (unsigned int)((result) + (2));
    v_stack_m108 = (unsigned int)(result);
    a1 = (unsigned int)(-(a1));
    v_r15 = (unsigned int)(((unsigned int)(0x80000ULL)) & (0x40000000ULL));
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)((unsigned int)(0x80000000ULL))));
    v_stack_mF8 = (unsigned int)(v_r15);
    v_stack_m120 = (unsigned int)((unsigned int)(0x2710ULL));
    v_stack_m124 = 0;
    if (((unsigned int)(v_rbx)) != 16) goto loc_007D477C;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 6530268)))) >= ((unsigned int)((unsigned int)(0x2710ULL)))) goto loc_007D4732;
    v_stack_m120 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 6530268)));
    goto loc_007D4760;
loc_007D4732:
    if (((unsigned int)((unsigned int)(v_stack_p10))) < ((unsigned int)((unsigned int)(0x2710ULL)))) goto loc_007D475C;
    result = *(unsigned __int8 *)(v_rip + 6530244);
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 6530244)) != 0) {
        a1 = 1;
        result = CMFRegisterEventTime(a1, (unsigned int)(0x2710ULL), a3, *(unsigned __int64 *)(v_rip + 7449348));
        *(unsigned __int8 *)(v_rip + 6530225) = 0;
    }
    v_stack_m128 = 0xC000000DULL;
    goto loc_007D4BE0;
loc_007D475C:
    v_stack_m120 = (unsigned int)((unsigned int)(v_stack_p10));
loc_007D4760:
    v_r13 = (unsigned int)(a1);
    if ((((unsigned __int8)(v_r12)) & (2)) != 0) { v_r13 = 1; }
    v_stack_m124 = (unsigned __int8)(v_r13);
    goto loc_007D4835;
loc_007D477C:
    if (((unsigned int)(v_rbx)) != 32) goto loc_007D4842;
    if (((unsigned int)(v_rip + 7448617)) >= 30) goto loc_007D474F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 6530164)))) == ((unsigned int)((unsigned int)(0x2710ULL)))) goto loc_007D474F;
    v_stack_m120 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 6530164)));
    if ((*(unsigned __int64 *)(v_rip + 7448608)) != 0) goto loc_007D4816;
    result = ExAllocatePool2(240 + 16, 240, (unsigned int)(0x636D6650ULL), *(unsigned __int64 *)(v_rip + 7449348));
    v_stack_m118 = result;
    if (result != 0) goto loc_007D47CE;
    v_stack_m128 = 0xC0000017ULL;
    goto loc_007D4BE0;
loc_007D47CE:
    a2 = 0;
    result = memset(result, a2, 240, *(unsigned __int64 *)(v_rip + 7449348));
    result = 0;
    v_stack_m50 = 0;
    if (!(condition_is_equal)) {
        a2 = 0;
        a1 = v_stack_m118;
        result = ExFreePoolWithTag(a1, a2, 240, *(unsigned __int64 *)(v_rip + 7449348));
    }
    v_stack_m118 = 0;
loc_007D4816:
    result = (unsigned __int8)(v_stack_m124);
    if ((((unsigned __int8)((unsigned int)(v_stack_m10C))) & (4)) != 0) { result = 1; }
    v_stack_m124 = (unsigned __int8)(result);
loc_007D4835:
    v_stack_mE8 = *(unsigned __int64 *)(v_rip + 7448463) + (unsigned int)((unsigned int)(v_rip + 7448617)) * 8;
    goto loc_007D48B8;
loc_007D4842:
    if (((unsigned int)((unsigned int)(v_stack_p8))) != 256) goto loc_007D474F;
    v_stack_m120 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 6529968)));
    result = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rip + 7448617))));
    if ((((unsigned __int8)((unsigned int)(v_stack_m10C))) & (8)) != 0) { result = 1; }
    v_stack_m124 = (unsigned __int8)(result);
    v_stack_mE8 = v_rip + 7448360;
    if (*(unsigned __int64 *)(v_rip + 7448345) != 0) goto loc_007D4AAF;
    *(unsigned __int64 *)(v_rip + 7448332) = *(unsigned __int64 *)((unsigned int)((unsigned int)(v_rip + 7448617)));
loc_007D48B8:
    if (*(unsigned __int64 *)(v_rip + 7448360) != 0) goto loc_007D4AAF;
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_rip + 7448264), a2, 240, *(unsigned __int64 *)(v_rip + 7449348));
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(v_rip + 7448249), 1, 240, *(unsigned __int64 *)(v_rip + 7449348));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m10C)))) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 7448299)))));
    if ((((unsigned int)((unsigned int)(0x1C0000ULL))) & ((unsigned int)(result))) == 0) goto loc_007D4908;
    if ((((unsigned int)((unsigned int)(0x180000ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 7448299))))) == 0) goto loc_007D4908;
    v_stack_m128 = 0xC0000001ULL;
    goto loc_007D4BE0;
loc_007D4908:
    if ((*(unsigned __int64 *)(v_stack_mE8)) != 0) goto loc_007D4A9C;
    v_stack_mD0 = 0x8000000ULL;
    v_stack_mCC = (unsigned int)((unsigned int)(v_stack_m120));
    v_stack_mC8 = (unsigned int)((unsigned int)(v_stack_mF8));
    v_stack_mC4 = (unsigned __int8)(v_stack_m124);
    v_stack_mC0 = 0;
    v_stack_mB8 = (unsigned int)((unsigned int)(v_stack_m10C));
    v_stack_mB4 = (unsigned int)((unsigned int)(v_stack_p10));
    v_stack_mB0 = (unsigned int)((unsigned int)(v_stack_m108));
    v_stack_mA8 = v_stack_mE8;
    v_stack_mA0 = (unsigned int)((unsigned int)(v_stack_p8));
    a3 = 0;
    result = KeInitializeEvent(v_stack_m68, 1, a3, *(unsigned __int64 *)(v_rip + 7449348));
    v_stack_mC0 = v_stack_m68;
    v_stack_m98 = 48;
    v_stack_m90 = 0;
    v_stack_m80 = 512;
    v_stack_m88 = 0;
    v_stack_m78 = v_xmm0;
    v_stack_m138 = 0;
    v_stack_m140 = 0;
    v_stack_m148 = v_stack_mD0;
    v_stack_m150 = v_rip - 3964;
    v_stack_m158 = 0;
    a4 = 0;
    result = PsCreateSystemThreadEx(v_stack_mD8, (unsigned int)(0x1FFFFFULL), v_stack_m98, a4);
    v_stack_m128 = (unsigned int)(result);
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xC0000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_007D4BE6;
    result = ZwClose(v_stack_mD8, (unsigned int)(0x1FFFFFULL), v_stack_m98, a4);
    v_stack_m158 = 0;
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(v_stack_m68, a2, a3, a4);
    v_stack_m128 = (unsigned int)(result);
    if ((unsigned int)(result) == 0) goto loc_007D4A6B;
    if (sign_flag) goto loc_007D4BE6;
    v_stack_m128 = 0xC0000001ULL;
    goto loc_007D4BE6;
loc_007D4A6B:
    v_stack_m10C = (unsigned int)((unsigned int)(v_stack_mB8));
    v_stack_m128 = (unsigned int)((unsigned int)(v_stack_mAC));
    result = (unsigned int)(((unsigned int)(v_stack_mAC)) & ((unsigned int)((unsigned int)(0xC0000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_007D4BE6;
    if (((unsigned int)((unsigned int)(v_stack_p8))) != 16) goto loc_007D4AA1;
    result = CMFRegisterEventTime((unsigned int)(v_stack_p8) - 14, a2, a3, a4);
    goto loc_007D4AA1;
loc_007D4A9C:
loc_007D4AA1:
    result = ExConvertExclusiveToSharedLite(*(unsigned __int64 *)(v_rip + 7447784), a2, a3, a4);
    goto loc_007D4AB4;
loc_007D4AAF:
loc_007D4AB4:
    v_stack_m118 = 0;
    v_stack_m100 = 0;
    v_stack_mF0 = 0;
    if (a6 == 0) goto loc_007D4BE0;
    if (((unsigned int)((unsigned int)(v_stack_p8))) == 256) goto loc_007D4B04;
    result = CMFCheckAccess(*(unsigned __int64 *)(v_stack_mE8), (unsigned int)((unsigned int)((unsigned int)(v_stack_mF8))), v_stack_m110, a4);
    v_stack_m128 = (unsigned int)(result);
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xC0000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_007D4BE6;
    goto loc_007D4B0A;
loc_007D4B04:
loc_007D4B0A:
    v_stack_m48 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m130 = (unsigned int)((unsigned int)(v_stack_m108));
    v_stack_m138 = 0x400000ULL;
    v_stack_m140 = 1;
    v_stack_m148 = v_stack_m100;
    v_stack_m150 = v_stack_mF0;
    v_stack_m158 = 0;
    a4 = 0;
    result = MmMapViewOfSection(*(unsigned __int64 *)(v_stack_mE8), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), v_stack_m118, a4);
    v_stack_m128 = (unsigned int)(result);
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xC0000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_007D4B7B;
    v_stack_m118 = 0;
    goto loc_007D4BE6;
loc_007D4B7B:
    if (v_stack_p8 != 256) goto loc_007D4BE6;
    result = (result) + (*(unsigned __int64 *)(v_rip + 7447577));
    if ((*(unsigned __int64 *)((unsigned int)(v_stack_p8))) <= result) goto loc_007D4BE6;
    if ((*(unsigned __int64 *)(v_rip + 7447577)) != (*(unsigned __int64 *)(v_rip + 7447577))) goto loc_007D4BE6;
    result = CMFFlushHitsFile(v_stack_m118, v_stack_m100, v_stack_m118, a4);
    if (!sign_flag) goto loc_007D4BE6;
    goto loc_007D4BE6;
loc_007D4BE0:
loc_007D4BE6:
loc_007D4BEE:
loc_007D4BF6:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_rip + 7447443), v_stack_m100, v_stack_m118, a4);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_rip + 7447443), v_stack_m100, v_stack_m118, a4);
    result = (unsigned int)(((unsigned int)(v_stack_m128)) & ((unsigned int)((unsigned int)(0xC0000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_007D4CAB;
    if (a6 != 0) {
        a1 = v_stack_m100;
        if (a6 < v_stack_m100) { a1 = a6; }
        result = *(unsigned __int64 *)(a1);
        *(unsigned __int64 *)(a1) = result;
        result = v_stack_m118;
        *(unsigned __int64 *)(a6) = result;
        v_stack_m118 = 0;
    }
    if (a5 != 0) {
        a1 = v_stack_m100;
        if (a5 < v_stack_m100) { a1 = a5; }
        result = *(unsigned int *)(a1);
        *(unsigned int *)(a1) = (unsigned int)(result);
        result = v_stack_m100;
        *(unsigned int *)(a5) = (unsigned int)(result);
    }
    if (v_stack_p18 != 0) {
        a1 = v_stack_m100;
        if (v_stack_p18 < v_stack_m100) { a1 = v_stack_p18; }
        result = *(unsigned int *)(a1);
        *(unsigned int *)(a1) = (unsigned int)(result);
        result = v_stack_m120;
        *(unsigned int *)(v_stack_p18) = (unsigned int)(result);
    }
    if (v_stack_p20 != 0) {
        a2 = v_stack_m100;
        if (v_stack_p20 < v_stack_m100) { a2 = v_stack_p20; }
        result = *(unsigned int *)(a2);
        *(unsigned int *)(a2) = (unsigned int)(result);
        result = v_stack_m10C;
        *(unsigned int *)(v_stack_p20) = (unsigned int)(result);
    }
    goto loc_007D4454;
loc_007D4CAB:
    if (v_stack_m118 != 0) {
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        a1 = *(unsigned __int64 *)(result + 184);
        a4 = 0;
        a3 = 0;
        a2 = v_stack_m118;
        result = MiUnmapViewOfSection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (320);
    return (unsigned int)(v_stack_m128);
}
```

## 5. (Beta) C Style

```c
int64_t NtMapCMFModule(int32_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m108;
    uint32_t v_stack_m10C;
    uint8_t v_stack_m110;
    uint64_t v_stack_m118;
    uint32_t v_stack_m120;
    uint8_t v_stack_m124;
    uint32_t v_stack_m128;
    uint32_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mAC;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint8_t v_stack_mC4;
    uint32_t v_stack_mC8;
    uint32_t v_stack_mCC;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF8;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (320);
    local_rdi = 0;
    v_stack_m120 = 0;
    v_stack_m10C = 0;
    result = 0;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x78) = 0;
    *(uint32_t *)(local_rsp - 0x70) = 0;
    *(uint64_t *)(local_rsp - 0xF0) = 0;
    *(uint64_t *)(local_rsp - 0x68) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x58) = 0;
    *(uint64_t *)(local_rsp - 0xD8) = 0;
    v_stack_mD0 = v_xmm0;
    v_stack_mC0 = v_xmm0;
    v_stack_mB0 = v_xmm0;
    *(uint64_t *)(local_rsp - 0xA0) = 0;
    v_stack_m118 = 0;
    v_stack_m100 = 0;
    v_stack_m120 = 0;
    v_stack_m10C = 0;
    v_stack_m110 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 0) goto loc_007D43D3;
loc_007D43C6:
    v_stack_m128 = 0xC0000001ULL;
    goto loc_007D4CAB;
loc_007D43D3:
    if ((*(uint32_t *)(v_rip + 0x7EFDEB)) != 0) goto loc_007D43C6;
    if ((((uint32_t)((uint32_t)(v_stack_p8))) & (0xFFE0FE81ULL)) == 0) goto loc_007D43F7;
loc_007D43EA:
    v_stack_m128 = 0xC000000DULL;
    goto loc_007D4CAB;
loc_007D43F7:
    result = MUIInitializeResourceLock(v_rip + 7449490, Arg2, Arg3, Arg4);
    v_stack_m128 = (uint32_t)(result);
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xC0000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_007D4CAB;
    if (((uint32_t)(result)) >= ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_007D45E3;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p8)))) & ((uint32_t)((uint32_t)(0x180000ULL))));
    Arg1 = (condition_is_not_equal) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_007D43EA;
    if (((uint32_t)(Arg3)) == ((uint32_t)((uint32_t)(0x180000ULL)))) goto loc_007D43EA;
    local_rbx = (uint32_t)(((uint32_t)(v_stack_p8)) & ((uint32_t)((uint32_t)(0x1C0000ULL))));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x71AB83))) & ((uint32_t)((uint32_t)(0x1C0000ULL))));
    if (((uint32_t)(local_rbx)) != ((uint32_t)(result))) goto loc_007D445D;
loc_007D4454:
    v_stack_m128 = 0;
    goto loc_007D4CAB;
loc_007D445D:
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(v_rip + 0x71AB12), 1, Arg3, Arg4);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x71AB46))) & ((uint32_t)((uint32_t)(0x1C0000ULL))));
    if (((uint32_t)(local_rbx)) == Arg1) goto loc_007D45C9;
    if (*(uint64_t *)(v_rip + 0x71AB04) == 0) goto loc_007D44EF;
    if ((uint32_t)(local_rbx) != 0) goto loc_007D44B2;
    v_stack_m128 = 0xC00000BBULL;
    goto loc_007D45CD;
loc_007D44B2:
    if (*(uint64_t *)(v_rip + 0x71AB04) == 0) goto loc_007D44EF;
    v_stack_mE0 = (uint32_t)((uint32_t)(0x80000000ULL));
    result = (uint32_t)(0x80000000ULL);
    if (Arg1 != 0) { result = (uint32_t)((uint32_t)(0xC0000000ULL)); }
    v_stack_mE0 = (uint32_t)(result);
    result = CMFCheckAccess(*(uint64_t *)(v_rip + 0x71AB04), (uint32_t)((uint32_t)(result)), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), *(uint64_t *)(v_rip + 0x71AB04));
    v_stack_m128 = (uint32_t)(result);
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xC0000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_007D45CD;
loc_007D44EF:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x71AADB))) & ((uint32_t)((uint32_t)(0xFFE3FFFFULL))));
    *(uint32_t *)(v_rip + 0x71AACC) = (uint32_t)(result);
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)(result)));
    *(uint32_t *)(v_rip + 0x71AAC4) = (uint32_t)(local_rbx);
    if (*(uint64_t *)(v_rip + 0x71AA8D) == 0) goto loc_007D45C9;
    if ((((uint32_t)((uint32_t)(0x80000ULL))) & ((uint32_t)(local_rbx))) != 0) goto loc_007D4534;
    if ((((uint32_t)((uint32_t)(0x100000ULL))) & ((uint32_t)(local_rbx))) == 0) goto loc_007D45C9;
loc_007D4534:
    v_stack_m118 = 0;
    v_stack_m100 = 104;
    v_stack_mF0 = 0;
    result = MmMapViewInSessionSpace(*(uint64_t *)(v_rip + 0x71AA8D), v_stack_m118, v_stack_m100, *(uint64_t *)(v_rip + 0x71AB04));
    if (sign_flag) goto loc_007D45A5;
    if (v_stack_m118 == 0) goto loc_007D45A5;
    if (v_stack_m100 >= 104) {
        result = *(uint32_t *)(v_rip + 0x71AA57);
        result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0x80000ULL))));
        result = (uint32_t)(-(result));
        Arg3 = (uint32_t)((v_stack_m100) & (0xFFF80000ULL));
        Arg3 = (uint32_t)((Arg3) + ((uint32_t)((uint32_t)(0x100000ULL))));
        Arg3 = (uint32_t)((Arg3) | (*(uint32_t *)(v_stack_m118 + 0x30)));
        *(uint32_t *)(v_stack_m118 + 0x30) = (uint32_t)(Arg3);
        Arg1 = v_stack_m118;
    }
    result = MiRemoveFromSystemSpace(Arg1, 1, Arg3, *(uint64_t *)(v_rip + 0x71AB04));
    v_stack_m118 = 0;
loc_007D45A5:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x71AA25))) & ((uint32_t)((uint32_t)(0x100000ULL))));
    result = (uint32_t)(-(result));
    Arg1 = (uint32_t)((Arg1) & (272));
    Arg1 = (uint32_t)((Arg1) + (32));
    result = CMFUnmapModules(Arg1, 1, Arg3, *(uint64_t *)(v_rip + 0x71AB04));
    result = CMFRegisterEventTime(4, 1, Arg3, *(uint64_t *)(v_rip + 0x71AB04));
loc_007D45C9:
    v_stack_m128 = 0;
loc_007D45CD:
    result = ExReleaseResourceLite(*(uint64_t *)(v_rip + 0x71A9BC), 1, Arg3, *(uint64_t *)(v_rip + 0x71AB04));
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_rip + 0x71A9BC), 1, Arg3, *(uint64_t *)(v_rip + 0x71AB04));
    goto loc_007D4CAB;
loc_007D45E3:
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_rip + 0x71A98C), 1, Arg3, *(uint64_t *)(v_rip + 0x71AB04));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x71A9C0))) == 0) goto loc_007D46B4;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x71A9C0))))) & (15));
    if (condition_is_equal) goto loc_007D4634;
    local_rbx = (uint32_t)(((uint32_t)(v_stack_p8)) & (0xFFFFFFF0ULL));
    v_stack_p8 = (uint32_t)(local_rbx);
    local_rbx = (uint32_t)((local_rbx) | (Arg1));
    goto loc_007D4637;
loc_007D4634:
    local_rbx = (uint32_t)((local_rbx) | (1));
loc_007D4637:
    v_stack_p8 = (uint32_t)(local_rbx);
    if ((((uint32_t)((uint32_t)(0x100000ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x71A9C0))))) == 0) goto loc_007D4664;
    if (condition_is_below) goto loc_007D4660;
    v_stack_m128 = 0xC0000098ULL;
    goto loc_007D4BF6;
loc_007D4660:
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)((uint32_t)(0x100000ULL))));
    goto loc_007D46A4;
loc_007D4664:
    if ((((uint32_t)((uint32_t)(0x80000ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x71A9C0))))) == 0) goto loc_007D4699;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (304));
    if (((uint32_t)(result)) != 32) goto loc_007D4694;
    if (((uint32_t)(result)) < 32) goto loc_007D4694;
    v_stack_m128 = 0xC0000098ULL;
    goto loc_007D4BEE;
loc_007D4694:
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)((uint32_t)(0x80000ULL))));
    goto loc_007D46A4;
loc_007D4699:
    if ((((uint32_t)((uint32_t)(0x40000ULL))) & ((uint32_t)(result))) == 0) goto loc_007D46AB;
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)((uint32_t)(0x40000ULL))));
loc_007D46A4:
    v_stack_p8 = (uint32_t)(local_rbx);
loc_007D46AB:
    goto loc_007D46BE;
loc_007D46B4:
    local_rbx = (uint32_t)((local_rbx) | (1));
    v_stack_p8 = (uint32_t)(local_rbx);
loc_007D46BE:
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (0xFFFFFECFULL));
    v_stack_m10C = (uint32_t)(local_r12);
    local_rbx = (uint32_t)((local_rbx) & (304));
    v_stack_p8 = (uint32_t)(local_rbx);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) & (64));
    result = (uint32_t)(-((uint32_t)(Arg1)));
    result = (uint32_t)((result) & (2));
    result = (uint32_t)((result) + (2));
    v_stack_m108 = (uint32_t)(result);
    Arg1 = (uint32_t)(-(Arg1));
    local_r15 = (uint32_t)(((uint32_t)(0x80000ULL)) & (0x40000000ULL));
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)((uint32_t)(0x80000000ULL))));
    v_stack_mF8 = (uint32_t)(local_r15);
    v_stack_m120 = (uint32_t)((uint32_t)(0x2710ULL));
    v_stack_m124 = 0;
    if (((uint32_t)(local_rbx)) != 16) goto loc_007D477C;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x63A4DC)))) >= ((uint32_t)((uint32_t)(0x2710ULL)))) goto loc_007D4732;
    v_stack_m120 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x63A4DC)));
    goto loc_007D4760;
loc_007D4732:
    if (((uint32_t)((uint32_t)(v_stack_p10))) < ((uint32_t)((uint32_t)(0x2710ULL)))) goto loc_007D475C;
    result = *(uint8_t *)(v_rip + 0x63A4C4);
    if ((uint8_t)(*(uint8_t *)(v_rip + 0x63A4C4)) != 0) {
        Arg1 = 1;
        result = CMFRegisterEventTime(Arg1, (uint32_t)(0x2710ULL), Arg3, *(uint64_t *)(v_rip + 0x71AB04));
        *(uint8_t *)(v_rip + 0x63A4B1) = 0;
    }
    v_stack_m128 = 0xC000000DULL;
    goto loc_007D4BE0;
loc_007D475C:
    v_stack_m120 = (uint32_t)((uint32_t)(v_stack_p10));
loc_007D4760:
    local_r13 = (uint32_t)(Arg1);
    if ((((uint8_t)(local_r12)) & (2)) != 0) { local_r13 = 1; }
    v_stack_m124 = (uint8_t)(local_r13);
    goto loc_007D4835;
loc_007D477C:
    if (((uint32_t)(local_rbx)) != 32) goto loc_007D4842;
    if (((uint32_t)(v_rip + 7448617)) >= 30) goto loc_007D474F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x63A474)))) == ((uint32_t)((uint32_t)(0x2710ULL)))) goto loc_007D474F;
    v_stack_m120 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x63A474)));
    if ((*(uint64_t *)(v_rip + 0x71A820)) != 0) goto loc_007D4816;
    result = ExAllocatePool2(240 + 16, 240, (uint32_t)(0x636D6650ULL), *(uint64_t *)(v_rip + 0x71AB04));
    v_stack_m118 = result;
    if (result != 0) goto loc_007D47CE;
    v_stack_m128 = 0xC0000017ULL;
    goto loc_007D4BE0;
loc_007D47CE:
    Arg2 = 0;
    result = memset(result, Arg2, 240, *(uint64_t *)(v_rip + 0x71AB04));
    result = 0;
    v_stack_m50 = 0;
    if (!(condition_is_equal)) {
        Arg2 = 0;
        Arg1 = v_stack_m118;
        result = ExFreePoolWithTag(Arg1, Arg2, 240, *(uint64_t *)(v_rip + 0x71AB04));
    }
    v_stack_m118 = 0;
loc_007D4816:
    result = (uint8_t)(v_stack_m124);
    if ((((uint8_t)((uint32_t)(v_stack_m10C))) & (4)) != 0) { result = 1; }
    v_stack_m124 = (uint8_t)(result);
loc_007D4835:
    v_stack_mE8 = *(uint64_t *)(v_rip + 0x71A78F) + (uint32_t)((uint32_t)(v_rip + 7448617)) * 8;
    goto loc_007D48B8;
loc_007D4842:
    if (((uint32_t)((uint32_t)(v_stack_p8))) != 256) goto loc_007D474F;
    v_stack_m120 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x63A3B0)));
    result = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_rip + 7448617))));
    if ((((uint8_t)((uint32_t)(v_stack_m10C))) & (8)) != 0) { result = 1; }
    v_stack_m124 = (uint8_t)(result);
    v_stack_mE8 = v_rip + 7448360;
    if (*(uint64_t *)(v_rip + 0x71A719) != 0) goto loc_007D4AAF;
    *(uint64_t *)(v_rip + 0x71A70C) = *(uint64_t *)((uint32_t)((uint32_t)(v_rip + 0x71A829)));
loc_007D48B8:
    if (*(uint64_t *)(v_rip + 0x71A728) != 0) goto loc_007D4AAF;
    result = ExReleaseResourceLite(*(uint64_t *)(v_rip + 0x71A6C8), Arg2, 240, *(uint64_t *)(v_rip + 0x71AB04));
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(v_rip + 0x71A6B9), 1, 240, *(uint64_t *)(v_rip + 0x71AB04));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m10C)))) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x71A6EB)))));
    if ((((uint32_t)((uint32_t)(0x1C0000ULL))) & ((uint32_t)(result))) == 0) goto loc_007D4908;
    if ((((uint32_t)((uint32_t)(0x180000ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x71A6EB))))) == 0) goto loc_007D4908;
    v_stack_m128 = 0xC0000001ULL;
    goto loc_007D4BE0;
loc_007D4908:
    if ((*(uint64_t *)(v_stack_mE8)) != 0) goto loc_007D4A9C;
    v_stack_mD0 = 0x8000000ULL;
    v_stack_mCC = (uint32_t)((uint32_t)(v_stack_m120));
    v_stack_mC8 = (uint32_t)((uint32_t)(v_stack_mF8));
    v_stack_mC4 = (uint8_t)(v_stack_m124);
    v_stack_mC0 = 0;
    v_stack_mB8 = (uint32_t)((uint32_t)(v_stack_m10C));
    v_stack_mB4 = (uint32_t)((uint32_t)(v_stack_p10));
    v_stack_mB0 = (uint32_t)((uint32_t)(v_stack_m108));
    v_stack_mA8 = v_stack_mE8;
    v_stack_mA0 = (uint32_t)((uint32_t)(v_stack_p8));
    Arg3 = 0;
    result = KeInitializeEvent(v_stack_m68, 1, Arg3, *(uint64_t *)(v_rip + 0x71AB04));
    v_stack_mC0 = v_stack_m68;
    v_stack_m98 = 48;
    v_stack_m90 = 0;
    v_stack_m80 = 512;
    v_stack_m88 = 0;
    v_stack_m78 = v_xmm0;
    v_stack_m138 = 0;
    v_stack_m140 = 0;
    v_stack_m148 = v_stack_mD0;
    v_stack_m150 = v_rip - 3964;
    v_stack_m158 = 0;
    Arg4 = 0;
    result = PsCreateSystemThreadEx(v_stack_mD8, (uint32_t)(0x1FFFFFULL), v_stack_m98, Arg4);
    v_stack_m128 = (uint32_t)(result);
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xC0000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_007D4BE6;
    result = ZwClose(v_stack_mD8, (uint32_t)(0x1FFFFFULL), v_stack_m98, Arg4);
    v_stack_m158 = 0;
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(v_stack_m68, Arg2, Arg3, Arg4);
    v_stack_m128 = (uint32_t)(result);
    if ((uint32_t)(result) == 0) goto loc_007D4A6B;
    if (sign_flag) goto loc_007D4BE6;
    v_stack_m128 = 0xC0000001ULL;
    goto loc_007D4BE6;
loc_007D4A6B:
    v_stack_m10C = (uint32_t)((uint32_t)(v_stack_mB8));
    v_stack_m128 = (uint32_t)((uint32_t)(v_stack_mAC));
    result = (uint32_t)(((uint32_t)(v_stack_mAC)) & ((uint32_t)((uint32_t)(0xC0000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_007D4BE6;
    if (((uint32_t)((uint32_t)(v_stack_p8))) != 16) goto loc_007D4AA1;
    result = CMFRegisterEventTime((uint32_t)(v_stack_p8) - 14, Arg2, Arg3, Arg4);
    goto loc_007D4AA1;
loc_007D4A9C:
loc_007D4AA1:
    result = ExConvertExclusiveToSharedLite(*(uint64_t *)(v_rip + 0x71A4E8), Arg2, Arg3, Arg4);
    goto loc_007D4AB4;
loc_007D4AAF:
loc_007D4AB4:
    v_stack_m118 = 0;
    v_stack_m100 = 0;
    v_stack_mF0 = 0;
    if (Arg6 == 0) goto loc_007D4BE0;
    if (((uint32_t)((uint32_t)(v_stack_p8))) == 256) goto loc_007D4B04;
    result = CMFCheckAccess(*(uint64_t *)(v_stack_mE8), (uint32_t)((uint32_t)((uint32_t)(v_stack_mF8))), v_stack_m110, Arg4);
    v_stack_m128 = (uint32_t)(result);
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xC0000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_007D4BE6;
    goto loc_007D4B0A;
loc_007D4B04:
loc_007D4B0A:
    v_stack_m48 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m130 = (uint32_t)((uint32_t)(v_stack_m108));
    v_stack_m138 = 0x400000ULL;
    v_stack_m140 = 1;
    v_stack_m148 = v_stack_m100;
    v_stack_m150 = v_stack_mF0;
    v_stack_m158 = 0;
    Arg4 = 0;
    result = MmMapViewOfSection(*(uint64_t *)(v_stack_mE8), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), v_stack_m118, Arg4);
    v_stack_m128 = (uint32_t)(result);
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xC0000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_007D4B7B;
    v_stack_m118 = 0;
    goto loc_007D4BE6;
loc_007D4B7B:
    if (v_stack_p8 != 256) goto loc_007D4BE6;
    result = (result) + (*(uint64_t *)(v_rip + 0x71A419));
    if ((*(uint64_t *)((uint32_t)(v_stack_p8))) <= result) goto loc_007D4BE6;
    if ((*(uint64_t *)(v_rip + 0x71A419)) != (*(uint64_t *)(v_rip + 0x71A419))) goto loc_007D4BE6;
    result = CMFFlushHitsFile(v_stack_m118, v_stack_m100, v_stack_m118, Arg4);
    if (!sign_flag) goto loc_007D4BE6;
    goto loc_007D4BE6;
loc_007D4BE0:
loc_007D4BE6:
loc_007D4BEE:
loc_007D4BF6:
    result = ExReleaseResourceLite(*(uint64_t *)(v_rip + 0x71A393), v_stack_m100, v_stack_m118, Arg4);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_rip + 0x71A393), v_stack_m100, v_stack_m118, Arg4);
    result = (uint32_t)(((uint32_t)(v_stack_m128)) & ((uint32_t)((uint32_t)(0xC0000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_007D4CAB;
    if (Arg6 != 0) {
        Arg1 = v_stack_m100;
        if (Arg6 < v_stack_m100) { Arg1 = Arg6; }
        result = *(uint64_t *)(Arg1);
        *(uint64_t *)(Arg1) = result;
        result = v_stack_m118;
        *(uint64_t *)(Arg6) = result;
        v_stack_m118 = 0;
    }
    if (Arg5 != 0) {
        Arg1 = v_stack_m100;
        if (Arg5 < v_stack_m100) { Arg1 = Arg5; }
        result = *(uint32_t *)(Arg1);
        *(uint32_t *)(Arg1) = (uint32_t)(result);
        result = v_stack_m100;
        *(uint32_t *)(Arg5) = (uint32_t)(result);
    }
    if (v_stack_p18 != 0) {
        Arg1 = v_stack_m100;
        if (v_stack_p18 < v_stack_m100) { Arg1 = v_stack_p18; }
        result = *(uint32_t *)(Arg1);
        *(uint32_t *)(Arg1) = (uint32_t)(result);
        result = v_stack_m120;
        *(uint32_t *)(v_stack_p18) = (uint32_t)(result);
    }
    if (v_stack_p20 != 0) {
        Arg2 = v_stack_m100;
        if (v_stack_p20 < v_stack_m100) { Arg2 = v_stack_p20; }
        result = *(uint32_t *)(Arg2);
        *(uint32_t *)(Arg2) = (uint32_t)(result);
        result = v_stack_m10C;
        *(uint32_t *)(v_stack_p20) = (uint32_t)(result);
    }
    goto loc_007D4454;
loc_007D4CAB:
    if (v_stack_m118 != 0) {
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg1 = *(uint64_t *)(result + 0xB8);
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_stack_m118;
        result = MiUnmapViewOfSection(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (320);
    return (uint32_t)(v_stack_m128);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007D4310&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
