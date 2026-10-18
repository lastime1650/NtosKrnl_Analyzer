# DifIoOpenDeviceRegistryKeyWrapper

- RVA: `0x0062BA50`–`0x0062BBD9` (길이 `393` bytes)
- VA: `0x000000014062BA50`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2B7C`
- 디코드: `113`개 명령, `393/393` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062BA92` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062BABA` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062BAF6` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062BB1C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062BB35` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062BB47` → [IoOpenDeviceRegistryKey](../../page/99/IoOpenDeviceRegistryKey_function_00999250.md) (function, `0x00999250`)
- `0x0062BB73` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062BB99` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062BBB2` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062BACA` → RVA `0x00F048B8` (`.data`; read)
- `0x0062BAE3` → RVA `0x00F04980` (`.data`; read)
- `0x0062BAEF` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0062BB47` → [IoOpenDeviceRegistryKey](../../page/99/IoOpenDeviceRegistryKey_function_00999250.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062BA50  48 8B C4                        mov rax, rsp
0062BA53  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0062BA57  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0062BA5B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0062BA5F  48 89 48 08                     mov qword ptr [rax + 8], rcx
0062BA63  55                              push rbp
0062BA64  41 54                           push r12
0062BA66  41 55                           push r13
0062BA68  41 56                           push r14
0062BA6A  41 57                           push r15
0062BA6C  48 8B EC                        mov rbp, rsp
0062BA6F  48 83 EC 50                     sub rsp, 0x50
0062BA73  0F 57 C0                        xorps xmm0, xmm0
0062BA76  33 C0                           xor eax, eax
0062BA78  B9 45 01 00 00                  mov ecx, 0x145
0062BA7D  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0062BA81  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0062BA85  4D 8B F9                        mov r15, r9
0062BA88  45 8B E0                        mov r12d, r8d
0062BA8B  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0062BA8F  44 8B EA                        mov r13d, edx
0062BA92  E8 9D 9F E6 FF                  call 0x140495a34
0062BA97  4C 8B F0                        mov r14, rax
0062BA9A  48 85 C0                        test rax, rax
0062BA9D  0F 84 97 00 00 00               je 0x14062bb3a
0062BAA3  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
0062BAA6  F6 C1 18                        test cl, 0x18
0062BAA9  74 0A                           je 0x14062bab5
0062BAAB  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0062BAAF  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0062BAB3  EB 0E                           jmp 0x14062bac3
0062BAB5  F6 C1 04                        test cl, 4
0062BAB8  74 09                           je 0x14062bac3
0062BABA  E8 49 81 EA FF                  call 0x1404d3c08
0062BABF  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0062BAC3  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
0062BAC7  40 32 F6                        xor sil, sil
0062BACA  40 38 35 E7 8D 8D 00            cmp byte ptr [rip + 0x8d8de7], sil
0062BAD1  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0062BAD5  44 89 6D E4                     mov dword ptr [rbp - 0x1c], r13d
0062BAD9  44 89 65 E0                     mov dword ptr [rbp - 0x20], r12d
0062BADD  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
0062BAE1  75 0C                           jne 0x14062baef
0062BAE3  F7 05 93 8E 8D 00 00 08 00 00   test dword ptr [rip + 0x8d8e93], 0x800
0062BAED  74 13                           je 0x14062bb02
0062BAEF  48 8D 0D 8A 83 8D 00            lea rcx, [rip + 0x8d838a]
0062BAF6  E8 25 AB BE FF                  call 0x140216620
0062BAFB  40 8A F0                        mov sil, al
0062BAFE  84 C0                           test al, al
0062BB00  74 38                           je 0x14062bb3a
0062BB02  49 8D 7E 20                     lea rdi, [r14 + 0x20]
0062BB06  48 8B 1F                        mov rbx, qword ptr [rdi]
0062BB09  EB 19                           jmp 0x14062bb24
0062BB0B  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062BB0F  48 85 C0                        test rax, rax
0062BB12  74 0D                           je 0x14062bb21
0062BB14  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062BB18  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0062BB1C  E8 AF EF 08 00                  call 0x1406baad0
0062BB21  48 8B 1B                        mov rbx, qword ptr [rbx]
0062BB24  48 3B DF                        cmp rbx, rdi
0062BB27  75 E2                           jne 0x14062bb0b
0062BB29  40 84 F6                        test sil, sil
0062BB2C  74 0C                           je 0x14062bb3a
0062BB2E  48 8D 0D 4B 83 8D 00            lea rcx, [rip + 0x8d834b]
0062BB35  E8 46 E3 D1 FF                  call 0x140349e80
0062BB3A  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0062BB3E  4D 8B CF                        mov r9, r15
0062BB41  45 8B C4                        mov r8d, r12d
0062BB44  41 8B D5                        mov edx, r13d
0062BB47  E8 04 D7 36 00                  call 0x140999250
0062BB4C  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0062BB4F  4D 85 F6                        test r14, r14
0062BB52  74 63                           je 0x14062bbb7
0062BB54  40 32 FF                        xor dil, dil
0062BB57  40 38 3D 5A 8D 8D 00            cmp byte ptr [rip + 0x8d8d5a], dil
0062BB5E  75 0C                           jne 0x14062bb6c
0062BB60  F7 05 16 8E 8D 00 00 08 00 00   test dword ptr [rip + 0x8d8e16], 0x800
0062BB6A  74 13                           je 0x14062bb7f
0062BB6C  48 8D 0D 0D 83 8D 00            lea rcx, [rip + 0x8d830d]
0062BB73  E8 A8 AA BE FF                  call 0x140216620
0062BB78  40 8A F8                        mov dil, al
0062BB7B  84 C0                           test al, al
0062BB7D  74 38                           je 0x14062bbb7
0062BB7F  49 8D 76 30                     lea rsi, [r14 + 0x30]
0062BB83  48 8B 1E                        mov rbx, qword ptr [rsi]
0062BB86  EB 19                           jmp 0x14062bba1
0062BB88  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062BB8C  48 85 C0                        test rax, rax
0062BB8F  74 0D                           je 0x14062bb9e
0062BB91  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062BB95  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0062BB99  E8 32 EF 08 00                  call 0x1406baad0
0062BB9E  48 8B 1B                        mov rbx, qword ptr [rbx]
0062BBA1  48 3B DE                        cmp rbx, rsi
0062BBA4  75 E2                           jne 0x14062bb88
0062BBA6  40 84 FF                        test dil, dil
0062BBA9  74 0C                           je 0x14062bbb7
0062BBAB  48 8D 0D CE 82 8D 00            lea rcx, [rip + 0x8d82ce]
0062BBB2  E8 C9 E2 D1 FF                  call 0x140349e80
0062BBB7  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0062BBBA  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0062BBBF  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0062BBC3  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0062BBC7  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0062BBCB  49 8B E3                        mov rsp, r11
0062BBCE  41 5F                           pop r15
0062BBD0  41 5E                           pop r14
0062BBD2  41 5D                           pop r13
0062BBD4  41 5C                           pop r12
0062BBD6  5D                              pop rbp
0062BBD7  C3                              ret
0062BBD8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoOpenDeviceRegistryKeyWrapper(__int64 a1, int a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m44;
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
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(325, a2, a3, a4);
    if (result == 0) goto loc_0062BB3A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062BAB5;
    v_stack_m58 = v_stack_p0;
    goto loc_0062BAC3;
loc_0062BAB5:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m44 = (unsigned int)((unsigned int)(a2));
    v_stack_m48 = (unsigned int)((unsigned int)(a3));
    v_stack_m50 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9276903)) != 0) goto loc_0062BAEF;
    if (((*(unsigned int *)(v_rip + 9277075)) & (0x800ULL)) == 0) goto loc_0062BB02;
