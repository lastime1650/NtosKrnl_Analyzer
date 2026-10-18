# KiForceIdleUpdateSchedulerParkState

- RVA: `0x0048D874`–`0x0048DCB7` (길이 `1,091` bytes)
- VA: `0x000000014048D874`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B146C`
- 디코드: `278`개 명령, `1,091/1,091` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x0048D8BE` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0048D8CC` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0048D8F9` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0048D930` → [KeRemoveQueueDpcEx](../46/KeRemoveQueueDpcEx_function_0046CDC0.md) (function, `0x0046CDC0`)
- `0x0048D93F` → [KeAddProcessorAffinityEx](../25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x0048D98D` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0048D9D0` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0048DA03` → [KiOrAffinityEx](../39/KiOrAffinityEx_function_0039A84C.md) (function, `0x0039A84C`)
- `0x0048DA0F` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0048DA4F` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0048DA90` → [KeAndAffinityEx2](../3C/KeAndAffinityEx2_function_003C0740.md) (function, `0x003C0740`)
- `0x0048DB1F` → [Feature_ForceIdleReschedulingFix__private_IsEnabledDeviceUsageNoInline](../4F/Feature_ForceIdleReschedulingFix__private_IsEnabledDeviceUsageNoInline_function_004F789C.md) (function, `0x004F789C`)
- `0x0048DB58` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x0048DB71` → [KiForceIdleParkUnparkProcessor](../35/KiForceIdleParkUnparkProcessor_function_003523B8.md) (function, `0x003523B8`)
- `0x0048DB85` → [KeInsertQueueDpc](../20/KeInsertQueueDpc_function_00207C50.md) (function, `0x00207C50`)
- `0x0048DB94` → [KeEnumerateNextProcessor](../41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x0048DBB4` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x0048DBC4` → [KiCheckPrcbAffinityEx](../43/KiCheckPrcbAffinityEx_function_004366A0.md) (function, `0x004366A0`)
- `0x0048DBE1` → [KiForceIdleParkUnparkProcessor](../35/KiForceIdleParkUnparkProcessor_function_003523B8.md) (function, `0x003523B8`)
- `0x0048DBF8` → [KeInsertQueueDpc](../20/KeInsertQueueDpc_function_00207C50.md) (function, `0x00207C50`)
- `0x0048DC1A` → [KeYieldProcessorEx](../3F/KeYieldProcessorEx_function_003FBD00.md) (function, `0x003FBD00`)
- `0x0048DC72` → [KiSendSoftwareInterrupt](../25/KiSendSoftwareInterrupt_function_00250A30.md) (function, `0x00250A30`)
- `0x0048DC90` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KiForceIdleStopDpcRoutine](KiForceIdleStopDpcRoutine_function_0048D7B0.md) at `0x0048D7B8`
- [KiForceIdleStartDpcRoutine](../4C/KiForceIdleStartDpcRoutine_function_004C3F40.md) at `0x004C4005`

### Static image references
- `0x0048D89A` → RVA `0x00E0A740` (`.data`; read)
- `0x0048D8FE` → RVA `0x00F233D0` (`.data`; read)
- `0x0048D90D` → RVA `0x00FC6A80` (`ALMOSTRO`; read)
- `0x0048D91A` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x0048D946` → RVA `0x00F233D0` (`.data`; read/write)
- `0x0048D99C` → RVA `0x00E0AEC0` (`.data`; read)
- `0x0048D9C0` → RVA `0x00E0AEC8` (`.data`; read)
- `0x0048D9F7` → RVA `0x00E0ADB0` (`.data`; read)
- `0x0048DA1D` → RVA `0x00FC7120` (`ALMOSTRO`; read)
- `0x0048DA3F` → RVA `0x00FC7128` (`ALMOSTRO`; read)
- `0x0048DA9A` → RVA `0x00F231B0` (`.data`; read)
- `0x0048DAEC` → RVA `0x00F233D0` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0048D874  48 8B C4                        mov rax, rsp
0048D877  48 89 58 08                     mov qword ptr [rax + 8], rbx
0048D87B  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
0048D87F  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
0048D883  55                              push rbp
0048D884  41 54                           push r12
0048D886  41 55                           push r13
0048D888  41 56                           push r14
0048D88A  41 57                           push r15
0048D88C  48 8D A8 58 FE FF FF            lea rbp, [rax - 0x1a8]
0048D893  48 81 EC 80 02 00 00            sub rsp, 0x280
0048D89A  48 8B 05 9F CE 97 00            mov rax, qword ptr [rip + 0x97ce9f]
0048D8A1  48 33 C4                        xor rax, rsp
0048D8A4  48 89 85 70 01 00 00            mov qword ptr [rbp + 0x170], rax
0048D8AB  0F B6 F1                        movzx esi, cl
0048D8AE  41 BD 00 01 00 00               mov r13d, 0x100
0048D8B4  45 8B C5                        mov r8d, r13d
0048D8B7  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
0048D8BC  33 D2                           xor edx, edx
0048D8BE  E8 7D 93 23 00                  call 0x1406c6c40
0048D8C3  45 8B C5                        mov r8d, r13d
0048D8C6  48 8D 4D 68                     lea rcx, [rbp + 0x68]
0048D8CA  33 D2                           xor edx, edx
0048D8CC  E8 6F 93 23 00                  call 0x1406c6c40
0048D8D1  65 4C 8B 34 25 20 00 00 00      mov r14, qword ptr gs:[0x20]
0048D8DA  48 8D 4D 68                     lea rcx, [rbp + 0x68]
0048D8DE  41 BC 01 00 00 00               mov r12d, 1
0048D8E4  48 C7 45 60 01 00 20 00         mov qword ptr [rbp + 0x60], 0x200001
0048D8EC  45 8B C5                        mov r8d, r13d
0048D8EF  33 D2                           xor edx, edx
0048D8F1  45 33 FF                        xor r15d, r15d
0048D8F4  41 8D 5C 24 1F                  lea ebx, [r12 + 0x1f]
0048D8F9  E8 42 93 23 00                  call 0x1406c6c40
0048D8FE  8B 05 CC 5A A9 00               mov eax, dword ptr [rip + 0xa95acc]
0048D904  85 C0                           test eax, eax
0048D906  75 05                           jne 0x14048d90d
0048D908  41 8B FC                        mov edi, r12d
0048D90B  EB 59                           jmp 0x14048d966
0048D90D  8B 05 6D 91 B3 00               mov eax, dword ptr [rip + 0xb3916d]
0048D913  41 8B DF                        mov ebx, r15d
0048D916  85 C0                           test eax, eax
0048D918  74 40                           je 0x14048d95a
0048D91A  48 8D 05 1F B3 B3 00            lea rax, [rip + 0xb3b31f]
0048D921  8B CB                           mov ecx, ebx
0048D923  33 D2                           xor edx, edx
0048D925  48 8B 0C C8                     mov rcx, qword ptr [rax + rcx*8]
0048D929  48 81 C1 98 8A 00 00            add rcx, 0x8a98
0048D930  E8 8B F4 FD FF                  call 0x14046cdc0
0048D935  84 C0                           test al, al
0048D937  75 0D                           jne 0x14048d946
0048D939  8B D3                           mov edx, ebx
0048D93B  48 8D 4D 60                     lea rcx, [rbp + 0x60]
0048D93F  E8 AC DD DC FF                  call 0x14025b6f0
0048D944  EB 07                           jmp 0x14048d94d
0048D946  F0 FF 0D 83 5A A9 00            lock dec dword ptr [rip + 0xa95a83]
0048D94D  8B 05 2D 91 B3 00               mov eax, dword ptr [rip + 0xb3912d]
0048D953  41 03 DC                        add ebx, r12d
0048D956  3B D8                           cmp ebx, eax
0048D958  72 C0                           jb 0x14048d91a
0048D95A  41 8B FF                        mov edi, r15d
0048D95D  BB 20 00 00 00                  mov ebx, 0x20
0048D962  EB 02                           jmp 0x14048d966
0048D964  F3 90                           pause
0048D966  8B 05 64 5A A9 00               mov eax, dword ptr [rip + 0xa95a64]
0048D96C  85 C0                           test eax, eax
0048D96E  75 F4                           jne 0x14048d964
0048D970  33 D2                           xor edx, edx
0048D972  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
0048D977  4D 8B C5                        mov r8, r13
0048D97A  40 84 F6                        test sil, sil
0048D97D  0F 85 87 00 00 00               jne 0x14048da0a
0048D983  F0 44 09 3C 24                  lock or dword ptr [rsp], r15d
0048D988  66 89 5C 24 52                  mov word ptr [rsp + 0x52], bx
0048D98D  E8 AE 92 23 00                  call 0x1406c6c40
0048D992  44 0F B7 4C 24 52               movzx r9d, word ptr [rsp + 0x52]
0048D998  41 0F B7 CF                     movzx ecx, r15w
0048D99C  0F B7 1D 1D D5 97 00            movzx ebx, word ptr [rip + 0x97d51d]
0048D9A3  66 41 3B D9                     cmp bx, r9w
0048D9A7  44 89 7C 24 54                  mov dword ptr [rsp + 0x54], r15d
0048D9AC  66 41 0F 47 D9                  cmova bx, r9w
0048D9B1  66 89 5C 24 50                  mov word ptr [rsp + 0x50], bx
0048D9B6  66 44 3B FB                     cmp r15w, bx
0048D9BA  73 30                           jae 0x14048d9ec
0048D9BC  44 0F B7 C3                     movzx r8d, bx
0048D9C0  48 8D 15 01 D5 97 00            lea rdx, [rip + 0x97d501]
0048D9C7  49 C1 E0 03                     shl r8, 3
0048D9CB  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
0048D9D0  E8 6B 8E 23 00                  call 0x1406c6840
0048D9D5  0F B7 CB                        movzx ecx, bx
0048D9D8  EB 0C                           jmp 0x14048d9e6
0048D9DA  0F B7 C1                        movzx eax, cx
0048D9DD  66 41 03 CC                     add cx, r12w
0048D9E1  4C 89 7C C4 58                  mov qword ptr [rsp + rax*8 + 0x58], r15
0048D9E6  44 0F B7 4C 24 52               movzx r9d, word ptr [rsp + 0x52]
0048D9EC  66 41 3B C9                     cmp cx, r9w
0048D9F0  72 E8                           jb 0x14048d9da
0048D9F2  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
0048D9F7  48 8D 15 B2 D3 97 00            lea rdx, [rip + 0x97d3b2]
0048D9FE  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
0048DA03  E8 44 CE F0 FF                  call 0x14039a84c
0048DA08  EB 6F                           jmp 0x14048da79
0048DA0A  66 89 5C 24 52                  mov word ptr [rsp + 0x52], bx
0048DA0F  E8 2C 92 23 00                  call 0x1406c6c40
0048DA14  0F B7 44 24 52                  movzx eax, word ptr [rsp + 0x52]
0048DA19  41 0F B7 CF                     movzx ecx, r15w
0048DA1D  0F B7 1D FC 96 B3 00            movzx ebx, word ptr [rip + 0xb396fc]
0048DA24  66 3B D8                        cmp bx, ax
0048DA27  44 89 7C 24 54                  mov dword ptr [rsp + 0x54], r15d
0048DA2C  66 0F 47 D8                     cmova bx, ax
0048DA30  66 89 5C 24 50                  mov word ptr [rsp + 0x50], bx
0048DA35  66 44 3B FB                     cmp r15w, bx
0048DA39  73 26                           jae 0x14048da61
0048DA3B  44 0F B7 C3                     movzx r8d, bx
0048DA3F  48 8D 15 E2 96 B3 00            lea rdx, [rip + 0xb396e2]
0048DA46  49 C1 E0 03                     shl r8, 3
0048DA4A  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
0048DA4F  E8 EC 8D 23 00                  call 0x1406c6840
0048DA54  0F B7 44 24 52                  movzx eax, word ptr [rsp + 0x52]
0048DA59  0F B7 CB                        movzx ecx, bx
0048DA5C  0F B7 5C 24 50                  movzx ebx, word ptr [rsp + 0x50]
0048DA61  66 3B C8                        cmp cx, ax
0048DA64  73 18                           jae 0x14048da7e
0048DA66  0F B7 C1                        movzx eax, cx
0048DA69  66 41 03 CC                     add cx, r12w
0048DA6D  4C 89 7C C4 58                  mov qword ptr [rsp + rax*8 + 0x58], r15
0048DA72  66 3B 4C 24 52                  cmp cx, word ptr [rsp + 0x52]
0048DA77  72 ED                           jb 0x14048da66
0048DA79  0F B7 5C 24 50                  movzx ebx, word ptr [rsp + 0x50]
0048DA7E  85 FF                           test edi, edi
0048DA80  75 18                           jne 0x14048da9a
0048DA82  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
0048DA87  48 8D 55 60                     lea rdx, [rbp + 0x60]
0048DA8B  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
0048DA90  E8 AB 2C F3 FF                  call 0x1403c0740
0048DA95  0F B7 5C 24 50                  movzx ebx, word ptr [rsp + 0x50]
0048DA9A  48 8B 05 0F 57 A9 00            mov rax, qword ptr [rip + 0xa9570f]
0048DAA1  41 8B 4E 24                     mov ecx, dword ptr [r14 + 0x24]
0048DAA5  8B 0C 88                        mov ecx, dword ptr [rax + rcx*4]
0048DAA8  8B D1                           mov edx, ecx
0048DAAA  C1 EA 06                        shr edx, 6
0048DAAD  83 E1 3F                        and ecx, 0x3f
0048DAB0  0F B7 C3                        movzx eax, bx
0048DAB3  3B D0                           cmp edx, eax
0048DAB5  73 3D                           jae 0x14048daf4
0048DAB7  48 8B 54 D4 58                  mov rdx, qword ptr [rsp + rdx*8 + 0x58]
0048DABC  48 D3 EA                        shr rdx, cl
0048DABF  41 85 D4                        test r12d, edx
0048DAC2  74 30                           je 0x14048daf4
0048DAC4  41 8B D7                        mov edx, r15d
0048DAC7  66 44 3B FB                     cmp r15w, bx
0048DACB  73 1C                           jae 0x14048dae9
0048DACD  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
0048DAD2  44 0F B7 CB                     movzx r9d, bx
0048DAD6  49 8B 00                        mov rax, qword ptr [r8]
0048DAD9  4D 8D 40 08                     lea r8, [r8 + 8]
0048DADD  F3 48 0F B8 C8                  popcnt rcx, rax
0048DAE2  03 D1                           add edx, ecx
0048DAE4  4D 2B CC                        sub r9, r12
0048DAE7  75 ED                           jne 0x14048dad6
0048DAE9  8D 42 FF                        lea eax, [rdx - 1]
0048DAEC  89 05 DE 58 A9 00               mov dword ptr [rip + 0xa958de], eax
0048DAF2  EB 2B                           jmp 0x14048db1f
0048DAF4  41 8B D7                        mov edx, r15d
0048DAF7  66 44 3B FB                     cmp r15w, bx
0048DAFB  73 1C                           jae 0x14048db19
0048DAFD  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
0048DB02  44 0F B7 CB                     movzx r9d, bx
0048DB06  49 8B 00                        mov rax, qword ptr [r8]
0048DB09  4D 8D 40 08                     lea r8, [r8 + 8]
0048DB0D  F3 48 0F B8 C8                  popcnt rcx, rax
0048DB12  03 D1                           add edx, ecx
0048DB14  4D 2B CC                        sub r9, r12
0048DB17  75 ED                           jne 0x14048db06
0048DB19  89 15 B1 58 A9 00               mov dword ptr [rip + 0xa958b1], edx
0048DB1F  E8 78 9D 06 00                  call 0x1404f789c
0048DB24  85 C0                           test eax, eax
0048DB26  75 7A                           jne 0x14048dba2
0048DB28  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0048DB2D  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0048DB32  48 8D 44 24 50                  lea rax, [rsp + 0x50]
0048DB37  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0048DB3C  44 89 7C 24 20                  mov dword ptr [rsp + 0x20], r15d
0048DB41  44 89 7C 24 3A                  mov dword ptr [rsp + 0x3a], r15d
0048DB46  66 44 89 7C 24 3E               mov word ptr [rsp + 0x3e], r15w
0048DB4C  66 44 89 7C 24 38               mov word ptr [rsp + 0x38], r15w
0048DB52  EB 36                           jmp 0x14048db8a
0048DB54  8B 4C 24 20                     mov ecx, dword ptr [rsp + 0x20]
0048DB58  E8 73 AA E4 FF                  call 0x1402d85d0
0048DB5D  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0048DB66  48 3B C1                        cmp rax, rcx
0048DB69  75 0D                           jne 0x14048db78
0048DB6B  40 8A D6                        mov dl, sil
0048DB6E  48 8B C8                        mov rcx, rax
0048DB71  E8 42 48 EC FF                  call 0x1403523b8
0048DB76  EB 12                           jmp 0x14048db8a
0048DB78  48 8B D6                        mov rdx, rsi
0048DB7B  48 8D 88 98 8A 00 00            lea rcx, [rax + 0x8a98]
0048DB82  45 33 C0                        xor r8d, r8d
0048DB85  E8 C6 A0 D7 FF                  call 0x140207c50
0048DB8A  48 8D 54 24 28                  lea rdx, [rsp + 0x28]
0048DB8F  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0048DB94  E8 E7 78 F8 FF                  call 0x140415480
0048DB99  85 C0                           test eax, eax
0048DB9B  74 B7                           je 0x14048db54
0048DB9D  E9 E4 00 00 00                  jmp 0x14048dc86
0048DBA2  44 39 3D D7 8E B3 00            cmp dword ptr [rip + 0xb38ed7], r15d
0048DBA9  41 8B FF                        mov edi, r15d
0048DBAC  0F 86 D4 00 00 00               jbe 0x14048dc86
0048DBB2  8B CF                           mov ecx, edi
0048DBB4  E8 17 AA E4 FF                  call 0x1402d85d0
0048DBB9  48 8B D0                        mov rdx, rax
0048DBBC  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
0048DBC1  48 8B D8                        mov rbx, rax
0048DBC4  E8 D7 8A FA FF                  call 0x1404366a0
0048DBC9  84 C0                           test al, al
0048DBCB  74 32                           je 0x14048dbff
0048DBCD  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0048DBD6  48 3B D1                        cmp rdx, rcx
0048DBD9  75 10                           jne 0x14048dbeb
0048DBDB  40 8A D6                        mov dl, sil
0048DBDE  48 8B CB                        mov rcx, rbx
0048DBE1  E8 D2 47 EC FF                  call 0x1403523b8
0048DBE6  E9 8C 00 00 00                  jmp 0x14048dc77
0048DBEB  48 8B D6                        mov rdx, rsi
0048DBEE  48 8D 8B 98 8A 00 00            lea rcx, [rbx + 0x8a98]
0048DBF5  45 33 C0                        xor r8d, r8d
0048DBF8  E8 53 A0 D7 FF                  call 0x140207c50
0048DBFD  EB 78                           jmp 0x14048dc77
0048DBFF  40 84 F6                        test sil, sil
0048DC02  75 73                           jne 0x14048dc77
0048DC04  45 8A F7                        mov r14b, r15b
0048DC07  44 89 7C 24 24                  mov dword ptr [rsp + 0x24], r15d
0048DC0C  F0 48 0F BA 6B 30 00            lock bts qword ptr [rbx + 0x30], 0
0048DC13  73 15                           jae 0x14048dc2a
0048DC15  48 8D 4C 24 24                  lea rcx, [rsp + 0x24]
0048DC1A  E8 E1 E0 F6 FF                  call 0x1403fbd00
0048DC1F  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
0048DC23  48 85 C0                        test rax, rax
0048DC26  75 ED                           jne 0x14048dc15
0048DC28  EB E2                           jmp 0x14048dc0c
0048DC2A  44 84 63 23                     test byte ptr [rbx + 0x23], r12b
0048DC2E  75 27                           jne 0x14048dc57
0048DC30  48 8B 83 48 8E 00 00            mov rax, qword ptr [rbx + 0x8e48]
0048DC37  8B 8B D8 83 00 00               mov ecx, dword ptr [rbx + 0x83d8]
0048DC3D  8B 40 08                        mov eax, dword ptr [rax + 8]
0048DC40  0B C1                           or eax, ecx
0048DC42  75 09                           jne 0x14048dc4d
0048DC44  4C 39 BB 30 84 00 00            cmp qword ptr [rbx + 0x8430], r15
0048DC4B  74 0A                           je 0x14048dc57
0048DC4D  44 88 A3 BB 38 00 00            mov byte ptr [rbx + 0x38bb], r12b
0048DC54  45 8A F4                        mov r14b, r12b
0048DC57  F0 4C 21 7B 30                  lock and qword ptr [rbx + 0x30], r15
0048DC5C  45 84 F6                        test r14b, r14b
0048DC5F  74 16                           je 0x14048dc77
0048DC61  8B 4B 24                        mov ecx, dword ptr [rbx + 0x24]
0048DC64  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
0048DC6C  3B C1                           cmp eax, ecx
0048DC6E  74 07                           je 0x14048dc77
0048DC70  B2 02                           mov dl, 2
0048DC72  E8 B9 2D DC FF                  call 0x140250a30
0048DC77  41 03 FC                        add edi, r12d
0048DC7A  3B 3D 00 8E B3 00               cmp edi, dword ptr [rip + 0xb38e00]
0048DC80  0F 82 2C FF FF FF               jb 0x14048dbb2
0048DC86  48 8B 8D 70 01 00 00            mov rcx, qword ptr [rbp + 0x170]
0048DC8D  48 33 CC                        xor rcx, rsp
0048DC90  E8 AB E9 21 00                  call 0x1406ac640
0048DC95  4C 8D 9C 24 80 02 00 00         lea r11, [rsp + 0x280]
0048DC9D  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0048DCA1  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
0048DCA5  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
0048DCA9  49 8B E3                        mov rsp, r11
0048DCAC  41 5F                           pop r15
0048DCAE  41 5E                           pop r14
0048DCB0  41 5D                           pop r13
0048DCB2  41 5C                           pop r12
0048DCB4  5D                              pop rbp
0048DCB5  C3                              ret
0048DCB6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiForceIdleUpdateSchedulerParkState(unsigned __int8 a1, int a2)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m250;
    unsigned int v_stack_m254;
    unsigned __int16 v_stack_m256;
    unsigned __int16 v_stack_m258;
    unsigned __int16 v_stack_m26A;
    unsigned int v_stack_m26E;
    unsigned __int16 v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m280;
    unsigned int v_stack_m284;
    unsigned int v_stack_m288;
    unsigned int v_stack_m2A8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (640);
    result = (*(unsigned __int64 *)(v_rip + 9948831)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 424 + 368) = result;
    a2 = 0;
    result = memset(v_stack_m250, a2, 256, a4);
    a2 = 0;
    result = memset(v_rsp - 424 + 104, a2, 256, a4);
    *(unsigned __int64 *)(v_rsp - 424 + 96) = 0x200001ULL;
    a2 = 0;
    v_r15 = 0;
    result = memset(v_rsp - 424 + 104, a2, 256, a4);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11098828))) != 0) goto loc_0048D90D;
    goto loc_0048D966;
