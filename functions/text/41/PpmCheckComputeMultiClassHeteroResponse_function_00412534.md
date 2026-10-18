# PpmCheckComputeMultiClassHeteroResponse

- RVA: `0x00412534`–`0x00412ADA` (길이 `1,446` bytes)
- VA: `0x0000000140412534`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009BF04`
- 디코드: `353`개 명령, `1,446/1,446` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x00412679` → [PpmHeteroComputeCoreParkingUtilities](PpmHeteroComputeCoreParkingUtilities_function_00412AE0.md) (function, `0x00412AE0`)
- `0x00412730` → [PpmHeteroUtilityGreaterThanOrEqualThreshold](PpmHeteroUtilityGreaterThanOrEqualThreshold_function_004124A0.md) (function, `0x004124A0`)
- `0x00412748` → [PpmHeteroUtilityGreaterThanOrEqualThreshold](PpmHeteroUtilityGreaterThanOrEqualThreshold_function_004124A0.md) (function, `0x004124A0`)
- `0x004127B4` → [PpmHeteroUtilityGreaterThanOrEqualThreshold](PpmHeteroUtilityGreaterThanOrEqualThreshold_function_004124A0.md) (function, `0x004124A0`)
- `0x004127CF` → [PpmHeteroUtilityGreaterThanOrEqualThreshold](PpmHeteroUtilityGreaterThanOrEqualThreshold_function_004124A0.md) (function, `0x004124A0`)
- `0x0041290C` → [PpmEventTraceMultiClassHeteroResponse](PpmEventTraceMultiClassHeteroResponse_function_004135AC.md) (function, `0x004135AC`)
- `0x0041293A` → [PpmHeteroComputeMultiClassUnparkCount](PpmHeteroComputeMultiClassUnparkCount_function_00411F94.md) (function, `0x00411F94`)
- `0x00412964` → [PpmEventTraceHeteroResponse](PpmEventTraceHeteroResponse_function_004133AC.md) (function, `0x004133AC`)
- `0x00412989` → [PpmParkCalculateUnparkCount](PpmParkCalculateUnparkCount_function_00413750.md) (function, `0x00413750`)
- `0x00412A97` → [PpmEventTraceMultiClassHeteroResponseUpdate](../4D/PpmEventTraceMultiClassHeteroResponseUpdate_function_004D0B1C.md) (function, `0x004D0B1C`)
- `0x00412AB3` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PpmCheckComputeHeteroResponse](../4A/PpmCheckComputeHeteroResponse_function_004AACD0.md) at `0x004AAD93`

