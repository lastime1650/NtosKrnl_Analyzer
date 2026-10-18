# DifIoGetDeviceDirectoryWrapper

- RVA: `0x0062A880`–`0x0062AA16` (길이 `406` bytes)
- VA: `0x000000014062A880`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2BBC`
- 디코드: `116`개 명령, `406/406` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062A8C0` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062A8E6` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062A92A` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062A950` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062A969` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062A984` → [IoGetDeviceDirectory](../../page/72/IoGetDeviceDirectory_function_00728370.md) (function, `0x00728370`)
- `0x0062A9B0` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062A9D6` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062A9EF` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062A8F6` → RVA `0x00F048B8` (`.data`; read)
- `0x0062A917` → RVA `0x00F04980` (`.data`; read)
- `0x0062A923` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0062A984` → [IoGetDeviceDirectory](../../page/72/IoGetDeviceDirectory_function_00728370.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062A880  48 8B C4                        mov rax, rsp
0062A883  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0062A887  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0062A88B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0062A88F  48 89 48 08                     mov qword ptr [rax + 8], rcx
0062A893  55                              push rbp
0062A894  41 54                           push r12
0062A896  41 55                           push r13
0062A898  41 56                           push r14
0062A89A  41 57                           push r15
0062A89C  48 8B EC                        mov rbp, rsp
0062A89F  48 83 EC 60                     sub rsp, 0x60
0062A8A3  0F 57 C0                        xorps xmm0, xmm0
0062A8A6  B9 51 01 00 00                  mov ecx, 0x151
0062A8AB  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0062A8AF  4D 8B F9                        mov r15, r9
0062A8B2  45 8B E0                        mov r12d, r8d
0062A8B5  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0062A8B9  44 8B EA                        mov r13d, edx
0062A8BC  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
0062A8C0  E8 6F B1 E6 FF                  call 0x140495a34
0062A8C5  48 8B F0                        mov rsi, rax
0062A8C8  48 85 C0                        test rax, rax
0062A8CB  0F 84 9D 00 00 00               je 0x14062a96e
0062A8D1  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062A8D4  A8 18                           test al, 0x18
0062A8D6  74 0A                           je 0x14062a8e2
0062A8D8  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0062A8DC  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0062A8E0  EB 0D                           jmp 0x14062a8ef
0062A8E2  A8 04                           test al, 4
0062A8E4  74 09                           je 0x14062a8ef
0062A8E6  E8 1D 93 EA FF                  call 0x1404d3c08
0062A8EB  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0062A8EF  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
0062A8F3  45 32 F6                        xor r14b, r14b
0062A8F6  44 38 35 BB 9F 8D 00            cmp byte ptr [rip + 0x8d9fbb], r14b
0062A8FD  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0062A901  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
0062A905  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
0062A909  44 89 6D EC                     mov dword ptr [rbp - 0x14], r13d
0062A90D  44 89 65 E8                     mov dword ptr [rbp - 0x18], r12d
0062A911  4C 89 7D E0                     mov qword ptr [rbp - 0x20], r15
0062A915  75 0C                           jne 0x14062a923
0062A917  F7 05 5F A0 8D 00 00 08 00 00   test dword ptr [rip + 0x8da05f], 0x800
0062A921  74 13                           je 0x14062a936
0062A923  48 8D 0D 56 95 8D 00            lea rcx, [rip + 0x8d9556]
0062A92A  E8 F1 BC BE FF                  call 0x140216620
0062A92F  44 8A F0                        mov r14b, al
0062A932  84 C0                           test al, al
0062A934  74 38                           je 0x14062a96e
0062A936  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0062A93A  48 8B 1F                        mov rbx, qword ptr [rdi]
0062A93D  EB 19                           jmp 0x14062a958
0062A93F  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062A943  48 85 C0                        test rax, rax
0062A946  74 0D                           je 0x14062a955
0062A948  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062A94C  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0062A950  E8 7B 01 09 00                  call 0x1406baad0
0062A955  48 8B 1B                        mov rbx, qword ptr [rbx]
0062A958  48 3B DF                        cmp rbx, rdi
0062A95B  75 E2                           jne 0x14062a93f
0062A95D  45 84 F6                        test r14b, r14b
0062A960  74 0C                           je 0x14062a96e
0062A962  48 8D 0D 17 95 8D 00            lea rcx, [rip + 0x8d9517]
0062A969  E8 12 F5 D1 FF                  call 0x140349e80
0062A96E  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
0062A972  4D 8B CF                        mov r9, r15
0062A975  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0062A979  45 8B C4                        mov r8d, r12d
0062A97C  41 8B D5                        mov edx, r13d
0062A97F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0062A984  E8 E7 D9 0F 00                  call 0x140728370
0062A989  89 45 F8                        mov dword ptr [rbp - 8], eax
0062A98C  48 85 F6                        test rsi, rsi
0062A98F  74 63                           je 0x14062a9f4
0062A991  40 32 FF                        xor dil, dil
0062A994  40 38 3D 1D 9F 8D 00            cmp byte ptr [rip + 0x8d9f1d], dil
0062A99B  75 0C                           jne 0x14062a9a9
0062A99D  F7 05 D9 9F 8D 00 00 08 00 00   test dword ptr [rip + 0x8d9fd9], 0x800
0062A9A7  74 13                           je 0x14062a9bc
0062A9A9  48 8D 0D D0 94 8D 00            lea rcx, [rip + 0x8d94d0]
0062A9B0  E8 6B BC BE FF                  call 0x140216620
0062A9B5  40 8A F8                        mov dil, al
0062A9B8  84 C0                           test al, al
0062A9BA  74 38                           je 0x14062a9f4
0062A9BC  48 83 C6 30                     add rsi, 0x30
0062A9C0  48 8B 1E                        mov rbx, qword ptr [rsi]
0062A9C3  EB 19                           jmp 0x14062a9de
0062A9C5  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062A9C9  48 85 C0                        test rax, rax
0062A9CC  74 0D                           je 0x14062a9db
0062A9CE  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062A9D2  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0062A9D6  E8 F5 00 09 00                  call 0x1406baad0
0062A9DB  48 8B 1B                        mov rbx, qword ptr [rbx]
0062A9DE  48 3B DE                        cmp rbx, rsi
0062A9E1  75 E2                           jne 0x14062a9c5
0062A9E3  40 84 FF                        test dil, dil
0062A9E6  74 0C                           je 0x14062a9f4
0062A9E8  48 8D 0D 91 94 8D 00            lea rcx, [rip + 0x8d9491]
0062A9EF  E8 8C F4 D1 FF                  call 0x140349e80
0062A9F4  8B 45 F8                        mov eax, dword ptr [rbp - 8]
0062A9F7  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
0062A9FC  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0062AA00  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0062AA04  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0062AA08  49 8B E3                        mov rsp, r11
0062AA0B  41 5F                           pop r15
0062AA0D  41 5E                           pop r14
0062AA0F  41 5D                           pop r13
0062AA11  41 5C                           pop r12
0062AA13  5D                              pop rbp
0062AA14  C3                              ret
0062AA15  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoGetDeviceDirectoryWrapper(__int64 a1, int a2, int a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (96);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(337, a2, a3, a4);
    if (result == 0) goto loc_0062A96E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062A8E2;
    v_stack_m58 = v_stack_p0;
    goto loc_0062A8EF;
loc_0062A8E2:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m50 = a5;
    v_stack_m3C = (unsigned int)((unsigned int)(a2));
    v_stack_m40 = (unsigned int)((unsigned int)(a3));
    v_stack_m48 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9281467)) != 0) goto loc_0062A923;
    if (((*(unsigned int *)(v_rip + 9281631)) & (0x800ULL)) == 0) goto loc_0062A936;
loc_0062A923:
    result = ExAcquireRundownProtection(v_rip + 9278806, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062A96E;
loc_0062A936:
    goto loc_0062A958;
loc_0062A93F:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062A958:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062A93F;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9278743;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m68 = a5;
    result = IoGetDeviceDirectory(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_0062A9F4;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9281309)) != 0) goto loc_0062A9A9;
    if (((*(unsigned int *)(v_rip + 9281497)) & (0x800ULL)) == 0) goto loc_0062A9BC;
loc_0062A9A9:
    result = ExAcquireRundownProtection(v_rip + 9278672, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062A9F4;
loc_0062A9BC:
    v_rsi = (result) + (48);
    goto loc_0062A9DE;
loc_0062A9C5:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
loc_0062A9DE:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062A9C5;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9278609;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifIoGetDeviceDirectoryWrapper(int64_t Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (96);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(337, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0062A96E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062A8E2;
    v_stack_m58 = v_stack_p0;
    goto loc_0062A8EF;
loc_0062A8E2:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m50 = Arg5;
    v_stack_m3C = (uint32_t)((uint32_t)(Arg2));
    v_stack_m40 = (uint32_t)((uint32_t)(Arg3));
    v_stack_m48 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8D9FBB)) != 0) goto loc_0062A923;
    if (((*(uint32_t *)(v_rip + 0x8DA05F)) & (0x800ULL)) == 0) goto loc_0062A936;
loc_0062A923:
    result = ExAcquireRundownProtection(v_rip + 9278806, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0062A96E;
loc_0062A936:
    goto loc_0062A958;
loc_0062A93F:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0062A958:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062A93F;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9278743;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m68 = Arg5;
    result = IoGetDeviceDirectory(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_0062A9F4;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D9F1D)) != 0) goto loc_0062A9A9;
    if (((*(uint32_t *)(v_rip + 0x8D9FD9)) & (0x800ULL)) == 0) goto loc_0062A9BC;
loc_0062A9A9:
    result = ExAcquireRundownProtection(v_rip + 9278672, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_0062A9F4;
loc_0062A9BC:
    local_rsi = (result) + (48);
    goto loc_0062A9DE;
loc_0062A9C5:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
loc_0062A9DE:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062A9C5;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9278609;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062A880&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062A880[BB_0062A880]
  bb_0062A8D1[BB_0062A8D1]
  bb_0062A8D8[BB_0062A8D8]
  bb_0062A8E2[BB_0062A8E2]
  bb_0062A8E6[BB_0062A8E6]
  bb_0062A8EF[BB_0062A8EF]
  bb_0062A917[BB_0062A917]
  bb_0062A923[BB_0062A923]
  bb_0062A936[BB_0062A936]
  bb_0062A93F[BB_0062A93F]
  bb_0062A948[BB_0062A948]
  bb_0062A955[BB_0062A955]
  bb_0062A958[BB_0062A958]
  bb_0062A95D[BB_0062A95D]
  bb_0062A962[BB_0062A962]
  bb_0062A96E[BB_0062A96E]
  bb_0062A991[BB_0062A991]
  bb_0062A99D[BB_0062A99D]
  bb_0062A9A9[BB_0062A9A9]
  bb_0062A9BC[BB_0062A9BC]
  bb_0062A9C5[BB_0062A9C5]
  bb_0062A9CE[BB_0062A9CE]
  bb_0062A9DB[BB_0062A9DB]
  bb_0062A9DE[BB_0062A9DE]
  bb_0062A9E3[BB_0062A9E3]
  bb_0062A9E8[BB_0062A9E8]
  bb_0062A9F4[BB_0062A9F4]
  bb_0062AA15[BB_0062AA15]
  bb_0062A880 -->|branch| bb_0062A96E
  bb_0062A880 -->|fallthrough| bb_0062A8D1
  bb_0062A8D1 -->|branch| bb_0062A8E2
  bb_0062A8D1 -->|fallthrough| bb_0062A8D8
  bb_0062A8D8 -->|branch| bb_0062A8EF
  bb_0062A8E2 -->|branch| bb_0062A8EF
  bb_0062A8E2 -->|fallthrough| bb_0062A8E6
  bb_0062A8E6 -->|flow| bb_0062A8EF
  bb_0062A8EF -->|branch| bb_0062A923
  bb_0062A8EF -->|fallthrough| bb_0062A917
  bb_0062A917 -->|branch| bb_0062A936
  bb_0062A917 -->|fallthrough| bb_0062A923
  bb_0062A923 -->|branch| bb_0062A96E
  bb_0062A923 -->|fallthrough| bb_0062A936
  bb_0062A936 -->|branch| bb_0062A958
  bb_0062A93F -->|branch| bb_0062A955
  bb_0062A93F -->|fallthrough| bb_0062A948
  bb_0062A948 -->|flow| bb_0062A955
  bb_0062A955 -->|flow| bb_0062A958
  bb_0062A958 -->|branch| bb_0062A93F
  bb_0062A958 -->|fallthrough| bb_0062A95D
  bb_0062A95D -->|branch| bb_0062A96E
  bb_0062A95D -->|fallthrough| bb_0062A962
  bb_0062A962 -->|flow| bb_0062A96E
  bb_0062A96E -->|branch| bb_0062A9F4
  bb_0062A96E -->|fallthrough| bb_0062A991
  bb_0062A991 -->|branch| bb_0062A9A9
  bb_0062A991 -->|fallthrough| bb_0062A99D
  bb_0062A99D -->|branch| bb_0062A9BC
  bb_0062A99D -->|fallthrough| bb_0062A9A9
  bb_0062A9A9 -->|branch| bb_0062A9F4
  bb_0062A9A9 -->|fallthrough| bb_0062A9BC
  bb_0062A9BC -->|branch| bb_0062A9DE
  bb_0062A9C5 -->|branch| bb_0062A9DB
  bb_0062A9C5 -->|fallthrough| bb_0062A9CE
  bb_0062A9CE -->|flow| bb_0062A9DB
  bb_0062A9DB -->|flow| bb_0062A9DE
  bb_0062A9DE -->|branch| bb_0062A9C5
  bb_0062A9DE -->|fallthrough| bb_0062A9E3
  bb_0062A9E3 -->|branch| bb_0062A9F4
  bb_0062A9E3 -->|fallthrough| bb_0062A9E8
  bb_0062A9E8 -->|flow| bb_0062A9F4
```