loc_0048D90D:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11768173))) == 0) goto loc_0048D95A;
loc_0048D91A:
    a2 = 0;
    a1 = (*(unsigned __int64 *)(v_rip + 11776799 + 0 * 8)) + (0x8A98ULL);
    result = KeRemoveQueueDpcEx(a1, a2, 256, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0048D946;
    result = KeAddProcessorAffinityEx(v_rsp - 424 + 96, 0, 256, a4);
    goto loc_0048D94D;
loc_0048D946:
loc_0048D94D:
    v_rbx = (unsigned int)((0) + (1));
    if (((unsigned int)(v_rbx)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11768109))))) goto loc_0048D91A;
loc_0048D95A:
    goto loc_0048D966;
loc_0048D964:
loc_0048D966:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11098724))) != 0) goto loc_0048D964;
    a2 = 0;
    if (a1 != 0) goto loc_0048DA0A;
    v_stack_m256 = 32;
    result = memset(v_stack_m250, a2, 256, a4);
    v_stack_m254 = 0;
    v_rbx = *(unsigned __int16 *)(v_rip + 9950493);
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rip + 9950493))) > ((unsigned __int16)(v_stack_m256))) { v_rbx = (unsigned __int16)(v_stack_m256); }
    v_stack_m258 = (unsigned __int16)(v_rbx);
    if (0 >= ((unsigned __int16)(v_rbx))) goto loc_0048D9EC;
    a3 = ((unsigned __int16)(v_rbx)) << (3);
    result = memcpy(v_stack_m250, v_rip + 9950465, a3, v_stack_m256);
    goto loc_0048D9E6;