### Static image references
- `0x0041255A` → RVA `0x00E0A740` (`.data`; read)
- `0x0041256B` → RVA `0x00E08380` (`.data`; read)
- `0x00412574` → RVA `0x00F0CE0C` (`.data`; read)
- `0x0041259D` → RVA `0x00F083E0` (`.data`; read)
- `0x004125C0` → RVA `0x00F083D8` (`.data`; read)
- `0x004125C7` → RVA `0x00FC6A86` (`ALMOSTRO`; read)
- `0x00412825` → RVA `0x00F0B244` (`.data`; read)
- `0x00412A0D` → RVA `0x00F083A0` (`.data`; read)
- `0x00412A19` → RVA `0x00F083A2` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00412534  48 8B C4                        mov rax, rsp
00412537  48 89 58 08                     mov qword ptr [rax + 8], rbx
0041253B  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
0041253F  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
00412543  55                              push rbp
00412544  41 54                           push r12
00412546  41 55                           push r13
00412548  41 56                           push r14
0041254A  41 57                           push r15
0041254C  48 8D A8 28 FC FF FF            lea rbp, [rax - 0x3d8]
00412553  48 81 EC B0 04 00 00            sub rsp, 0x4b0
0041255A  48 8B 05 DF 81 9F 00            mov rax, qword ptr [rip + 0x9f81df]
00412561  48 33 C4                        xor rax, rsp
00412564  48 89 85 A0 03 00 00            mov qword ptr [rbp + 0x3a0], rax
0041256B  48 8B 3D 0E 5E 9F 00            mov rdi, qword ptr [rip + 0x9f5e0e]
00412572  33 DB                           xor ebx, ebx
00412574  48 63 05 91 A8 AF 00            movsxd rax, dword ptr [rip + 0xafa891]
0041257B  48 83 C7 28                     add rdi, 0x28
0041257F  48 69 C8 E8 01 00 00            imul rcx, rax, 0x1e8
00412586  0F 57 C0                        xorps xmm0, xmm0
00412589  0F 11 45 88                     movups xmmword ptr [rbp - 0x78], xmm0
0041258D  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
00412592  8D 73 01                        lea esi, [rbx + 1]
00412595  48 03 F9                        add rdi, rcx
00412598  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
0041259D  39 1D 3D 5E AF 00               cmp dword ptr [rip + 0xaf5e3d], ebx
004125A3  8B CB                           mov ecx, ebx
004125A5  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
004125AA  89 5C 24 68                     mov dword ptr [rsp + 0x68], ebx
004125AE  0F 84 D5 03 00 00               je 0x140412989
004125B4  8B C1                           mov eax, ecx
004125B6  44 8B F3                        mov r14d, ebx
004125B9  48 69 F8 10 05 00 00            imul rdi, rax, 0x510
004125C0  48 03 3D 11 5E AF 00            add rdi, qword ptr [rip + 0xaf5e11]
004125C7  38 1D B9 44 BB 00               cmp byte ptr [rip + 0xbb44b9], bl
004125CD  48 89 7D 80                     mov qword ptr [rbp - 0x80], rdi
004125D1  75 0C                           jne 0x1404125df
004125D3  38 9F A1 04 00 00               cmp byte ptr [rdi + 0x4a1], bl
004125D9  0F 84 93 03 00 00               je 0x140412972
004125DF  0F 57 C0                        xorps xmm0, xmm0
004125E2  89 5C 24 58                     mov dword ptr [rsp + 0x58], ebx
004125E6  0F 11 45 88                     movups xmmword ptr [rbp - 0x78], xmm0
004125EA  0F B7 47 04                     movzx eax, word ptr [rdi + 4]
004125EE  44 8B FB                        mov r15d, ebx
004125F1  66 89 45 90                     mov word ptr [rbp - 0x70], ax
004125F5  44 8A EB                        mov r13b, bl
004125F8  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
004125FC  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00412600  0F B6 57 0C                     movzx edx, byte ptr [rdi + 0xc]
00412604  40 3A D6                        cmp dl, sil
00412607  76 2B                           jbe 0x140412634
00412609  48 8B 8F 08 05 00 00            mov rcx, qword ptr [rdi + 0x508]
00412610  48 81 C1 80 02 00 00            add rcx, 0x280
00412617  2B D6                           sub edx, esi
00412619  0F B7 41 08                     movzx eax, word ptr [rcx + 8]
0041261D  44 02 29                        add r13b, byte ptr [rcx]
00412620  44 03 F8                        add r15d, eax
00412623  48 8D 89 80 02 00 00            lea rcx, [rcx + 0x280]
0041262A  48 2B D6                        sub rdx, rsi
0041262D  75 EA                           jne 0x140412619
0041262F  44 89 7C 24 58                  mov dword ptr [rsp + 0x58], r15d
00412634  38 1D 4C 44 BB 00               cmp byte ptr [rip + 0xbb444c], bl
0041263A  74 18                           je 0x140412654
0041263C  48 8B 87 08 05 00 00            mov rax, qword ptr [rdi + 0x508]
00412643  44 8A 6F 0A                     mov r13b, byte ptr [rdi + 0xa]
00412647  44 0F B7 B8 88 02 00 00         movzx r15d, word ptr [rax + 0x288]
0041264F  44 89 7C 24 58                  mov dword ptr [rsp + 0x58], r15d
00412654  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00412659  33 C9                           xor ecx, ecx
0041265B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00412660  4C 8D 4D A0                     lea r9, [rbp - 0x60]
00412664  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00412669  4C 8D 85 A0 00 00 00            lea r8, [rbp + 0xa0]
00412670  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00412675  48 8D 55 88                     lea rdx, [rbp - 0x78]
00412679  E8 62 04 00 00                  call 0x140412ae0
0041267E  0F B7 4F 0A                     movzx ecx, word ptr [rdi + 0xa]
00412682  4C 8B D3                        mov r10, rbx
00412685  48 8B 87 68 04 00 00            mov rax, qword ptr [rdi + 0x468]
0041268C  4C 8B CB                        mov r9, rbx
0041268F  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
00412694  85 C9                           test ecx, ecx
00412696  74 36                           je 0x1404126ce
00412698  8B D1                           mov edx, ecx
0041269A  4C 8D 04 C8                     lea r8, [rax + rcx*8]
0041269E  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
004126A3  49 0F AF 00                     imul rax, qword ptr [r8]
004126A7  4C 03 C8                        add r9, rax
004126AA  48 8B C2                        mov rax, rdx
004126AD  FF C9                           dec ecx
004126AF  48 2B D6                        sub rdx, rsi
004126B2  4C 89 8C CD A0 01 00 00         mov qword ptr [rbp + rcx*8 + 0x1a0], r9
004126BA  49 0F AF 00                     imul rax, qword ptr [r8]
004126BE  4D 8D 40 F8                     lea r8, [r8 - 8]
004126C2  4C 03 D0                        add r10, rax
004126C5  85 C9                           test ecx, ecx
004126C7  75 D5                           jne 0x14041269e
004126C9  4C 89 54 24 50                  mov qword ptr [rsp + 0x50], r10
004126CE  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
004126D3  45 85 FF                        test r15d, r15d
004126D6  74 15                           je 0x1404126ed
004126D8  48 8D 4D A0                     lea rcx, [rbp - 0x60]
004126DC  41 8B D7                        mov edx, r15d
004126DF  8B 01                           mov eax, dword ptr [rcx]
004126E1  48 8D 49 04                     lea rcx, [rcx + 4]
004126E5  4C 2B E0                        sub r12, rax
004126E8  48 2B D6                        sub rdx, rsi
004126EB  75 F2                           jne 0x1404126df
004126ED  45 0F B6 ED                     movzx r13d, r13b
004126F1  41 8B F7                        mov esi, r15d
004126F4  45 3B FD                        cmp r15d, r13d
004126F7  0F 83 83 00 00 00               jae 0x140412780
004126FD  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
00412702  41 BF 01 00 00 00               mov r15d, 1
00412708  EB 05                           jmp 0x14041270f
0041270A  4C 8B 54 24 50                  mov r10, qword ptr [rsp + 0x50]
0041270F  8B C6                           mov eax, esi
00412711  49 8B CA                        mov rcx, r10
00412714  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
00412718  4C 8B 84 C5 A0 01 00 00         mov r8, qword ptr [rbp + rax*8 + 0x1a0]
00412720  44 0F B6 8C 38 33 01 00 00      movzx r9d, byte ptr [rax + rdi + 0x133]
00412729  8B 94 85 A0 00 00 00            mov edx, dword ptr [rbp + rax*4 + 0xa0]
00412730  E8 6B FD FF FF                  call 0x1404124a0
00412735  85 C0                           test eax, eax
00412737  74 29                           je 0x140412762
00412739  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0041273E  45 33 C0                        xor r8d, r8d
00412741  49 8B D4                        mov rdx, r12
00412744  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
00412748  E8 53 FD FF FF                  call 0x1404124a0
0041274D  85 C0                           test eax, eax
0041274F  74 11                           je 0x140412762
00412751  8B C6                           mov eax, esi
00412753  41 03 F7                        add esi, r15d
00412756  8B 44 85 A0                     mov eax, dword ptr [rbp + rax*4 - 0x60]
0041275A  4C 2B E0                        sub r12, rax
0041275D  41 3B F5                        cmp esi, r13d
00412760  72 A8                           jb 0x14041270a
00412762  44 8B 7C 24 58                  mov r15d, dword ptr [rsp + 0x58]
00412767  48 8B 7D 80                     mov rdi, qword ptr [rbp - 0x80]
0041276B  41 3B F7                        cmp esi, r15d
0041276E  76 0B                           jbe 0x14041277b
00412770  BA 02 00 00 00                  mov edx, 2
00412775  44 8D 42 FF                     lea r8d, [rdx - 1]
00412779  EB 6F                           jmp 0x1404127ea
0041277B  4C 8B 54 24 50                  mov r10, qword ptr [rsp + 0x50]
00412780  44 8B EE                        mov r13d, esi
00412783  85 F6                           test esi, esi
00412785  74 54                           je 0x1404127db
00412787  FF CE                           dec esi
00412789  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
0041278D  49 8B CA                        mov rcx, r10
00412790  8B 44 B5 A0                     mov eax, dword ptr [rbp + rsi*4 - 0x60]
00412794  4C 8B 84 F5 A0 01 00 00         mov r8, qword ptr [rbp + rsi*8 + 0x1a0]
0041279C  4C 03 E0                        add r12, rax
0041279F  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
004127A4  8B 94 B5 A0 00 00 00            mov edx, dword ptr [rbp + rsi*4 + 0xa0]
004127AB  44 0F B6 8C 06 B3 00 00 00      movzx r9d, byte ptr [rsi + rax + 0xb3]
004127B4  E8 E7 FC FF FF                  call 0x1404124a0
004127B9  4C 8B 54 24 50                  mov r10, qword ptr [rsp + 0x50]
004127BE  85 C0                           test eax, eax
004127C0  74 BE                           je 0x140412780
004127C2  45 33 C0                        xor r8d, r8d
004127C5  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
004127C9  49 8B D4                        mov rdx, r12
004127CC  49 8B CA                        mov rcx, r10
004127CF  E8 CC FC FF FF                  call 0x1404124a0
004127D4  85 C0                           test eax, eax
004127D6  74 A3                           je 0x14041277b
004127D8  41 8B F5                        mov esi, r13d
004127DB  41 3B F7                        cmp esi, r15d
004127DE  8B D3                           mov edx, ebx
004127E0  41 B8 01 00 00 00               mov r8d, 1
004127E6  41 0F 42 D0                     cmovb edx, r8d
004127EA  0F BE 87 A4 04 00 00            movsx eax, byte ptr [rdi + 0x4a4]
004127F1  44 8A EB                        mov r13b, bl
004127F4  3B C2                           cmp eax, edx
004127F6  75 14                           jne 0x14041280c
004127F8  8A 87 A2 04 00 00               mov al, byte ptr [rdi + 0x4a2]
004127FE  41 02 C0                        add al, r8b
00412801  0F B6 C8                        movzx ecx, al
00412804  88 8F A2 04 00 00               mov byte ptr [rdi + 0x4a2], cl
0041280A  EB 19                           jmp 0x140412825
0041280C  88 97 A4 04 00 00               mov byte ptr [rdi + 0x4a4], dl
00412812  41 8B C8                        mov ecx, r8d
00412815  44 88 87 A2 04 00 00            mov byte ptr [rdi + 0x4a2], r8b
0041281C  45 8A E8                        mov r13b, r8b
0041281F  41 BE 04 00 00 00               mov r14d, 4
00412825  83 3D 18 8A AF 00 05            cmp dword ptr [rip + 0xaf8a18], 5
0041282C  44 8A E3                        mov r12b, bl
0041282F  75 06                           jne 0x140412837
00412831  41 83 CE 10                     or r14d, 0x10
00412835  EB 34                           jmp 0x14041286b
00412837  83 FA 02                        cmp edx, 2
0041283A  75 16                           jne 0x140412852
0041283C  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00412841  0F B6 80 B2 00 00 00            movzx eax, byte ptr [rax + 0xb2]
00412848  3B C8                           cmp ecx, eax
0041284A  72 34                           jb 0x140412880
0041284C  41 83 CE 20                     or r14d, 0x20
00412850  EB 19                           jmp 0x14041286b
00412852  41 3B D0                        cmp edx, r8d
00412855  75 29                           jne 0x140412880
00412857  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0041285C  0F B6 80 B1 00 00 00            movzx eax, byte ptr [rax + 0xb1]
00412863  3B C8                           cmp ecx, eax
00412865  72 19                           jb 0x140412880
00412867  41 83 CE 40                     or r14d, 0x40
0041286B  48 8B 87 08 05 00 00            mov rax, qword ptr [rdi + 0x508]
00412872  45 8A E0                        mov r12b, r8b
00412875  40 0F B6 CE                     movzx ecx, sil
00412879  66 89 88 86 02 00 00            mov word ptr [rax + 0x286], cx
00412880  8A 87 A0 04 00 00               mov al, byte ptr [rdi + 0x4a0]
00412886  24 FD                           and al, 0xfd
00412888  0C 04                           or al, 4
0041288A  38 1D F6 41 BB 00               cmp byte ptr [rip + 0xbb41f6], bl
00412890  88 87 A0 04 00 00               mov byte ptr [rdi + 0x4a0], al
00412896  74 2F                           je 0x1404128c7
00412898  48 8B 8F 08 05 00 00            mov rcx, qword ptr [rdi + 0x508]
0041289F  41 0F BA EE 07                  bts r14d, 7
004128A4  0F B7 81 86 02 00 00            movzx eax, word ptr [rcx + 0x286]
004128AB  66 89 81 88 02 00 00            mov word ptr [rcx + 0x288], ax
004128B2  48 8B 87 08 05 00 00            mov rax, qword ptr [rdi + 0x508]
004128B9  0F B7 88 86 02 00 00            movzx ecx, word ptr [rax + 0x286]
004128C0  66 89 8F F0 04 00 00            mov word ptr [rdi + 0x4f0], cx
004128C7  8A 8F 98 04 00 00               mov cl, byte ptr [rdi + 0x498]
004128CD  4C 8D 4D A0                     lea r9, [rbp - 0x60]
004128D1  48 8B 87 80 04 00 00            mov rax, qword ptr [rdi + 0x480]
004128D8  40 2A CE                        sub cl, sil
004128DB  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
004128E0  45 0B F0                        or r14d, r8d
004128E3  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
004128E8  4C 8D 85 A0 00 00 00            lea r8, [rbp + 0xa0]
004128EF  40 88 74 24 40                  mov byte ptr [rsp + 0x40], sil
004128F4  88 4C 24 38                     mov byte ptr [rsp + 0x38], cl
004128F8  33 C9                           xor ecx, ecx
004128FA  88 54 24 30                     mov byte ptr [rsp + 0x30], dl
004128FE  48 8D 55 88                     lea rdx, [rbp - 0x78]
00412902  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
00412907  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0041290C  E8 9B 0C 00 00                  call 0x1404135ac
00412911  38 1D 6F 41 BB 00               cmp byte ptr [rip + 0xbb416f], bl
00412917  75 2B                           jne 0x140412944
00412919  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
0041291E  4C 8D 4D A0                     lea r9, [rbp - 0x60]
00412922  44 88 6C 24 30                  mov byte ptr [rsp + 0x30], r13b
00412927  4C 8D 85 A0 00 00 00            lea r8, [rbp + 0xa0]
0041292E  44 88 64 24 28                  mov byte ptr [rsp + 0x28], r12b
00412933  48 8B CF                        mov rcx, rdi
00412936  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
0041293A  E8 55 F6 FF FF                  call 0x140411f94
0041293F  41 0F BA EE 08                  bts r14d, 8
00412944  4C 8B 4C 24 50                  mov r9, qword ptr [rsp + 0x50]
00412949  4C 8D 85 A0 01 00 00            lea r8, [rbp + 0x1a0]
00412950  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
00412955  48 8D 95 A0 00 00 00            lea rdx, [rbp + 0xa0]
0041295C  48 8B CF                        mov rcx, rdi
0041295F  40 88 74 24 20                  mov byte ptr [rsp + 0x20], sil
00412964  E8 43 0A 00 00                  call 0x1404133ac
00412969  8B 4C 24 68                     mov ecx, dword ptr [rsp + 0x68]
0041296D  BE 01 00 00 00                  mov esi, 1
00412972  03 CE                           add ecx, esi
00412974  3B 0D 66 5A AF 00               cmp ecx, dword ptr [rip + 0xaf5a66]
0041297A  89 4C 24 68                     mov dword ptr [rsp + 0x68], ecx
0041297E  0F 82 30 FC FF FF               jb 0x1404125b4
00412984  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
00412989  E8 C2 0D 00 00                  call 0x140413750
0041298E  8B 0D 4C 5A AF 00               mov ecx, dword ptr [rip + 0xaf5a4c]
00412994  85 C9                           test ecx, ecx
00412996  0F 84 D3 00 00 00               je 0x140412a6f
0041299C  4C 8B 05 35 5A AF 00            mov r8, qword ptr [rip + 0xaf5a35]
004129A3  44 8B D1                        mov r10d, ecx
004129A6  49 81 C0 98 04 00 00            add r8, 0x498
004129AD  41 38 58 09                     cmp byte ptr [r8 + 9], bl
004129B1  0F 84 A8 00 00 00               je 0x140412a5f
004129B7  41 0F B6 80 74 FB FF FF         movzx eax, byte ptr [r8 - 0x48c]
004129BF  44 8B CB                        mov r9d, ebx
004129C2  3B C6                           cmp eax, esi
004129C4  76 20                           jbe 0x1404129e6
004129C6  49 8B 48 70                     mov rcx, qword ptr [r8 + 0x70]
004129CA  8D 50 FF                        lea edx, [rax - 1]
004129CD  48 81 C1 86 02 00 00            add rcx, 0x286
004129D4  0F B7 01                        movzx eax, word ptr [rcx]
004129D7  48 8D 89 80 02 00 00            lea rcx, [rcx + 0x280]
004129DE  44 03 C8                        add r9d, eax
004129E1  48 2B D6                        sub rdx, rsi
004129E4  75 EE                           jne 0x1404129d4
004129E6  41 0F B7 08                     movzx ecx, word ptr [r8]
004129EA  44 3B C9                        cmp r9d, ecx
004129ED  41 0F B6 C1                     movzx eax, r9b
004129F1  0F B6 D1                        movzx edx, cl
004129F4  49 8B 48 70                     mov rcx, qword ptr [r8 + 0x70]
004129F8  0F 42 D0                        cmovb edx, eax
004129FB  41 8A 00                        mov al, byte ptr [r8]
004129FE  2A C2                           sub al, dl
00412A00  0F B6 D0                        movzx edx, al
00412A03  0F B7 01                        movzx eax, word ptr [rcx]
00412A06  66 3B D0                        cmp dx, ax
00412A09  66 0F 43 D0                     cmovae dx, ax
00412A0D  38 1D 8D 59 AF 00               cmp byte ptr [rip + 0xaf598d], bl
00412A13  66 89 51 06                     mov word ptr [rcx + 6], dx
00412A17  74 15                           je 0x140412a2e
00412A19  66 39 35 82 59 AF 00            cmp word ptr [rip + 0xaf5982], si
00412A20  75 3D                           jne 0x140412a5f
00412A22  8A 87 8E 00 00 00               mov al, byte ptr [rdi + 0x8e]
00412A28  41 38 40 02                     cmp byte ptr [r8 + 2], al
00412A2C  76 31                           jbe 0x140412a5f
00412A2E  45 0F B6 88 74 FB FF FF         movzx r9d, byte ptr [r8 - 0x48c]
00412A36  8B D3                           mov edx, ebx
00412A38  41 3B D1                        cmp edx, r9d
00412A3B  73 22                           jae 0x140412a5f
00412A3D  8B C2                           mov eax, edx
00412A3F  48 8D 0C 80                     lea rcx, [rax + rax*4]
00412A43  48 C1 E1 07                     shl rcx, 7
00412A47  49 03 48 70                     add rcx, qword ptr [r8 + 0x70]
00412A4B  0F B7 41 06                     movzx eax, word ptr [rcx + 6]
00412A4F  66 3B 01                        cmp ax, word ptr [rcx]
00412A52  72 04                           jb 0x140412a58
00412A54  03 D6                           add edx, esi
00412A56  EB E0                           jmp 0x140412a38
00412A58  66 03 C6                        add ax, si
00412A5B  66 89 41 06                     mov word ptr [rcx + 6], ax
00412A5F  49 81 C0 10 05 00 00            add r8, 0x510
00412A66  4C 2B D6                        sub r10, rsi
00412A69  0F 85 3E FF FF FF               jne 0x1404129ad
00412A6F  39 1D 6B 59 AF 00               cmp dword ptr [rip + 0xaf596b], ebx
00412A75  76 2F                           jbe 0x140412aa6
00412A77  8B CB                           mov ecx, ebx
00412A79  48 69 D1 10 05 00 00            imul rdx, rcx, 0x510
00412A80  33 C9                           xor ecx, ecx
00412A82  48 03 15 4F 59 AF 00            add rdx, qword ptr [rip + 0xaf594f]
00412A89  4C 8B 82 A8 04 00 00            mov r8, qword ptr [rdx + 0x4a8]
00412A90  48 8B 92 08 05 00 00            mov rdx, qword ptr [rdx + 0x508]
00412A97  E8 80 E0 0B 00                  call 0x1404d0b1c
00412A9C  03 DE                           add ebx, esi
00412A9E  3B 1D 3C 59 AF 00               cmp ebx, dword ptr [rip + 0xaf593c]
00412AA4  72 D1                           jb 0x140412a77
00412AA6  40 8A C6                        mov al, sil
00412AA9  48 8B 8D A0 03 00 00            mov rcx, qword ptr [rbp + 0x3a0]
00412AB0  48 33 CC                        xor rcx, rsp
00412AB3  E8 88 9B 29 00                  call 0x1406ac640
00412AB8  4C 8D 9C 24 B0 04 00 00         lea r11, [rsp + 0x4b0]
00412AC0  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00412AC4  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
00412AC8  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
00412ACC  49 8B E3                        mov rsp, r11
00412ACF  41 5F                           pop r15
00412AD1  41 5E                           pop r14
00412AD3  41 5D                           pop r13
00412AD5  41 5C                           pop r12
00412AD7  5D                              pop rbp
00412AD8  C3                              ret
00412AD9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmCheckComputeMultiClassHeteroResponse(void)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m460;
    unsigned __int64 v_stack_m468;
    unsigned int v_stack_m470;
    unsigned __int64 v_stack_m478;
    unsigned int v_stack_m480;
    unsigned __int64 v_stack_m488;
    unsigned __int64 v_stack_m490;
    unsigned __int8 v_stack_m498;
    unsigned __int8 v_stack_m4A0;
    unsigned __int8 v_stack_m4A8;
    unsigned __int64 v_stack_m4B0;
    unsigned __int64 v_stack_m4B8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (0x4B0ULL);
    result = (*(unsigned __int64 *)(v_rip + 10453471)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 984 + 928) = result;
    v_rbx = 0;
    v_rdi = (*(unsigned __int64 *)(v_rip + 10444302)) + (40);
    a1 = (a1) * ((int)(*(unsigned int *)(v_rip + 11511953)));
    *(unsigned __int64 *)(v_rsp - 984 - 120) = v_xmm0;
    v_stack_m468 = 0;
    v_rdi = (v_rdi) + (a1);
    v_stack_m460 = 0;
    v_stack_m478 = v_rdi;
    v_stack_m470 = 0;
    if ((*(unsigned int *)(v_rip + 11492925)) == 0) goto loc_00412989;
