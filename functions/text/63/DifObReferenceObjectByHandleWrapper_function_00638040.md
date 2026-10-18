# DifObReferenceObjectByHandleWrapper

- RVA: `0x00638040`–`0x006381FF` (길이 `447` bytes)
- VA: `0x0000000140638040`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BC530`
- 디코드: `124`개 명령, `447/447` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00638079` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00638083` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006380AB` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006380F7` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063811D` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00638136` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063815F` → [ObReferenceObjectByHandle](../../page/86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00638196` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006381BC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006381D5` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006380BB` → RVA `0x00F048B8` (`.data`; read)
- `0x006380E4` → RVA `0x00F04980` (`.data`; read)
- `0x006380F0` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0063815F` → [ObReferenceObjectByHandle](../../page/86/ObReferenceObjectByHandle_function_00868DB0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00638040  48 8B C4                        mov rax, rsp
00638043  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00638047  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0063804B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0063804F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00638053  55                              push rbp
00638054  41 54                           push r12
00638056  41 55                           push r13
00638058  41 56                           push r14
0063805A  41 57                           push r15
0063805C  48 8B EC                        mov rbp, rsp
0063805F  48 81 EC 80 00 00 00            sub rsp, 0x80
00638066  44 8B EA                        mov r13d, edx
00638069  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0063806D  33 D2                           xor edx, edx
0063806F  4D 8B E0                        mov r12, r8
00638072  45 8A F9                        mov r15b, r9b
00638075  44 8D 42 40                     lea r8d, [rdx + 0x40]
00638079  E8 C2 EB 08 00                  call 0x1406c6c40
0063807E  B9 CA 00 00 00                  mov ecx, 0xca
00638083  E8 AC D9 E5 FF                  call 0x140495a34
00638088  4C 8B F0                        mov r14, rax
0063808B  48 85 C0                        test rax, rax
0063808E  0F 84 A7 00 00 00               je 0x14063813b
00638094  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
00638097  F6 C1 18                        test cl, 0x18
0063809A  74 0A                           je 0x1406380a6
0063809C  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
006380A0  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
006380A4  EB 0E                           jmp 0x1406380b4
006380A6  F6 C1 04                        test cl, 4
006380A9  74 09                           je 0x1406380b4
006380AB  E8 58 BB E9 FF                  call 0x1404d3c08
006380B0  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
006380B4  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
006380B8  40 32 F6                        xor sil, sil
006380BB  40 38 35 F6 C7 8C 00            cmp byte ptr [rip + 0x8cc7f6], sil
006380C2  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
006380C6  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
006380CA  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
006380CE  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
006380D2  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
006380D6  44 89 6D E8                     mov dword ptr [rbp - 0x18], r13d
006380DA  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
006380DE  44 88 7D D8                     mov byte ptr [rbp - 0x28], r15b
006380E2  75 0C                           jne 0x1406380f0
006380E4  F7 05 92 C8 8C 00 00 08 00 00   test dword ptr [rip + 0x8cc892], 0x800
006380EE  74 13                           je 0x140638103
006380F0  48 8D 0D 89 BD 8C 00            lea rcx, [rip + 0x8cbd89]
006380F7  E8 24 E5 BD FF                  call 0x140216620
006380FC  40 8A F0                        mov sil, al
006380FF  84 C0                           test al, al
00638101  74 38                           je 0x14063813b
00638103  49 8D 7E 20                     lea rdi, [r14 + 0x20]
00638107  48 8B 1F                        mov rbx, qword ptr [rdi]
0063810A  EB 19                           jmp 0x140638125
0063810C  48 8D 43 F0                     lea rax, [rbx - 0x10]
00638110  48 85 C0                        test rax, rax
00638113  74 0D                           je 0x140638122
00638115  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00638119  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0063811D  E8 AE 29 08 00                  call 0x1406baad0
00638122  48 8B 1B                        mov rbx, qword ptr [rbx]
00638125  48 3B DF                        cmp rbx, rdi
00638128  75 E2                           jne 0x14063810c
0063812A  40 84 F6                        test sil, sil
0063812D  74 0C                           je 0x14063813b
0063812F  48 8D 0D 4A BD 8C 00            lea rcx, [rip + 0x8cbd4a]
00638136  E8 45 1D D1 FF                  call 0x140349e80
0063813B  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
0063813F  45 8A CF                        mov r9b, r15b
00638142  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00638146  4D 8B C4                        mov r8, r12
00638149  48 83 65 B0 00                  and qword ptr [rbp - 0x50], 0
0063814E  41 8B D5                        mov edx, r13d
00638151  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00638156  48 8D 45 B0                     lea rax, [rbp - 0x50]
0063815A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0063815F  E8 4C 0C 23 00                  call 0x140868db0
00638164  48 8B 55 50                     mov rdx, qword ptr [rbp + 0x50]
00638168  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
0063816C  89 45 F8                        mov dword ptr [rbp - 8], eax
0063816F  48 89 0A                        mov qword ptr [rdx], rcx
00638172  4D 85 F6                        test r14, r14
00638175  74 63                           je 0x1406381da
00638177  40 32 FF                        xor dil, dil
0063817A  40 38 3D 37 C7 8C 00            cmp byte ptr [rip + 0x8cc737], dil
00638181  75 0C                           jne 0x14063818f
00638183  F7 05 F3 C7 8C 00 00 08 00 00   test dword ptr [rip + 0x8cc7f3], 0x800
0063818D  74 13                           je 0x1406381a2
0063818F  48 8D 0D EA BC 8C 00            lea rcx, [rip + 0x8cbcea]
00638196  E8 85 E4 BD FF                  call 0x140216620
0063819B  40 8A F8                        mov dil, al
0063819E  84 C0                           test al, al
006381A0  74 38                           je 0x1406381da
006381A2  49 8D 76 30                     lea rsi, [r14 + 0x30]
006381A6  48 8B 1E                        mov rbx, qword ptr [rsi]
006381A9  EB 19                           jmp 0x1406381c4
006381AB  48 8D 43 F0                     lea rax, [rbx - 0x10]
006381AF  48 85 C0                        test rax, rax
006381B2  74 0D                           je 0x1406381c1
006381B4  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006381B8  48 8D 4D C0                     lea rcx, [rbp - 0x40]
006381BC  E8 0F 29 08 00                  call 0x1406baad0
006381C1  48 8B 1B                        mov rbx, qword ptr [rbx]
006381C4  48 3B DE                        cmp rbx, rsi
006381C7  75 E2                           jne 0x1406381ab
006381C9  40 84 FF                        test dil, dil
006381CC  74 0C                           je 0x1406381da
006381CE  48 8D 0D AB BC 8C 00            lea rcx, [rip + 0x8cbcab]
006381D5  E8 A6 1C D1 FF                  call 0x140349e80
006381DA  8B 45 F8                        mov eax, dword ptr [rbp - 8]
006381DD  4C 8D 9C 24 80 00 00 00         lea r11, [rsp + 0x80]
006381E5  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
006381E9  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
006381ED  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
006381F1  49 8B E3                        mov rsp, r11
006381F4  41 5F                           pop r15
006381F6  41 5E                           pop r14
006381F8  41 5D                           pop r13
006381FA  41 5C                           pop r12
006381FC  5D                              pop rbp
006381FD  C3                              ret
006381FE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifObReferenceObjectByHandleWrapper(__int64 a1, int a2, __int64 a3, unsigned __int8 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int8 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (128);
    a2 = 0;
    result = memset(v_stack_m68, a2, a2 + 64, a4);
    result = DifGetAPIThunkContextById(202, a2, a2 + 64, a4);
    if (result == 0) goto loc_0063813B;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006380A6;
    v_stack_m68 = v_stack_p0;
    goto loc_006380B4;
loc_006380A6:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a2 + 64, a4);
        v_stack_m68 = result;
    }
    v_rsi = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m58 = a5;
    v_stack_m60 = a6;
    v_stack_m40 = (unsigned int)((unsigned int)(a2));
    v_stack_m48 = a3;
    v_stack_m50 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9226230)) != 0) goto loc_006380F0;
    if (((*(unsigned int *)(v_rip + 9226386)) & (0x800ULL)) == 0) goto loc_00638103;