loc_0048D9DA:
    a1 = (unsigned __int16)(((unsigned __int16)(v_rbx)) + (1));
    *(unsigned __int64 *)(v_rsp + (unsigned __int16)((unsigned __int16)(v_rbx)) * 8 + 88) = 0;
loc_0048D9E6:
loc_0048D9EC:
    if (a1 < ((unsigned __int16)(v_stack_m256))) goto loc_0048D9DA;
    result = KiOrAffinityEx(v_stack_m258, v_rip + 9950130, v_stack_m258, v_stack_m256);
    goto loc_0048DA79;
loc_0048DA0A:
    v_stack_m256 = (unsigned __int16)(v_rbx);
    result = memset(v_stack_m258, v_rip + 9950130, v_stack_m258, v_stack_m256);
    v_stack_m254 = 0;
    v_rbx = *(unsigned __int16 *)(v_rip + 11769596);
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rip + 11769596))) > ((unsigned __int16)(v_stack_m256))) { v_rbx = (unsigned __int16)(v_stack_m256); }
    v_stack_m258 = (unsigned __int16)(v_rbx);
    result = v_stack_m256;
    if (0 < ((unsigned __int16)(v_rbx))) {
        a3 = (unsigned __int16)(v_rbx);
        a2 = v_rip + 11769570;
        a3 = (a3) << (3);
        a1 = v_stack_m250;
        result = memcpy(a1, a2, a3, v_stack_m256);
        result = v_stack_m256;
        a1 = (unsigned __int16)(v_rbx);
        v_rbx = v_stack_m258;
    }
    if (a1 >= ((unsigned __int16)(result))) goto loc_0048DA7E;