loc_004125B4:
    v_rdi = (v_rdi) * (0);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(v_rip + 11492881));
    *(unsigned __int64 *)(v_rsp - 984 - 128) = v_rdi;
    if ((*(unsigned __int8 *)(v_rip + 12272825)) != 0) goto loc_004125DF;
    if ((*(unsigned __int8 *)(v_rdi + 1185)) == 0) goto loc_00412972;
loc_004125DF:
    v_stack_m480 = 0;
    *(unsigned __int64 *)(v_rsp - 984 - 120) = v_xmm0;
    *(unsigned __int16 *)(v_rsp - 984 - 112) = (unsigned __int16)(*(unsigned __int16 *)(v_rdi + 4));
    *(unsigned __int64 *)(v_rsp - 984 - 120) = *(unsigned __int64 *)(v_rdi + 16);
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rdi + 12))) <= ((unsigned __int8)(v_rbx + 1))) goto loc_00412634;
    a1 = (*(unsigned __int64 *)(v_rdi + 1288)) + (640);
    a2 = (unsigned int)((*(unsigned __int8 *)(v_rdi + 12)) - ((unsigned int)(v_rbx + 1)));
loc_00412619:
    v_r13 = (unsigned __int8)((0) + (*(unsigned __int8 *)(a1)));
    v_r15 = (unsigned int)((0) + ((unsigned int)(*(unsigned __int16 *)(a1 + 8))));
    a2 = (a2) - (v_rbx + 1);
    if (condition_is_not_equal) goto loc_00412619;
    v_stack_m480 = (unsigned int)(v_r15);
