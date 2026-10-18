# PnpTraceWatchdogViolation

- RVA: `0x005AA2FC`–`0x005AA434` (길이 `312` bytes)
- VA: `0x00000001405AA2FC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A68C4`
- 디코드: `71`개 명령, `312/312` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x005AA33C` → [tlgKeywordOn](../42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x005AA419` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x005AA425` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PnpWatchdogEtwWrite](../4D/PnpWatchdogEtwWrite_function_004D2FB0.md) at `0x004D32C5`

### Static image references
- `0x005AA30A` → RVA `0x00E0A740` (`.data`; read)
- `0x005AA318` → RVA `0x00E06F90` (`.data`; read)
- `0x005AA3B7` → RVA `0x00046F5D` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005AA2FC  40 55                           push rbp
005AA2FE  48 8D 6C 24 B1                  lea rbp, [rsp - 0x4f]
005AA303  48 81 EC 00 01 00 00            sub rsp, 0x100
005AA30A  48 8B 05 2F 04 86 00            mov rax, qword ptr [rip + 0x86042f]
005AA311  48 33 C4                        xor rax, rsp
005AA314  48 89 45 3F                     mov qword ptr [rbp + 0x3f], rax
005AA318  83 3D 71 CC 85 00 05            cmp dword ptr [rip + 0x85cc71], 5
005AA31F  44 8A D2                        mov r10b, dl
005AA322  44 8B D9                        mov r11d, ecx
005AA325  0F 86 F3 00 00 00               jbe 0x1405aa41e
005AA32B  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
005AA335  48 8D 0D 54 CC 85 00            lea rcx, [rip + 0x85cc54]
005AA33C  E8 5F 47 E8 FF                  call 0x14042eaa0
005AA341  84 C0                           test al, al
005AA343  0F 84 D5 00 00 00               je 0x1405aa41e
005AA349  48 8B 55 7F                     mov rdx, qword ptr [rbp + 0x7f]
005AA34D  48 8D 45 8F                     lea rax, [rbp - 0x71]
005AA351  83 65 CB 00                     and dword ptr [rbp - 0x35], 0
005AA355  B9 04 00 00 00                  mov ecx, 4
005AA35A  83 65 DB 00                     and dword ptr [rbp - 0x25], 0
005AA35E  83 65 EB 00                     and dword ptr [rbp - 0x15], 0
005AA362  83 65 FB 00                     and dword ptr [rbp - 5], 0
005AA366  83 65 0B 00                     and dword ptr [rbp + 0xb], 0
005AA36A  83 65 1B 00                     and dword ptr [rbp + 0x1b], 0
005AA36E  83 65 2B 00                     and dword ptr [rbp + 0x2b], 0
005AA372  83 65 3B 00                     and dword ptr [rbp + 0x3b], 0
005AA376  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
005AA37A  48 8D 45 83                     lea rax, [rbp - 0x7d]
005AA37E  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
005AA382  48 8D 45 87                     lea rax, [rbp - 0x79]
005AA386  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
005AA38A  48 8D 45 07                     lea rax, [rbp + 7]
005AA38E  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
005AA392  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
005AA396  48 89 45 FF                     mov qword ptr [rbp - 1], rax
005AA39A  41 0F B7 01                     movzx eax, word ptr [r9]
005AA39E  45 33 C9                        xor r9d, r9d
005AA3A1  89 45 07                        mov dword ptr [rbp + 7], eax
005AA3A4  48 8D 45 27                     lea rax, [rbp + 0x27]
005AA3A8  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
005AA3AC  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
005AA3B0  48 89 45 1F                     mov qword ptr [rbp + 0x1f], rax
005AA3B4  0F B7 02                        movzx eax, word ptr [rdx]
005AA3B7  48 8D 15 9F CB A9 FF            lea rdx, [rip - 0x563461]
005AA3BE  89 45 27                        mov dword ptr [rbp + 0x27], eax
005AA3C1  48 8D 44 24 30                  lea rax, [rsp + 0x30]
005AA3C6  89 4D D7                        mov dword ptr [rbp - 0x29], ecx
005AA3C9  89 4D E7                        mov dword ptr [rbp - 0x19], ecx
005AA3CC  B9 02 00 00 00                  mov ecx, 2
005AA3D1  48 89 45 2F                     mov qword ptr [rbp + 0x2f], rax
005AA3D5  48 8D 45 9F                     lea rax, [rbp - 0x61]
005AA3D9  44 89 45 87                     mov dword ptr [rbp - 0x79], r8d
005AA3DD  45 33 C0                        xor r8d, r8d
005AA3E0  89 4D F7                        mov dword ptr [rbp - 9], ecx
005AA3E3  89 4D 17                        mov dword ptr [rbp + 0x17], ecx
005AA3E6  48 8D 0D A3 CB 85 00            lea rcx, [rip + 0x85cba3]
005AA3ED  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005AA3F2  C7 44 24 20 0A 00 00 00         mov dword ptr [rsp + 0x20], 0xa
005AA3FA  48 C7 45 8F 00 00 00 01         mov qword ptr [rbp - 0x71], 0x1000000
005AA402  C7 45 C7 08 00 00 00            mov dword ptr [rbp - 0x39], 8
005AA409  44 89 5D 83                     mov dword ptr [rbp - 0x7d], r11d
005AA40D  44 88 54 24 30                  mov byte ptr [rsp + 0x30], r10b
005AA412  C7 45 37 01 00 00 00            mov dword ptr [rbp + 0x37], 1
005AA419  E8 C2 BC E7 FF                  call 0x1404260e0
005AA41E  48 8B 4D 3F                     mov rcx, qword ptr [rbp + 0x3f]
005AA422  48 33 CC                        xor rcx, rsp
005AA425  E8 16 22 10 00                  call 0x1406ac640
005AA42A  48 81 C4 00 01 00 00            add rsp, 0x100
005AA431  5D                              pop rbp
005AA432  C3                              ret
005AA433  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpTraceWatchdogViolation(int a1, unsigned __int8 a2, int a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m57;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD4;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE8;

    v_rsp = (v_rsp) - (256);
    result = (*(unsigned __int64 *)(v_rip + 8782895)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(v_rip + 8768625)) <= 5) goto loc_005AA41E;
    result = tlgKeywordOn(v_rip + 8768596, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a2 = a5;
        result = v_stack_mC8;
        a1 = 4;
        v_stack_m98 = result;
        result = v_stack_mD4;
        v_stack_m88 = result;
        result = v_stack_mD0;
        v_stack_m78 = result;
        result = v_stack_m50;
        v_stack_m68 = result;
        result = *(unsigned __int64 *)(a4 + 8);
        v_stack_m58 = result;
        result = *(unsigned __int16 *)(a4);
        a4 = 0;
        v_stack_m50 = (unsigned int)(result);
        result = v_stack_m30;
        v_stack_m48 = result;
        result = *(unsigned __int64 *)(a2 + 8);
        v_stack_m38 = result;
        result = *(unsigned __int16 *)(a2);
        a2 = v_rip - 5649505;
        v_stack_m30 = (unsigned int)(result);
        result = v_stack_mD8;
        v_stack_m80 = a1;
        v_stack_m70 = a1;
        a1 = 2;
        v_stack_m28 = result;
        result = v_stack_mB8;
        v_stack_mD0 = a3;
        a3 = 0;
        v_stack_m60 = a1;
        v_stack_m40 = a1;
        a1 = v_rip + 8768419;
        v_stack_mE0 = result;
        v_stack_mE8 = 10;
        v_stack_mC8 = 0x1000000ULL;
        v_stack_m90 = 8;
        v_stack_mD4 = (unsigned int)((unsigned int)(a1));
        v_stack_mD8 = a2;
        v_stack_m20 = 1;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (256);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PnpTraceWatchdogViolation(int32_t Arg1, uint8_t Arg2, int32_t Arg3, int64_t Arg4, void *Arg5)
{
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint64_t v_stack_m50;
    uint64_t v_stack_m57;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD4;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE8;

    local_rsp = (local_rsp) - (256);
    result = (*(uint64_t *)(v_rip + 0x86042F)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(v_rip + 0x85CC71)) <= 5) goto loc_005AA41E;
    result = tlgKeywordOn(v_rip + 8768596, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg2 = Arg5;
        result = v_stack_mC8;
        Arg1 = 4;
        v_stack_m98 = result;
        result = v_stack_mD4;
        v_stack_m88 = result;
        result = v_stack_mD0;
        v_stack_m78 = result;
        result = v_stack_m50;
        v_stack_m68 = result;
        result = *(uint64_t *)(Arg4 + 0x8);
        v_stack_m58 = result;
        result = *(uint16_t *)(Arg4);
        Arg4 = 0;
        v_stack_m50 = (uint32_t)(result);
        result = v_stack_m30;
        v_stack_m48 = result;
        result = *(uint64_t *)(Arg2 + 0x8);
        v_stack_m38 = result;
        result = *(uint16_t *)(Arg2);
        Arg2 = v_rip - 5649505;
        v_stack_m30 = (uint32_t)(result);
        result = v_stack_mD8;
        v_stack_m80 = Arg1;
        v_stack_m70 = Arg1;
        Arg1 = 2;
        v_stack_m28 = result;
        result = v_stack_mB8;
        v_stack_mD0 = Arg3;
        Arg3 = 0;
        v_stack_m60 = Arg1;
        v_stack_m40 = Arg1;
        Arg1 = v_rip + 8768419;
        v_stack_mE0 = result;
        v_stack_mE8 = 10;
        v_stack_mC8 = 0x1000000ULL;
        v_stack_m90 = 8;
        v_stack_mD4 = (uint32_t)((uint32_t)(Arg1));
        v_stack_mD8 = Arg2;
        v_stack_m20 = 1;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (256);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0` | `16` | `R` |
| `Arg5` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005AA2FC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005AA2FC[BB_005AA2FC]
  bb_005AA32B[BB_005AA32B]
  bb_005AA349[BB_005AA349]
  bb_005AA41E[BB_005AA41E]
  bb_005AA433[BB_005AA433]
  bb_005AA2FC -->|branch| bb_005AA41E
  bb_005AA2FC -->|fallthrough| bb_005AA32B
  bb_005AA32B -->|branch| bb_005AA41E
  bb_005AA32B -->|fallthrough| bb_005AA349
  bb_005AA349 -->|flow| bb_005AA41E
```