loc_0048DA66:
    a1 = (unsigned __int16)((a1) + (1));
    *(unsigned __int64 *)(v_rsp + a1 * 8 + 88) = 0;
    if (a1 < v_stack_m256) goto loc_0048DA66;
loc_0048DA79:
loc_0048DA7E:
    result = a1;
    v_rbx = v_stack_m258;
    if (0 == 0) {
        a3 = v_stack_m258;
        a2 = v_rsp - 424 + 96;
        a1 = v_stack_m258;
        result = KeAndAffinityEx2(a1, a2, a3, v_stack_m256);
        v_rbx = v_stack_m258;
    }
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11097871) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36)) * 4))))) >> (6));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11097871) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36)) * 4))) & (63));
    if (a2 >= ((unsigned int)((unsigned __int16)(v_rbx)))) goto loc_0048DAF4;
    a2 = (*(unsigned __int64 *)(v_rsp + a2 * 8 + 88)) >> (a1);
    if (((1) & (a2)) == 0) goto loc_0048DAF4;
    if (0 >= ((unsigned __int16)(v_rbx))) goto loc_0048DAE9;
loc_0048DAD6:
    a2 = (unsigned int)((0) + (a1));
    a4 = ((unsigned __int16)(v_rbx)) - (1);
    if (condition_is_not_equal) goto loc_0048DAD6;