loc_00412634:
    result = *(unsigned __int16 *)(a1 + 8);
    if ((*(unsigned __int8 *)(v_rip + 12272716)) != 0) {
        result = *(unsigned __int64 *)(v_rdi + 1288);
        v_r13 = *(unsigned __int8 *)(v_rdi + 10);
        v_r15 = *(unsigned __int16 *)(result + 648);
        v_stack_m480 = (unsigned int)(v_r15);
    }
    a1 = 0;
    v_stack_m4B0 = v_stack_m468;
    v_stack_m4B8 = v_stack_m460;
    result = PpmHeteroComputeCoreParkingUtilities(a1, v_rsp - 984 - 120, v_rsp - 984 + 160, v_rsp - 984 - 96);
    v_stack_m488 = 0;
    if ((unsigned int)(*(unsigned __int16 *)(v_rdi + 10)) == 0) goto loc_004126CE;
loc_0041269E:
    result = (v_stack_m460) * (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 1128) + *(unsigned __int16 *)(v_rdi + 10) * 8));
    a4 = (0) + (result);
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rdi + 10)) - 1);
    a2 = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rdi + 10)))) - (v_rbx + 1);
    *(unsigned __int64 *)(v_rsp - 984 + a1 * 8 + 416) = a4;
    result = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rdi + 10)))) * (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 1128) + *(unsigned __int16 *)(v_rdi + 10) * 8));
    v_r10 = (0) + (result);
    if ((unsigned int)(a1) != 0) goto loc_0041269E;
    v_stack_m488 = v_r10;
