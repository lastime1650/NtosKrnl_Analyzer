# sub_008BBC01

- RVA: `0x008BBC01`–`0x008BC246` (길이 `1,605` bytes)
- VA: `0x00000001408BBC01`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00082ED8`
- 디코드: `387`개 명령, `1,605/1,605` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x008BBCBA` → [RtlFindAceByType](../../text/41/RtlFindAceByType_function_00410AF0.md) (function, `0x00410AF0`)
- `0x008BBD21` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008BBD2D` → [SepCopyTokenIntegrity](../../text/41/SepCopyTokenIntegrity_function_00419D10.md) (function, `0x00419D10`)
- `0x008BBD36` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008BBD44` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008BBD5F` → [RtlSidDominates](../../text/3F/RtlSidDominates_function_003FBD50.md) (function, `0x003FBD50`)
- `0x008BBDC8` → [SepLocateTokenTrustLevel](../../text/3E/SepLocateTokenTrustLevel_function_003EDA40.md) (function, `0x003EDA40`)
- `0x008BBDFA` → [RtlFindAceByType](../../text/41/RtlFindAceByType_function_00410AF0.md) (function, `0x00410AF0`)
- `0x008BBE40` → [RtlFindAceByType](../../text/41/RtlFindAceByType_function_00410AF0.md) (function, `0x00410AF0`)
- `0x008BBE77` → [RtlpValidFilterAclSubjectContext](RtlpValidFilterAclSubjectContext_function_008BCE60.md) (function, `0x008BCE60`)
- `0x008BBF3A` → [RtlFindAceBySid](../../text/40/RtlFindAceBySid_function_004004E0.md) (function, `0x004004E0`)
- `0x008BBF81` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008BBF9B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008BBFB5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008BC180` → [RtlpCombineAcls](../92/RtlpCombineAcls_function_0092CD70.md) (function, `0x0092CD70`)
- `0x008BC1C4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008BC1E7` → [RtlpValidTrustSubjectContext](../../text/3E/RtlpValidTrustSubjectContext_function_003ED770.md) (function, `0x003ED770`)
- `0x008BC219` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x008BBCDF` → RVA `0x00FD9AA0` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **16**
  - `0x008BBCBA` → [RtlFindAceByType](../../text/41/RtlFindAceByType_function_00410AF0.md) (`PAGE` → `.text`)
  - `0x008BBD21` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008BBD2D` → [SepCopyTokenIntegrity](../../text/41/SepCopyTokenIntegrity_function_00419D10.md) (`PAGE` → `.text`)
  - `0x008BBD36` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008BBD44` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008BBD5F` → [RtlSidDominates](../../text/3F/RtlSidDominates_function_003FBD50.md) (`PAGE` → `.text`)
  - `0x008BBDC8` → [SepLocateTokenTrustLevel](../../text/3E/SepLocateTokenTrustLevel_function_003EDA40.md) (`PAGE` → `.text`)
  - `0x008BBDFA` → [RtlFindAceByType](../../text/41/RtlFindAceByType_function_00410AF0.md) (`PAGE` → `.text`)
  - `0x008BBE40` → [RtlFindAceByType](../../text/41/RtlFindAceByType_function_00410AF0.md) (`PAGE` → `.text`)
  - `0x008BBF3A` → [RtlFindAceBySid](../../text/40/RtlFindAceBySid_function_004004E0.md) (`PAGE` → `.text`)
  - `0x008BBF81` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008BBF9B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008BBFB5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008BC1C4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008BC1E7` → [RtlpValidTrustSubjectContext](../../text/3E/RtlpValidTrustSubjectContext_function_003ED770.md) (`PAGE` → `.text`)
  - `0x008BC219` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **45**
  - `0x008BBC07` → [sub_008BB9AC + 0x49](Unknown_function_008BB9AC.md) (`tail-transfer`)
  - `0x008BBC0D` → [sub_008BB9AC + 0x234](Unknown_function_008BB9AC.md) (`tail-transfer`)
  - `0x008BBC2A` → [sub_008BB9AC + 0x12A](Unknown_function_008BB9AC.md) (`tail-transfer`)
  - `0x008BBC33` → [sub_008BB534 + 0x2D3](Unknown_function_008BB534.md) (`tail-transfer`)
  - `0x008BBC39` → [sub_008BB9AC + 0x100](Unknown_function_008BB9AC.md) (`tail-transfer`)
  - `0x008BBC41` → [sub_008BC25B + 0x11](Unknown_function_008BC25B.md) (`tail-transfer`)
  - `0x008BBC6E` → [sub_008BB9AC + 0x10F](Unknown_function_008BB9AC.md) (`tail-transfer`)
  - `0x008BBC74` → [sub_008BB9AC + 0x117](Unknown_function_008BB9AC.md) (`tail-transfer`)
  - `0x008BBC7C` → [sub_008BC3C4 + 0x46](Unknown_function_008BC3C4.md) (`tail-transfer`)
  - `0x008BBC87` → [sub_008BC25B + 0x123](Unknown_function_008BC25B.md) (`tail-transfer`)
  - `0x008BBC91` → [sub_008BB9AC + 0x12A](Unknown_function_008BB9AC.md) (`tail-transfer`)
  - `0x008BBD4D` → [sub_008BC3C4 + 0x66](Unknown_function_008BC3C4.md) (`tail-transfer`)
  - `0x008BBD73` → [sub_008BC3C4 + 0x2CF](Unknown_function_008BC3C4.md) (`tail-transfer`)
  - `0x008BBE4B` → [sub_008BC3C4 + 0x2B8](Unknown_function_008BC3C4.md) (`tail-transfer`)
  - `0x008BBE60` → [sub_008BB534 + 0x419](Unknown_function_008BB534.md) (`tail-transfer`)
  - `0x008BBE80` → [sub_008BB534 + 0x419](Unknown_function_008BB534.md) (`tail-transfer`)
  - `0x008BBEAB` → [sub_008BC3C4 + 0x17F](Unknown_function_008BC3C4.md) (`tail-transfer`)
  - `0x008BBEFF` → [sub_008BB534 + 0x311](Unknown_function_008BB534.md) (`tail-transfer`)
  - `0x008BBF28` → [sub_008BC3C4 + 0x21](Unknown_function_008BC3C4.md) (`tail-transfer`)
  - `0x008BBF42` → [sub_008BC3C4 + 0x463](Unknown_function_008BC3C4.md) (`tail-transfer`)
  - `0x008BBF4C` → [sub_008BB534 + 0x311](Unknown_function_008BB534.md) (`tail-transfer`)
  - `0x008BBF6C` → [sub_008BB534 + 0x419](Unknown_function_008BB534.md) (`tail-transfer`)
  - `0x008BBF76` → [sub_008BB534 + 0x3F4](Unknown_function_008BB534.md) (`tail-transfer`)
  - `0x008BBF86` → [sub_008BB534 + 0x3F4](Unknown_function_008BB534.md) (`tail-transfer`)
  - `0x008BBF90` → [sub_008BB534 + 0x3EB](Unknown_function_008BB534.md) (`tail-transfer`)
  - `0x008BBFA0` → [sub_008BB534 + 0x3EB](Unknown_function_008BB534.md) (`tail-transfer`)
  - `0x008BBFAA` → [sub_008BB534 + 0x3E2](Unknown_function_008BB534.md) (`tail-transfer`)
  - `0x008BBFBA` → [sub_008BB534 + 0x3E2](Unknown_function_008BB534.md) (`tail-transfer`)
  - `0x008BBFE3` → [sub_008BC3C4 + 0x237](Unknown_function_008BC3C4.md) (`tail-transfer`)
  - `0x008BC02D` → [sub_008BC3C4 + 0xBB](Unknown_function_008BC3C4.md) (`tail-transfer`)
  - `0x008BC04F` → [sub_008BC3C4 + 0x3C7](Unknown_function_008BC3C4.md) (`tail-transfer`)
  - `0x008BC068` → [sub_00B1A906 + 0xA2](../B1/Unknown_function_00B1A906.md) (`tail-transfer`)
  - `0x008BC0AA` → [sub_008BB534 + 0x307](Unknown_function_008BB534.md) (`tail-transfer`)
  - `0x008BC0DB` → [sub_00B1A906 + 0x16B](../B1/Unknown_function_00B1A906.md) (`tail-transfer`)
  - `0x008BC0FD` → [sub_008BC3C4 + 0x3D4](Unknown_function_008BC3C4.md) (`tail-transfer`)
  - `0x008BC189` → [sub_008BC3C4 + 0x205](Unknown_function_008BC3C4.md) (`tail-transfer`)
  - `0x008BC19C` → [sub_008BC25B + 0x134](Unknown_function_008BC25B.md) (`tail-transfer`)
  - `0x008BC1AF` → [sub_008BB534 + 0x245](Unknown_function_008BB534.md) (`tail-transfer`)
  - `0x008BC1B9` → [sub_008BB534 + 0x3D9](Unknown_function_008BB534.md) (`tail-transfer`)
  - `0x008BC1C9` → [sub_008BB534 + 0x3D9](Unknown_function_008BB534.md) (`tail-transfer`)
  - `0x008BC1F9` → [sub_008BB534 + 0x419](Unknown_function_008BB534.md) (`tail-transfer`)
  - `0x008BC204` → [sub_008BB9AC + 0x86](Unknown_function_008BB9AC.md) (`tail-transfer`)
  - `0x008BC20E` → [sub_008BB534 + 0x3D0](Unknown_function_008BB534.md) (`tail-transfer`)
  - `0x008BC21E` → [sub_008BB534 + 0x3D0](Unknown_function_008BB534.md) (`tail-transfer`)
  - `0x008BC241` → [sub_008BB534 + 0x3A4](Unknown_function_008BB534.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008BBC01  41 8D 40 F3                     lea eax, [r8 - 0xd]
008BBC05  3C 01                           cmp al, 1
008BBC07  0F 87 E8 FD FF FF               ja 0x1408bb9f5
008BBC0D  EB D1                           jmp 0x1408bbbe0
008BBC0F  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
008BBC13  45 33 C0                        xor r8d, r8d
008BBC16  44 8B 74 24 54                  mov r14d, dword ptr [rsp + 0x54]
008BBC1B  48 8B 00                        mov rax, qword ptr [rax]
008BBC1E  0F B7 48 02                     movzx ecx, word ptr [rax + 2]
008BBC22  F6 C1 04                        test cl, 4
008BBC25  75 52                           jne 0x1408bbc79
008BBC27  45 8B E0                        mov r12d, r8d
008BBC2A  E9 A7 FE FF FF                  jmp 0x1408bbad6
008BBC2F  2C 0D                           sub al, 0xd
008BBC31  3C 01                           cmp al, 1
008BBC33  0F 87 CE FB FF FF               ja 0x1408bb807
008BBC39  E9 6E FE FF FF                  jmp 0x1408bbaac
008BBC3E  66 85 C9                        test cx, cx
008BBC41  0F 88 25 06 00 00               js 0x1408bc26c
008BBC47  4D 8B 65 20                     mov r12, qword ptr [r13 + 0x20]
008BBC4B  8B 54 24 54                     mov edx, dword ptr [rsp + 0x54]
008BBC4F  8B C1                           mov eax, ecx
008BBC51  4C 8B 7D F8                     mov r15, qword ptr [rbp - 8]
008BBC55  25 00 10 00 00                  and eax, 0x1000
008BBC5A  83 C8 04                        or eax, 4
008BBC5D  0B D0                           or edx, eax
008BBC5F  B8 00 05 00 00                  mov eax, 0x500
008BBC64  66 23 C8                        and cx, ax
008BBC67  89 54 24 54                     mov dword ptr [rsp + 0x54], edx
008BBC6B  66 3B C8                        cmp cx, ax
008BBC6E  0F 84 47 FE FF FF               je 0x1408bbabb
008BBC74  E9 4A FE FF FF                  jmp 0x1408bbac3
008BBC79  66 85 C9                        test cx, cx
008BBC7C  0F 89 88 07 00 00               jns 0x1408bc40a
008BBC82  8B 48 10                        mov ecx, dword ptr [rax + 0x10]
008BBC85  85 C9                           test ecx, ecx
008BBC87  0F 84 F1 06 00 00               je 0x1408bc37e
008BBC8D  4C 8D 24 08                     lea r12, [rax + rcx]
008BBC91  E9 40 FE FF FF                  jmp 0x1408bbad6
008BBC96  41 8B C6                        mov eax, r14d
008BBC99  83 E0 10                        and eax, 0x10
008BBC9C  89 45 CC                        mov dword ptr [rbp - 0x34], eax
008BBC9F  0F 84 1F 01 00 00               je 0x1408bbdc4
008BBCA5  44 89 64 24 5C                  mov dword ptr [rsp + 0x5c], r12d
008BBCAA  45 32 ED                        xor r13b, r13b
008BBCAD  4C 8D 44 24 5C                  lea r8, [rsp + 0x5c]
008BBCB2  BA 11 00 00 00                  mov edx, 0x11
008BBCB7  48 8B CE                        mov rcx, rsi
008BBCBA  E8 31 4E B5 FF                  call 0x140410af0
008BBCBF  48 8B F8                        mov rdi, rax
008BBCC2  48 85 C0                        test rax, rax
008BBCC5  0F 85 86 02 00 00               jne 0x1408bbf51
008BBCCB  C6 44 24 50 00                  mov byte ptr [rsp + 0x50], 0
008BBCD0  0F 57 C0                        xorps xmm0, xmm0
008BBCD3  49 8B F4                        mov rsi, r12
008BBCD6  0F 11 45 F8                     movups xmmword ptr [rbp - 8], xmm0
008BBCDA  4D 85 E4                        test r12, r12
008BBCDD  75 0E                           jne 0x1408bbced
008BBCDF  48 8B 05 BA DD 71 00            mov rax, qword ptr [rip + 0x71ddba]
008BBCE6  48 8B B0 E8 01 00 00            mov rsi, qword ptr [rax + 0x1e8]
008BBCED  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
008BBCF1  48 8B 18                        mov rbx, qword ptr [rax]
008BBCF4  48 85 DB                        test rbx, rbx
008BBCF7  75 04                           jne 0x1408bbcfd
008BBCF9  48 8B 58 10                     mov rbx, qword ptr [rax + 0x10]
008BBCFD  83 BB C0 00 00 00 02            cmp dword ptr [rbx + 0xc0], 2
008BBD04  0F 84 28 04 00 00               je 0x1408bc132
008BBD0A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008BBD13  B2 01                           mov dl, 1
008BBD15  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008BBD1C  90                              nop
008BBD1D  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
008BBD21  E8 9A 5E 95 FF                  call 0x140211bc0
008BBD26  48 8D 55 F8                     lea rdx, [rbp - 8]
008BBD2A  48 8B CB                        mov rcx, rbx
008BBD2D  E8 DE DF B5 FF                  call 0x140419d10
008BBD32  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
008BBD36  E8 D5 3C 9A FF                  call 0x14025fa10
008BBD3B  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008BBD44  E8 A7 32 9A FF                  call 0x14025eff0
008BBD49  41 F6 C5 08                     test r13b, 8
008BBD4D  0F 85 D7 06 00 00               jne 0x1408bc42a
008BBD53  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
008BBD57  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
008BBD5C  48 8B D6                        mov rdx, rsi
008BBD5F  E8 EC FF B3 FF                  call 0x1403fbd50
008BBD64  85 C0                           test eax, eax
008BBD66  0F 88 FB 01 00 00               js 0x1408bbf67
008BBD6C  0F B6 44 24 50                  movzx eax, byte ptr [rsp + 0x50]
008BBD71  84 C0                           test al, al
008BBD73  0F 84 1A 09 00 00               je 0x1408bc693
008BBD79  FF 44 24 5C                     inc dword ptr [rsp + 0x5c]
008BBD7D  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
008BBD82  48 85 FF                        test rdi, rdi
008BBD85  0F 85 22 FF FF FF               jne 0x1408bbcad
008BBD8B  0F B6 44 24 58                  movzx eax, byte ptr [rsp + 0x58]
008BBD90  4C 8B 45 10                     mov r8, qword ptr [rbp + 0x10]
008BBD94  88 44 24 50                     mov byte ptr [rsp + 0x50], al
008BBD98  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
008BBD9C  48 89 45 F8                     mov qword ptr [rbp - 8], rax
008BBDA0  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
008BBDA4  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
008BBDA8  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
008BBDAC  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
008BBDB0  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
008BBDB4  4C 89 45 A0                     mov qword ptr [rbp - 0x60], r8
008BBDB8  4C 8B 45 20                     mov r8, qword ptr [rbp + 0x20]
008BBDBC  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
008BBDC0  4C 89 45 A8                     mov qword ptr [rbp - 0x58], r8
008BBDC4  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
008BBDC8  E8 73 1C B3 FF                  call 0x1403eda40
008BBDCD  45 8B EE                        mov r13d, r14d
008BBDD0  48 8B F8                        mov rdi, rax
008BBDD3  41 81 E5 80 00 00 00            and r13d, 0x80
008BBDDA  74 38                           je 0x1408bbe14
008BBDDC  48 85 C0                        test rax, rax
008BBDDF  0F 84 0F 04 00 00               je 0x1408bc1f4
008BBDE5  C7 44 24 5C 00 00 00 00         mov dword ptr [rsp + 0x5c], 0
008BBDED  4C 8D 44 24 5C                  lea r8, [rsp + 0x5c]
008BBDF2  BA 14 00 00 00                  mov edx, 0x14
008BBDF7  48 8B CE                        mov rcx, rsi
008BBDFA  E8 F1 4C B5 FF                  call 0x140410af0
008BBDFF  48 8B D8                        mov rbx, rax
008BBE02  48 85 C0                        test rax, rax
008BBE05  0F 85 C3 03 00 00               jne 0x1408bc1ce
008BBE0B  FF 44 24 5C                     inc dword ptr [rsp + 0x5c]
008BBE0F  48 85 DB                        test rbx, rbx
008BBE12  75 D9                           jne 0x1408bbded
008BBE14  45 8B E6                        mov r12d, r14d
008BBE17  41 81 E4 00 01 00 00            and r12d, 0x100
008BBE1E  74 66                           je 0x1408bbe86
008BBE20  33 C0                           xor eax, eax
008BBE22  66 C7 45 6C 00 01               mov word ptr [rbp + 0x6c], 0x100
008BBE28  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
008BBE2C  89 45 68                        mov dword ptr [rbp + 0x68], eax
008BBE2F  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
008BBE33  4C 8D 44 24 5C                  lea r8, [rsp + 0x5c]
008BBE38  BA 15 00 00 00                  mov edx, 0x15
008BBE3D  48 8B CE                        mov rcx, rsi
008BBE40  E8 AB 4C B5 FF                  call 0x140410af0
008BBE45  4C 8B C0                        mov r8, rax
008BBE48  48 85 C0                        test rax, rax
008BBE4B  0F 85 2B 08 00 00               jne 0x1408bc67c
008BBE51  FF 44 24 5C                     inc dword ptr [rsp + 0x5c]
008BBE55  4D 85 C0                        test r8, r8
008BBE58  75 D9                           jne 0x1408bbe33
008BBE5A  8B 5C 24 70                     mov ebx, dword ptr [rsp + 0x70]
008BBE5E  85 DB                           test ebx, ebx
008BBE60  0F 88 E7 FA FF FF               js 0x1408bb94d
008BBE66  8B 85 10 01 00 00               mov eax, dword ptr [rbp + 0x110]
008BBE6C  83 E0 02                        and eax, 2
008BBE6F  75 15                           jne 0x1408bbe86
008BBE71  48 8B D7                        mov rdx, rdi
008BBE74  49 8B CF                        mov rcx, r15
008BBE77  E8 E4 0F 00 00                  call 0x1408bce60
008BBE7C  8B D8                           mov ebx, eax
008BBE7E  85 C0                           test eax, eax
008BBE80  0F 88 C7 FA FF FF               js 0x1408bb94d
008BBE86  8B BD 10 01 00 00               mov edi, dword ptr [rbp + 0x110]
008BBE8C  BB 00 0A 00 00                  mov ebx, 0xa00
008BBE91  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
008BBE95  83 E7 02                        and edi, 2
008BBE98  41 F6 C6 08                     test r14b, 8
008BBE9C  0F 84 1D 01 00 00               je 0x1408bbfbf
008BBEA2  0F B7 51 02                     movzx edx, word ptr [rcx + 2]
008BBEA6  44 8B CA                        mov r9d, edx
008BBEA9  85 FF                           test edi, edi
008BBEAB  0F 85 92 06 00 00               jne 0x1408bc543
008BBEB1  41 81 E1 00 20 00 00            and r9d, 0x2000
008BBEB8  48 89 75 68                     mov qword ptr [rbp + 0x68], rsi
008BBEBC  41 81 C9 10 80 00 00            or r9d, 0x8010
008BBEC3  66 23 D3                        and dx, bx
008BBEC6  44 89 4C 24 54                  mov dword ptr [rsp + 0x54], r9d
008BBECB  66 3B D3                        cmp dx, bx
008BBECE  0F 85 F5 00 00 00               jne 0x1408bbfc9
008BBED4  41 BA 00 08 00 00               mov r10d, 0x800
008BBEDA  45 0B CA                        or r9d, r10d
008BBEDD  44 89 4C 24 54                  mov dword ptr [rsp + 0x54], r9d
008BBEE2  E9 E8 00 00 00                  jmp 0x1408bbfcf
008BBEE7  49 8B 45 00                     mov rax, qword ptr [r13]
008BBEEB  0F B7 48 02                     movzx ecx, word ptr [rax + 2]
008BBEEF  B8 0C 14 00 00                  mov eax, 0x140c
008BBEF4  66 23 C8                        and cx, ax
008BBEF7  66 09 4E 02                     or word ptr [rsi + 2], cx
008BBEFB  80 7D F0 00                     cmp byte ptr [rbp - 0x10], 0
008BBEFF  0F 84 40 F9 FF FF               je 0x1408bb845
008BBF05  45 33 ED                        xor r13d, r13d
008BBF08  C7 45 70 01 01 00 00            mov dword ptr [rbp + 0x70], 0x101
008BBF0F  44 89 6C 24 5C                  mov dword ptr [rsp + 0x5c], r13d
008BBF14  C7 45 74 00 00 00 03            mov dword ptr [rbp + 0x74], 0x3000000
008BBF1B  C7 45 78 04 00 00 00            mov dword ptr [rbp + 0x78], 4
008BBF22  0F B7 46 02                     movzx eax, word ptr [rsi + 2]
008BBF26  A8 04                           test al, 4
008BBF28  0F 85 B7 04 00 00               jne 0x1408bc3e5
008BBF2E  49 8B CD                        mov rcx, r13
008BBF31  4C 8D 44 24 5C                  lea r8, [rsp + 0x5c]
008BBF36  48 8D 55 70                     lea rdx, [rbp + 0x70]
008BBF3A  E8 A1 45 B4 FF                  call 0x1404004e0
008BBF3F  48 85 C0                        test rax, rax
008BBF42  0F 85 DF 08 00 00               jne 0x1408bc827
008BBF48  4C 8B 6D B8                     mov r13, qword ptr [rbp - 0x48]
008BBF4C  E9 F4 F8 FF FF                  jmp 0x1408bb845
008BBF51  F7 40 04 F8 FF FF FF            test dword ptr [rax + 4], 0xfffffff8
008BBF58  4C 8D 60 08                     lea r12, [rax + 8]
008BBF5C  44 0F B6 68 01                  movzx r13d, byte ptr [rax + 1]
008BBF61  0F 84 64 FD FF FF               je 0x1408bbccb
008BBF67  BB 46 04 00 C0                  mov ebx, 0xc0000446
008BBF6C  E9 DC F9 FF FF                  jmp 0x1408bb94d
008BBF71  80 7C 24 6C 00                  cmp byte ptr [rsp + 0x6c], 0
008BBF76  0F 84 AC F9 FF FF               je 0x1408bb928
008BBF7C  33 D2                           xor edx, edx
008BBF7E  48 8B CF                        mov rcx, rdi
008BBF81  E8 EA 68 2C 00                  call 0x140b82870
008BBF86  E9 9D F9 FF FF                  jmp 0x1408bb928
008BBF8B  80 7C 24 6B 00                  cmp byte ptr [rsp + 0x6b], 0
008BBF90  0F 84 89 F9 FF FF               je 0x1408bb91f
008BBF96  33 D2                           xor edx, edx
008BBF98  49 8B CE                        mov rcx, r14
008BBF9B  E8 D0 68 2C 00                  call 0x140b82870
008BBFA0  E9 7A F9 FF FF                  jmp 0x1408bb91f
008BBFA5  80 7C 24 6A 00                  cmp byte ptr [rsp + 0x6a], 0
008BBFAA  0F 84 66 F9 FF FF               je 0x1408bb916
008BBFB0  33 D2                           xor edx, edx
008BBFB2  49 8B CC                        mov rcx, r12
008BBFB5  E8 B6 68 2C 00                  call 0x140b82870
008BBFBA  E9 57 F9 FF FF                  jmp 0x1408bb916
008BBFBF  4C 89 7D 68                     mov qword ptr [rbp + 0x68], r15
008BBFC3  41 B9 00 80 00 00               mov r9d, 0x8000
008BBFC9  41 BA 00 08 00 00               mov r10d, 0x800
008BBFCF  41 8B F1                        mov esi, r9d
008BBFD2  41 F6 C6 20                     test r14b, 0x20
008BBFD6  74 39                           je 0x1408bc011
008BBFD8  0F B7 51 02                     movzx edx, word ptr [rcx + 2]
008BBFDC  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
008BBFE1  85 FF                           test edi, edi
008BBFE3  0F 85 12 06 00 00               jne 0x1408bc5fb
008BBFE9  8B C2                           mov eax, edx
008BBFEB  4C 89 45 98                     mov qword ptr [rbp - 0x68], r8
008BBFEF  25 00 20 00 00                  and eax, 0x2000
008BBFF4  66 23 D3                        and dx, bx
008BBFF7  83 C8 10                        or eax, 0x10
008BBFFA  44 0B C8                        or r9d, eax
008BBFFD  44 89 4C 24 54                  mov dword ptr [rsp + 0x54], r9d
008BC002  66 3B D3                        cmp dx, bx
008BC005  75 13                           jne 0x1408bc01a
008BC007  45 0B CA                        or r9d, r10d
008BC00A  44 89 4C 24 54                  mov dword ptr [rsp + 0x54], r9d
008BC00F  EB 09                           jmp 0x1408bc01a
008BC011  4C 89 7D 98                     mov qword ptr [rbp - 0x68], r15
008BC015  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
008BC01A  41 8B F1                        mov esi, r9d
008BC01D  41 F6 C6 40                     test r14b, 0x40
008BC021  0F 84 0C 02 00 00               je 0x1408bc233
008BC027  0F B7 51 02                     movzx edx, word ptr [rcx + 2]
008BC02B  85 FF                           test edi, edi
008BC02D  0F 85 4C 04 00 00               jne 0x1408bc47f
008BC033  8B C2                           mov eax, edx
008BC035  4C 89 45 A0                     mov qword ptr [rbp - 0x60], r8
008BC039  25 00 20 00 00                  and eax, 0x2000
008BC03E  66 23 D3                        and dx, bx
008BC041  83 C8 10                        or eax, 0x10
008BC044  44 0B C8                        or r9d, eax
008BC047  44 89 4C 24 54                  mov dword ptr [rsp + 0x54], r9d
008BC04C  66 3B D3                        cmp dx, bx
008BC04F  0F 84 36 07 00 00               je 0x1408bc78b
008BC055  45 85 ED                        test r13d, r13d
008BC058  41 8B F1                        mov esi, r9d
008BC05B  4C 8B 6D E0                     mov r13, qword ptr [rbp - 0x20]
008BC05F  74 4E                           je 0x1408bc0af
008BC061  41 0F B7 55 02                  movzx edx, word ptr [r13 + 2]
008BC066  85 FF                           test edi, edi
008BC068  0F 85 3A E9 25 00               jne 0x140b1a9a8
008BC06E  4C 8B 54 24 78                  mov r10, qword ptr [rsp + 0x78]
008BC073  8B C2                           mov eax, edx
008BC075  25 00 20 00 00                  and eax, 0x2000
008BC07A  4C 89 55 90                     mov qword ptr [rbp - 0x70], r10
008BC07E  83 C8 10                        or eax, 0x10
008BC081  66 23 D3                        and dx, bx
008BC084  44 0B C8                        or r9d, eax
008BC087  4D 8B DA                        mov r11, r10
008BC08A  44 89 4C 24 54                  mov dword ptr [rsp + 0x54], r9d
008BC08F  66 3B D3                        cmp dx, bx
008BC092  75 27                           jne 0x1408bc0bb
008BC094  B8 00 08 00 00                  mov eax, 0x800
008BC099  44 0B C8                        or r9d, eax
008BC09C  44 89 4C 24 54                  mov dword ptr [rsp + 0x54], r9d
008BC0A1  EB 18                           jmp 0x1408bc0bb
008BC0A3  48 8D 7E 10                     lea rdi, [rsi + 0x10]
008BC0A7  44 89 17                        mov dword ptr [rdi], r10d
008BC0AA  E9 8C F7 FF FF                  jmp 0x1408bb83b
008BC0AF  4D 8B DF                        mov r11, r15
008BC0B2  4C 89 7D 90                     mov qword ptr [rbp - 0x70], r15
008BC0B6  4C 8B 54 24 78                  mov r10, qword ptr [rsp + 0x78]
008BC0BB  45 85 E4                        test r12d, r12d
008BC0BE  41 8B F1                        mov esi, r9d
008BC0C1  41 BC 00 08 00 00               mov r12d, 0x800
008BC0C7  0F 84 56 01 00 00               je 0x1408bc223
008BC0CD  41 0F B7 55 02                  movzx edx, word ptr [r13 + 2]
008BC0D2  85 FF                           test edi, edi
008BC0D4  48 8B 7D 80                     mov rdi, qword ptr [rbp - 0x80]
008BC0D8  4D 8B C2                        mov r8, r10
008BC0DB  0F 85 90 E9 25 00               jne 0x140b1aa71
008BC0E1  8B C2                           mov eax, edx
008BC0E3  4C 89 55 A8                     mov qword ptr [rbp - 0x58], r10
008BC0E7  25 00 20 00 00                  and eax, 0x2000
008BC0EC  66 23 D3                        and dx, bx
008BC0EF  83 C8 10                        or eax, 0x10
008BC0F2  44 0B C8                        or r9d, eax
008BC0F5  44 89 4C 24 54                  mov dword ptr [rsp + 0x54], r9d
008BC0FA  66 3B D3                        cmp dx, bx
008BC0FD  0F 84 95 06 00 00               je 0x1408bc798
008BC103  83 7D CC 00                     cmp dword ptr [rbp - 0x34], 0
008BC107  74 3B                           je 0x1408bc144
008BC109  41 0F B7 4D 02                  movzx ecx, word ptr [r13 + 2]
008BC10E  8B C1                           mov eax, ecx
008BC110  66 23 CB                        and cx, bx
008BC113  25 00 20 00 00                  and eax, 0x2000
008BC118  83 C8 10                        or eax, 0x10
008BC11B  44 0B C8                        or r9d, eax
008BC11E  44 89 4C 24 54                  mov dword ptr [rsp + 0x54], r9d
008BC123  66 3B CB                        cmp cx, bx
008BC126  75 1F                           jne 0x1408bc147
008BC128  45 0B CC                        or r9d, r12d
008BC12B  44 89 4C 24 54                  mov dword ptr [rsp + 0x54], r9d
008BC130  EB 15                           jmp 0x1408bc147
008BC132  83 BB C4 00 00 00 02            cmp dword ptr [rbx + 0xc4], 2
008BC139  0F 8D CB FB FF FF               jge 0x1408bbd0a
008BC13F  E9 23 FE FF FF                  jmp 0x1408bbf67
008BC144  4D 8B D7                        mov r10, r15
008BC147  4C 8B 65 A0                     mov r12, qword ptr [rbp - 0x60]
008BC14B  48 8D 45 28                     lea rax, [rbp + 0x28]
008BC14F  48 8B 75 68                     mov rsi, qword ptr [rbp + 0x68]
008BC153  4D 8B CC                        mov r9, r12
008BC156  48 C7 44 24 40 00 00 00 00      mov qword ptr [rsp + 0x40], 0
008BC15F  49 8B D2                        mov rdx, r10
008BC162  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008BC167  48 8B CE                        mov rcx, rsi
008BC16A  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
008BC16F  4C 8B 7D 98                     mov r15, qword ptr [rbp - 0x68]
008BC173  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
008BC178  4D 8B C7                        mov r8, r15
008BC17B  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
008BC180  E8 EB 0B 07 00                  call 0x14092cd70
008BC185  8B D8                           mov ebx, eax
008BC187  85 C0                           test eax, eax
008BC189  0F 88 3A 04 00 00               js 0x1408bc5c9
008BC18F  48 83 7D 68 00                  cmp qword ptr [rbp + 0x68], 0
008BC194  48 8B 75 28                     mov rsi, qword ptr [rbp + 0x28]
008BC198  48 89 75 D0                     mov qword ptr [rbp - 0x30], rsi
008BC19C  0F 84 ED 01 00 00               je 0x1408bc38f
008BC1A2  48 8B 5D C0                     mov rbx, qword ptr [rbp - 0x40]
008BC1A6  4C 8B 55 88                     mov r10, qword ptr [rbp - 0x78]
008BC1AA  C6 44 24 6D 01                  mov byte ptr [rsp + 0x6d], 1
008BC1AF  E9 C5 F5 FF FF                  jmp 0x1408bb779
008BC1B4  80 7C 24 69 00                  cmp byte ptr [rsp + 0x69], 0
008BC1B9  0F 84 4E F7 FF FF               je 0x1408bb90d
008BC1BF  33 D2                           xor edx, edx
008BC1C1  49 8B CF                        mov rcx, r15
008BC1C4  E8 A7 66 2C 00                  call 0x140b82870
008BC1C9  E9 3F F7 FF FF                  jmp 0x1408bb90d
008BC1CE  F7 40 04 00 00 00 FF            test dword ptr [rax + 4], 0xff000000
008BC1D5  0F 85 8C FD FF FF               jne 0x1408bbf67
008BC1DB  48 8D 50 08                     lea rdx, [rax + 8]
008BC1DF  48 8B CF                        mov rcx, rdi
008BC1E2  4C 8D 4C 24 70                  lea r9, [rsp + 0x70]
008BC1E7  E8 84 15 B3 FF                  call 0x1403ed770
008BC1EC  84 C0                           test al, al
008BC1EE  0F 85 17 FC FF FF               jne 0x1408bbe0b
008BC1F4  BB 22 00 00 C0                  mov ebx, 0xc0000022
008BC1F9  E9 4F F7 FF FF                  jmp 0x1408bb94d
008BC1FE  45 33 D2                        xor r10d, r10d
008BC201  45 8B F2                        mov r14d, r10d
008BC204  E9 29 F8 FF FF                  jmp 0x1408bba32
008BC209  80 7C 24 68 00                  cmp byte ptr [rsp + 0x68], 0
008BC20E  0F 84 F0 F6 FF FF               je 0x1408bb904
008BC214  33 D2                           xor edx, edx
008BC216  48 8B CE                        mov rcx, rsi
008BC219  E8 52 66 2C 00                  call 0x140b82870
008BC21E  E9 E1 F6 FF FF                  jmp 0x1408bb904
008BC223  48 8B 7D 80                     mov rdi, qword ptr [rbp - 0x80]
008BC227  4D 8B C7                        mov r8, r15
008BC22A  4C 89 7D A8                     mov qword ptr [rbp - 0x58], r15
008BC22E  E9 D0 FE FF FF                  jmp 0x1408bc103
008BC233  4C 89 7D A0                     mov qword ptr [rbp - 0x60], r15
008BC237  E9 19 FE FF FF                  jmp 0x1408bc055
008BC23C  BB 17 00 00 C0                  mov ebx, 0xc0000017
008BC241  E9 92 F6 FF FF                  jmp 0x1408bb8d8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_008BBC01(__int64 a1, __int64 a2, __int64 a3)
{
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int8 v_stack_p50;
    unsigned int v_stack_p54;
    unsigned __int8 v_stack_p58;
    unsigned int v_stack_p5C;
    unsigned __int8 v_stack_p68;
    unsigned __int8 v_stack_p69;
    unsigned __int8 v_stack_p6A;
    unsigned __int8 v_stack_p6B;
    unsigned __int8 v_stack_p6C;
    unsigned __int8 v_stack_p6D;
    unsigned int v_stack_p70;
    unsigned __int64 v_stack_p78;
}
```

## 5. (Beta) C Style

```c
int64_t sub_008BBC01(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint8_t v_stack_p50;
    uint32_t v_stack_p54;
    uint8_t v_stack_p58;
    uint32_t v_stack_p5C;
    uint8_t v_stack_p68;
    uint8_t v_stack_p69;
    uint8_t v_stack_p6A;
    uint8_t v_stack_p6B;
    uint8_t v_stack_p6C;
    uint8_t v_stack_p6D;
    uint32_t v_stack_p70;
    uint64_t v_stack_p78;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `- 0xD` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008BBC01&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