loc_0048DAE9:
    *(unsigned int *)(v_rip + 11098334) = (unsigned int)(a2 - 1);
    goto loc_0048DB1F;
loc_0048DAF4:
    if (0 >= ((unsigned __int16)(v_rbx))) goto loc_0048DB19;
loc_0048DB06:
    a2 = (unsigned int)((0) + (a1));
    a4 = ((unsigned __int16)(v_rbx)) - (1);
    if (condition_is_not_equal) goto loc_0048DB06;
loc_0048DB19:
    *(unsigned int *)(v_rip + 11098289) = a2;
loc_0048DB1F:
    result = Feature_ForceIdleReschedulingFix__private_IsEnabledDeviceUsageNoInline(a1, a2, v_stack_m250 + 8, a4);
    if ((unsigned int)(result) != 0) goto loc_0048DBA2;
    v_stack_m278 = v_stack_m250;
    v_stack_m280 = v_stack_m258;
    v_stack_m288 = 0;
    v_stack_m26E = 0;
    v_stack_m26A = 0;
    v_stack_m270 = 0;
    goto loc_0048DB8A;
loc_0048DB54:
    result = KeGetPrcb((unsigned int)(v_stack_m288), a2, v_stack_m250 + 8, a4);
    if (result != (*(unsigned __int64 *)(gs_base + (0 + 32)))) goto loc_0048DB78;
    result = KiForceIdleParkUnparkProcessor(result, a1, v_stack_m250 + 8, a4);
    goto loc_0048DB8A;