loc_004126CE:
    if ((unsigned int)(v_r15) == 0) goto loc_004126ED;
loc_004126DF:
    v_r12 = (v_stack_m468) - ((unsigned int)(*(unsigned int *)(v_rsp - 984 - 96)));
    a2 = ((unsigned int)((unsigned int)(v_r15))) - (v_rbx + 1);
    if (condition_is_not_equal) goto loc_004126DF;
loc_004126ED:
    if (((unsigned int)(v_r15)) >= ((unsigned int)((unsigned __int8)(v_r13)))) goto loc_00412780;
    goto loc_0041270F;
loc_0041270A:
loc_0041270F:
    v_stack_m4B8 = 0;
    result = PpmHeteroUtilityGreaterThanOrEqualThreshold(v_stack_m488, (unsigned int)(*(unsigned int *)(v_rsp - 984 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r15)))) * 4 + 160)), *(unsigned __int64 *)(v_rsp - 984 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r15)))) * 8 + 416), *(unsigned __int8 *)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r15)))) + v_stack_m478 * 1 + 307));
    if ((unsigned int)(result) == 0) goto loc_00412762;
    a3 = 0;
    v_stack_m4B8 = 0;
    result = PpmHeteroUtilityGreaterThanOrEqualThreshold(v_stack_m488, v_r12, a3, *(unsigned __int8 *)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r15)))) + v_stack_m478 * 1 + 307));
    if ((unsigned int)(result) == 0) goto loc_00412762;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) + (1));
    v_r12 = (v_r12) - ((unsigned int)(*(unsigned int *)(v_rsp - 984 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r15)))) * 4 - 96)));
    if (((unsigned int)(v_rsi)) < ((unsigned int)((unsigned __int8)(v_r13)))) goto loc_0041270A;
loc_00412762:
    if (((unsigned int)(v_rsi)) <= ((unsigned int)((unsigned int)(v_stack_m480)))) goto loc_0041277B;
    goto loc_004127EA;
loc_0041277B:
loc_00412780:
    if ((unsigned int)(v_rsi) == 0) goto loc_004127DB;
    v_rsi = (unsigned int)((v_rsi) - 1);
    v_stack_m4B8 = 0;
    v_r12 = (v_r12) + ((unsigned int)(*(unsigned int *)(v_rsp - 984 + v_rsi * 4 - 96)));
    result = PpmHeteroUtilityGreaterThanOrEqualThreshold(v_stack_m488, (unsigned int)(*(unsigned int *)(v_rsp - 984 + v_rsi * 4 + 160)), *(unsigned __int64 *)(v_rsp - 984 + v_rsi * 8 + 416), *(unsigned __int8 *)(v_rsi + v_stack_m478 * 1 + 179));
    if ((unsigned int)(result) == 0) goto loc_00412780;
    a3 = 0;
    v_stack_m4B8 = 0;
    result = PpmHeteroUtilityGreaterThanOrEqualThreshold(v_stack_m488, v_r12, a3, *(unsigned __int8 *)(v_rsi + v_stack_m478 * 1 + 179));
    if ((unsigned int)(result) == 0) goto loc_0041277B;
loc_004127DB:
    a2 = 0;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi)))))) < ((unsigned int)((unsigned int)(v_stack_m480)))) { a2 = 1; }
loc_004127EA:
    if (((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 984 - 128) + 1188)))) != ((unsigned int)(a2))) goto loc_0041280C;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 984 - 128) + 1186)) + (1));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 984 - 128) + 1186) = (unsigned __int8)((unsigned __int8)(result));
    goto loc_00412825;
loc_0041280C:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 984 - 128) + 1188) = (unsigned __int8)(a2);
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 984 - 128) + 1186) = 1;
loc_00412825:
    if ((*(unsigned int *)(v_rip + 11504152)) != 5) goto loc_00412837;
    v_r14 = (unsigned int)((4) | (16));
    goto loc_0041286B;
loc_00412837:
    if (((unsigned int)(a2)) != 2) goto loc_00412852;
    if (1 < ((unsigned int)(*(unsigned __int8 *)(v_stack_m478 + 178)))) goto loc_00412880;
    v_r14 = (unsigned int)((v_r14) | (32));
    goto loc_0041286B;
loc_00412852:
    if (((unsigned int)(a2)) != 1) goto loc_00412880;
    if (1 < ((unsigned int)(*(unsigned __int8 *)(v_stack_m478 + 177)))) goto loc_00412880;
    v_r14 = (unsigned int)((v_r14) | (64));
loc_0041286B:
    *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 984 - 128) + 1288) + 646) = (unsigned __int16)((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi))))));
loc_00412880:
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 984 - 128) + 1184)) & (253));
    result = (unsigned __int8)((result) | (4));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 984 - 128) + 1184) = (unsigned __int8)(result);
    if ((*(unsigned __int8 *)(v_rip + 12272118)) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 984 - 128) + 1288);
        result = *(unsigned __int16 *)(a1 + 646);
        *(unsigned __int16 *)(a1 + 648) = (unsigned __int16)(result);
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 984 - 128) + 1288);
        a1 = *(unsigned __int16 *)(result + 646);
        *(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 984 - 128) + 1264) = (unsigned __int16)(a1);
    }
    a1 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 984 - 128) + 1176)) - ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi)))))));
    v_stack_m490 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 984 - 128) + 1152);
    v_r14 = (unsigned int)((v_r14) | (1));
    v_stack_m498 = (unsigned __int8)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi)))));
    v_stack_m4A0 = (unsigned __int8)(a1);
    a1 = 0;
    v_stack_m4A8 = (unsigned __int8)(a2);
    v_stack_m4B0 = (unsigned int)((unsigned int)(v_stack_m480));
    v_stack_m4B8 = v_stack_m468;
    result = PpmEventTraceMultiClassHeteroResponse(a1, v_rsp - 984 - 120, v_rsp - 984 + 160, v_rsp - 984 - 96);
    if ((*(unsigned __int8 *)(v_rip + 12271983)) == 0) {
        a2 = v_stack_m478;
        a4 = v_rsp - 984 - 96;
        v_stack_m4A8 = 1;
        a3 = v_rsp - 984 + 160;
        v_stack_m4B0 = 1;
        a1 = *(unsigned __int64 *)(v_rsp - 984 - 128);
        v_stack_m4B8 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi)))));
        result = PpmHeteroComputeMultiClassUnparkCount(a1, a2, a3, a4);
    }
    v_stack_m4B0 = (unsigned int)(v_r14);
    v_stack_m4B8 = (unsigned __int8)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi)))));
    result = PpmEventTraceHeteroResponse(*(unsigned __int64 *)(v_rsp - 984 - 128), v_rsp - 984 + 160, v_rsp - 984 + 416, v_stack_m488);