loc_006380F0:
    result = ExAcquireRundownProtection(v_rip + 9223561, a2, a2 + 64, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063813B;
loc_00638103:
    goto loc_00638125;
loc_0063810C:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a2 + 64, a4);
    }
loc_00638125:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063810C;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9223498;
        result = ExReleaseRundownProtection(a1, a2, a2 + 64, a4);
    }
    v_stack_m80 = a6;
    v_stack_m88 = v_stack_m78;
    result = ObReferenceObjectByHandle(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m30 = (unsigned int)(result);
    *(unsigned __int64 *)(a5) = v_stack_m78;
    if (result == 0) goto loc_006381DA;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9226039)) != 0) goto loc_0063818F;
    if (((*(unsigned int *)(v_rip + 9226227)) & (0x800ULL)) == 0) goto loc_006381A2;
loc_0063818F:
    result = ExAcquireRundownProtection(v_rip + 9223402, a5, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006381DA;
loc_006381A2:
    goto loc_006381C4;
loc_006381AB:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a5, a3, a4);
    }
loc_006381C4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_006381AB;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9223339;
        result = ExReleaseRundownProtection(a1, a5, a3, a4);
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifObReferenceObjectByHandleWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, uint8_t Arg4, void *Arg5, int64_t Arg6)
{
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint8_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (128);
    Arg2 = 0;
    result = memset(v_stack_m68, Arg2, Arg2 + 64, Arg4);
    result = DifGetAPIThunkContextById(202, Arg2, Arg2 + 64, Arg4);
    if (result == 0) goto loc_0063813B;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006380A6;
    v_stack_m68 = v_stack_p0;
    goto loc_006380B4;
loc_006380A6:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg2 + 64, Arg4);
        v_stack_m68 = result;
    }
    local_rsi = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m58 = Arg5;
    v_stack_m60 = Arg6;
    v_stack_m40 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m48 = Arg3;
    v_stack_m50 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8CC7F6)) != 0) goto loc_006380F0;
    if (((*(uint32_t *)(v_rip + 0x8CC892)) & (0x800ULL)) == 0) goto loc_00638103;