loc_0048DB78:
    a3 = 0;
    result = KeInsertQueueDpc(result + 35480, a1, a3, a4);
loc_0048DB8A:
    result = KeEnumerateNextProcessor(v_stack_m288, v_stack_m280, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0048DB54;
    goto loc_0048DC86;
loc_0048DBA2:
    if ((*(unsigned int *)(v_rip + 11767511)) <= 0) goto loc_0048DC86;
loc_0048DBB2:
    result = KeGetPrcb(0, v_stack_m280, a3, a4);
    result = KiCheckPrcbAffinityEx(v_stack_m258, result, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0048DBFF;
    if (result != (*(unsigned __int64 *)(gs_base + (0 + 32)))) goto loc_0048DBEB;
    result = KiForceIdleParkUnparkProcessor(result, a1, a3, a4);
    goto loc_0048DC77;
loc_0048DBEB:
    a3 = 0;
    result = KeInsertQueueDpc(result + 35480, a1, a3, a4);
    goto loc_0048DC77;
loc_0048DBFF:
    if (a1 != 0) goto loc_0048DC77;
    v_stack_m284 = 0;
loc_0048DC0C:
    if (condition_is_above_or_equal) goto loc_0048DC2A;
loc_0048DC15:
    result = KeYieldProcessorEx(v_stack_m284, a1, a3, a4);
    if (*(unsigned __int64 *)(result + 48) != 0) goto loc_0048DC15;
    goto loc_0048DC0C;
loc_0048DC2A:
    if (((*(unsigned __int8 *)(result + 35)) & (1)) != 0) goto loc_0048DC57;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 36424) + 8))) | ((unsigned int)((unsigned int)(*(unsigned int *)(result + 33752)))));
    if (condition_is_not_equal) goto loc_0048DC4D;
    v_r14 = 0;
    if ((*(unsigned __int64 *)(result + 33840)) != 0) {
        *(unsigned __int8 *)(result + 14523) = 1;
        v_r14 = 1;
    }
    if ((unsigned __int8)(v_r14) == 0) goto loc_0048DC77;
    result = (unsigned int)(*(unsigned int *)(gs_base + (0 + 420)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) != ((unsigned int)((unsigned int)(*(unsigned int *)(result + 36))))) {
        a2 = 2;
        result = KiSendSoftwareInterrupt((unsigned int)(*(unsigned int *)(result + 36)), a2, a3, a4);
    }
    v_rdi = (unsigned int)((0) + (1));
    if (((unsigned int)(v_rdi)) < (*(unsigned int *)(v_rip + 11767296))) goto loc_0048DBB2;