loc_00412972:
    a1 = (unsigned int)(((unsigned int)(v_stack_m470)) + (1));
    v_stack_m470 = (unsigned int)(a1);
    if (((unsigned int)(a1)) < (*(unsigned int *)(v_rip + 11491942))) goto loc_004125B4;
loc_00412989:
    result = PpmParkCalculateUnparkCount(a1, v_rsp - 984 + 160, v_rsp - 984 + 416, v_stack_m488);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11491916))) == 0) goto loc_00412A6F;
    a3 = (*(unsigned __int64 *)(v_rip + 11491893)) + (0x498ULL);
loc_004129AD:
    if ((*(unsigned __int8 *)(a3 + 9)) == 0) goto loc_00412A5F;
    if (((unsigned int)(*(unsigned __int8 *)(a3 - 1164))) <= 1) goto loc_004129E6;
    a1 = (*(unsigned __int64 *)(a3 + 112)) + (646);
loc_004129D4:
    a4 = (unsigned int)((0) + ((unsigned int)(*(unsigned __int16 *)(a1))));
    a2 = (*(unsigned __int8 *)(a3 - 1164) - 1) - (1);
    if (condition_is_not_equal) goto loc_004129D4;
loc_004129E6:
    a2 = (unsigned __int8)(*(unsigned __int16 *)(a3));
    if (((unsigned int)(a4)) < ((unsigned int)(*(unsigned __int16 *)(a3)))) { a2 = (unsigned int)((unsigned __int8)(a4)); }
    result = (unsigned __int8)((*(unsigned __int8 *)(a3)) - ((unsigned __int8)(a2)));
    a2 = (unsigned __int8)(result);
    if (((unsigned __int16)((unsigned __int8)(result))) >= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a3 + 112))))) { a2 = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a3 + 112))); }
    *(unsigned __int16 *)(*(unsigned __int64 *)(a3 + 112) + 6) = (unsigned __int16)(a2);
    if ((*(unsigned __int8 *)(v_rip + 11491725)) == 0) goto loc_00412A2E;
    if ((*(unsigned __int16 *)(v_rip + 11491714)) != 1) goto loc_00412A5F;
    if ((*(unsigned __int8 *)(a3 + 2)) <= ((unsigned __int8)(*(unsigned __int8 *)(v_stack_m478 + 142)))) goto loc_00412A5F;
loc_00412A2E:
loc_00412A38:
    if (0 >= ((unsigned int)(*(unsigned __int8 *)(a3 - 1164)))) goto loc_00412A5F;
    a1 = (0 + 0 * 4) << (7);
    a1 = (a1) + (*(unsigned __int64 *)(a3 + 112));
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 6))) < (*(unsigned __int16 *)(a1))) goto loc_00412A58;
    a2 = (unsigned int)((0) + (1));
    goto loc_00412A38;
loc_00412A58:
    result = (unsigned __int16)((*(unsigned __int16 *)(a1 + 6)) + (1));
    *(unsigned __int16 *)(a1 + 6) = (unsigned __int16)(result);
loc_00412A5F:
    a3 = (a3) + (0x510ULL);
    v_r10 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11491916))))) - (1);
    if (condition_is_not_equal) goto loc_004129AD;
loc_00412A6F:
    if ((*(unsigned int *)(v_rip + 11491691)) <= 0) goto loc_00412AA6;
loc_00412A77:
    a2 = (a2) * (0);
    a1 = 0;
    a2 = (a2) + (*(unsigned __int64 *)(v_rip + 11491663));
    result = PpmEventTraceMultiClassHeteroResponseUpdate(a1, *(unsigned __int64 *)(a2 + 1288), *(unsigned __int64 *)(a2 + 1192), *(unsigned __int8 *)(a3 - 1164));
    v_rbx = (unsigned int)((v_rbx) + (1));
    if (((unsigned int)(v_rbx)) < (*(unsigned int *)(v_rip + 11491644))) goto loc_00412A77;
loc_00412AA6:
    a1 = (*(unsigned __int64 *)(v_rsp - 984 + 928)) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(a2 + 1288), *(unsigned __int64 *)(a2 + 1192), *(unsigned __int8 *)(a3 - 1164));
    return result;
}
```

## 5. (Beta) C Style

```c
void PpmCheckComputeMultiClassHeteroResponse(void)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m460;
    uint64_t v_stack_m468;
    uint32_t v_stack_m470;
    uint64_t v_stack_m478;
    uint32_t v_stack_m480;
    uint64_t v_stack_m488;
    uint64_t v_stack_m490;
    uint8_t v_stack_m498;
    uint8_t v_stack_m4A0;
    uint8_t v_stack_m4A8;
    uint64_t v_stack_m4B0;
    uint64_t v_stack_m4B8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (0x4B0ULL);
    result = (*(uint64_t *)(v_rip + 0x9F81DF)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x3D8 + 0x3A0) = result;
    local_rbx = 0;
    local_rdi = (*(uint64_t *)(v_rip + 0x9F5E0E)) + (40);
    a1 = (a1) * ((int32_t)(*(uint32_t *)(v_rip + 0xAFA891)));
    *(uint64_t *)(local_rsp - 0x3D8 - 0x78) = v_xmm0;
    v_stack_m468 = 0;
    local_rdi = (local_rdi) + (a1);
    v_stack_m460 = 0;
    v_stack_m478 = local_rdi;
    v_stack_m470 = 0;
    if ((*(uint32_t *)(v_rip + 0xAF5E3D)) == 0) goto loc_00412989;
loc_004125B4:
    local_rdi = (local_rdi) * (0);
    local_rdi = (local_rdi) + (*(uint64_t *)(v_rip + 0xAF5E11));
    *(uint64_t *)(local_rsp - 0x3D8 - 0x80) = local_rdi;
    if ((*(uint8_t *)(v_rip + 0xBB44B9)) != 0) goto loc_004125DF;
    if ((*(uint8_t *)(local_rdi + 0x4A1)) == 0) goto loc_00412972;