loc_0062BAEF:
    result = ExAcquireRundownProtection(v_rip + 9274250, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062BB3A;
loc_0062BB02:
    goto loc_0062BB24;
loc_0062BB0B:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062BB24:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062BB0B;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9274187;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = IoOpenDeviceRegistryKey(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_0062BBB7;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9276762)) != 0) goto loc_0062BB6C;
    if (((*(unsigned int *)(v_rip + 9276950)) & (0x800ULL)) == 0) goto loc_0062BB7F;
loc_0062BB6C:
    result = ExAcquireRundownProtection(v_rip + 9274125, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062BBB7;
loc_0062BB7F:
    goto loc_0062BBA1;
loc_0062BB88:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
loc_0062BBA1:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_0062BB88;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9274062;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifIoOpenDeviceRegistryKeyWrapper(int64_t Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint32_t v_stack_m44;
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
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(325, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0062BB3A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062BAB5;
    v_stack_m58 = v_stack_p0;
    goto loc_0062BAC3;
loc_0062BAB5:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m44 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m48 = (uint32_t)((uint32_t)(Arg3));
    v_stack_m50 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8D8DE7)) != 0) goto loc_0062BAEF;
    if (((*(uint32_t *)(v_rip + 0x8D8E93)) & (0x800ULL)) == 0) goto loc_0062BB02;
loc_0062BAEF:
    result = ExAcquireRundownProtection(v_rip + 9274250, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0062BB3A;
loc_0062BB02:
    goto loc_0062BB24;
loc_0062BB0B:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0062BB24:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062BB0B;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9274187;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    result = IoOpenDeviceRegistryKey(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_0062BBB7;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D8D5A)) != 0) goto loc_0062BB6C;
    if (((*(uint32_t *)(v_rip + 0x8D8E16)) & (0x800ULL)) == 0) goto loc_0062BB7F;