loc_0048DC86:
    a1 = (*(unsigned __int64 *)(v_rsp - 424 + 368)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiForceIdleUpdateSchedulerParkState(uint8_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m250;
    uint32_t v_stack_m254;
    uint16_t v_stack_m256;
    uint16_t v_stack_m258;
    uint16_t v_stack_m26A;
    uint32_t v_stack_m26E;
    uint16_t v_stack_m270;
    uint64_t v_stack_m278;
    uint64_t v_stack_m28;
    uint64_t v_stack_m280;
    uint32_t v_stack_m284;
    uint32_t v_stack_m288;
    uint32_t v_stack_m2A8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (640);
    result = (*(uint64_t *)(v_rip + 0x97CE9F)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x1A8 + 0x170) = result;
    Arg2 = 0;
    result = memset(v_stack_m250, Arg2, 256, a4);
    Arg2 = 0;
    result = memset(local_rsp - 424 + 104, Arg2, 256, a4);
    *(uint64_t *)(local_rsp - 0x1A8 + 0x60) = 0x200001ULL;
    Arg2 = 0;
    local_r15 = 0;
    result = memset(local_rsp - 424 + 104, Arg2, 256, a4);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA95ACC))) != 0) goto loc_0048D90D;
    goto loc_0048D966;
loc_0048D90D:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB3916D))) == 0) goto loc_0048D95A;
loc_0048D91A:
    Arg2 = 0;
    Arg1 = (*(uint64_t *)(v_rip + 0xB3B31F + 0x0 * 8)) + (0x8A98ULL);
    result = KeRemoveQueueDpcEx(Arg1, Arg2, 256, a4);
    if ((uint8_t)(result) != 0) goto loc_0048D946;
    result = KeAddProcessorAffinityEx(local_rsp - 424 + 96, 0, 256, a4);
    goto loc_0048D94D;
loc_0048D946:
loc_0048D94D:
    local_rbx = (uint32_t)((0) + (1));
    if (((uint32_t)(local_rbx)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB3912D))))) goto loc_0048D91A;
loc_0048D95A:
    goto loc_0048D966;
loc_0048D964:
loc_0048D966:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA95A64))) != 0) goto loc_0048D964;
    Arg2 = 0;
    if (Arg1 != 0) goto loc_0048DA0A;
    v_stack_m256 = 32;
    result = memset(v_stack_m250, Arg2, 256, a4);
    v_stack_m254 = 0;
    local_rbx = *(uint16_t *)(v_rip + 0x97D51D);
    if (((uint16_t)(*(uint16_t *)(v_rip + 0x97D51D))) > ((uint16_t)(v_stack_m256))) { local_rbx = (uint16_t)(v_stack_m256); }
    v_stack_m258 = (uint16_t)(local_rbx);
    if (0 >= ((uint16_t)(local_rbx))) goto loc_0048D9EC;
    a3 = ((uint16_t)(local_rbx)) << (3);
    result = memcpy(v_stack_m250, v_rip + 9950465, a3, v_stack_m256);
    goto loc_0048D9E6;
loc_0048D9DA:
    Arg1 = (uint16_t)(((uint16_t)(local_rbx)) + (1));
    *(uint64_t *)(local_rsp + (uint16_t)((uint16_t)(local_rbx)) * 8 + 0x58) = 0;
loc_0048D9E6:
loc_0048D9EC:
    if (Arg1 < ((uint16_t)(v_stack_m256))) goto loc_0048D9DA;
    result = KiOrAffinityEx(v_stack_m258, v_rip + 9950130, v_stack_m258, v_stack_m256);
    goto loc_0048DA79;
loc_0048DA0A:
    v_stack_m256 = (uint16_t)(local_rbx);
    result = memset(v_stack_m258, v_rip + 9950130, v_stack_m258, v_stack_m256);
    v_stack_m254 = 0;
    local_rbx = *(uint16_t *)(v_rip + 0xB396FC);
    if (((uint16_t)(*(uint16_t *)(v_rip + 0xB396FC))) > ((uint16_t)(v_stack_m256))) { local_rbx = (uint16_t)(v_stack_m256); }
    v_stack_m258 = (uint16_t)(local_rbx);
    result = v_stack_m256;
    if (0 < ((uint16_t)(local_rbx))) {
        a3 = (uint16_t)(local_rbx);
        Arg2 = v_rip + 11769570;
        a3 = (a3) << (3);
        Arg1 = v_stack_m250;
        result = memcpy(Arg1, Arg2, a3, v_stack_m256);
        result = v_stack_m256;
        Arg1 = (uint16_t)(local_rbx);
        local_rbx = v_stack_m258;
    }
    if (Arg1 >= ((uint16_t)(result))) goto loc_0048DA7E;
loc_0048DA66:
    Arg1 = (uint16_t)((Arg1) + (1));
    *(uint64_t *)(local_rsp + Arg1 * 8 + 0x58) = 0;
    if (Arg1 < v_stack_m256) goto loc_0048DA66;