loc_004125DF:
    v_stack_m480 = 0;
    *(uint64_t *)(local_rsp - 0x3D8 - 0x78) = v_xmm0;
    *(uint16_t *)(local_rsp - 0x3D8 - 0x70) = (uint16_t)(*(uint16_t *)(local_rdi + 0x4));
    *(uint64_t *)(local_rsp - 0x3D8 - 0x78) = *(uint64_t *)(local_rdi + 0x10);
    if (((uint8_t)(*(uint8_t *)(local_rdi + 0xC))) <= ((uint8_t)(local_rbx + 1))) goto loc_00412634;
    a1 = (*(uint64_t *)(local_rdi + 0x508)) + (640);
    a2 = (uint32_t)((*(uint8_t *)(local_rdi + 0xC)) - ((uint32_t)(local_rbx + 1)));
loc_00412619:
    local_r13 = (uint8_t)((0) + (*(uint8_t *)(a1)));
    local_r15 = (uint32_t)((0) + ((uint32_t)(*(uint16_t *)(a1 + 0x8))));
    a2 = (a2) - (local_rbx + 1);
    if (condition_is_not_equal) goto loc_00412619;
    v_stack_m480 = (uint32_t)(local_r15);
loc_00412634:
    result = *(uint16_t *)(a1 + 0x8);
    if ((*(uint8_t *)(v_rip + 0xBB444C)) != 0) {
        result = *(uint64_t *)(local_rdi + 0x508);
        local_r13 = *(uint8_t *)(local_rdi + 0xA);
        local_r15 = *(uint16_t *)(result + 0x288);
        v_stack_m480 = (uint32_t)(local_r15);
    }
    a1 = 0;
    v_stack_m4B0 = v_stack_m468;
    v_stack_m4B8 = v_stack_m460;
    result = PpmHeteroComputeCoreParkingUtilities(a1, local_rsp - 984 - 120, local_rsp - 984 + 160, local_rsp - 984 - 96);
    v_stack_m488 = 0;
    if ((uint32_t)(*(uint16_t *)(local_rdi + 0xA)) == 0) goto loc_004126CE;
loc_0041269E:
    result = (v_stack_m460) * (*(uint64_t *)(*(uint64_t *)(local_rdi + 0x468) + *(uint16_t *)(local_rdi + 0xA) * 8));
    a4 = (0) + (result);
    a1 = (uint32_t)((*(uint16_t *)(local_rdi + 0xA)) - 1);
    a2 = ((uint32_t)((uint32_t)(*(uint16_t *)(local_rdi + 0xA)))) - (local_rbx + 1);
    *(uint64_t *)(local_rsp - 0x3D8 + a1 * 8 + 0x1A0) = a4;
    result = ((uint32_t)((uint32_t)(*(uint16_t *)(local_rdi + 0xA)))) * (*(uint64_t *)(*(uint64_t *)(local_rdi + 0x468) + *(uint16_t *)(local_rdi + 0xA) * 8));
    local_r10 = (0) + (result);
    if ((uint32_t)(a1) != 0) goto loc_0041269E;
    v_stack_m488 = local_r10;
loc_004126CE:
    if ((uint32_t)(local_r15) == 0) goto loc_004126ED;
loc_004126DF:
    local_r12 = (v_stack_m468) - ((uint32_t)(*(uint32_t *)(local_rsp - 0x3D8 - 0x60)));
    a2 = ((uint32_t)((uint32_t)(local_r15))) - (local_rbx + 1);
    if (condition_is_not_equal) goto loc_004126DF;
loc_004126ED:
    if (((uint32_t)(local_r15)) >= ((uint32_t)((uint8_t)(local_r13)))) goto loc_00412780;
    goto loc_0041270F;
loc_0041270A:
loc_0041270F:
    v_stack_m4B8 = 0;
    result = PpmHeteroUtilityGreaterThanOrEqualThreshold(v_stack_m488, (uint32_t)(*(uint32_t *)(local_rsp - 0x3D8 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r15)))) * 4 + 0xA0)), *(uint64_t *)(local_rsp - 0x3D8 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r15)))) * 8 + 0x1A0), *(uint8_t *)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r15)))) + v_stack_m478 * 1 + 0x133));
    if ((uint32_t)(result) == 0) goto loc_00412762;
    a3 = 0;
    v_stack_m4B8 = 0;
    result = PpmHeteroUtilityGreaterThanOrEqualThreshold(v_stack_m488, local_r12, a3, *(uint8_t *)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r15)))) + v_stack_m478 * 1 + 0x133));
    if ((uint32_t)(result) == 0) goto loc_00412762;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) + (1));
    local_r12 = (local_r12) - ((uint32_t)(*(uint32_t *)(local_rsp - 0x3D8 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r15)))) * 4 - 0x60)));
    if (((uint32_t)(local_rsi)) < ((uint32_t)((uint8_t)(local_r13)))) goto loc_0041270A;
loc_00412762:
    if (((uint32_t)(local_rsi)) <= ((uint32_t)((uint32_t)(v_stack_m480)))) goto loc_0041277B;
    goto loc_004127EA;
loc_0041277B:
loc_00412780:
    if ((uint32_t)(local_rsi) == 0) goto loc_004127DB;
    local_rsi = (uint32_t)((local_rsi) - 1);
    v_stack_m4B8 = 0;
    local_r12 = (local_r12) + ((uint32_t)(*(uint32_t *)(local_rsp - 0x3D8 + local_rsi * 4 - 0x60)));
    result = PpmHeteroUtilityGreaterThanOrEqualThreshold(v_stack_m488, (uint32_t)(*(uint32_t *)(local_rsp - 0x3D8 + local_rsi * 4 + 0xA0)), *(uint64_t *)(local_rsp - 0x3D8 + local_rsi * 8 + 0x1A0), *(uint8_t *)(local_rsi + v_stack_m478 * 1 + 0xB3));
    if ((uint32_t)(result) == 0) goto loc_00412780;
    a3 = 0;
    v_stack_m4B8 = 0;
    result = PpmHeteroUtilityGreaterThanOrEqualThreshold(v_stack_m488, local_r12, a3, *(uint8_t *)(local_rsi + v_stack_m478 * 1 + 0xB3));
    if ((uint32_t)(result) == 0) goto loc_0041277B;
loc_004127DB:
    a2 = 0;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi)))))) < ((uint32_t)((uint32_t)(v_stack_m480)))) { a2 = 1; }
loc_004127EA:
    if (((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(local_rsp - 0x3D8 - 0x80) + 0x4A4)))) != ((uint32_t)(a2))) goto loc_0041280C;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(local_rsp - 0x3D8 - 0x80) + 0x4A2)) + (1));
    *(uint8_t *)(*(uint64_t *)(local_rsp - 0x3D8 - 0x80) + 0x4A2) = (uint8_t)((uint8_t)(result));
    goto loc_00412825;
loc_0041280C:
    *(uint8_t *)(*(uint64_t *)(local_rsp - 0x3D8 - 0x80) + 0x4A4) = (uint8_t)(a2);
    *(uint8_t *)(*(uint64_t *)(local_rsp - 0x3D8 - 0x80) + 0x4A2) = 1;
loc_00412825:
    if ((*(uint32_t *)(v_rip + 0xAF8A18)) != 5) goto loc_00412837;
    local_r14 = (uint32_t)((4) | (16));
    goto loc_0041286B;
loc_00412837:
    if (((uint32_t)(a2)) != 2) goto loc_00412852;
    if (1 < ((uint32_t)(*(uint8_t *)(v_stack_m478 + 0xB2)))) goto loc_00412880;
    local_r14 = (uint32_t)((local_r14) | (32));
    goto loc_0041286B;