loc_006380F0:
    result = ExAcquireRundownProtection(v_rip + 9223561, Arg2, Arg2 + 64, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0063813B;
loc_00638103:
    goto loc_00638125;
loc_0063810C:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg2 + 64, Arg4);
    }
loc_00638125:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063810C;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9223498;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg2 + 64, Arg4);
    }
    v_stack_m80 = Arg6;
    v_stack_m88 = v_stack_m78;
    result = ObReferenceObjectByHandle(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    v_stack_m30 = (uint32_t)(result);
    *(uint64_t *)(arg5) = v_stack_m78;
    if (result == 0) goto loc_006381DA;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CC737)) != 0) goto loc_0063818F;
    if (((*(uint32_t *)(v_rip + 0x8CC7F3)) & (0x800ULL)) == 0) goto loc_006381A2;
loc_0063818F:
    result = ExAcquireRundownProtection(v_rip + 9223402, Arg5, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_006381DA;
loc_006381A2:
    goto loc_006381C4;
loc_006381AB:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg5, Arg3, Arg4);
    }
loc_006381C4:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_006381AB;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9223339;
        result = ExReleaseRundownProtection(Arg1, Arg5, Arg3, Arg4);
    }
    return (uint32_t)(v_stack_m30);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00638040&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00638040[BB_00638040]
  bb_00638094[BB_00638094]
  bb_0063809C[BB_0063809C]
  bb_006380A6[BB_006380A6]
  bb_006380AB[BB_006380AB]
  bb_006380B4[BB_006380B4]
  bb_006380E4[BB_006380E4]
  bb_006380F0[BB_006380F0]
  bb_00638103[BB_00638103]
  bb_0063810C[BB_0063810C]
  bb_00638115[BB_00638115]
  bb_00638122[BB_00638122]
  bb_00638125[BB_00638125]
  bb_0063812A[BB_0063812A]
  bb_0063812F[BB_0063812F]
  bb_0063813B[BB_0063813B]
  bb_00638177[BB_00638177]
  bb_00638183[BB_00638183]
  bb_0063818F[BB_0063818F]
  bb_006381A2[BB_006381A2]
  bb_006381AB[BB_006381AB]
  bb_006381B4[BB_006381B4]
  bb_006381C1[BB_006381C1]
  bb_006381C4[BB_006381C4]
  bb_006381C9[BB_006381C9]
  bb_006381CE[BB_006381CE]
  bb_006381DA[BB_006381DA]
  bb_006381FE[BB_006381FE]
  bb_00638040 -->|branch| bb_0063813B
  bb_00638040 -->|fallthrough| bb_00638094
  bb_00638094 -->|branch| bb_006380A6
  bb_00638094 -->|fallthrough| bb_0063809C
  bb_0063809C -->|branch| bb_006380B4
  bb_006380A6 -->|branch| bb_006380B4
  bb_006380A6 -->|fallthrough| bb_006380AB
  bb_006380AB -->|flow| bb_006380B4
  bb_006380B4 -->|branch| bb_006380F0
  bb_006380B4 -->|fallthrough| bb_006380E4
  bb_006380E4 -->|branch| bb_00638103
  bb_006380E4 -->|fallthrough| bb_006380F0
  bb_006380F0 -->|branch| bb_0063813B
  bb_006380F0 -->|fallthrough| bb_00638103
  bb_00638103 -->|branch| bb_00638125
  bb_0063810C -->|branch| bb_00638122
  bb_0063810C -->|fallthrough| bb_00638115
  bb_00638115 -->|flow| bb_00638122
  bb_00638122 -->|flow| bb_00638125
  bb_00638125 -->|branch| bb_0063810C
  bb_00638125 -->|fallthrough| bb_0063812A
  bb_0063812A -->|branch| bb_0063813B
  bb_0063812A -->|fallthrough| bb_0063812F
  bb_0063812F -->|flow| bb_0063813B
  bb_0063813B -->|branch| bb_006381DA
  bb_0063813B -->|fallthrough| bb_00638177
  bb_00638177 -->|branch| bb_0063818F
  bb_00638177 -->|fallthrough| bb_00638183
  bb_00638183 -->|branch| bb_006381A2
  bb_00638183 -->|fallthrough| bb_0063818F
  bb_0063818F -->|branch| bb_006381DA
  bb_0063818F -->|fallthrough| bb_006381A2
  bb_006381A2 -->|branch| bb_006381C4
  bb_006381AB -->|branch| bb_006381C1
  bb_006381AB -->|fallthrough| bb_006381B4
  bb_006381B4 -->|flow| bb_006381C1
  bb_006381C1 -->|flow| bb_006381C4
  bb_006381C4 -->|branch| bb_006381AB
  bb_006381C4 -->|fallthrough| bb_006381C9
  bb_006381C9 -->|branch| bb_006381DA
  bb_006381C9 -->|fallthrough| bb_006381CE
  bb_006381CE -->|flow| bb_006381DA
```