loc_0048DA79:
loc_0048DA7E:
    result = Arg1;
    local_rbx = v_stack_m258;
    if (0 == 0) {
        a3 = v_stack_m258;
        Arg2 = local_rsp - 424 + 96;
        Arg1 = v_stack_m258;
        result = KeAndAffinityEx2(Arg1, Arg2, a3, v_stack_m256);
        local_rbx = v_stack_m258;
    }
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA9570F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x24)) * 4))))) >> (6));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA9570F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x24)) * 4))) & (63));
    if (Arg2 >= ((uint32_t)((uint16_t)(local_rbx)))) goto loc_0048DAF4;
    Arg2 = (*(uint64_t *)(local_rsp + Arg2 * 8 + 0x58)) >> (Arg1);
    if (((1) & (Arg2)) == 0) goto loc_0048DAF4;
    if (0 >= ((uint16_t)(local_rbx))) goto loc_0048DAE9;
loc_0048DAD6:
    Arg2 = (uint32_t)((0) + (Arg1));
    a4 = ((uint16_t)(local_rbx)) - (1);
    if (condition_is_not_equal) goto loc_0048DAD6;
loc_0048DAE9:
    *(uint32_t *)(v_rip + 0xA958DE) = (uint32_t)(Arg2 - 1);
    goto loc_0048DB1F;
loc_0048DAF4:
    if (0 >= ((uint16_t)(local_rbx))) goto loc_0048DB19;
loc_0048DB06:
    Arg2 = (uint32_t)((0) + (Arg1));
    a4 = ((uint16_t)(local_rbx)) - (1);
    if (condition_is_not_equal) goto loc_0048DB06;
loc_0048DB19:
    *(uint32_t *)(v_rip + 0xA958B1) = Arg2;
loc_0048DB1F:
    result = Feature_ForceIdleReschedulingFix__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, v_stack_m250 + 8, a4);
    if ((uint32_t)(result) != 0) goto loc_0048DBA2;
    v_stack_m278 = v_stack_m250;
    v_stack_m280 = v_stack_m258;
    v_stack_m288 = 0;
    v_stack_m26E = 0;
    v_stack_m26A = 0;
    v_stack_m270 = 0;
    goto loc_0048DB8A;
loc_0048DB54:
    result = KeGetPrcb((uint32_t)(v_stack_m288), Arg2, v_stack_m250 + 8, a4);
    if (result != (*(uint64_t *)(gs_base + (0 + 0x20)))) goto loc_0048DB78;
    result = KiForceIdleParkUnparkProcessor(result, Arg1, v_stack_m250 + 8, a4);
    goto loc_0048DB8A;
loc_0048DB78:
    a3 = 0;
    result = KeInsertQueueDpc(result + 35480, Arg1, a3, a4);
loc_0048DB8A:
    result = KeEnumerateNextProcessor(v_stack_m288, v_stack_m280, a3, a4);
    if ((uint32_t)(result) == 0) goto loc_0048DB54;
    goto loc_0048DC86;
loc_0048DBA2:
    if ((*(uint32_t *)(v_rip + 0xB38ED7)) <= 0) goto loc_0048DC86;
loc_0048DBB2:
    result = KeGetPrcb(0, v_stack_m280, a3, a4);
    result = KiCheckPrcbAffinityEx(v_stack_m258, result, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0048DBFF;
    if (result != (*(uint64_t *)(gs_base + (0 + 0x20)))) goto loc_0048DBEB;
    result = KiForceIdleParkUnparkProcessor(result, Arg1, a3, a4);
    goto loc_0048DC77;
loc_0048DBEB:
    a3 = 0;
    result = KeInsertQueueDpc(result + 35480, Arg1, a3, a4);
    goto loc_0048DC77;
loc_0048DBFF:
    if (Arg1 != 0) goto loc_0048DC77;
    v_stack_m284 = 0;
loc_0048DC0C:
    if (condition_is_above_or_equal) goto loc_0048DC2A;
loc_0048DC15:
    result = KeYieldProcessorEx(v_stack_m284, Arg1, a3, a4);
    if (*(uint64_t *)(result + 0x30) != 0) goto loc_0048DC15;
    goto loc_0048DC0C;
loc_0048DC2A:
    if (((*(uint8_t *)(result + 0x23)) & (1)) != 0) goto loc_0048DC57;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x8E48) + 0x8))) | ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x83D8)))));
    if (condition_is_not_equal) goto loc_0048DC4D;
    local_r14 = 0;
    if ((*(uint64_t *)(result + 0x8430)) != 0) {
        *(uint8_t *)(result + 0x38BB) = 1;
        local_r14 = 1;
    }
    if ((uint8_t)(local_r14) == 0) goto loc_0048DC77;
    result = (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) != ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x24))))) {
        Arg2 = 2;
        result = KiSendSoftwareInterrupt((uint32_t)(*(uint32_t *)(result + 0x24)), Arg2, a3, a4);
    }
    local_rdi = (uint32_t)((0) + (1));
    if (((uint32_t)(local_rdi)) < (*(uint32_t *)(v_rip + 0xB38E00))) goto loc_0048DBB2;
loc_0048DC86:
    Arg1 = (*(uint64_t *)(local_rsp - 0x1A8 + 0x170)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, a4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0048D874&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