loc_0062BB6C:
    result = ExAcquireRundownProtection(v_rip + 9274125, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_0062BBB7;
loc_0062BB7F:
    goto loc_0062BBA1;
loc_0062BB88:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
loc_0062BBA1:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_0062BB88;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9274062;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062BA50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062BA50[BB_0062BA50]
  bb_0062BAA3[BB_0062BAA3]
  bb_0062BAAB[BB_0062BAAB]
  bb_0062BAB5[BB_0062BAB5]
  bb_0062BABA[BB_0062BABA]
  bb_0062BAC3[BB_0062BAC3]
  bb_0062BAE3[BB_0062BAE3]
  bb_0062BAEF[BB_0062BAEF]
  bb_0062BB02[BB_0062BB02]
  bb_0062BB0B[BB_0062BB0B]
  bb_0062BB14[BB_0062BB14]
  bb_0062BB21[BB_0062BB21]
  bb_0062BB24[BB_0062BB24]
  bb_0062BB29[BB_0062BB29]
  bb_0062BB2E[BB_0062BB2E]
  bb_0062BB3A[BB_0062BB3A]
  bb_0062BB54[BB_0062BB54]
  bb_0062BB60[BB_0062BB60]
  bb_0062BB6C[BB_0062BB6C]
  bb_0062BB7F[BB_0062BB7F]
  bb_0062BB88[BB_0062BB88]
  bb_0062BB91[BB_0062BB91]
  bb_0062BB9E[BB_0062BB9E]
  bb_0062BBA1[BB_0062BBA1]
  bb_0062BBA6[BB_0062BBA6]
  bb_0062BBAB[BB_0062BBAB]
  bb_0062BBB7[BB_0062BBB7]
  bb_0062BBD8[BB_0062BBD8]
  bb_0062BA50 -->|branch| bb_0062BB3A
  bb_0062BA50 -->|fallthrough| bb_0062BAA3
  bb_0062BAA3 -->|branch| bb_0062BAB5
  bb_0062BAA3 -->|fallthrough| bb_0062BAAB
  bb_0062BAAB -->|branch| bb_0062BAC3
  bb_0062BAB5 -->|branch| bb_0062BAC3
  bb_0062BAB5 -->|fallthrough| bb_0062BABA
  bb_0062BABA -->|flow| bb_0062BAC3
  bb_0062BAC3 -->|branch| bb_0062BAEF
  bb_0062BAC3 -->|fallthrough| bb_0062BAE3
  bb_0062BAE3 -->|branch| bb_0062BB02
  bb_0062BAE3 -->|fallthrough| bb_0062BAEF
  bb_0062BAEF -->|branch| bb_0062BB3A
  bb_0062BAEF -->|fallthrough| bb_0062BB02
  bb_0062BB02 -->|branch| bb_0062BB24
  bb_0062BB0B -->|branch| bb_0062BB21
  bb_0062BB0B -->|fallthrough| bb_0062BB14
  bb_0062BB14 -->|flow| bb_0062BB21
  bb_0062BB21 -->|flow| bb_0062BB24
  bb_0062BB24 -->|branch| bb_0062BB0B
  bb_0062BB24 -->|fallthrough| bb_0062BB29
  bb_0062BB29 -->|branch| bb_0062BB3A
  bb_0062BB29 -->|fallthrough| bb_0062BB2E
  bb_0062BB2E -->|flow| bb_0062BB3A
  bb_0062BB3A -->|branch| bb_0062BBB7
  bb_0062BB3A -->|fallthrough| bb_0062BB54
  bb_0062BB54 -->|branch| bb_0062BB6C
  bb_0062BB54 -->|fallthrough| bb_0062BB60
  bb_0062BB60 -->|branch| bb_0062BB7F
  bb_0062BB60 -->|fallthrough| bb_0062BB6C
  bb_0062BB6C -->|branch| bb_0062BBB7
  bb_0062BB6C -->|fallthrough| bb_0062BB7F
  bb_0062BB7F -->|branch| bb_0062BBA1
  bb_0062BB88 -->|branch| bb_0062BB9E
  bb_0062BB88 -->|fallthrough| bb_0062BB91
  bb_0062BB91 -->|flow| bb_0062BB9E
  bb_0062BB9E -->|flow| bb_0062BBA1
  bb_0062BBA1 -->|branch| bb_0062BB88
  bb_0062BBA1 -->|fallthrough| bb_0062BBA6
  bb_0062BBA6 -->|branch| bb_0062BBB7
  bb_0062BBA6 -->|fallthrough| bb_0062BBAB
  bb_0062BBAB -->|flow| bb_0062BBB7
```
