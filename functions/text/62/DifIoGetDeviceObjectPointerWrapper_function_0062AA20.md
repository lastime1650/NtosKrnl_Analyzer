# DifIoGetDeviceObjectPointerWrapper

- RVA: `0x0062AA20`–`0x0062ABA5` (길이 `389` bytes)
- VA: `0x000000014062AA20`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2B7C`
- 디코드: `112`개 명령, `389/389` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062AA60` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062AA86` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062AAC2` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062AAE8` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062AB01` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062AB13` → [IoGetDeviceObjectPointer](../../page/95/IoGetDeviceObjectPointer_function_00953220.md) (function, `0x00953220`)
- `0x0062AB3F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062AB65` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062AB7E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062AA96` → RVA `0x00F048B8` (`.data`; read)
- `0x0062AAAF` → RVA `0x00F04980` (`.data`; read)
- `0x0062AABB` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0062AB13` → [IoGetDeviceObjectPointer](../../page/95/IoGetDeviceObjectPointer_function_00953220.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062AA20  48 8B C4                        mov rax, rsp
0062AA23  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0062AA27  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0062AA2B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0062AA2F  48 89 48 08                     mov qword ptr [rax + 8], rcx
0062AA33  55                              push rbp
0062AA34  41 54                           push r12
0062AA36  41 55                           push r13
0062AA38  41 56                           push r14
0062AA3A  41 57                           push r15
0062AA3C  48 8B EC                        mov rbp, rsp
0062AA3F  48 83 EC 50                     sub rsp, 0x50
0062AA43  0F 57 C0                        xorps xmm0, xmm0
0062AA46  B9 50 01 00 00                  mov ecx, 0x150
0062AA4B  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0062AA4F  4D 8B F9                        mov r15, r9
0062AA52  4D 8B E0                        mov r12, r8
0062AA55  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0062AA59  44 8B EA                        mov r13d, edx
0062AA5C  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
0062AA60  E8 CF AF E6 FF                  call 0x140495a34
0062AA65  48 8B F0                        mov rsi, rax
0062AA68  48 85 C0                        test rax, rax
0062AA6B  0F 84 95 00 00 00               je 0x14062ab06
0062AA71  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062AA74  A8 18                           test al, 0x18
0062AA76  74 0A                           je 0x14062aa82
0062AA78  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0062AA7C  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0062AA80  EB 0D                           jmp 0x14062aa8f
0062AA82  A8 04                           test al, 4
0062AA84  74 09                           je 0x14062aa8f
0062AA86  E8 7D 91 EA FF                  call 0x1404d3c08
0062AA8B  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0062AA8F  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
0062AA93  45 32 F6                        xor r14b, r14b
0062AA96  44 38 35 1B 9E 8D 00            cmp byte ptr [rip + 0x8d9e1b], r14b
0062AA9D  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0062AAA1  44 89 6D E8                     mov dword ptr [rbp - 0x18], r13d
0062AAA5  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0062AAA9  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
0062AAAD  75 0C                           jne 0x14062aabb
0062AAAF  F7 05 C7 9E 8D 00 00 08 00 00   test dword ptr [rip + 0x8d9ec7], 0x800
0062AAB9  74 13                           je 0x14062aace
0062AABB  48 8D 0D BE 93 8D 00            lea rcx, [rip + 0x8d93be]
0062AAC2  E8 59 BB BE FF                  call 0x140216620
0062AAC7  44 8A F0                        mov r14b, al
0062AACA  84 C0                           test al, al
0062AACC  74 38                           je 0x14062ab06
0062AACE  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0062AAD2  48 8B 1F                        mov rbx, qword ptr [rdi]
0062AAD5  EB 19                           jmp 0x14062aaf0
0062AAD7  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062AADB  48 85 C0                        test rax, rax
0062AADE  74 0D                           je 0x14062aaed
0062AAE0  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062AAE4  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0062AAE8  E8 E3 FF 08 00                  call 0x1406baad0
0062AAED  48 8B 1B                        mov rbx, qword ptr [rbx]
0062AAF0  48 3B DF                        cmp rbx, rdi
0062AAF3  75 E2                           jne 0x14062aad7
0062AAF5  45 84 F6                        test r14b, r14b
0062AAF8  74 0C                           je 0x14062ab06
0062AAFA  48 8D 0D 7F 93 8D 00            lea rcx, [rip + 0x8d937f]
0062AB01  E8 7A F3 D1 FF                  call 0x140349e80
0062AB06  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0062AB0A  4D 8B CF                        mov r9, r15
0062AB0D  4D 8B C4                        mov r8, r12
0062AB10  41 8B D5                        mov edx, r13d
0062AB13  E8 08 87 32 00                  call 0x140953220
0062AB18  89 45 F8                        mov dword ptr [rbp - 8], eax
0062AB1B  48 85 F6                        test rsi, rsi
0062AB1E  74 63                           je 0x14062ab83
0062AB20  40 32 FF                        xor dil, dil
0062AB23  40 38 3D 8E 9D 8D 00            cmp byte ptr [rip + 0x8d9d8e], dil
0062AB2A  75 0C                           jne 0x14062ab38
0062AB2C  F7 05 4A 9E 8D 00 00 08 00 00   test dword ptr [rip + 0x8d9e4a], 0x800
0062AB36  74 13                           je 0x14062ab4b
0062AB38  48 8D 0D 41 93 8D 00            lea rcx, [rip + 0x8d9341]
0062AB3F  E8 DC BA BE FF                  call 0x140216620
0062AB44  40 8A F8                        mov dil, al
0062AB47  84 C0                           test al, al
0062AB49  74 38                           je 0x14062ab83
0062AB4B  48 83 C6 30                     add rsi, 0x30
0062AB4F  48 8B 1E                        mov rbx, qword ptr [rsi]
0062AB52  EB 19                           jmp 0x14062ab6d
0062AB54  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062AB58  48 85 C0                        test rax, rax
0062AB5B  74 0D                           je 0x14062ab6a
0062AB5D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062AB61  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0062AB65  E8 66 FF 08 00                  call 0x1406baad0
0062AB6A  48 8B 1B                        mov rbx, qword ptr [rbx]
0062AB6D  48 3B DE                        cmp rbx, rsi
0062AB70  75 E2                           jne 0x14062ab54
0062AB72  40 84 FF                        test dil, dil
0062AB75  74 0C                           je 0x14062ab83
0062AB77  48 8D 0D 02 93 8D 00            lea rcx, [rip + 0x8d9302]
0062AB7E  E8 FD F2 D1 FF                  call 0x140349e80
0062AB83  8B 45 F8                        mov eax, dword ptr [rbp - 8]
0062AB86  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0062AB8B  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0062AB8F  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0062AB93  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0062AB97  49 8B E3                        mov rsp, r11
0062AB9A  41 5F                           pop r15
0062AB9C  41 5E                           pop r14
0062AB9E  41 5D                           pop r13
0062ABA0  41 5C                           pop r12
0062ABA2  5D                              pop rbp
0062ABA3  C3                              ret
0062ABA4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoGetDeviceObjectPointerWrapper(__int64 a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (80);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(336, a2, a3, a4);
    if (result == 0) goto loc_0062AB06;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062AA82;
    v_stack_m58 = v_stack_p0;
    goto loc_0062AA8F;
loc_0062AA82:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m40 = (unsigned int)((unsigned int)(a2));
    v_stack_m48 = a3;
    v_stack_m50 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9281051)) != 0) goto loc_0062AABB;
    if (((*(unsigned int *)(v_rip + 9281223)) & (0x800ULL)) == 0) goto loc_0062AACE;
loc_0062AABB:
    result = ExAcquireRundownProtection(v_rip + 9278398, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062AB06;
loc_0062AACE:
    goto loc_0062AAF0;
loc_0062AAD7:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062AAF0:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062AAD7;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9278335;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = IoGetDeviceObjectPointer(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_0062AB83;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9280910)) != 0) goto loc_0062AB38;
    if (((*(unsigned int *)(v_rip + 9281098)) & (0x800ULL)) == 0) goto loc_0062AB4B;
loc_0062AB38:
    result = ExAcquireRundownProtection(v_rip + 9278273, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062AB83;
loc_0062AB4B:
    v_rsi = (result) + (48);
    goto loc_0062AB6D;
loc_0062AB54:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_0062AB6D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062AB54;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9278210;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifIoGetDeviceObjectPointerWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (80);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(336, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0062AB06;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062AA82;
    v_stack_m58 = v_stack_p0;
    goto loc_0062AA8F;
loc_0062AA82:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m40 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m48 = Arg3;
    v_stack_m50 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8D9E1B)) != 0) goto loc_0062AABB;
    if (((*(uint32_t *)(v_rip + 0x8D9EC7)) & (0x800ULL)) == 0) goto loc_0062AACE;
loc_0062AABB:
    result = ExAcquireRundownProtection(v_rip + 9278398, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0062AB06;
loc_0062AACE:
    goto loc_0062AAF0;
loc_0062AAD7:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0062AAF0:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062AAD7;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9278335;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    result = IoGetDeviceObjectPointer(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_0062AB83;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D9D8E)) != 0) goto loc_0062AB38;
    if (((*(uint32_t *)(v_rip + 0x8D9E4A)) & (0x800ULL)) == 0) goto loc_0062AB4B;
loc_0062AB38:
    result = ExAcquireRundownProtection(v_rip + 9278273, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0062AB83;
loc_0062AB4B:
    local_rsi = (result) + (48);
    goto loc_0062AB6D;
loc_0062AB54:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
loc_0062AB6D:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062AB54;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9278210;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062AA20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062AA20[BB_0062AA20]
  bb_0062AA71[BB_0062AA71]
  bb_0062AA78[BB_0062AA78]
  bb_0062AA82[BB_0062AA82]
  bb_0062AA86[BB_0062AA86]
  bb_0062AA8F[BB_0062AA8F]
  bb_0062AAAF[BB_0062AAAF]
  bb_0062AABB[BB_0062AABB]
  bb_0062AACE[BB_0062AACE]
  bb_0062AAD7[BB_0062AAD7]
  bb_0062AAE0[BB_0062AAE0]
  bb_0062AAED[BB_0062AAED]
  bb_0062AAF0[BB_0062AAF0]
  bb_0062AAF5[BB_0062AAF5]
  bb_0062AAFA[BB_0062AAFA]
  bb_0062AB06[BB_0062AB06]
  bb_0062AB20[BB_0062AB20]
  bb_0062AB2C[BB_0062AB2C]
  bb_0062AB38[BB_0062AB38]
  bb_0062AB4B[BB_0062AB4B]
  bb_0062AB54[BB_0062AB54]
  bb_0062AB5D[BB_0062AB5D]
  bb_0062AB6A[BB_0062AB6A]
  bb_0062AB6D[BB_0062AB6D]
  bb_0062AB72[BB_0062AB72]
  bb_0062AB77[BB_0062AB77]
  bb_0062AB83[BB_0062AB83]
  bb_0062ABA4[BB_0062ABA4]
  bb_0062AA20 -->|branch| bb_0062AB06
  bb_0062AA20 -->|fallthrough| bb_0062AA71
  bb_0062AA71 -->|branch| bb_0062AA82
  bb_0062AA71 -->|fallthrough| bb_0062AA78
  bb_0062AA78 -->|branch| bb_0062AA8F
  bb_0062AA82 -->|branch| bb_0062AA8F
  bb_0062AA82 -->|fallthrough| bb_0062AA86
  bb_0062AA86 -->|flow| bb_0062AA8F
  bb_0062AA8F -->|branch| bb_0062AABB
  bb_0062AA8F -->|fallthrough| bb_0062AAAF
  bb_0062AAAF -->|branch| bb_0062AACE
  bb_0062AAAF -->|fallthrough| bb_0062AABB
  bb_0062AABB -->|branch| bb_0062AB06
  bb_0062AABB -->|fallthrough| bb_0062AACE
  bb_0062AACE -->|branch| bb_0062AAF0
  bb_0062AAD7 -->|branch| bb_0062AAED
  bb_0062AAD7 -->|fallthrough| bb_0062AAE0
  bb_0062AAE0 -->|flow| bb_0062AAED
  bb_0062AAED -->|flow| bb_0062AAF0
  bb_0062AAF0 -->|branch| bb_0062AAD7
  bb_0062AAF0 -->|fallthrough| bb_0062AAF5
  bb_0062AAF5 -->|branch| bb_0062AB06
  bb_0062AAF5 -->|fallthrough| bb_0062AAFA
  bb_0062AAFA -->|flow| bb_0062AB06
  bb_0062AB06 -->|branch| bb_0062AB83
  bb_0062AB06 -->|fallthrough| bb_0062AB20
  bb_0062AB20 -->|branch| bb_0062AB38
  bb_0062AB20 -->|fallthrough| bb_0062AB2C
  bb_0062AB2C -->|branch| bb_0062AB4B
  bb_0062AB2C -->|fallthrough| bb_0062AB38
  bb_0062AB38 -->|branch| bb_0062AB83
  bb_0062AB38 -->|fallthrough| bb_0062AB4B
  bb_0062AB4B -->|branch| bb_0062AB6D
  bb_0062AB54 -->|branch| bb_0062AB6A
  bb_0062AB54 -->|fallthrough| bb_0062AB5D
  bb_0062AB5D -->|flow| bb_0062AB6A
  bb_0062AB6A -->|flow| bb_0062AB6D
  bb_0062AB6D -->|branch| bb_0062AB54
  bb_0062AB6D -->|fallthrough| bb_0062AB72
  bb_0062AB72 -->|branch| bb_0062AB83
  bb_0062AB72 -->|fallthrough| bb_0062AB77
  bb_0062AB77 -->|flow| bb_0062AB83
```