loc_00412852:
    if (((uint32_t)(a2)) != 1) goto loc_00412880;
    if (1 < ((uint32_t)(*(uint8_t *)(v_stack_m478 + 0xB1)))) goto loc_00412880;
    local_r14 = (uint32_t)((local_r14) | (64));
loc_0041286B:
    *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3D8 - 0x80) + 0x508) + 0x286) = (uint16_t)((uint8_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi))))));
loc_00412880:
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(local_rsp - 0x3D8 - 0x80) + 0x4A0)) & (253));
    result = (uint8_t)((result) | (4));
    *(uint8_t *)(*(uint64_t *)(local_rsp - 0x3D8 - 0x80) + 0x4A0) = (uint8_t)(result);
    if ((*(uint8_t *)(v_rip + 0xBB41F6)) != 0) {
        a1 = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3D8 - 0x80) + 0x508);
        result = *(uint16_t *)(a1 + 0x286);
        *(uint16_t *)(a1 + 0x288) = (uint16_t)(result);
        result = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3D8 - 0x80) + 0x508);
        a1 = *(uint16_t *)(result + 0x286);
        *(uint16_t *)(*(uint64_t *)(local_rsp - 0x3D8 - 0x80) + 0x4F0) = (uint16_t)(a1);
    }
    a1 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(local_rsp - 0x3D8 - 0x80) + 0x498)) - ((uint8_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi)))))));
    v_stack_m490 = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3D8 - 0x80) + 0x480);
    local_r14 = (uint32_t)((local_r14) | (1));
    v_stack_m498 = (uint8_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi)))));
    v_stack_m4A0 = (uint8_t)(a1);
    a1 = 0;
    v_stack_m4A8 = (uint8_t)(a2);
    v_stack_m4B0 = (uint32_t)((uint32_t)(v_stack_m480));
    v_stack_m4B8 = v_stack_m468;
    result = PpmEventTraceMultiClassHeteroResponse(a1, local_rsp - 984 - 120, local_rsp - 984 + 160, local_rsp - 984 - 96);
    if ((*(uint8_t *)(v_rip + 0xBB416F)) == 0) {
        a2 = v_stack_m478;
        a4 = local_rsp - 984 - 96;
        v_stack_m4A8 = 1;
        a3 = local_rsp - 984 + 160;
        v_stack_m4B0 = 1;
        a1 = *(uint64_t *)(local_rsp - 0x3D8 - 0x80);
        v_stack_m4B8 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi)))));
        result = PpmHeteroComputeMultiClassUnparkCount(a1, a2, a3, a4);
    }
    v_stack_m4B0 = (uint32_t)(local_r14);
    v_stack_m4B8 = (uint8_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi)))));
    result = PpmEventTraceHeteroResponse(*(uint64_t *)(local_rsp - 0x3D8 - 0x80), local_rsp - 984 + 160, local_rsp - 984 + 416, v_stack_m488);
loc_00412972:
    a1 = (uint32_t)(((uint32_t)(v_stack_m470)) + (1));
    v_stack_m470 = (uint32_t)(a1);
    if (((uint32_t)(a1)) < (*(uint32_t *)(v_rip + 0xAF5A66))) goto loc_004125B4;
loc_00412989:
    result = PpmParkCalculateUnparkCount(a1, local_rsp - 984 + 160, local_rsp - 984 + 416, v_stack_m488);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAF5A4C))) == 0) goto loc_00412A6F;
    a3 = (*(uint64_t *)(v_rip + 0xAF5A35)) + (0x498ULL);
loc_004129AD:
    if ((*(uint8_t *)(a3 + 0x9)) == 0) goto loc_00412A5F;
    if (((uint32_t)(*(uint8_t *)(a3 - 0x48C))) <= 1) goto loc_004129E6;
    a1 = (*(uint64_t *)(a3 + 0x70)) + (646);
loc_004129D4:
    a4 = (uint32_t)((0) + ((uint32_t)(*(uint16_t *)(a1))));
    a2 = (*(uint8_t *)(a3 - 0x48C) - 1) - (1);
    if (condition_is_not_equal) goto loc_004129D4;
loc_004129E6:
    a2 = (uint8_t)(*(uint16_t *)(a3));
    if (((uint32_t)(a4)) < ((uint32_t)(*(uint16_t *)(a3)))) { a2 = (uint32_t)((uint8_t)(a4)); }
    result = (uint8_t)((*(uint8_t *)(a3)) - ((uint8_t)(a2)));
    a2 = (uint8_t)(result);
    if (((uint16_t)((uint8_t)(result))) >= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(a3 + 0x70))))) { a2 = (uint16_t)(*(uint16_t *)(*(uint64_t *)(a3 + 0x70))); }
    *(uint16_t *)(*(uint64_t *)(a3 + 0x70) + 0x6) = (uint16_t)(a2);
    if ((*(uint8_t *)(v_rip + 0xAF598D)) == 0) goto loc_00412A2E;
    if ((*(uint16_t *)(v_rip + 0xAF5982)) != 1) goto loc_00412A5F;
    if ((*(uint8_t *)(a3 + 0x2)) <= ((uint8_t)(*(uint8_t *)(v_stack_m478 + 0x8E)))) goto loc_00412A5F;
loc_00412A2E:
loc_00412A38:
    if (0 >= ((uint32_t)(*(uint8_t *)(a3 - 0x48C)))) goto loc_00412A5F;
    a1 = (0 + 0 * 4) << (7);
    a1 = (a1) + (*(uint64_t *)(a3 + 0x70));
    if (((uint16_t)(*(uint16_t *)(a1 + 0x6))) < (*(uint16_t *)(a1))) goto loc_00412A58;
    a2 = (uint32_t)((0) + (1));
    goto loc_00412A38;
loc_00412A58:
    result = (uint16_t)((*(uint16_t *)(a1 + 0x6)) + (1));
    *(uint16_t *)(a1 + 0x6) = (uint16_t)(result);
loc_00412A5F:
    a3 = (a3) + (0x510ULL);
    local_r10 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAF5A4C))))) - (1);
    if (condition_is_not_equal) goto loc_004129AD;
loc_00412A6F:
    if ((*(uint32_t *)(v_rip + 0xAF596B)) <= 0) goto loc_00412AA6;
loc_00412A77:
    a2 = (a2) * (0);
    a1 = 0;
    a2 = (a2) + (*(uint64_t *)(v_rip + 0xAF594F));
    result = PpmEventTraceMultiClassHeteroResponseUpdate(a1, *(uint64_t *)(a2 + 0x508), *(uint64_t *)(a2 + 0x4A8), *(uint8_t *)(a3 - 0x48C));
    local_rbx = (uint32_t)((local_rbx) + (1));
    if (((uint32_t)(local_rbx)) < (*(uint32_t *)(v_rip + 0xAF593C))) goto loc_00412A77;
loc_00412AA6:
    a1 = (*(uint64_t *)(local_rsp - 0x3D8 + 0x3A0)) ^ (local_rsp);
    result = _security_check_cookie(a1, *(uint64_t *)(a2 + 0x508), *(uint64_t *)(a2 + 0x4A8), *(uint8_t *)(a3 - 0x48C));
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00412534&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
